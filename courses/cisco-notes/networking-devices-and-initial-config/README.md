# Networking Devices and Initial Configuration — Cisco Networking Academy

## About This Course

Third cisco course i did, comes after Networking Basics and around the same time as Network Defense. This one's less about attacks, more about the actual mechanics — how networks get designed and how you actually sit down and configure a cisco device from nothing. Binary and hex, ethernet at the frame level, network and transport layers, then finally the IOS command line and building a small network from scratch.

Out of the three this is the one that felt least exciting going in and turned out to matter the most honestly. boring plumbing stuff. but everything else leans on it.

**Status:** Completed

---

## Whats In It

- Network design — reliable networks, hierarchical design (core/distribution/access, the usual model)
- Cloud and virtualization, but lighter then the full module in Network Defense — more "heres what it is" then "heres how to secure it"
- Number systems. binary, hex. why networking cares about both (MAC addresses, IPv6, subnetting math)
- Ethernet switching — frames, MAC addresses, how a switch actually builds it's MAC table instead of just flooding traffic everywhere
- Network layer stuff — IPv4 and IPv6 packet structure specifically, side by side
- IPv4 address structure in more depth then Networking Basics covered
- ARP again but deeper, plus this is where u actually watch ARP traffic in wireshark instead of just reading about it
- DNS and DHCP as actual running services
- Transport layer — probably the most thorough TCP/UDP breakdown out of anything ive done so far. port numbers, the TCP handshake process, flow control, UDP's whole different approach
- The cisco IOS command line itself — navigation, command structure, show commands
- Building a small cisco network end to end — switch config, router config, securing the devices, default gateway
- ICMP, ping, tracert — actual diagnostic use not just definitons

---

## What Actually Stuck

Module 3, the number systems one, mattered way more then i expected walking in. i'd already gotten through subnetting in Networking Basics but kinda just followed the steps without really getting why they worked. sitting down and doing binary/hex conversion properly here made the earlier subnetting stuff make sense retroactivley. annoying but useful, learning something out of order like that.

Module 11 — building the small network — is probably the best module across all three cisco courses so far. First time it felt like i was doing something real instead of learning about something real. configure the switch, configure the router, lock it down, get the gateway right. small but its a complete thing start to finish.

Transport layer module was also more then i expected — Networking Basics gives u TCP vs UDP at a surface level, this one actually goes into the handshake and reliability mechanics and stuff.

---

## Notes

- [`notes.md`](./notes.md) — module notes
- `labs.md` — coming once i redo the packet tracer labs properly (IOS navigation, router/switch config, SSH, ARP in wireshark, ICMP testing)
- `reference.md` — after that, condensed lookup version

---

*Done around the same time as Network Defense — this one's more about the device/config fundementals both the other two courses kind of assume u already have.*
