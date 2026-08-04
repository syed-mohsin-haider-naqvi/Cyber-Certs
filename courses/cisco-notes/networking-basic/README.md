# Networking Basics — Cisco Networking Academy (Skills for All)

## About This Course

This is the first proper networking course i did, comes after Intro to Cybersecurity. Way more hands on then that one — 17 modules plus checkpoint exams along the way, built around actually understanding how a network moves data instead of just security concepts at a high level.

Went into this already having done Intro to Cybersecurity so some of it wasnt totally new, but the actual networking fundamentals — how devices talk to eachother, subnetting, the whole OSI/TCP-IP thing — that part was genuinely new and took a few passes before it stuck properly.

**Status:** Completed

---

## What It Covered

17 modules total, roughly grouped like this:

- Modules 1-4: basic networking concepts, wireless/mobile networks, and building an actual home network (first hands on stuff in the course)
- Modules 5-7: communication protocols and standards, the OSI/TCP-IP models properly, network media types, the access layer and encapsulation
- Modules 8-11: IPv4 addressing, network segmentation, IPv6, and DHCP
- Modules 12-14: NAT, ARP, and routing between networks
- Modules 15-17: TCP vs UDP, application layer stuff (DNS, web, FTP, telnet/SSH, email), and network troubleshooting commands

Checkpoint exams show up after modules 4, 7, 11, and 14, then a final exam at the end covering everything.

---

## What Actually Took Time

IPv6 addressing in module 10 took more re-reading then i expected. the hex characters look intimidating at first and the shorthand rules (dropping leading zeros, using :: for compressed zero blocks) didnt click right away.

Subnetting was also rough honestly. watching someone explain it makes it look easy, actually doing it myself the first few times i kept second guessing my own math. had to just do a bunch of extra practice problems outside the course before it stopped feeling shaky.

Packet Tracer itself was easier then expected though — figured a whole simulation tool would be confusing but building small setups and watching traffic actually move (or fail to move when i messed up a config) made a lot of the earlier theory stuff make more sense in hindsight.

---

## Why This Mattered Later

This course is basically why i wasnt starting from zero when i got into cloud networking stuff (VPCs, subnets, security groups all use similar logic) or OT/ICS network segmentation later — same underlying ideas, just different context. building and breaking a small network in Packet Tracer first made those later concepts way less abstract when i got to them.

---

## Notes

- [`notes.md`](./notes.md) — module by module study notes
- [`labs.md`](./labs.md) — the Packet Tracer labs, commands used, and which ones i redid properly with screenshots
- [`reference.md`](./reference.md) — quick lookup sheet for commands and key concepts

---

*Completed before moving into cloud networking and OT/ICS coursework.*
