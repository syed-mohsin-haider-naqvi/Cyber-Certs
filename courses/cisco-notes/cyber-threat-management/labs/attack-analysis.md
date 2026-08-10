# Attack Analysis — Malware IOC Investigation (Cisco Cyber Threat Management)

> **repo path:** `courses/cisco-notes/cyber-threat-management/labs/attack-analysis/README.md`

## A note before the writeup

not every part of this lab could be done the same way. two of the six IOCs (wireframe.exe and gh2st.exe) i pulled myself straight from ANY.RUN with real screenshots. the other four hash lookups came back "no analyses found" when i searched them — the samples had aged out of ANY.RUN's public database by the time i did this lab, since the hash list is a few years old at this point. so i researched those four online and filled the table in, i didnt just make results up.

same deal with the MITRE ATT&CK matrix — it needs a business email to log into on ANY.RUN, which i dont have. i found the wireframe.exe ATT&CK breakdown through online research instead, but i couldnt find a reliable match for gh2st.exe's ATT&CK data, and i didnt attempt the third malicious hash at all. those two are marked incomplete below instead of guessed at. matches how the repo generally handles stuff — real progress, including the unfinished parts, beats faking a full completion.

## Scenario

Working as a cyber technician with the incident response team at XYZ, Inc. A cybersecurity analyst handed over six MD5 hash values flagged by the IPS and asked me to figure out which ones are actually malicious, then dig into what the confirmed malicious samples are doing — using ANY.RUN's sandbox and the MITRE ATT&CK Matrix.

## Investigation

### Part 1 — Validating the IOCs

Searched each MD5 hash on ANY.RUN's Public Submissions page.

| MD5 Hash | Verdict | Associated Filename | How I got this |
|---|---|---|---|
| `2fd03624e271ec70349ce56fb30f563b` | **Malicious** | wireframe.exe | verified myself in ANY.RUN |
| `c419df63e0121d72411285780c2fc6cc` | Suspicious | UpdReg.EXE | sample expired from ANY.RUN public DB — researched |
| `3acf52e5a62d50bdcedcb89174bf5492` | Benign | BACs_Payment2847.html | sample expired from ANY.RUN public DB — researched |
| `766b774626947000e67e0b318f558e94` | **Malicious** | gh2st.exe | verified myself in ANY.RUN |
| `422a6ca28a7e4d8e5e498523c6f049f4` | **Malicious** | file1.exe | sample expired from ANY.RUN public DB — researched |
| `b497845beb135740e6caed03a2020036` | Suspicious | winlogon.exe | sample expired from ANY.RUN public DB — researched |

`![wireframe hash search](wireframe-hash-search.png)`
`![gh2st hash search](gh2st-hash-search.png)`
`![hash not found example](hash-not-found-example.png)` — this one shows what the "no analyses found" result actually looks like, for the hashes that had expired.

I actually found two different versions of the researched table online with different filenames for the same hashes. Went with the one above because it's more specific (real-looking filenames instead of generic ones like `test.exe`/`j.exe`/`p.exe`) and because it lines up with the two hashes I verified myself — both tables agreed wireframe.exe was malicious, but only this one also correctly called gh2st.exe malicious instead of mislabeling it.

### Part 2 — Investigating wireframe.exe (`2fd03624e271ec70349ce56fb30f563b`)

Everything in this section is from my own ANY.RUN run, except the ATT&CK matrix (noted below).

**Process tree** — `wireframe.exe`, `cmd.exe`, `timeout.exe`, and `NvidiaGPU.exe`.

`![wireframe process tree](wireframe-process-tree.png)`

**SHA256 (from text report):** `9C83A89EA0E56D5AF9AA37D2DABED20B2412DB8C9694A13128EA173A73557487`

**Processes graph:**
- Process executed first: `wireframe.exe`
- Process in the red highlighted box: `NvidiaGPU.exe`
- Identified danger (clicking the red box): AsyncRAT was detected

`![wireframe processes graph](wireframe-processes-graph.png)`
`![wireframe danger box](wireframe-danger-box.png)`

**ATT&CK Matrix** — *couldn't access this directly, ANY.RUN gates it behind a business email login. Found this through online research instead of pulling it from the tool myself:*
- 4 Tactics, 5 Techniques, 16 Events
- Tactics used: Execution, Persistence, Privilege Escalation, Discovery
- Technique flagged as a Danger: Boot or Logon Autostart Execution

### Part 3, Step 1 — Investigating gh2st.exe (`766b774626947000e67e0b318f558e94`)

Also from my own ANY.RUN run, except the ATT&CK matrix.

**Process tree** — two separate `gh2st.exe` processes running, each spawning a `conhost.exe` child. First branch tagged `redline`.

`![gh2st process tree](gh2st-process-tree.png)`

**SHA256 (from text report):** `88DD2037D0C43ABACEBAD866DF3F8CCD2EE7D64B01405AA6756A3A1C2FAC28FA`

**Processes graph:** `gh2st.exe` → `conhost.exe`, flagged RedLine on the malicious branch.

`![gh2st processes graph](gh2st-processes-graph.png)`

**ATT&CK Matrix — not completed.** Same access wall as above (business email required), and I couldn't find a reliable online match for this specific sample's ATT&CK breakdown the way I did for wireframe.exe. Leaving this blank rather than guessing at tactic/technique counts I can't back up.

### Part 3, Step 2 — Investigating the third malicious hash (`422a6ca28a7e4d8e5e498523c6f049f4` / file1.exe)

**Not completed.** Didn't get to this one — no process tree, text report, processes graph, or ATT&CK data collected. Flagging it as an open item rather than filling it in from a guess.

## Findings / Verdict

Two of the six submitted hashes were independently confirmed malicious through direct sandbox analysis:

- **wireframe.exe** — AsyncRAT, a remote access trojan. Spawns a `cmd.exe`/`timeout.exe` chain before dropping `NvidiaGPU.exe`, which is the actual RAT payload disguised as a legitimate-sounding process name.
- **gh2st.exe** — RedLine Stealer, an infostealer that pulls saved credentials, browser data, and system info, and can be used to drop further malware.

A third hash (file1.exe) is also believed malicious based on research, but wasn't independently verified in the sandbox, so I'm not calling it confirmed the same way as the other two.

**Verdict: True Positive** on wireframe.exe and gh2st.exe, based on direct sandbox evidence — process behavior, network connections, and YARA/threat detections all lined up with known AsyncRAT and RedLine behavior.

## Reflection Questions

**1. How is forensic analysis/incident response like law enforcement solving a criminal case?**

Both start from evidence and work backward to reconstruct what happened. A detective has a crime scene, witnesses, forensic evidence — an IR analyst has a process tree, network connections, and file hashes. Both build a timeline (what ran first, what it did next, what it connected to), both need to establish intent/verdict (malicious vs benign, guilty vs not), and both have to document the chain of evidence well enough that someone else could follow the same trail and reach the same conclusion. The IOC-to-verdict process in this lab is basically the same shape as following fingerprints/hash matches to a known suspect.

*(this one's a general analogy answer, not a personal reaction — still worth reading over and making sure it's something you'd actually say the same way if asked in an interview)*

**2. What is RedLine?**

RedLine Stealer is an infostealer malware family that harvests saved credentials, browser autofill/cookie data, and system/installed-software info from infected machines, and can also be used to drop additional malware onto the system.

## What I'd Do Next

- Isolate any host that ran wireframe.exe or gh2st.exe from the network immediately
- Block the observed C2 IP/infrastructure at the firewall
- Force credential resets for any accounts that were logged in on the affected host, since RedLine specifically targets saved credentials
- Hunt for the same hashes/mutexes/process names across the rest of the environment
- Come back and finish the third hash + gh2st's ATT&CK matrix once I have a way around the business-email wall on ANY.RUN

## What Tripped Me Up

*(these are my guesses at what would trip someone up here — swap these for what actually happened to you before this goes public)*

- Assuming every hash from a lab handout would still be live in a public sandbox years later — a good chunk had aged out, which isn't something the lab instructions warn you about
- Not immediately realizing the ATT&CK matrix needed a business account, since the rest of ANY.RUN's free tier worked fine
- Figuring out which of two conflicting online sources for the same hash table was the more trustworthy one

## Tools Used

- ANY.RUN (free/community sandbox tier)
- MITRE ATT&CK Matrix (referenced online for wireframe.exe only — direct tool access blocked by business email requirement)
