# Notes — Endpoint Security (Cisco Networking Academy)

Same format as the other cisco notes, module by module. This one's 10 modules and honestly probably the densest course so far in terms of actual hands on labs — windows and linux both get proper coverage instead of just network theory.

---

## Module 1 — Cybersecurity Threats, Vulnerabilities, and Attacks

- Common threats — general overview, revisits some stuff from Intro to Cybersecurity but goes further
- Deception — social engineering specifically, theres a lab here exploring different techniques which was useful cause it forces u to actually think through examples instead of just reading definitions
- Cyber attacks — attacks generally, broader categories
- Wireless and mobile device attacks — specific to those device types
- Application attacks — attacks that target the application layer/software itself rather then network or OS

---

## Module 2 — Securing Networks

- Current state of affairs — basically the real world threat landscape right now, not just theoretical
- Who is attacking our network — actual threat actor types (script kiddies vs organized groups vs nation state stuff, that whole spectrum)

**Lab:** Investigate a Threat Landscape

---

## Module 3 — Attacking the Foundation

This one got technical fast.

- IP PDU details — going deeper into the actual packet structure then previous courses did
- IP vulnerabilities — where IP itself can be exploited
- TCP and UDP vulnerabilities — same thing but for the transport layer protocols

Honestly this module was harder then i expected going in. Network Defense and Networking Devices both covered TCP/UDP and IP pretty thoroughly already but this one goes a level deeper into "how do you actually abuse this" instead of just "how does this work." took some rereading.

---

## Module 4 — Attacking What We Do

- IP services — services that run on top of IP and how theyre targeted
- Enterprise services — bigger picture enterprise level services
- Mitigating common network attacks — the defensive side after all the attack stuff

**Labs:** Exploring DNS Traffic, Install a Virtual Machine on a Personal Computer, Attacking a mySQL Database, Reading Server Logs, Recommend Threat Mitigation Measures

Alot of labs in this module. The mySQL one specifically was interesting, first time the course had u actually attack something (in a safe lab environment obviously) instead of just defend or observe.

---

## Module 5 — Wireless Network Communication

- Wireless communications — basics revisited from a security angle
- WLAN threats — threats specific to wireless networks
- Secure WLANs — actually securing one

**Labs:** Configure Basic Wireless Security, Troubleshoot a Wireless Connection

---

## Module 6 — Network Security Infrastructure

- Security devices — the actual hardware/tools (firewalls, IPS, etc)
- Security services — services layered on top of the devices

**Lab:** Access Control List Demonstration

**Checkpoint Exam: Network Security**

---

## Module 7 — The Windows Operating System

- Windows history — brief background
- Windows architecture and operations — how windows is actually structured under the hood
- Windows configuration and monitoring — actually configuring and keeping an eye on a windows system
- Windows security — security specific windows features and settings

**Labs:** Exploring Processes, Threads, Handles, and Windows Registry / Create User Accounts / Using Windows PowerShell / Windows Task Manager / Monitor and Manage System Resources in Windows

This module had genuinely useful labs outside just passing the course. Ive used windows forever without really understanding whats going on with processes/threads/handles, or how the registry actually works. Task manager specifically — i used to just close whatever looked weird, now i actually understand more of what im looking at before deciding somethings a problem.

---

## Module 8 — Linux Overview

Biggest module, and the one that took the most adjustment for me personally since ive barely used linux before this.

- Linux basics
- Working in the Linux shell — actually typing commands instead of clicking
- Linux servers and clients
- Basic server administration
- The Linux file system — totally different mental model then windows file explorer
- Working with the Linux GUI
- Working on a Linux host generally

**Labs:** Working with Text Files in the CLI / Getting Familiar with the Linux Shell / Use a Port Scanner to Detect Open Ports / Linux Servers / Locating Log Files / Navigating the Linux Filesystem and Permission Settings / Configure Security Features in Windows and Linux

This module took way longer then any other one so far honestly. Coming from windows my whole life, navigating a filesystem through commands instead of just clicking felt slow and clunky at first, kept having to look up basic stuff like how to move between directories or list files properly. Got more comfortable by the end but this is the module id say i still need more practice with outside the course.

---

## Module 9 — System and Endpoint Protection

- Defending systems and devices — general endpoint defense
- Antimalware protection
- Host based intrusion prevention — HIPS specifically, different from network based
- Application security — securing the application layer at the endpoint level

**Labs:** Harden a Linux System / Recover Passwords / Recommend Endpoint Security Measures / Online Malware Investigation Tools

The harden a linux system lab connects directly back to how clunky module 8 felt — by this point id had enough linux practice that actually hardening a system (disabling stuff that shouldnt be running, tightening permissions) made more sense then it wouldve earlier in the course.

---

## Module 10 — Cybersecurity Principles, Practices, and Processes

- The three dimensions — a framework the course uses to tie security principles together (didnt fully click what this meant until doing the actual quizlet/cube lab honestly)
- States of data — data at rest, in transit, in use, and how protection differs for each
- Cybersecurity countermeasures — pulling everything together into actual defensive measures

**Labs:** The Cybersecurity Sorcery Cube Scatter Quizlet / File and Data Integrity Checks / Explore File and Data Encryption / Data Security Challenges

**Checkpoint Exam: OS and Endpoint Security**

---

## Endpoint Security (ESec) Final Exam

Covers all 10 modules.

---

## Overall

This course is where alot of the SOC lab stuff ive done on HTB and LetsDefend actually got explained properly instead of just assumed. Reading server logs, port scanning, malware investigation, hardening systems — ive been doing versions of this in the labs already but this course actually walked through why and how instead of just having me follow steps.

Linux (module 8) was the hardest adjustment by far, mostly just cause of lack of prior exposure rather then the material being conceptually difficult. Attacking the foundation (module 3) was the toughest conceptually — going a level deeper into IP/TCP/UDP vulnerabilities then earlier courses did.

Labs and reference sheet to follow — this course has more hands on labs then any other cisco course ive done so far, so same approach as before, gonna pick a handful to redo properly with real screenshots rather then try to cover all of them.
