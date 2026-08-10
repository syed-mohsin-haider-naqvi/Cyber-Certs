# Packet Tracer — Configure a ZPF (Zone-Based Policy Firewall)

**Course:** Network Defense (Cisco Networking Academy)
**Lab:** 6.3.11 — Configure a ZPF

---

## Scenario

Configure a basic Zone-Based Policy Firewall on edge router R3, with the goal of letting internal hosts reach external resources freely while blocking external hosts from reaching anything on the internal network. The lab has a pre-built topology with R1, R2, and R3 already routing between each other, plus PC-A (behind R1) and PC-C (behind R3).

**Pre-configured credentials given:**
```
Console password:      ciscoconpa55
VTY line password:     ciscovtypa55
Enable password:       ciscoenpa55
Local username/pass:   Admin / Adminpa55
```

**Addressing table:**

| Device | Interface | IP Address | Subnet Mask | Switch Port |
|---|---|---|---|---|
| R1 | G0/1 | 192.168.1.1 | 255.255.255.0 | S1 F0/5 |
| R1 | S0/0/0 | 10.1.1.1 | 255.255.255.252 | N/A |
| R2 | S0/0/0 | 10.1.1.2 | 255.255.255.252 | N/A |
| R2 | S0/0/1 | 10.2.2.2 | 255.255.255.252 | N/A |
| R3 | G0/1 | 192.168.3.1 | 255.255.255.0 | S3 F0/5 |
| R3 | S0/0/1 | 10.2.2.1 | 255.255.255.252 | N/A |
| PC-A | NIC | 192.168.1.3 | 255.255.255.0 | S1 F0/6 |
| PC-C | NIC | 192.168.3.3 | 255.255.255.0 | S3 F0/18 |

---

## Part 1 — Verifying Connectivity Before Any Firewall Config

Before touching R3's firewall configuration at all, the lab has you confirm the network works normally first — no point configuring a firewall to test against a network that's already broken for unrelated reasons.

**ICMP test:** Pinged from PC-A to PC-C (192.168.3.3) — successful, 0% loss.

<img width="359" height="470" alt="image" src="https://github.com/user-attachments/assets/3f85c678-2360-49fa-ab48-4361b9cbe148" />

**HTTP test:** Opened a web browser from PC-C to PC-A's address (192.168.1.3) — page loaded successfully, confirming HTTP reachability in both directions works pre-firewall.

<img width="363" height="507" alt="image" src="https://github.com/user-attachments/assets/92de856e-f7c2-4590-9547-05ca37468e34" />

**SSH test:** Established SSH sessions to R2's S0/0/1 interface (10.2.2.2) from both PCs. PC-C's first couple of attempts actually failed with "Login invalid" — worth noting since it wasn't a smooth first try — before succeeding on a retry with the correct credentials. PC-A connected cleanly on the first attempt.

<img width="360" height="480" alt="image" src="https://github.com/user-attachments/assets/95d80181-cae3-41cf-87f5-ee2ce8308fc0" />

All three protocols confirmed working normally in both directions before any firewall rules existed — this baseline matters because it means anything that stops working after configuring the ZPF is actually the firewall doing its job, not some unrelated network problem.

---

## Part 2 — Creating the Security Zones

Logged into R3 and started working toward creating the two zones (internal and external) the ZPF needs.

Hit a few genuine stumbling points getting into the right mode first:

```
R3>license boot module c1900 technology-package securityk9
      ^
% Invalid input detected at '^' marker.

R3>zone security IN-ZONE
    ^
% Invalid input detected at '^' marker.
```

Both of these failed because I was still in user EXEC mode (`R3>`) rather than privileged EXEC or global config — commands like `zone security` and the license activation need to be run from deeper in the CLI hierarchy, not directly from the base prompt.

```
R3>enable
Password:
R3#

R3#configure console
        ^
% Invalid input detected at '^' marker.
```

Another wrong guess — tried `configure console` instead of the actual command, `configure terminal`. Corrected and moved on:

```
R3#configure terminal
Enter configuration commands, one per line. End with CNTL/Z.
R3(config)#license boot module c1900 technology-package securityk9
```

This triggered a full Cisco license EULA prompt (the security feature set on this router model needs the `securityk9` technology package license activated before zone-based firewall commands become available at all). Accepted the terms:

```
ACCEPT? [yes/no]: yes
% use 'write' command to make license boot config take effect on next boot
```

With the license accepted, the zone commands worked:

```
R3(config)#zone security IN-ZONE
R3(config-sec-zone)#exit
R3(config)#zone security OUT-ZONE
R3(config-sec-zone)#exit
```

<img width="663" height="346" alt="image" src="https://github.com/user-attachments/assets/0a02a333-0d5c-4030-967d-f14ecc527133" />

---

## Part 3 — ACL and Class Map for Internal Traffic

Next step was defining what "internal traffic" actually means to the firewall — this needs an ACL identifying the internal network, then a class map that references that ACL so the firewall policy has something concrete to match against.

```
R3(config)#access-list 101 permit ip 192.168.3.0 0.0.0.255 any
R3(config)#class-map type inspect match-all IN-NET-CLASS-MAP
R3(config-cmap)#match access-group 101
R3(config-cmap)#exit
```

The ACL permits any traffic sourced from the `192.168.3.0/24` network (R3's internal LAN) heading to any destination — this is intentionally broad since the point isn't restricting *what* internal traffic can do, just identifying *which* traffic counts as "internal" for the firewall to apply inspection rules to.

<img width="717" height="400" alt="image" src="https://github.com/user-attachments/assets/e85716e8-7f49-4288-87aa-fe760de04cca" />

---

## Part 4 — Policy Map and Zone Pair

With the class map defining what to match, next came the actual policy — what to *do* with traffic that matches.

```
R3(config)#policy-map type inspect IN-2-OUT-PMAP
R3(config-pmap)#class type inspect IN-NET-CLASS-MAP
R3(config-pmap-c)#inspect
%No specific protocol configured in class IN-NET-CLASS-MAP for inspection. All protocols will be inspected
```

That warning isn't an error — it's IOS confirming the behavior: since the class map wasn't scoped to a specific protocol, `inspect` applies stateful inspection to all protocols matching the ACL, which is exactly what's wanted here (internal hosts should be able to initiate any kind of connection outward).

Then created the zone pair — this is the piece that actually ties the whole policy to a direction of traffic flow, specifying which zone is the source and which is the destination:

```
R3(config)#zone-pair security IN-2-OUT-ZPAIR source IN-ZONE destination OUT-ZONE
R3(config-sec-zone-pair)#service-policy type inspect IN-2-OUT-PMAP
```

This is the core logic of a ZPF — the policy only applies in one direction (internal → external here). Traffic initiated from internal hosts gets inspected and, because it's inspected, return traffic for those same sessions is automatically permitted back in. Traffic with no matching zone-pair policy in the other direction (external → internal) has no rule allowing it, so it gets dropped by default — which is exactly the intended behavior described in the scenario.

<img width="718" height="351" alt="image" src="https://github.com/user-attachments/assets/be146a13-9feb-41ef-9b9a-8c6f90eff01a" />

---

## Part 5 — Assigning Interfaces to Zones

Last configuration step — the zones and policy exist logically, but R3 doesn't yet know which physical interfaces actually belong to which zone. Assigned G0/1 (the internal-facing interface, connected to PC-C's network) to IN-ZONE, and S0/0/1 (the interface facing out toward R2/R1) to OUT-ZONE:

```
R3(config)# interface g0/1
R3(config-if)# zone-member security IN-ZONE
R3(config-if)# exit
R3(config)# interface s0/0/1
R3(config-if)# zone-member security OUT-ZONE
R3(config-if)# exit
```

Packet Tracer confirmed successful assignment and successful firewall policy configuration overall at this point.

<img width="724" height="331" alt="image" src="https://github.com/user-attachments/assets/5a1f911b-28d8-417e-a322-c691d7c0e95a" />

---

## Verification — Not Yet Completed

The lab's final section has you test connectivity again post-configuration (SSH from PC-C to R2, HTTP from PC-C to PC-A, ping between PC-A and PC-C, ping from R2 to PC-C) and use `show policy-map type inspect zone-pair sessions` to confirm session state.

I wasn't able to actually run these tests myself this time — hit a hardware issue partway through (PSU problem causing my machine to shut off) before getting to this stage, so I don't have real captured results for this section yet. Rather than presenting borrowed or assumed output as if I'd tested it myself, I'm leaving this section honestly incomplete for now and will come back to fill in real results once I can properly redo this part.

**The verification command itself, for reference:**
```
R3# show policy-map type inspect zone-pair sessions
```

This command shows any currently established sessions being tracked by the inspect policy — session state, source/destination IP and port, and how long the session's been active. It's the right tool for confirming whether the ZPF is actually behaving as expected (internal-initiated sessions showing as established, no equivalent sessions existing for anything externally-initiated).

**What I expect based on how the policy is configured**, to check against once I actually retest:
- SSH from PC-C outbound to R2 should succeed (internal-initiated, matches the IN-ZONE → OUT-ZONE policy)
- HTTP from PC-C to PC-A should succeed for the same reason
- Ping from PC-A to PC-C should fail — this is external-to-internal from R3's perspective relative to PC-C's zone, with no policy permitting that direction
- Ping from R2 to PC-C should also fail, same reasoning — R2 sits in the "external" direction relative to R3's IN-ZONE

---

## What Tripped Me Up

The two early syntax/mode errors (`configure console` instead of `configure terminal`, and trying zone commands from user EXEC mode) were straightforward mistakes to catch and fix. The license activation step was the one part I hadn't anticipated at all going in — I didn't know the `securityk9` technology package needed activating before zone-based firewall commands would even work, so hitting that EULA prompt mid-configuration was genuinely unexpected the first time through.

---

## Tools Used

- Cisco Packet Tracer (R3 CLI configuration, PC-A/PC-C for pre-config connectivity testing)
