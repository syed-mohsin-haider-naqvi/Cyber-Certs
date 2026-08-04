# Notes — Cyber Threat Management (Cisco Networking Academy)

Last one of the six cisco courses, same module by module format as the others. 6 modules total but they're each pretty dense, especially module 6.

---

## Module 1 — Governance and Compliance

- Governance — how security decisions actually get made and enforced at an organizational level, not just technical controls but the structure around them
- The ethics of cybersecurity — this section had a lab where u write ur own personal code of ethical conduct, which sounds like a throwaway exercise but actually made me think through stuff i hadnt really considered, like the line between legit security testing and actually crossing into something you shouldnt be doing
- IT security management framework — the structured approach orgs use to actually manage security instead of just doing things ad hoc

**Labs:** Develop Cybersecurity Policies and Procedures / Create Your Personal Code of Ethical Conduct / Recommend Security Measures to Meet Compliance Requirements

Went in expecting this module to be the boring one to get through fast. wasnt actually. the ethics lab specifically stuck with me more then i expected from a "governance" module.

---

## Module 2 — Network Security Testing

- Security assessments — the general process of evaluating how secure something actually is
- Network security testing techniques — the different approaches/methods
- Network security testing tools — actual tools used
- Penetration testing — pentesting specifically, as its own category within testing generally

**Labs:** Use Diagnostic Commands / Use Wireshark to Compare Telnet and SSH Traffic

The wireshark lab here connects back to stuff from earlier courses (networking devices and network defense both touched telnet vs ssh) but seeing it specifically framed as a security testing technique rather then just a networking concept was a useful reframe.

---

## Module 3 — Threat Intelligence

- Information sources — where threat intel actually comes from
- Threat intelligence services — the actual services/platforms orgs use to get this info

**Labs:** Evaluate Cybersecurity Reports / Identify Relevant Threat Intelligence

Shorter module then most but genuinely useful — a big part of SOC work is knowing which threat intel is actually relevant to your org vs just noise, and these labs made u practice that filtering process instead of just reading about it.

---

## Module 4 — Endpoint Vulnerability Assessment

- Network and server profiling — understanding whats normal for a network/server so u can actually spot whats abnormal
- CVSS (Common Vulnerability Scoring System) — how vulnerabilities actually get scored
- Secure device management — managing devices securely, tying back into alot of the hardening stuff from Endpoint Security

**Lab:** Evaluate Vulnerabilities

CVSS took longer to properly get then i expected. the score itself is just a number but what actually feeds into that number — attack vector, how complex the attack is, what privileges are needed, whether user interaction is required — thats alot of moving parts. took a few passes through the lab before i could look at a CVSS score and actually understand what it was telling me instead of just going "ok thats a high number, bad."

---

## Module 5 — Risk Management and Security Controls

- Risk management — the overall process of managing risk, not eliminating it entirely (which isnt realistic) but managing it down to acceptable levels
- Risk assessment — the actual process of assessing risk specifically
- Security controls — the controls u actually put in place as a result of risk management/assessment

**Labs:** Risk Management / Risk Analysis / Security Controls Implementation

**Checkpoint Exam: Vulnerability Assessment and Risk Management**

---

## Module 6 — Digital Forensics and Incident Analysis and Response

Biggest and most important module in the whole course honestly.

- Evidence handling and attack attribution — how to actually handle evidence properly (chain of custody type stuff) and figuring out who's actually behind an attack
- The Cyber Kill Chain — a framework breaking an attack down into stages, from recon all the way to actions on objectives
- The Diamond Model of Intrusion Analysis — a different framework for the same general goal (understanding an attack), but structured around four core things — adversary, capability, infrastructure, victim — and the relationships between them instead of a linear sequence
- Incident response — the actual process of responding once somethings happened
- Disaster recovery — recovering after, which is related to incident response but more about getting back to normal operations then investigating what happened

**Labs:** Gather System Information After an Incident / Attack Analysis / Incident Handling / Investigate Disaster Recovery / Recommend Disaster Recovery Measures

Kill Chain vs Diamond Model took some real effort to keep straight. Theyre both about understanding an attack but from different angles — Kill Chain is basically a timeline, step by step through what an attacker does. Diamond Model isnt really a timeline at all, its more about mapping the relationships between the four core elements for any given event. Took redoing the attack analysis lab a couple times applying both frameworks before the distinction between them actually stuck properly instead of blurring together in my head.

**Checkpoint Exam: Incident Response**

---

## Cyber Threat Management (CyberTM) Course Final Exam

Covers all 6 modules.

---

## Overall

This course pulled together alot of what the other five cisco courses built up separately. Networking Basics and Networking Devices gave the fundamentals, Network Defense and Endpoint Security gave the technical defense skills, and this one gives the process and framework side of things — how risk actually gets managed, how an incident actually gets handled start to finish, and frameworks like Kill Chain/Diamond Model for actually understanding an attack instead of just reacting to it.

Module 6 was the standout, both in terms of difficulty and in terms of how directly it connects to the SOC lab work ive already done on HTB and LetsDefend — turns out i was already sort of thinking in kill chain terms during those labs without having the actual name for the framework I was unconsciously using.

Labs and reference sheet to follow, same approach as the other courses — picking a handful of the more substantial labs (probably the CVSS evaluation and the kill chain/diamond model attack analysis specifically) to redo properly rather then trying to cover all of them.
