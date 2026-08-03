# Notes — Network Defense (Cisco Networking Academy)

Going through this one module by module like I did for Networking Basics — this course has 11 modules and is noticeably denser than the last one, so these notes took longer to put together properly.

---

## Module 1 — Understanding Defense

- **Defense-in-depth** — the layered security approach, revisited here in more depth than the Intro to Cybersecurity version. Not relying on any single control, so if one layer fails, others still catch the problem
- **Cybersecurity operations management** — how security operations actually get run day to day, not just the technical controls but the management side of it
- **Security policies, regulations, and standards** — the difference between an internal policy, an external regulation you have to comply with, and an industry standard you choose to follow

This module is mostly framing for everything that follows — establishing why defense needs to be layered and governed by policy, not just a pile of individual tools.

---

## Module 2 — System and Network Defense

Biggest module in terms of breadth — covers defense from several different angles:

- **Physical security** — the reminder that security isn't only digital; someone walking into a server room is still a security failure
- **Application security** — securing the software layer itself, not just the network around it
- **Network hardening: services and protocols** — turning off or securing unnecessary services, since anything running is a potential attack surface
- **Network hardening: segmentation** — splitting networks into zones so a breach in one area doesn't automatically expose everything else
- **Hardening wireless and mobile devices** — wireless-specific risks and how to reduce them
- **Cybersecurity resilience** — the ability to keep functioning (or recover quickly) even when something does go wrong, rather than assuming prevention will always work
- **Embedded and specialized systems** — devices that aren't standard computers (IoT, industrial systems) and why they need different defensive thinking. This section connects directly to the OT/ICS side of what I'm building toward separately

---

## Module 3 — Access Control

- **Access controls and access control concepts** — the general models for controlling who can do what
- **Account management** — the practical side of actually managing accounts over their lifecycle, not just the theory of access control
- **AAA (Authentication, Authorization, Accounting)** — three distinct things that get lumped together casually but are actually separate: proving who you are, deciding what you're allowed to do, and logging what you actually did

**Checkpoint Exam: Principles, Practices, and Processes of Network Defense**

---

## Module 4 — Access Control Lists

This module is where the course gets properly hands-on with configuration.

- **Introduction to ACLs** — what they are and the general logic of permit/deny rules
- **Wildcard masking** — the inverse-mask logic ACLs use instead of standard subnet masks, which took some real adjustment after getting used to normal subnet masks in Networking Basics
- **Configuring ACLs** — the actual process of building rule sets
- **Named standard IPv4 ACL syntax** — using names instead of numbers for readability
- **Implementing ACLs** — applying them to the right interfaces in the right direction (inbound/outbound matters a lot here)
- **Mitigating attacks with ACLs** — using ACLs defensively, not just as general traffic filters
- **IPv6 ACLs** — same core logic, different addressing and slightly different syntax

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
