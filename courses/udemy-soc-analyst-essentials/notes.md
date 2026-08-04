# Notes — SOC Analyst Essentials (Udemy)

Lecture by lecture since the course itself is structured that way, each ones short so these notes are shorter too compared to the cisco module notes.

---

## 1. What is a SOC?

Basically the team/facility responsible for monitoring and responding to security threats in an org, 24/7 usually. Nothing new here from the cisco courses but a clean fast recap.

## 2. Roles in Cyber Security

Quick overview of different roles — SOC analyst tiers (L1/L2/L3), pentester, security engineer, that whole spread. Useful as a refresher, matches roughly what Intro to Cybersecurity covered but faster.

## 3. SOC's Structure

How a SOC is actually organized internally, tiers of analysts, escalation paths — L1 catches the initial alert, escalates to L2 if it needs deeper investigation, L3 for the really complex stuff.

**Quiz 1**

---

## 4. Types of Hackers

Black hat, white hat, grey hat — the classic categories. Also touched on script kiddies vs more sophisticated/organized attackers, similar to what Endpoint Security covered under "who is attacking our network."

## 5. CIA

CIA triad again — confidentiality, integrity, availability. Third or fourth time seeing this covered across different courses at this point, which honestly just reinforces how central of a concept it actually is rather then feeling repetitive.

## 6. Zero Trust

Never trust, always verify — the idea that you dont automatically trust anything just cause its already inside the network perimeter. Different from older security models that assumed once you're inside the network you're basically safe. This was a newer concept for me, cisco courses didnt use this specific term as much even though some of the segmentation ideas overlap with it.

**Quiz 2**

---

## 7. What is a SIEM?

Security Information and Event Management. Collects logs from across an org and correlates them so analysts arent digging through separate log sources manually. This is the tool most directly tied to actual SOC analyst day to day work, basically the main dashboard.

## 8. What is a SOAR?

Security Orchestration, Automation and Response. Different from SIEM — SOAR is more about automating the response side once somethings been detected, running playbooks automatically instead of an analyst doing every step manually.

## 9. What is a firewall?

Covered already in cisco courses but quick recap here — controls what traffic is allowed in/out based on rules.

**Quiz 3**

---

## 10. What is an EDR?

Endpoint Detection and Response. Focused specifically on individual endpoints (laptops, servers) rather then the network as a whole, connects back to alot of what Endpoint Security course covered.

## 11. What are IDS and IPS?

Intrusion Detection System vs Intrusion Prevention System. IDS just detects and alerts, doesnt block anything itself. IPS actually blocks/prevents the traffic. Similar naming so easy to mix up, but the distinction is basically detect-only vs detect-and-block.

## 12. Recap of SOC's Softwares

Quick tie together of SIEM/SOAR/EDR/IDS-IPS/firewall, how they all fit together as a stack rather then being separate unrelated tools.

**Quiz 4**

---

## 13. IP Address

Basics, already covered thoroughly in Networking Basics, quick recap here.

## 14. What is DNS?

Same, already covered in Networking Basics and Networking Devices, recap.

## 15. Phishing

Recap from Intro to Cybersecurity, common attack types.

## 16. OSINT

Open Source Intelligence — gathering info from publicly available sources. This ones relevant beyond just SOC work too, connects to stuff ive been thinking about for the OT/ICS consulting side, like using public info to find exposed industrial devices.

**Quiz 5**

---

## 17. Linux

Quick overview, way lighter then the full Linux module in Endpoint Security obviously, but a decent fast intro if you havent touched Endpoint Security yet.

## 18. What is a Malware?

Recap of malware types, similar to Intro to Cybersecurity coverage.

**Quiz 6**

---

## 19. Course's Slides

Just the slides themselves for reference.

## 20. Let's Look for Job Positions on LinkedIn

Genuinely one of the more useful lectures despite not being technical at all. Walks through actually searching SOC job postings, what titles to look for, what the postings actually ask for in terms of skills/tools. Helped me get a clearer sense of what to prioritize learning based on what real postings want, instead of just guessing at whats important.

## 21. Bonus Lecture

Short closing lecture.

---

## Overall

This course worked well as a fast-paced supplement alongside the cisco courses rather then a replacement for them. Nothing here went as deep as cisco's material, but the SOC-tool-specific lectures (SIEM/SOAR/EDR/IDS-IPS) were more focused then how cisco touches on similar tools, and having them explained back to back made the distinctions between them clearer then when they show up scattered across different cisco modules. The linkedin job search lecture at the end was the most unexpectedly useful part of the whole course.
