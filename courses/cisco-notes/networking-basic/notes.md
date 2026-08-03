# Notes — Networking Basics (Cisco Networking Academy)

Going through this module by module. This course is a lot bigger than Intro to Cybersecurity was — 17 modules plus checkpoint exams — so these notes are organized to match the course structure rather than grouped by topic like my last set of notes.

---

## Module 1 — Communication in a Connected World

Covers network types and the basics of how data actually moves between devices — bandwidth vs throughput being the main distinction here.

- **Bandwidth** — the theoretical maximum amount of data that can move through a connection
- **Throughput** — what you actually get in practice, which is almost always lower than bandwidth because of network conditions, congestion, overhead

I used to think these two words basically meant the same thing. They don't — bandwidth is the advertised number, throughput is the real number.

---

## Module 2 — Network Components, Types, and Connections

- **Client/server relationship** — clients request, servers respond. Sounds obvious written out, but it's the foundation almost every other network service builds on
- **Network components** — the actual physical/logical pieces (switches, routers, hosts) and what role each plays
- **ISP connectivity options** — different ways an ISP actually gets a connection to you (cable, DSL, fiber, etc.) and the tradeoffs between them

---

## Module 3 — Wireless and Mobile Networks

- How wireless networks differ from wired in terms of setup and limitations
- Mobile device connectivity — how phones and similar devices connect and roam between networks

---

## Module 4 — Build a Home Network

This is where the course goes properly hands-on for the first time.

- Home network basics — what a typical home setup actually looks like end to end
- Network technologies used specifically in home environments
- Wireless standards (the different 802.11 versions and what changed between them)
- Actually setting up a home router — this was the first real hands-on task in the course, and honestly more involved than I expected for something I'd used passively my whole life without thinking about how it worked

**Checkpoint Exam: Build a Small Network** — first of several checkpoint exams spaced through the course, testing everything up to this point before moving on.

---

## Module 5 — Communication Principles

- Communication protocols and standards — the agreed-upon rules that let different devices/vendors talk to each other
- Network communication models — this is where OSI and TCP/IP get introduced properly

---

## Module 6 — Network Media

Covers the actual physical (and non-physical) mediums data travels across — copper cabling, fiber, wireless — and where each is used and why.

---

## Module 7 — The Access Layer

- **Encapsulation** — how data gets wrapped in headers as it moves down through the layers, and the Ethernet frame specifically as the access-layer unit of this
- The access layer's role generally — this is the layer closest to end devices

**Checkpoint Exam: Network Access**

---

## Module 8 — The Internet Protocol

- Purpose of an IPv4 address — why addressing exists at all, not just what it looks like
- IPv4 address structure — network portion vs host portion

---

## Module 9 — IPv4 and Network Segmentation

- Unicast, broadcast, multicast — three different ways traffic can be addressed depending on whether it's meant for one device, all devices, or a specific group
- Types of IPv4 addresses (public/private, static/dynamic distinctions start showing up here)
- **Network segmentation** — splitting a network into smaller pieces, which ties directly into subnetting

---

## Module 10 — IPv6 Addressing Formats and Rules

- IPv4 issues — mainly address exhaustion, which is the actual reason IPv6 exists at all
- IPv6 addressing format and the shorthand rules for writing it out (dropping leading zeros, double-colon compression)

Honestly this module took more re-reading than I expected — IPv6 addresses look intimidating with all the hex characters, but the shorthand rules make them more manageable once they actually click.

---

## Module 11 — Dynamic Addressing with DHCP

- Static vs dynamic addressing — manually assigning an IP vs having it handed out automatically
- DHCPv4 configuration

**Packet Tracer lab:** *Configure DHCP on a Wireless Router* — first Packet Tracer exercise where I actually configured a service rather than just observing traffic.

**Checkpoint Exam: The Internet Protocol**

---

## Module 12 — Gateways to Other Networks

- Network boundaries — where one network ends and another begins, and how traffic crosses that line
- **NAT (Network Address Translation)** — how private IP addresses get translated to a public one so devices on a home network can actually reach the internet

**Packet Tracer lab:** *Examine NAT on a Wireless Router*

---

## Module 13 — The ARP Process

- MAC addresses vs IP addresses — two different addressing systems operating at different layers, and ARP is the bridge between them
- Broadcast containment — why ARP broadcasts don't just flood every network endlessly

**Packet Tracer lab:** *Identify MAC and IP Addresses*

---

## Module 14 — Routing Between Networks

- Why routing is needed at all — devices on different networks can't talk without something to forward traffic between them
- The routing table — how a router actually decides where to send a packet next
- Creating a LAN hands-on

**Packet Tracer labs:** *Observe Traffic Flow in a Routed Network*, *Create a LAN*

**Checkpoint Exam: Communication Between Networks**

---

## Module 15 — TCP and UDP

- TCP vs UDP — reliable, connection-based delivery vs fast, no-guarantee delivery, and why you'd choose one over the other depending on the application
- Port numbers — how a single IP address can run many different services simultaneously

---

## Module 16 — Application Layer Services

Biggest module in the course, covers the actual services people interact with daily:
- Client-server relationship revisited at the application layer specifically
- Network application services generally
- **DNS** — how domain names actually resolve to IP addresses
- Web clients/servers, FTP clients/servers, virtual terminals (Telnet/SSH), email and messaging

**Packet Tracer labs:** *The Client Interaction*, *Observe Web Requests*, *Use FTP Services*, *Use Telnet and SSH*

This module had the most Packet Tracer labs by far, which makes sense — application layer services are the part of networking most visible in daily use, so there's more to actually practice.

---

## Module 17 — Network Testing Utilities

- Troubleshooting commands — the actual tools used to diagnose what's wrong with a connection

**Packet Tracer labs:** *Use the ipconfig Command*, *Use the ping Command*

**Checkpoint Exam: Protocols for Specific Tasks**

---

## Course Final Exam

Cumulative exam covering all 17 modules.

---

## Overall Takeaway

This course was a much bigger commitment than Intro to Cybersecurity — 17 modules with checkpoint exams spaced throughout meant I couldn't just breeze through it in a weekend. The Packet Tracer labs, especially from Module 11 onward, were where things actually started sticking. Reading about NAT or DHCP is one thing; actually configuring it in Packet Tracer and watching it work (or not work, when I got a setting wrong) made it real in a way the reading alone didn't.

IPv6 addressing and the routing table logic in Module 14 were the two spots I had to go back and re-read more than once. Everything else built up gradually enough that it made sense the first time through.

See [`labs.md`](./labs.md) for a closer look at the individual Packet Tracer exercises, and [`reference.md`](./reference.md) for a condensed lookup sheet.
