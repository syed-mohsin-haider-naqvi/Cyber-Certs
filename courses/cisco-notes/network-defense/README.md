# Network Defense (NetDef) — Cisco Networking Academy

## About This Course

This is the follow up to Networking Basics, and its a big step up honestly. Where Networking Basics was about how networks work, this one's about how they get attacked and defended — access control, firewalls, crypto, cloud security, and then finally actual security monitoring and alert evaluation, which is the closest this course gets to real SOC work.

Went into this already having done the SOC labs on HTB and LetsDefend so some of the alert evaluation stuff in the later modules felt kinda familiar. but the earlier modules — ACLs, firewall tech, crypto in proper depth — filled in a lot of the "why" behind stuff i'd been doing somewhat mechanically in the hands on labs without fully getting the logic behind it.

**Status:** Completed

---

## What It Covered

- Defense in depth and security ops management — the layered approach, and how policies/regulations/standards actually shape real operations
- System and network defense — physical security, application security, network hardening (services/protocols/segmentation), wireless/mobile hardening, embedded and specialized systems
- Access control — models, account management, AAA (authentication, authorization, accounting)
- ACLs — standard and extended, wildcard masking, named vs numbered syntax, using ACLs to mitigate attacks, IPv6 ACLs
- Firewall tech — how firewalls fit into network design, and Zone Based Policy Firewalls specifically including configuring one
- Cloud security — virtualization basics, the different domains of cloud security, infrastructure/app/data security, protecting VMs
- Cryptography — confidentiality, obscuring data, integrity/authenticity, hashing, public key crypto, PKI trust system
- Security monitoring — common protocols for monitoring, security tech generally, types of security data, end device logs, network logs
- Evaluating alerts — where alerts come from and how to actually evaluate them, most SOC relevant part of the whole course

---

## Why This One Mattered More Then Expected

Going in i figured this would mostly repeat stuff i already knew from the SOC labs. it didnt — the ACL and firewall modules especially gave me a way clearer picture of whats actually happening at the network layer to allow or block traffic, instead of just knowing "this alert means something bad happened." configuring ACLs and a zone based firewall connects directly to a lot of what shows up in SOC investigations honestly — ur often looking at whether a rule shouldve blocked something and didnt, or why traffic that shouldve been allowed got denied instead.

Crypto module was also more hands on then i expected — actual labs using OpenSSL to encrypt/decrypt stuff, looking at telnet vs ssh traffic in wireshark, digital signatures and certificate authority stores. step up from the conceptual crypto overview in Intro to Cybersecurity.

---

## Notes

- [`notes.md`](./notes.md) — module by module notes
- `labs.md` — coming once i work back through the packet tracer and standalone labs (this course has alot of them — ACL configs, firewall setup, openssl encryption labs, wireshark stuff, netflow, snort rules)
- `reference.md` — coming after labs, condensed lookup sheet

---

*Completed as the follow up to Networking Basics, moving from how networks function into how they get attacked and defended.*
