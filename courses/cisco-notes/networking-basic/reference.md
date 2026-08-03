# Reference — Networking Basics (Cisco Networking Academy)

Quick-lookup sheet. Full explanations are in [`notes.md`](./notes.md), and full lab context is in [`labs.md`](./labs.md) — this is just the condensed version for fast reference later, concepts and commands both.

---

## Core Concepts

### Bandwidth vs Throughput

| Term | Meaning |
|---|---|
| Bandwidth | Theoretical maximum capacity of a connection |
| Throughput | What you actually get in practice — usually lower than bandwidth |

### IPv4 Address Types

| Type | Meaning |
|---|---|
| Unicast | Sent to one specific device |
| Broadcast | Sent to all devices on a network |
| Multicast | Sent to a specific group of devices |

### Static vs Dynamic Addressing

| Type | Meaning |
|---|---|
| Static | IP address manually assigned, doesn't change |
| Dynamic | IP address assigned automatically, typically via DHCP |

### MAC vs IP Address

| | MAC Address | IP Address |
|---|---|---|
| Assigned by | Manufacturer (hardware-based) | Network (logical) |
| Scope | Local network segment | Can route across networks |
| Changes? | Fixed to the device | Can change depending on network/config |

### TCP vs UDP

| | TCP | UDP |
|---|---|---|
| Connection | Connection-based, reliable | Connectionless, no delivery guarantee |
| Speed | Slower (overhead from reliability checks) | Faster |
| Use case | Web browsing, file transfer | Streaming, gaming |

### Telnet vs SSH

| | Telnet | SSH |
|---|---|---|
| Encryption | None — plaintext | Encrypted |
| Use today | Largely outdated for real use | Standard for secure remote access |

### IPv6 — Why It Exists

IPv4 has a limited address pool and the world ran low on available addresses (IPv4 exhaustion). IPv6 uses a much larger address space to solve this long-term.

**Shorthand rules:**
- Leading zeros in a group can be dropped
- One consecutive run of all-zero groups can be replaced with `::` (only once per address)

---

## Command Quick Reference

### Basic Diagnostics

```bash
ipconfig              # view basic IP config (Windows)
ipconfig /all          # full details — MAC, DNS, DHCP lease info
ping <address>          # test connectivity
arp -a                 # view local ARP table (IP-to-MAC mappings)
```

### Static IP Configuration (Client)

```
IP Address:      192.168.1.10
Subnet Mask:      255.255.255.0
Default Gateway:  192.168.1.1
```

### DHCP Pool Configuration (Cisco Router)

```
Router(config)# ip dhcp pool HOME-NET
Router(dhcp-config)# network 192.168.1.0 255.255.255.0
Router(dhcp-config)# default-router 192.168.1.1
Router(dhcp-config)# dns-server 8.8.8.8
Router(dhcp-config)# exit
Router(config)# ip dhcp excluded-address 192.168.1.1 192.168.1.10
```

### NAT Overload / PAT Configuration (Cisco Router)

```
Router(config)# access-list 1 permit 192.168.1.0 0.0.0.255
Router(config)# interface GigabitEthernet0/1
Router(config-if)# ip nat outside
Router(config-if)# exit
Router(config)# interface GigabitEthernet0/0
Router(config-if)# ip nat inside
Router(config-if)# exit
Router(config)# ip nat inside source list 1 interface GigabitEthernet0/1 overload
```

### Basic Interface Setup (Building a LAN)

```
Router(config)# interface GigabitEthernet0/0
Router(config-if)# ip address 192.168.1.1 255.255.255.0
Router(config-if)# no shutdown
Router(config-if)# exit
```

### Viewing the Routing Table

```
Router# show ip route
```

### Enabling SSH on a Cisco Device

```
Router(config)# hostname R1
R1(config)# ip domain-name mynetwork.local
R1(config)# crypto key generate rsa
R1(config)# username admin secret StrongPassword123
R1(config)# line vty 0 4
R1(config-line)# transport input ssh
R1(config-line)# login local
```

### FTP Client Basics

```
ftp 192.168.1.100
> username
> password
> get filename.txt
> put filename.txt
> quit
```

### Telnet / SSH Client Connection

```bash
telnet 192.168.1.1          # plaintext — insecure
ssh -l admin 192.168.1.1     # encrypted — standard for real use
```

---

## Course Structure Quick Map

| Modules | Focus Area |
|---|---|
| 1–4 | Networking fundamentals, home network setup |
| 5–7 | Communication models, media, access layer |
| 8–11 | IPv4/IPv6 addressing, DHCP |
| 12–14 | NAT, ARP, routing |
| 15–17 | TCP/UDP, application layer services, troubleshooting tools |

---

*This is a condensed reference only — see `notes.md` for full explanations and `labs.md` for the hands-on Packet Tracer context behind each command.*
