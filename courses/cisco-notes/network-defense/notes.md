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

*Completed as the follow up to Networking Basics, moving from how networks function into how they get attacked and defended.*- **IPv6 ACLs** — same core logic, different addressing and slightly different syntax

Wildcard masking was genuinely the hardest single concept in this module — it's essentially the opposite logic of a subnet mask (0 means "must match," 1 means "don't care," which is backwards from what subnetting trained me to expect), so I had to consciously stop and think through it rather than pattern-matching off subnetting instincts.

---

## Module 5 — Firewall Technologies

- **Securing networks with firewalls** — general firewall role and function
- **Firewalls in network design** — where firewalls actually get placed in a real network topology and why placement matters

---

## Module 6 — Zone-Based Policy Firewalls

- **ZPF overview and operation** — a different model from a traditional single-interface firewall; ZPF groups interfaces into zones and applies policy between zones rather than per-interface
- **Configuring a ZPF** — actually building one

---

## Module 7 — Cloud Security

- **Virtualization and cloud computing** — the underlying concept that makes cloud possible in the first place
- **The domains of cloud security** — breaking cloud security into distinct areas rather than treating it as one big topic
- **Cloud infrastructure security, application security, data security** — each domain covered separately
- **Protecting VMs** — securing the virtual machines themselves, not just the cloud environment around them

This module lines up directly with the AWS Cloud Practitioner material I'm working through separately — a lot of the domain breakdown here (infrastructure/application/data) maps onto how AWS itself talks about the shared responsibility model.

---

## Module 8 — Cryptography

The most detailed crypto coverage I've had so far, well beyond the Intro to Cybersecurity overview.

- **Confidentiality** — revisited specifically in the context of how cryptography protects it
- **Obscuring data** — techniques for hiding data beyond just standard encryption (this is where steganography comes in, covered in the labs)
- **Integrity and authenticity** — two related but distinct properties: data wasn't altered (integrity), and it genuinely came from who it claims to (authenticity)
- **Using hashes** — practical hashing, building on the definition-level understanding from Intro to Cybersecurity
- **Public key cryptography** — asymmetric encryption in more depth
- **Authorities and the PKI trust system** — how certificate authorities and the broader PKI system establish trust between parties who've never directly exchanged keys
- **Applications and impacts of cryptography** — where this actually gets used in practice, and the broader implications

**Checkpoint Exam: Firewalls, Cryptography, and Cloud Security**

---

## Module 9 — Technologies and Protocols

- **Monitoring common protocols** — watching protocol behavior specifically for security monitoring purposes, not just understanding how the protocol works
- **Security technologies** — the tools and technology categories used across security monitoring generally

---

## Module 10 — Network Security Data

- **Types of security data** — the different categories of data a SOC analyst actually works with
- **End device logs** — logs generated on individual devices
- **Network logs** — logs generated by network infrastructure itself (this is where NetFlow comes in, covered in the labs)

This module is where the course starts feeling directly connected to the SOC lab work I've done on HTB and LetsDefend — a lot of what shows up here is the same underlying data types those platforms have you investigate, just introduced more formally here.

---

## Module 11 — Evaluating Alerts

- **Sources of alerts** — where alerts actually originate from across a security stack
- **Overview of alert evaluation** — the process of actually deciding whether an alert is a real problem or noise

This is the most direct SOC-analyst-relevant module in the entire course. Everything from Module 1 onward has been building toward being able to actually look at an alert and reason about it properly instead of just reacting to it.

**Checkpoint Exam: Evaluating Security Alerts**

---

## Network Defense Course Final Exam

Cumulative exam covering all 11 modules.

---

## Overall Takeaway

This course connected a lot of dots that the SOC labs had left slightly loose. Doing hands-on investigation on HTB/LetsDefend first, then coming back to this more formal course, meant I already had a rough intuition for a lot of Module 9-11 material — but Modules 4 through 8 (ACLs, firewalls, cloud security, cryptography) filled in real gaps, especially on the configuration side rather than just concepts.

Wildcard masking in Module 4 was the single hardest thing to get comfortable with. The cloud security module (7) was the most directly useful for what I'm building toward next, since it maps cleanly onto the AWS material I'm studying separately.

Labs and reference sheet to follow once I've worked back through the hands-on material — this course has considerably more labs than Networking Basics did (ACL configs, ZPF setup, OpenSSL encryption work, Wireshark examination, NetFlow, Snort rules), so I want to actually redo the key ones properly rather than just describe them from memory.
