# Cyber Threat Management (CyberTM) — Cisco Networking Academy

## About This Course

Last of the six cisco courses and honestly probably the most directly relevant to actual SOC analyst work out of all of them. Where Endpoint Security was about defending windows/linux systems specifically, this one zooms out into the bigger picture stuff — governance, risk management, threat intelligence, and then the big one at the end, digital forensics and incident response.

6 modules, starts with governance/compliance which i wasnt expecting to find interesting but actually did, then network security testing, threat intel, vulnerability assessment, risk management, and finishes with the incident response/forensics module which is basically the capstone of the whole thing.

**Status:** Completed

---

## What It Covered

- Governance and compliance — governance itself, ethics in cybersecurity, IT security management frameworks
- Network security testing — security assessments, testing techniques and tools, penetration testing
- Threat intelligence — information sources, threat intel services
- Endpoint vulnerability assessment — network/server profiling, CVSS (common vulnerability scoring system), secure device management

**Checkpoint Exam: Vulnerability Assessment and Risk Management**

- Risk management and security controls — risk management generally, risk assessment specifically, security controls
- Digital forensics and incident analysis and response — evidence handling and attack attribution, the Cyber Kill Chain, the Diamond Model of Intrusion Analysis, incident response, disaster recovery

**Checkpoint Exam: Incident Response**

---

## What Actually Took Time

Module 6 is the big one and it deserves it honestly — the Cyber Kill Chain and the Diamond Model of Intrusion Analysis are two different frameworks for basically doing the same thing (understanding how an attack unfolds) but they approach it differently enough that keeping them straight in my head took a minute. Kill Chain is more linear, step by step through an attack. Diamond Model is more about the relationships between the adversary, capability, infrastructure, and victim. Took redoing the lab a couple times before the distinction actually stuck.

CVSS in module 4 was also something i had to sit with longer then expected — the scoring system looks straightforward with a single number at the end but the actual factors that go into that number (attack vector, complexity, privileges required, all that) take some getting used to before you can look at a CVSS score and actually understand what its telling you instead of just seeing "7.5 = bad."

Governance and ethics in module 1 i genuinely didnt expect to care about going in, figured itd be the boring compliance stuff to get through fast. actually ended up being more relevant then i thought, especially the ethics lab where you write your own code of conduct — made me think about stuff i hadnt really considered before, like where the line actually is between legitimate security testing and going too far.

---

## Why This One Ties Everything Together

Out of all six cisco courses this is the one that felt like it pulled everything else into one place. Networking Basics and Networking Devices gave the foundation, Network Defense and Endpoint Security gave the technical defense side, and this course gives the process/framework side — how do you actually manage risk, respond to an incident properly, and communicate about it. The Kill Chain and Diamond Model specifically connect directly to stuff ive already been doing on HTB and LetsDefend without having a formal name for what i was doing — turns out i was already sort of thinking in kill chain terms without knowing the actual framework.

---

## Notes

- [`notes.md`](./notes.md) — module by module notes
- `labs.md` — coming once i work back through the labs (governance/ethics labs, threat intel evaluation, CVSS scoring, risk analysis, and the incident response/forensics labs specifically)
- `reference.md` — condensed lookup sheet, after labs

---

*Completed as the sixth and final course in this cisco series — the one that ties governance, risk, and incident response together with everything from the earlier five.*
