# Networking Devices and Initial Configuration — Cisco Networking Academy

## About This Course

This one sits between Networking Basics and Network Defense in terms of what it covers — it's less about attacks and defense, more about the actual mechanics of how networks are designed and how you configure a Cisco device from scratch. Binary and hex number systems, Ethernet switching at the frame level, the network and transport layers properly broken down, and then finally getting into the Cisco IOS command line and building a small network end to end.

Out of the three Cisco courses I've done so far, this is the one that felt most like "foundational plumbing" — the stuff that doesn't look exciting on its own but that everything else quietly depends on.

**Status:** Completed

---

## What It Covered

- **Network design** — what makes a network reliable, and hierarchical network design principles
- **Cloud and virtualization** — cloud services and virtualization at a conceptual level, earlier and lighter than the full Cloud Security module in Network Defense
- **Number systems** — binary and hexadecimal, and why networking leans on both constantly (IP addressing, MAC addresses, subnetting math)
- **Ethernet switching** — Ethernet itself, frame structure, MAC addresses, and how a switch actually builds and uses its MAC address table
- **Network layer** — network layer characteristics, and the IPv4 and IPv6 packet structures specifically
- **IPv4 address structure** — going deeper into IPv4 structure than Networking Basics did
- **Address resolution** — ARP, revisited here in more depth
- **IP addressing services** — DNS and DHCP as services, not just concepts
- **Transport layer** — a full breakdown of TCP and UDP, port numbers, the TCP communication process, reliability and flow control, and UDP communication specifically
- **The Cisco IOS command line** — actually navigating IOS, command structure, and viewing device information
- **Building a small Cisco network** — basic switch configuration, initial router settings, securing devices, and configuring a default gateway, all together as one build
- **ICMP** — ICMP messages, and using ping/traceroute for real testing

---

## Why This One Was Different From The Other Two

Networking Basics taught me how networks generally work. Network Defense taught me how they get attacked and defended. This course is the one that actually taught me how to sit down at a Cisco device and configure it — Module 10 (IOS command line) and Module 11 (building a small network) are where things stopped being conceptual and became "type this, verify that, fix it if it's wrong."

The binary and hex module (3) mattered more than I expected going in. I'd been doing IP addressing math somewhat mechanically before this, and actually working through binary conversion properly made subnetting logic (from Networking Basics) make a lot more sense in hindsight — I understood the "why" behind the math I'd already been doing.

The transport layer module (9) was also the most thorough TCP/UDP coverage I've had — Networking Basics introduced TCP vs UDP at a surface level, this course goes into the actual communication process, not just the definition.

---

## Notes

- [`notes.md`](./notes.md) — module-by-module study notes
- `labs.md` — coming once I work back through the Packet Tracer labs (IOS navigation, initial router/switch config, SSH setup, ARP in Wireshark, ICMP testing)
- `reference.md` — coming as a condensed lookup sheet once labs are documented

---

*Completed alongside Network Defense, filling in the device-configuration and network-design fundamentals that both Networking Basics and Network Defense build on top of.*
