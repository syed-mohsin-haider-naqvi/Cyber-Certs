# Endpoint Security (ESec) — Cisco Networking Academy

## About This Course

This one's a shift from the last few — Network Defense and Networking Devices were mostly about the network itself, this course zooms in on the actual endpoints. Windows, Linux, the operating systems people actually sit at every day, and how attacks target them specifically instead of just the network theyre connected to.

10 modules, starts with threats/attacks/vulnerabilities generally, then goes deep into network security infra, then spends a good chunk on Windows and Linux separately, then wraps up with endpoint protection and cybersecurity principles. Probably the most "hands on a real OS" course out of everything ive done so far — alot of the labs actually have u sitting in PowerShell or a Linux shell instead of just Packet Tracer.

**Status:** Completed

---

## What It Covered

- Cybersecurity threats, vulnerabilities and attacks — common threats, deception/social engineering, cyber attacks generally, wireless/mobile device attacks, application attacks
- Securing networks — current threat landscape, who's actually attacking networks and why
- Attacking the foundation — IP PDU details, IP vulnerabilities, TCP/UDP vulnerabilities
- Attacking what we do — IP services, enterprise services, mitigating common network attacks
- Wireless network communication — wireless comms basics, WLAN threats, securing WLANs
- Network security infrastructure — security devices and services

**Checkpoint Exam: Network Security**

- Windows Operating System — windows history, architecture and operations, configuration and monitoring, windows security specifically
- Linux Overview — basics, working in the shell, linux servers/clients, basic server admin, the linux file system, working with the GUI, general linux host stuff
- System and endpoint protection — defending systems/devices, antimalware, host based intrusion prevention, application security
- Cybersecurity principles, practices, and processes — the "three dimensions" thing, states of data, countermeasures

**Checkpoint Exam: OS and Endpoint Security**

---

## What Actually Took Time

Linux module (8) was the biggest one for me honestly. ive used windows my whole life basically so that module felt more like organizing stuff i sort of already knew. linux was different — navigating the filesystem, permissions, actually working in the shell instead of clicking around, that all took real practice before it stopped feeling clunky.

The attacking the foundation module (3) was also tougher then expected — going into IP PDU details and TCP/UDP vulnerabilities specifically at a level below "heres what TCP does" and more into "heres how TCP itself can be abused." connects back to stuff from Network Defense but goes further into the actual weaknesses.

Windows module had a few labs that were genuinely useful outside the course too — messing with processes/threads/handles and the registry, using task manager properly to actually monitor whats going on instead of just closing stuff that looks weird.

---

## Why This One Connects Directly To SOC Work

Out of every cisco course so far this is the one that lines up most with actual SOC analyst day to day stuff. Reading server logs, using a port scanner to find open ports, hardening a linux system, recovering passwords, investigating malware with online tools — this is basically the toolkit side of what id already been doing conceptually on HTB and LetsDefend. Doing it here in a structured way with actual windows/linux labs filled in gaps the SOC platforms dont really teach directly, they kind of assume u already know this stuff going in.

---

## Notes

- [`notes.md`](./notes.md) — module by module notes
- `labs.md` — coming once i work back through the labs (theres alot here — windows labs, linux labs, malware investigation, a couple packet tracer ones too)
- `reference.md` — condensed lookup sheet, after labs

---

*Completed after Network Defense — this one moves from network level defense down into the actual endpoint/OS level.*
