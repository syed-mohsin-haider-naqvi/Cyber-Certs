# SOC164 — Suspicious Mshta Behavior (EventID: 114)

**Platform:** LetsDefend (SOC Simulator)
**Severity:** High
**Host:** Roberto (172.16.17.38, Windows 10)

---

## Alert Summary

| Field | Detail |
|---|---|
| EventID | 114 |
| Event Time | Mar 05, 2022, 10:29 AM |
| Rule | SOC164 - Suspicious Mshta Behavior |
| Hostname | Roberto |
| IP Address | 172.16.17.38 |
| Related Binary | mshta.exe |
| Binary Path | C:\Windows\System32\mshta.exe |
| Command Line | `C:\Windows\System32\mshta.exe C:\Users\Roberto\Desktop\Ps1.hta` |
| MD5 of Ps1.hta | 6685c433705f558c5535789234db0e5a |
| Alert Trigger Reason | Low reputation hta file executed via mshta.exe |
| EDR Action | Allowed |

The alert flagged `mshta.exe` on Roberto's machine executing a file called `Ps1.hta` straight off the desktop. Nothing was blocked at this point — EDR let it through, just logged it as suspicious enough to alert on.

---

## Investigation

### Understanding what I was actually looking at first

Before doing anything else I wanted to actually understand what `mshta.exe` is, since I hadn't worked with it directly before. It's a legitimate Microsoft component — short for Microsoft HTML Applications — normally used to run `.hta` files, which are basically small GUI apps built with HTML plus a scripting language like JavaScript or VBScript.

The important part is that it's a legitimate Windows binary that also happens to be abusable — this is what's called a LOLBin (Living-off-the-Land Binary). Instead of dropping obviously malicious tools, an attacker uses a binary that's already trusted and signed by Microsoft, which lets them slip past a lot of basic whitelisting/security controls since the binary itself isn't inherently flagged as bad.

So right from the start, seeing mshta.exe running a random `.hta` file off someone's desktop was already a pattern worth being suspicious of, even before checking anything else.

### Checking the file itself

Next step was actually checking whether `Ps1.hta` itself was known-bad, not just assuming based on the binary alone. I took the MD5 hash from the alert (`6685c433705f558c5535789234db0e5a`) and ran it through VirusTotal.

**Result: 33 out of 61 security vendors flagged it as malicious.**

VirusTotal's own popular threat label came back as `trojan.valyria/powershell`, with threat categories listed as trojan and downloader. So this wasn't a borderline case — over half the engines checking it agreed it was malicious, and specifically flagged as something that downloads further payloads.

![VirusTotal detection results for Ps1.hta hash](./screenshots/vt-detection.png)

### Checking what actually happened on the host

With the file itself confirmed malicious, I went into the Endpoint Security section to look at Roberto's actual command line history around the alert time, to see what happened after the file executed.

```
05.03.2021 10:29 - C:/Windows/System32/mshta.exe C:/Users/roberto/Deskto...
05.03.2021 10:30 - C:/Windows/System32/WindowsPowerShell/v1.0/powershell...
```

One second after mshta.exe ran the .hta file, a PowerShell process fired off. Reading through the actual PowerShell command, it was obfuscated — deliberately hard to read, not normal formatting.

I want to be upfront that recognizing obfuscated PowerShell isn't something I could confidently spot on sight before this — I had to actually look at the structure and understand that attackers obfuscate code specifically to make it harder for a human (or a signature-based tool) to immediately tell what it's doing. Legitimate scripts don't typically look like that.

### Pulling the URL out of the obfuscated code

Reading through the obfuscated PowerShell, I was able to pick out an embedded URL:

```
hxxp://193[.]193[.]142[.]58[.]23/Server[.]txt
```

(written defanged like that on purpose — standard practice so the URL doesn't become clickable/active by accident when documenting it)

This told me the PowerShell script wasn't just running locally — it was reaching out somewhere. My assumption at this point was that this was likely a next-stage payload download, so I went to check Log Management to see if that connection attempt actually happened and what the result was.

### Confirming the network connection

In Log Management, filtering for the IP `193.142.58.23` showed two firewall log entries:

```
Mar 05, 2022 10:29 AM  Firewall  172.16.17.38:42611 -> 193.142.58.23:80
Mar 05, 2022 10:30 AM  Firewall  193.142.58.23:80 -> 172.16.17.38:42611
```

So Roberto's machine did reach out to that external IP on port 80, right around the same time as the mshta/PowerShell activity. Pulling the raw log for that request confirmed it:

```
Request URL: http://193.142.58.23/Server.txt
Response: 404 Not Found
```

**Result: connection attempt confirmed, but the actual payload file (Server.txt) wasn't there — 404.** So the callback happened, but whatever the attacker was trying to deliver at that point either wasn't hosted anymore or the URL had already changed by the time this ran.

![Firewall log showing connection to malicious IP](./screenshots/firewall-connection.png)
![Raw log confirming 404 response](./screenshots/raw-log-404.png)

---

## Working Through The Playbook

LetsDefend's playbook for this alert walks through a structured set of questions after the initial investigation:

**Determine Suspicious Activity — is this suspicious?**
Yes. Between the low-reputation hta file, the VirusTotal detections, the obfuscated PowerShell, and the outbound connection to an external IP right after execution, this checked basically every box.

**What is the purpose of the suspicious activity performed with legal binaries for this incident?**
Answer: **Execute**. The core thing happening here is mshta.exe being used to execute a malicious file it wasn't really meant to run in this context — that's the actual abuse taking place, as opposed to something like persistence or credential theft specifically (those might come later in a real attack chain, but based on what's visible here, execution is the answer).

**Who performed the activity?**
Answer: **User**. Checking Endpoint Security confirmed this ran under Roberto's own user context, not under a separate malware/service account — meaning this was likely triggered by the user themselves running the file (classic scenario: user opens a file they shouldn't have, maybe from a phishing email or download).

**Containment**
Went to the EDR page and contained Roberto's machine — isolating it from the network to stop any further communication with the attacker's infrastructure or lateral movement while the investigation/remediation continues.

![Host containment confirmation](./screenshots/host-contained.png)

---

## Verdict

**True Positive.**

Every piece of evidence lined up consistently — a low-reputation file executed through a legitimate-but-abusable binary, confirmed malicious by the majority of VirusTotal engines, followed almost immediately by obfuscated PowerShell reaching out to an external IP address. This wasn't an edge case or something that needed a judgment call between true/false positive — the chain from execution to callback was clear and consistent.

Alert closed as True Positive, host contained, all playbook steps answered correctly for +5 points each.

---

## What I'd Do Next

If this were a real environment rather than a simulation, beyond containment I'd want to:
- Check whether that `Server.txt` file had actually been successfully delivered earlier (before the 404), since a 404 at the time I checked doesn't necessarily mean it was never live
- Pull other hosts to see if any of them also reached out to `193.142.58.23`, in case this wasn't isolated to just Roberto's machine
- Find out how the `.hta` file actually got onto Roberto's desktop in the first place — email attachment, download, USB — since that's the actual entry point and needs to be closed off, not just this one execution

---

## What Tripped Me Up

Recognizing the obfuscated PowerShell as obfuscated (rather than just "code I don't understand yet") took a moment — I had to actually read into what obfuscation looks like and why an attacker would do it before I felt confident calling it out specifically rather than just noting "this looks weird."

Also had to stop and actually look up what mshta.exe and LOLBins are before this alert made full sense — hadn't encountered either term working through this specific scenario before.

---

## Tools Used

- LetsDefend Endpoint Security (command line history, process view)
- LetsDefend Log Management (firewall logs, raw log view)
- VirusTotal (hash lookup)
- LetsDefend EDR (containment action)
