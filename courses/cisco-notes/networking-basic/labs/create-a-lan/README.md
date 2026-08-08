# Packet Tracer — Create a LAN

**Course:** Networking Basics (Cisco Networking Academy)
**Lab:** 14.3.4 — Create a LAN

---

## Scenario

A new branch office is opening and needs its LAN set up from scratch — the network devices exist already, but nothing is connected, addressed, or verified. The task covers the full chain: physically wiring devices together, configuring IPv4 addressing (DHCP for the PCs, static for the printer), then verifying connectivity both locally and out to the internet, and finally using `ipconfig` and `tracert` to actually look at what the network is doing under the hood.

**Target topology:**
```
Admin PC ---
             \
Manager PC --- Switch --- Office Router --- Internet --- www.cisco.pt
             /
Printer -----
```

**Addressing table given:**

| Device | IPv4 Address | Subnet Mask |
|---|---|---|
| Admin PC | DHCP | N/A |
| Manager PC | DHCP | N/A |
| Printer | 192.168.1.100 | 255.255.255.0 |
| www.cisco.pt | 209.165.200.225 | N/A |

---

## Part 1 — Connecting Devices

First step was just physically powering everything on — clicked into each device's Physical tab and hit the power switch, checked for the green light confirming it was actually on.

<img width="368" height="366" alt="image" src="https://github.com/user-attachments/assets/52762027-83f1-47cd-ad8c-19b7dfe7f8b3" />

Then wired everything per the connections table — Office Router to the ISP cloud on G0/0, Office Router to the Switch on G0/1, and the two PCs plus the printer into the switch's FastEthernet ports (F0/1, F0/2, F0/24 respectively), all using copper straight-through cables. After a short delay, all the link lights came up green, confirming the physical connections were good before moving on to addressing.

<img width="502" height="441" alt="image" src="https://github.com/user-attachments/assets/41e95234-5e11-4aaf-b5a3-1741f920e3f0" />

---

## Part 2 — Configuring IPv4 Addressing

For the Admin and Manager PCs, the lab calls for DHCP — the Office Router is meant to be already configured to hand out addresses to the branch office LAN automatically, so the plan was just to set each PC's IP Configuration to DHCP and let it pull an address.

For the printer, manual static addressing made sense per the addressing table (192.168.1.100 / 255.255.255.0) — printers and other shared devices generally get static addresses specifically because other devices are configured to reach them at a fixed IP, so letting that address drift via DHCP would break things down the line.

<img width="374" height="377" alt="image" src="https://github.com/user-attachments/assets/40e4876c-c760-47a8-948a-448d2171fe5b" />

### Something worth flagging honestly here

Looking back at my actual PC configuration screenshots, the Manager PC ended up set to **Static** rather than DHCP, with an IP of `192.169.1.2` — not `192.168.1.x` like the addressing table specifies. That's a typo-level difference (169 vs 168) but it matters, since it puts the device on a completely different network than intended. I'm noting this rather than glossing over it, since catching a mismatch like this is exactly the kind of thing that matters in real configuration work — a single digit off in an IP address is a classic source of "why can't this device reach anything" problems.

If I were redoing this properly, the fix would be going back into each PC's IP Configuration, switching the radio button to DHCP like the lab actually asks for, and letting the Office Router hand out the correct `192.168.1.0/24` address automatically instead of leaving a manually-typed static address sitting there.

**Reflection question — why are the PCs' IP addresses different but their subnet mask and default gateway the same?**
Because they're on the same LAN, they share the same network portion of the address (same subnet mask, same gateway to reach anything outside the local network) — but each device still needs a unique host portion of the address so they don't conflict with each other on the network. DHCP handles assigning each one a different available address within that shared subnet automatically.

**Reflection question — what default gateway would the printer use, and how would you figure that out?**
Even though the printer doesn't strictly need a default gateway for local-only access, if it needed one it would use the same gateway address as the PCs on that LAN — `192.168.1.1`, the Office Router's LAN-facing interface. You can determine this by checking what default gateway the DHCP-assigned PCs on the same subnet received, since every device on the same LAN segment routes off-network traffic through the same router interface.

---

## Part 3 — Verifying Connectivity

### Local connectivity — pinging the printer

From the Admin PC's command prompt, pinged the printer's static IP (192.168.1.100), then repeated from the Manager PC. Both came back with successful replies, confirming the devices were correctly connected, powered, and addressed at the local network level.

### Internet connectivity — IP vs URL

Opened the web browser on the PCs and tried reaching the internet server two ways — directly by its IP address (209.165.200.225), and then by its URL (www.cisco.pt).

**Question — if you can connect by IP but not by URL, what's the likely cause?**
Since URLs get resolved to IP addresses through DNS, being able to reach the destination by IP but not by URL points specifically at a DNS problem — either the DNS server itself isn't reachable (a connectivity issue), or the DNS server address configured on the host is missing or wrong. The connection working fine by IP rules out a general network/routing problem, which is what narrows it down specifically to DNS rather than something broader.

---

## Part 4 — Networking Commands

### ipconfig

Ran `ipconfig` on the Admin PC first, which showed the basic addressing info — IPv4 address, subnet mask, default gateway.

```
FastEthernet0 Connection:(default port)
   Link-local IPv6 Address..........: FE80::260:5CFF:FE88:4291
   IPv6 Address......................: ::
   IPv4 Address......................: 192.168.1.2
   Subnet Mask........................: 255.255.255.0
   Default Gateway....................: ::
                                          192.168.1.1
```

Then ran `ipconfig /all` for the fuller picture — added the physical (MAC) address of the NIC on top of what basic `ipconfig` shows, along with the DHCP and DNS server addresses. That extra detail is useful specifically when troubleshooting deeper issues, like confirming whether a device actually pulled its address from the expected DHCP server or checking hardware-level identification via the MAC address.

<img width="735" height="549" alt="image" src="https://github.com/user-attachments/assets/20089692-b2b2-4413-acf8-9f214bce7aa0" />
<img width="366" height="377" alt="image" src="https://github.com/user-attachments/assets/c1565f89-e064-46b6-9b80-45c8ca828312" />

Running the same command on the Manager PC actually surfaced the addressing mismatch mentioned earlier — its output also showed `192.169.1.2` rather than the expected `192.168.1.x`, confirming the typo wasn't a one-off but was present on both PCs' configuration.

### tracert

Ran `tracert` from a PC targeting the URL of the web server, since `tracert` uses ICMP to map out every router hop between source and destination.

**Question — how many routers are passed, and how are they identified?**
Two routers. Each hop gets identified by the IP address of the incoming interface on that router as the trace passes through it — `tracert` lists each hop in order with its response time and the IP that answered.

**Question — where is the second router located?**
The second router sits inside the internet cloud itself — representing the ISP-side infrastructure between the branch office's own router and the destination server, rather than being a device on the local branch network.

---

## Reflection

**Question — what's the biggest facilities challenge in setting up a similar LAN in a new physical location?**
Physical infrastructure readiness is probably the realistic biggest challenge — having actual cabling run to where devices need to sit, power available at each device location, and a reliable internet handoff point (the ISP connection) actually provisioned and working before any of the logical configuration in this lab even becomes relevant. The addressing and connectivity verification steps in this lab all assume the physical side is already sorted; in a real new-location setup, that physical groundwork is usually the slower, more failure-prone part compared to configuring IP addresses once the wiring is actually in place.

---

## What Tripped Me Up

The static-vs-DHCP mismatch on the PCs was the main thing worth noting — going back through my own screenshots after the fact, I caught that both PCs ended up statically configured with a mistyped subnet (192.169 instead of 192.168) rather than pulling a DHCP address like the lab intended. Worth treating as a real lesson: always double check the actual configured values against what the addressing table specifies, rather than assuming a config is correct just because a device shows *some* IP address and appears to be working.

---

## Tools Used

- Cisco Packet Tracer (topology build, device configuration, command prompt simulation)
---



