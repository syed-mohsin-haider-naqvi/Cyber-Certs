# Network Defense (NetDef) — Cisco Networking Academy

## About This Course

This is the follow-up to Networking Basics, and it's a big step up in scope. Where Networking Basics was about how networks function, this course is about how they get attacked and defended — access control, firewalls, cryptography, cloud security, and finally into actual security monitoring and alert evaluation, which is the closest this course gets to real SOC work.

I went into this one already having done the SOC labs on HTB and LetsDefend, so some of the alert-evaluation material in the later modules felt familiar. But the earlier modules — ACLs, firewall technologies, cryptography in proper depth — filled in a lot of the "why" behind things I'd been doing somewhat mechanically in the hands-on labs without fully understanding the underlying logic.

**Status:** Completed

---

## What It Covered

- **Defense-in-depth and security operations management** — the layered approach to security, and how security policies/regulations/standards actually shape real operations
- **System and network defense** — physical security, application security, network hardening (services, protocols, segmentation), wireless/mobile hardening, and a look at embedded/specialized systems
- **Access control** — access control models, account management, and AAA (Authentication, Authorization, Accounting)
- **Access Control Lists (ACLs)** — standard and extended ACLs, wildcard masking, named vs numbered syntax, using ACLs to mitigate attacks, and IPv6 ACLs specifically
- **Firewall technologies** — how firewalls fit into network design, and Zone-Based Policy Firewalls (ZPF) specifically, including configuring one
- **Cloud security** — virtualization basics, the different domains of cloud security, cloud infrastructure/application/data security, and protecting VMs
- **Cryptography** — confidentiality, obscuring data, integrity and authenticity, hashing, public key cryptography, and the PKI trust system
- **Security monitoring** — common protocols used for monitoring, security technologies generally, types of security data, end device logs, and network logs
- **Evaluating alerts** — sources of alerts and how to actually evaluate them, which is the most SOC-relevant material in the whole course

---

## Why This One Mattered More Than Expected

Going in, I expected this to mostly repeat what I already knew from the SOC labs. It didn't — the ACL and firewall modules especially gave me a much clearer picture of what's actually happening at the network layer to enable or block traffic, rather than just knowing "this alert means something bad happened." Configuring ACLs and a Zone-Based Firewall directly connects to a lot of what shows up in SOC investigations — you're often looking at whether a rule should have blocked something and didn't, or why traffic that should've been allowed got denied.

The cryptography module was also more hands-on than I expected — actual labs using OpenSSL to encrypt/decrypt data, examining Telnet vs SSH traffic in Wireshark, working with digital signatures and certificate authority stores. That's a step beyond the conceptual crypto overview from Intro to Cybersecurity.

---

## Notes

- [`notes.md`](./notes.md) — module-by-module study notes
- `labs.md` — coming once I work back through the Packet Tracer and standalone labs (this course has a lot of them — ACL configs, firewall setup, OpenSSL encryption labs, Wireshark examination, NetFlow, Snort rules)
- `reference.md` — coming as a condensed lookup sheet once labs are documented

---

*Completed as a follow-up to Networking Basics, moving from how networks function into how they're attacked and defended.*
