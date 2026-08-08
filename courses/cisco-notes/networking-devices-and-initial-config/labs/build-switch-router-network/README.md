# Packet Tracer — Build a Switch and Router Network

**Course:** Networking Devices and Initial Configuration (Cisco Networking Academy)
**Lab:** 11.4.4 — Packet Tracer Tutored Activity

---

## Scenario

Framed as helping out a family member's small insurance agency — she'd bought a Cisco router and switch and had two wired PCs that needed connecting. The job was the full stack: physically wire the devices, do basic IOS configuration on both the router and switch, verify end-to-end connectivity actually works, and then lock down remote access to the router with SSH instead of leaving it open.

**Target topology:**
```
PCA --- S1 --- R1 --- PCB
```

**Addressing table:**

| Device | Interface | IP Address | Subnet Mask | Default Gateway |
|---|---|---|---|---|
| R1 | G0/0/0 | 192.168.0.1 | 255.255.255.0 | N/A |
| R1 | G0/0/1 | 192.168.1.1 | 255.255.255.0 | N/A |
| S1 | VLAN 1 | 192.168.1.2 | 255.255.255.0 | 192.168.1.1 |
| PCA | NIC | 192.168.1.3 | 255.255.255.0 | 192.168.1.1 |
| PCB | NIC | 192.168.0.3 | 255.255.255.0 | 192.168.0.1 |

---

## Part 1 — Connecting Devices and Configuring the PCs

Wired everything with copper straight-through cables per the instructions — R1's G0/0/1 to a port on S1, PCA to a port on S1, and PCB directly to R1's G0/0/0. That put PCA and S1 on one side of the router and PCB on the other, which matches the addressing table having PCA/S1 on the `192.168.1.0/24` network and PCB alone on `192.168.0.0/24`.

![Physical topology connected](./screenshots/01-topology.png)

Configured static IPv4 addressing on both PCs directly from the addressing table — PCA got 192.168.1.3/24 with gateway 192.168.1.1, PCB got 192.168.0.3/24 with gateway 192.168.0.1.

![PCA IP configuration](./screenshots/02-pca-config.png)

---

## Part 2 — First Connectivity Test (Expected Failure)

Before touching the router or switch configuration at all, the lab has you test connectivity between PCA and PCB immediately — and as expected at this stage, it failed:

```
C:\>ping 192.168.0.3

Pinging 192.168.0.3 with 32 bytes of data:
Request timed out.
Request timed out.
Request timed out.
Request timed out.

Ping statistics for 192.168.0.3:
    Packets: Sent = 4, Received = 0, Lost = 4 (100% loss)
```

**Why did this fail?**

The router's interfaces — which are the default gateways both PCs rely on to reach anything outside their own local subnet — hadn't been configured yet. With no IP addressing or activation done on R1's interfaces, there was nothing actually routing traffic between the `192.168.0.0/24` and `192.168.1.0/24` networks, so the ping had no path to follow. Worth noting the link lights on the router's connections were showing red at this point too — a visual confirmation that those interfaces genuinely weren't up yet, not just unconfigured but literally down at the interface level.

This step was actually useful precisely because it failed — it confirmed the physical wiring and PC-level addressing were fine on their own, and isolated the actual problem specifically to the router not being configured, rather than some other part of the setup being wrong.

![Failed ping before router configuration](./screenshots/03-ping-fail.png)

---

## Part 3 — Configuring R1

Opened R1's CLI directly (rather than console cabling in from a PC, since Packet Tracer lets you click straight into the device) and worked through the required basic settings — hostname, passwords, password encryption, a warning banner, and then the actual interface addressing.

```
Router>enable
Router#configure terminal
Enter configuration commands, one per line. End with CNTL/Z.
Router(config)#hostname R1
R1(config)#enable secret class
R1(config)#line con 0
R1(config-line)#password cisco
R1(config-line)#enable login
              ^
% Invalid input detected at '^' marker.
```

Hit an actual error here — `enable login` isn't valid syntax under the console line context; the correct command is just `login` on its own once you're already inside `line con 0`. Small syntax mistake, but a genuine one, not something I got right on the first try.

```
R1(config)# ip domain-name academy.net
R1(config-line)#login
R1(config-line)#secret password-encryption
              ^
% Invalid input detected at '^' marker.
```

Second error — tried `secret password-encryption` which isn't a real command either. The actual command for encrypting the plaintext passwords stored in the config is `service password-encryption`, run from global config mode, not something scoped under a specific line.

```
R1(config-line)#service password-encryption
R1(config)#banner motd $Authorized Access Only!$
R1(config)#interface g0/0/0
R1(config-if)#ip address 192.168.0.1 255.255.255.0
R1(config-if)#no shutdown

%LINK-5-CHANGED: Interface GigabitEthernet0/0/0, changed state to up
%LINEPROTO-5-UPDOWN: Line protocol on Interface GigabitEthernet0/0/0, changed state to up

interface g0/0/1
R1(config-if)#ip address 192.168.1.1 255.255.255.0
R1(config-if)#no shutdown

%LINK-5-CHANGED: Interface GigabitEthernet0/0/1, changed state to up
%LINEPROTO-5-UPDOWN: Line protocol on Interface GigabitEthernet0/0/1, changed state to up

R1(config)# exit
R1# copy running-config startup-config
Destination filename [startup-config]?
Building configuration...
[OK]
```

Both interfaces came up cleanly once addressed and activated with `no shutdown` — the `%LINK-5-CHANGED` and `%LINEPROTO-5-UPDOWN` messages confirming each interface transitioned to an up state. Saved the config with `copy running-config startup-config` so it would persist.

![R1 configuration in progress](./screenshots/04-r1-config.png)

---

## Part 4 — Second Connectivity Test (Success, With A Catch)

Tested the ping again between PCA and PCB now that R1's interfaces were up:

```
C:\>ping 192.168.0.3

Pinging 192.168.0.3 with 32 bytes of data:
Request timed out.
Reply from 192.168.0.3: bytes=32 time=1ms TTL=127
Reply from 192.168.0.3: bytes=32 time<1ms TTL=127
Reply from 192.168.0.3: bytes=32 time<1ms TTL=127

Ping statistics for 192.168.0.3:
    Packets: Sent = 4, Received = 3, Lost = 1 (25% loss)
```

**Why were these pings successful (with the first one still timing out)?**

Now that R1 was routing between the two networks, the ping traffic had a path to actually follow — but the very first ping in the sequence still timed out. That first failure is expected and normal here rather than a real problem: it's ARP resolving the destination's MAC address for the first time before the actual ICMP traffic can flow, which eats up the time budget on that initial packet. Every ping after that succeeded cleanly once ARP had already resolved. The switch itself needed no manual configuration to allow this — its default settings automatically enable interfaces as soon as a device gets connected to them.

![Successful ping with initial timeout, then replies](./screenshots/05-ping-success.png)

---

## Part 5 — Configuring S1

Same category of basic setup as R1, but scoped to a switch instead of a router — hostname, passwords, encryption, banner, and then VLAN 1 interface addressing plus a default gateway (switches need a default gateway configured too, for their own management traffic to be able to leave the local subnet, even though they're not routing user traffic the way R1 does).

```
Switch>enable
Switch#configure terminal
Enter configuration commands, one per line. End with CNTL/Z.
Switch(config)#hostname S1
S1(config)#enable secret class
S1(config)#line con 0
S1(config-line)#password cisco
S1(config-line)#login
S1(config-line)#service password-encryption
S1(config)#banner motd $Authorized Access Only!$
S1(config)#interface vlan 1
S1(config-if)#ip address 192.168.1.2 255.255.255.0
S1(config-if)#no shutdown

%LINK-3-UPDOWN: Interface Vlan1, changed state to down
%LINEPROTO-5-UPDOWN: Line protocol on Interface Vlan1, changed state to up

ip default-gateway 192.168.1.1
S1(config)#exit
S1#
%SYS-5-CONFIG_I: Configured from console by console
copy running-config startup-config
Destination filename [startup-config]?
Building configuration...
[OK]
```

Went through this configuration cleanly the second time around — having already made the `enable login` and `secret password-encryption` mistakes on R1 meant I used the correct `login` and `service password-encryption` syntax directly here without repeating either error.

![S1 configuration](./screenshots/06-s1-config.png)

---

## Part 6 — Securing Remote Access to R1

Last part of the lab — getting SSH working on R1 instead of relying on unencrypted Telnet or leaving the VTY lines open without proper authentication.

```
R1(config)# ip domain-name academy.net
R1(config)# crypto key generate rsa
The name for the keys will be: R1.academy.net
How many bits in the modulus [512]: 1024
% Generating 1024 bit RSA keys, keys will be non-exportable... [OK]

R1(config)# username SSHuser secret cisco

R1(config)# line vty 0 4
R1(config-line)# login local
R1(config-line)# transport input ssh
```

The domain name has to be set before generating RSA keys — the key naming convention (`R1.academy.net` here) is built from the hostname plus domain name together, so trying to generate keys without a domain name set first would fail. Used a 1024-bit modulus rather than the 512-bit default, since a bigger key is meaningfully stronger and 1024 is a reasonable minimum for this kind of lab exercise.

Created a local user (`SSHuser` / `cisco`) so there was an actual account to authenticate against, then pointed the VTY lines at that local username database with `login local`, and restricted `transport input` to `ssh` only — meaning Telnet specifically can no longer be used to reach these lines at all, only SSH.

### Verifying SSH actually works

From PCA's command prompt:

```
C:\>ssh -l SSHuser 192.168.1.1
```

Entered `cisco` when prompted for the password.

**What message displayed?** The configured banner MOTD — "Authorized Access Only!" — appeared, then dropped into R1's prompt. Getting the banner to display on login was actually a useful confirmation in itself, beyond just successfully connecting — it meant the SSH session was genuinely hitting R1's actual CLI, not some cached or partial connection, since the banner is set to display specifically on real login.

![Successful SSH connection showing banner](./screenshots/07-ssh-success.png)

---

## Putting It Together

This lab moved through the full lifecycle of standing up a small two-network setup from nothing: wire it, prove it doesn't work yet (the first failed ping), configure the router and switch properly, prove it works now (the second successful ping, ARP timeout aside), and then harden remote access so the router isn't left wide open. The two syntax errors on R1 (`enable login`, `secret password-encryption`) were genuinely useful in a roundabout way — hitting them once meant I didn't repeat either mistake configuring S1 afterward, so the second device's configuration went through clean on the first pass.

---

## What Tripped Me Up

The two invalid command errors on R1 were the main friction points — `enable login` and `secret password-encryption` both looked like reasonable guesses at command syntax based on what I already knew, but IOS's actual command structure didn't match what I assumed. Correcting both meant paying closer attention to exactly which config context a command needs to be run in (global config vs line config specifically), rather than assuming similar-sounding commands work the same way across contexts.

Also had to stop and think through why the very first ping in the successful test still timed out — my first instinct was to worry something was still misconfigured, before realizing that single dropped packet was just normal ARP resolution overhead on the first attempt, not an actual problem.

---

## Tools Used

- Cisco Packet Tracer (topology build, router/switch CLI configuration, SSH verification)
