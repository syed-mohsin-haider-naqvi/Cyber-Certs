# Windows Event Logs & Finding Evil — Skills Assessment (HTB Academy)

**Module:** Security Monitoring & SIEM Fundamentals → Windows Event Logs & Finding Evil
**Format:** Live RDP lab environment, real .evtx log files across multiple attack-technique folders

---

## Scenario

Framed as a SOC manager assigning a review of older attack logs — the task was to RDP into a live Windows target, dig through several folders under `C:\Logs\` (each one representing a different technique: DLL hijacking, unmanaged PowerShell execution, process injection, an LSASS dump, and a strange parent-child process relationship), and pull out the specific process responsible for each piece of malicious activity using nothing but the raw Sysmon event logs.

Connected in with:
```
xfreerdp /u:Administrator /p:'HTB_@cad3my_lab_W1n10_r00t!@0' /v:[Target IP] /dynamic-resolution
```

---

## Investigation

### DLL Hijacking — `C:\Logs\DLLHijack`

DLL loads specifically show up under **Sysmon Event ID 7** — that's the event ID that logs when an image (DLL) gets loaded into a process. Since I already knew that pattern from earlier in the module, I went straight for it instead of scrolling through the whole log blind:

```powershell
Get-WinEvent -FilterHashtable @{Path='C:\Logs\DLLHijack\*.evtx'; Id=7} | Format-List
```

That returned way more than was actually useful — a lot of it was just normal browser DLL loading noise. Rather than reading through everything, I narrowed it down by searching specifically for the DLL name that kept showing up repeatedly across the noise, since a DLL appearing suspiciously often across multiple events is usually a decent signal something's using it as a delivery mechanism:

```powershell
Get-WinEvent -FilterHashtable @{Path='C:\Logs\DLLHijack\*.evtx'; Id=7} |
Where-Object { $_.Message -like "*DismCore.dll*" } |
Format-List
```

That narrowed it to two specific events. One showed `rundll32.exe` loading `DismCore.dll` — that's the actual hijack, a legitimate Windows binary being used to load a DLL it shouldn't normally be touching. The other showed `Dism.exe` loading the same DLL, which looked like the more "expected" legitimate load being used as cover.

**Answer: `Dism.exe`**

![Sysmon Event ID 7 showing DismCore.dll loaded by both Dism.exe and rundll32.exe](./screenshots/dllhijack-eventid7.png)

---

### Unmanaged PowerShell Execution — `C:\Logs\PowershellExec`

**Question: which process executed unmanaged PowerShell code?**

This one took a bit of prior knowledge I picked up going through the module material first — unmanaged PowerShell is when PowerShell-style code gets executed inside a process that isn't `powershell.exe` itself, using the .NET runtime directly. The tell for this is that the non-PowerShell process ends up loading `clrjit.dll` or `clr.dll` — DLLs that belong specifically to the .NET runtime and have no business being loaded by a process that shouldn't be running managed code.

So again, Event ID 7 for image loads, filtered specifically for that DLL:

```powershell
Get-WinEvent -FilterHashtable @{Path="C:\Logs\PowershellExec\*.evtx"; Id=7} |
Where-Object {$_.Properties[5].Value -like "*clrjit.dll*"} |
Select-Object -ExpandProperty Message
```

That returned a single clean hit — `Calculator.exe` loading `clrjit.dll`. A calculator app has zero legitimate reason to be loading .NET JIT compiler DLLs, so this was a pretty unambiguous find once filtered correctly.

**Answer: `Calculator.exe`**

![Event showing Calculator.exe loading clrjit.dll](./screenshots/powershellexec-clrjit.png)

**Follow-up question: which process injected into the process running unmanaged PowerShell?**

Process injection specifically logs under **Sysmon Event ID 8** (CreateRemoteThread) — different event ID from the DLL load one, since this is about one process reaching into another's memory space rather than a DLL simply being loaded.

```powershell
Get-WinEvent -FilterHashtable @{Path='C:\Logs\PowershellExec\*.evtx'; Id=8} | Format-List
```

The message field laid it out directly — `SourceImage: rundll32.exe`, `TargetImage: Calculator.exe`. Rundll32 injecting into the Calculator process that was already flagged as running the unmanaged PowerShell — so the full chain here was rundll32.exe doing the injection, Calculator.exe being the process actually running the malicious code inside it.

**Answer: `rundll32.exe`**

![CreateRemoteThread event showing rundll32.exe injecting into Calculator.exe](./screenshots/powershellexec-eventid8-injection.png)

---

### LSASS Dump — `C:\Logs\Dump`

**Question: which process performed the LSASS dump?**

LSASS credential dumping shows up under **Sysmon Event ID 10** (Process Access) — this logs whenever one process opens a handle to another process's memory, which is exactly what a credential dumping tool needs to do to read LSASS's memory space.

Looking through the ID 10 events in this folder, `ProcessHacker.exe` showed up as the source process accessing `lsass.exe` with the kind of access rights consistent with memory reading rather than something benign.

**Answer: `ProcessHacker.exe`**

![Sysmon Event ID 10 showing ProcessHacker.exe accessing lsass.exe](./screenshots/dump-eventid10.png)

**Follow-up question: did an ill-intended login occur after the dump?**

This one needed a timeline approach rather than just another filtered event pull. First step was pinning down exactly when the dump happened from the Event ID 10 timestamp, then checking all logon events (**Event ID 4624**) that occurred after that point:

```powershell
$dumpTime = Get-Date "2022-04-28 02:08:47Z"

Get-WinEvent -FilterHashtable @{Path='C:\Logs\Dump\*.evtx'; Id=4624} |
Where-Object { $_.TimeCreated -gt $dumpTime } |
Format-List
```

The only logon after that timestamp was a **Logon Type 5** (Service Logon) under the SYSTEM account — that's completely normal background service activity, not an interactive login from an actual person. No Logon Type 3 (network) or Type 9 (new credentials) showed up, which would've been the real red flags for someone actually using the dumped credentials to move laterally.

**Answer: No** — no suspicious login followed the dump, at least not within what this log captured.

---

### Strange Parent-Child Process Relationship — `C:\Logs\StrangePPID`

**Question: which process was used to temporarily execute code based on a strange parent-child relationship?**

Parent-child relationship anomalies (including parent PID spoofing) log under **Sysmon Event ID 1** (Process Creation). Rather than trusting the raw property index positions in the event object (which can shift and aren't reliable to reference blindly), I parsed the actual XML structure of each event to pull the Image and ParentImage fields properly by name:

```powershell
Get-WinEvent -FilterHashtable @{Path='C:\Logs\StrangePPID\*.evtx'; Id=1} |
ForEach-Object {
    $xml = [xml]$_.ToXml()
    $image = $xml.Event.EventData.Data | Where-Object { $_.Name -eq 'Image' } | Select-Object -ExpandProperty '#text'
    $parentImage = $xml.Event.EventData.Data | Where-Object { $_.Name -eq 'ParentImage' } | Select-Object -ExpandProperty '#text'
    [PSCustomObject]@{
        TimeCreated = $_.TimeCreated
        ParentImage = $parentImage
        Image       = $image
    }
} | Format-Table -AutoSize
```

That gave a clean, readable timeline of every parent-child pair. Most of it was completely ordinary — normal process trees you'd expect. But one line broke the pattern:

```
WerFault.exe → cmd.exe
```

WerFault is the Windows Error Reporting process — it should never be the parent of a Command Prompt session. Seeing that pairing was the clear anomaly the question was pointing at.

**Answer: `WerFault.exe`**

![Formatted table showing the WerFault.exe -> cmd.exe anomalous parent-child relationship](./screenshots/strangeppid-table.png)

---

## Putting It Together

Across all five folders, the actual investigative pattern was consistent even though each technique was different: figure out which specific Sysmon Event ID actually captures the behavior in question first (image load, process access, remote thread creation, process creation), then filter down to just the relevant entries instead of reading raw logs top to bottom. DLL hijacking and unmanaged PowerShell execution both hinge on Event ID 7 but with different DLL names to search for; process injection needed Event ID 8; the LSASS dump needed Event ID 10 plus a timeline check against Event ID 4624; and the strange parent-child relationship needed Event ID 1 parsed properly through XML rather than relying on property indexes.

---

## What Tripped Me Up

Knowing that unmanaged PowerShell specifically tips its hand through `clrjit.dll`/`clr.dll` loads wasn't something I'd have guessed without the module explaining that connection first — that's a fairly specific piece of knowledge about how the .NET runtime gets pulled into a process, not something obvious just from staring at a process list.

The XML parsing step on the last question also took a moment to get right — pulling fields by name instead of by property index isn't something I'd have thought to do carefully on my own without running into the problem of indexes not lining up consistently first.

---

## Tools Used

- Sysmon (event source)
- PowerShell `Get-WinEvent` with `-FilterHashtable` for targeted event pulls
- RDP into the live HTB lab target
