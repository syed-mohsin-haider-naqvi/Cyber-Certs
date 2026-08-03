# Networking Basics — Cisco Networking Academy (Skills for All)

## About This Course

This is Cisco's Networking Basics course through Skills for All (Networking Academy). Compared to the Intro to Cybersecurity course, this one's a lot more hands-on — it's built around setting up and understanding a small office/home office (SOHO) network rather than just covering security concepts at a high level.

I went into this one already having done Intro to Cybersecurity, so some of the security-adjacent stuff wasn't brand new, but the actual networking fundamentals — how devices talk to each other, how data actually moves, subnetting — that part was genuinely new territory for me and took a few passes to properly stick.

**Status:** Completed

---

## What It Covered

- How networks are actually built — devices, cabling, how a home/small office network is structured
- The OSI and TCP/IP models, and how they map onto each other (this one took me a while to get comfortable with)
- IP addressing and subnetting, including CIDR notation
- Common network devices — routers, switches, access points — what each one actually does versus what people assume they do
- Basic Cisco IOS and the CLI — navigating and running basic commands on Cisco devices
- Packet Tracer — Cisco's simulation tool, used for building and testing network setups without needing physical hardware
- Basic network security concepts — traffic analysis and defending against common network-level threats, tied back into what I'd already covered in Intro to Cybersecurity

---

## What Actually Took Time To Understand

Subnetting was the one that slowed me down the most. Watching someone explain it in a video makes it look straightforward, but actually sitting down and working out a subnet mask myself the first few times, I kept second-guessing the math. It didn't fully click until I just did a bunch of practice problems on my own outside the course material.

Packet Tracer was the opposite — I expected it to be confusing since it's a full simulation tool, but it turned out to be one of the more intuitive parts. Being able to actually build a small topology, plug in devices, and watch traffic behave (or fail to behave, when I misconfigured something) made the OSI model concepts land in a way that just reading about them didn't.

---

## Why This Mattered For What I'm Building Toward

This course is the reason I'm not starting from zero when I get into cloud networking (VPCs, subnets, security groups) or OT/ICS network segmentation later on — a lot of that is the same underlying logic, just applied in AWS or an industrial context instead of a home router. Having actually built and broken a small network in Packet Tracer first made those later concepts feel less abstract.

---

## Notes

- [`notes.md`](./notes.md) — my study notes from working through the material
- [`labs.md`](./labs.md) — Packet Tracer exercises and hands-on activities from the course
- [`reference.md`](./reference.md) — quick-lookup sheet for OSI/TCP-IP layers, subnetting, and common commands

---

*Completed as part of building networking fundamentals before moving into cloud networking and OT/ICS coursework.*
