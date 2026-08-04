# Notes — Networking Basics (Cisco Networking Academy)

Going through module by module again like i did for the other cisco courses. This one's got 17 modules total plus checkpoints so its a bigger course then Intro to Cybersecurity was.

---

## Module 1 — Communication in a Connected World

Network types and how data actually moves between devices. Main thing here is bandwidth vs throughput:

- **Bandwidth** — theoretical max of a connection
- **Throughput** — what u actually get in practice, almost always less then bandwidth cause of congestion and overhead and stuff

I used to think these were basically the same word tbh. Bandwidth is the advertised number, throughput is the real one.

---

## Module 2 — Network Components, Types, and Connections

- Client/server relationship — client asks, server answers, sounds obvious but basically everything else builds on this
- Network components — the actual pieces (switches, routers, hosts) and what each does
- ISP connectivity options — different ways an ISP gets a connection to u (cable, DSL, fiber) and tradeoffs between them

---

## Module 3 — Wireless and Mobile Networks

How wireless differs from wired setup wise, plus mobile device connectivity and roaming between networks.

---

## Module 4 — Build a Home Network

First real hands on module.

- Home network basics
- Network tech used specifically at home
- Wireless standards (the different 802.11 versions)
- Actually setting up a home router — first proper hands on task, more involved then i expected for something ive used passively my whole life without thinking about it

**Checkpoint Exam: Build a Small Network**

---

## Module 5 — Communication Principles

- Communication protocols/standards — the agreed rules that let different devices talk to eachother
- Network communication models — OSI and TCP/IP get introduced properly here

---

## Module 6 — Network Media

The actual physical (and wireless) mediums data moves across, copper, fiber, wireless, where each gets used and why.

---

## Module 7 — The Access Layer

- Encapsulation — how data gets wrapped in headers moving down the layers, ethernet frame specifically here
- The access layer role generally — closest layer to end devices

**Checkpoint Exam: Network Access**

---

## Module 8 — The Internet Protocol

- Why IPv4 addressing exists at all, not just what it looks like
- IPv4 structure — network portion vs host portion

---

## Module 9 — IPv4 and Network Segmentation

- Unicast/broadcast/multicast — three ways traffic can be addressed
- Types of IPv4 addresses (public/private, static/dynamic starts here)
- Network segmentation — splitting into smaller pieces, ties into subnetting

---

## Module 10 — IPv6 Addressing Formats and Rules

- IPv4 issues — mainly just running out of addresses, thats the actual reason IPv6 exists
- IPv6 format and shorthand rules

This one took more re reading then i expected. the addresses look intimidating with all the hex but the shorthand rules make it manageable once it actually clicks. took me a bit longer then it probably shouldve.

---

## Module 11 — Dynamic Addressing with DHCP

- Static vs dynamic — manual IP vs auto assigned
- DHCPv4 config

**Lab:** Configure DHCP on a Wireless Router — first lab where i actually configured a service instead of just watching traffic

**Checkpoint Exam: The Internet Protocol**

---

## Module 12 — Gateways to Other Networks

- Network boundaries, where one network ends and another begins
- NAT — how private IPs get translated to a public one so devices can actually reach the internet

**Lab:** Examine NAT on a Wireless Router

---

## Module 13 — The ARP Process

- MAC vs IP — two totally different addressing systems at different layers, ARP bridges them
- Broadcast containment — why ARP doesnt just flood everything forever

**Lab:** Identify MAC and IP Addresses

---

## Module 14 — Routing Between Networks

- Why routing exists — devices on different networks cant talk without something forwarding between them
- The routing table, how a router decides where to send stuff next
- Creating a LAN hands on

**Labs:** Observe Traffic Flow in a Routed Network, Create a LAN

**Checkpoint Exam: Communication Between Networks**

---

## Module 15 — TCP and UDP

- TCP vs UDP — reliable connection based delivery vs fast no guarantee delivery, why youd pick one over the other
- Port numbers — how one IP can run a bunch of services at once

---

## Module 16 — Application Layer Services

Biggest module, covers stuff people actually interact with daily:
- Client server relationship again but at application layer specifically
- DNS — how domain names resolve to IPs
- Web clients/servers, FTP, telnet/SSH, email/messaging

**Labs:** The Client Interaction, Observe Web Requests, Use FTP Services, Use Telnet and SSH

Most labs by far in this module, makes sense since application layer stuff is what u actually see and use day to day.

---

## Module 17 — Network Testing Utilities

- Troubleshooting commands, the actual tools to figure out whats wrong

**Labs:** Use the ipconfig Command, Use the ping Command

**Checkpoint Exam: Protocols for Specific Tasks**

---

## Course Final Exam

Covers all 17 modules.

---

## Overall

Bigger commitment then Intro to Cybersecurity for sure, cant just breeze through this one in a weekend with checkpoints spaced throughout. Packet Tracer labs from module 11 onward is where stuff actually started sticking for me — reading about NAT or DHCP is one thing, actually configuring it and watching it work (or not work when i messed something up) made it real.

IPv6 and the routing table logic in module 14 were the two i had to go back and reread the most. everything else built up gradually enough that it made sense first time through mostly.

See [`labs.md`](./labs.md) for the actual Packet Tracer stuff and [`reference.md`](./reference.md) for the condensed version.
