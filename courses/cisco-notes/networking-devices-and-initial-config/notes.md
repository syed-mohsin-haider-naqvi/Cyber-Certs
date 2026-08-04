
# Notes — Networking Devices and Initial Configuration (Cisco Networking Academy)

Same format as my other cisco notes, module by module. 12 modules this time and probably the most config heavy of the three courses so far.

---

## Module 1 — Network Design

Reliable networks — what actually makes one dependable, not just working on day one. And heirarchical design, which is basically dont build a network flat, build it in layers (core, distribution, access) so it doesnt turn into a mess once it grows.

---

## Module 2 — Cloud and Virtualization

Cloud and cloud services, virtualization — the idea of running virtual stuff on top of physical hardware, which cloud computing is basically built on top of. this is a lighter version of the topic, Network Defense has a whole seperate module that goes way deeper into securing cloud environments specifically. this one's more "heres what it is" territory.

---

## Module 3 — Number Systems

Binary. hex. why networking runs on both — MAC addresses and IPv6 use hex constantly cause its a shorter way to write out binary values without it becoming unreadable.

Didnt expect this module to matter as much as it did. i'd already gotten through the subnetting stuff back in Networking Basics, sort of mechanically — follow the steps, get the answer, move on. actually sitting with binary/hex conversion here made that earlier subnetting logic click properly, after the fact. kind of backwards, learning the why after already knowing the how, but it worked out.

**Checkpoint Exam: Characteristics of Network Design**

---

## Module 4 — Ethernet Switching

Ethernet itself, frame structure (this builds on encapsulation from Networking Basics but goes deeper into ethernet specifically), MAC address structure — vendor prefix plus the device specific part — and then the MAC address table itself. how a switch actually learns which MAC lives on which port instead of just blasting every frame out every port like a hub would basically.

---

## Module 5 — Network Layer

Network layer characterstics — what its actually responsible for versus the layers above and below. then IPv4 packet structure and IPv6 packet structure, feild by feild, side by side. useful seeing them next to eachother, the structures are genuinely different not just "same thing but longer address."

---

## Module 6 — IPv4 Address Structure

Goes deeper then Networking Basics did. that course covered IPv4 addressing generally, this one's specifically about structure.

**Checkpoint Exam: Network Addressing**

---

## Module 7 — Address Resolution

ARP again — covered before but more depth here, and this is where the actual hands on ARP stuff lives. examining the ARP table directly, and watching ARP traffic in wireshark.

Seeing it in wireshark is what made it click tbh. reading "ARP resolves IP to MAC" is one thing, watching the broadcast go out and a specific device answer back is different, u can actually see it happen instead of just trusting the definition.

---

## Module 8 — IP Addressing Services

DNS and DHCP but treated here as actual services running on the network rather then abstract concepts. small shift in framing but it matters i think.

---

## Module 9 — Transport Layer

Most thorough transport layer coverage out of all three cisco courses combined, easily.

Transportation of data generally then TCP overview and UDP overview covered seperately (more depth then the Networking Basics comparison), port numbers again with more context this time, and then the actual TCP communication proccess — this is where the three way handshake shows up properly. reliability and flow control — how TCP actually gaurantees stuff gets there and manages pacing. then UDP communication which is basically the opposite philosophy, send it and dont worry about it.

**Checkpoint Exam: ARP, DNS, DHCP and the Transport Layer**

---

## Module 10 — The Cisco IOS Command Line

This is where it stops being "understand networking" and starts being "operate a cisco device."

IOS navigation — moving between user exec, priviliged exec, global config, that whole mode structure. command structure — how IOS syntax is actually built. viewing device info — the show commands u use constantly to check whats actually going on with a device.

**Labs:** Navigate the IOS, Use Cisco IOS Show Commands

---

## Module 11 — Build a Small Cisco Network

The main event of the course honestly. broken into stages:

Basic switch config from a blank state. initial router settings. securing the devices — actually locking things down instead of leaving default acess sitting open. configuring the default gateway so devices actually know where to send traffic leaving the local network.

**Labs:** Implement Basic Connectivity, Configure Initial Router Settings, Configure SSH, Build a Switch and Router Network (tutored), Troubleshoot Default Gateway Issues

Everything from Module 1 through 10 basically feeds into this module. its the first point in the course where it actually felt like doing the job instead of learning about the job if that makes sense.

---

## Module 12 — ICMP

ICMP messages, then ping and tracert for actual diagnostics — not just running them cause the lab says to but understanding what ur actually looking at in the output.

**Labs:** Verify IPv4 and IPv6 Addressing, Use Ping and Traceroute to Test Network Connectivity, Use ICMP to Test and Correct Network Connectivity

**Checkpoint Exam: Configure Cisco Devices**

---

## Course Final Exam

Covers everything, all 12 modules.

---

## Overall

Module 3 was the quiet MVP here honestly — doesnt look important on paper, ended up being the thing that made an earlier courses material actually make sense. Module 11 was the best module across all three cisco courses so far in terms of just feeling like real complete work, small network but built and secured start to finish.

Labs and refrence sheet coming once i get through the packet tracer excercises again, going to redo a handful properly rather then try to cover everything.
