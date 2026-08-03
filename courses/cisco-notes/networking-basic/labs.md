# Labs — Networking Basics (Cisco Networking Academy)

Packet Tracer exercises from the course, in the order they appear. Each one builds on something covered in the notes for that module — putting them here separately since there ended up being more hands-on labs in this course than I expected, and they deserve their own space rather than being buried inside the module notes.

---

## 4.4.4 — Configure a Wireless Router and Client

**Module:** 4 — Build a Home Network

First real hands-on task in the course. Set up a wireless router and got a client device connected to it. Sounds basic, but this was the first time I actually walked through router configuration screen by screen instead of just using a router that was already set up for me at home.

---

## 8.1.3 — Connect to a Web Server

**Module:** 8 — The Internet Protocol

Configuring a device with an IPv4 address and getting it to actually reach a web server. Useful for making the abstract "IP addresses let devices find each other" idea concrete — you can see the request actually leave the client and hit the server.

---

## 11.2.3 — Configure DHCP on a Wireless Router

**Module:** 11 — Dynamic Addressing with DHCP

Set up DHCP so that devices connecting to the router got IP addresses automatically instead of needing manual configuration. This is the lab where dynamic addressing actually clicked for me — before this it was just a definition, after this I'd actually watched a client pull an address from the pool.

---

## 12.2.2 — Examine NAT on a Wireless Router

**Module:** 12 — Gateways to Other Networks

Looked at how NAT translates private addresses to a public one. This lab is more about observing than configuring — watching how the router handles the translation rather than building it from scratch.

---

## 13.1.3 — Identify MAC and IP Addresses

**Module:** 13 — The ARP Process

Exercise in pulling MAC and IP addresses off devices and understanding which is which and why both exist. Reinforced the Module 13 point that these are two separate addressing systems operating at different layers, not two names for the same thing.

---

## 14.3.3 — Observe Traffic Flow in a Routed Network

**Module:** 14 — Routing Between Networks

Watched how traffic actually moves once routing is involved rather than staying on a single local network. Useful for seeing the routing table concept from the notes actually being used in real time rather than just described.

---

## 14.3.4 — Create a LAN

**Module:** 14 — Routing Between Networks

Built a small LAN from scratch. This was the first lab that felt like actually constructing something rather than configuring one setting on an existing setup — closer to what I imagine real network setup work looks like.

---

## 16.1.5 — The Client Interaction

**Module:** 16 — Application Layer Services

Basic client-server interaction exercise, laying the groundwork before the more specific application-layer labs that follow.

---

## 16.4.3 — Observe Web Requests

**Module:** 16 — Application Layer Services

Watched an actual web request happen — client sends the request, server responds. Ties directly back into the 8.1.3 lab but goes further into what's actually happening at the application layer during that exchange.

---

## 16.5.3 — Use FTP Services

**Module:** 16 — Application Layer Services

Set up and used FTP to transfer files between a client and server. First time actually using a protocol other than plain web traffic in the labs.

---

## 16.6.4 — Use Telnet and SSH

**Module:** 16 — Application Layer Services

Compared Telnet and SSH directly. This lab is where the difference between them stopped being abstract — Telnet sends everything in plaintext, SSH doesn't, and you can genuinely see why that distinction actually matters once you're the one connecting to a device.

---

## 17.1.3 — Use the ipconfig Command

**Module:** 17 — Network Testing Utilities

Basic but genuinely useful — pulling actual configuration details off a device using ipconfig. Simple command, but it's one I've already gone back to using outside the course just to check things.

---

## 17.1.6 — Use the ping Command

**Module:** 17 — Network Testing Utilities

Used ping to test connectivity between devices. Straightforward lab, but a good closing point for the course — basically the simplest troubleshooting tool, after 17 modules building up everything that could go wrong for it to be diagnosing.

---

## Overall

Doing these roughly in course order made the later ones easier — by the time I got to the Module 16 application layer labs, configuring things in Packet Tracer felt normal instead of intimidating, which wasn't the case back at 4.4.4. The DHCP and NAT labs (11.2.3, 12.2.2) were the two that took the concepts from the notes and actually made them feel real rather than theoretical.
