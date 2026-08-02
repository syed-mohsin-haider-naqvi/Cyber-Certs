# Notes — Introduction to Cybersecurity (Cisco Networking Academy)

Study notes from working through the course. Mix of definitions I wanted to keep straight and my own explanations where something took a bit to click.

---

## 🔐 The CIA Triad

The core framework almost everything else in security gets measured against.

- **Confidentiality** — only the people who are supposed to see data can see it. Broken by things like data breaches, weak access controls, unencrypted data.
- **Integrity** — data hasn't been changed or tampered with, whether by accident or on purpose. Broken by things like unauthorized edits, man-in-the-middle attacks altering data in transit.
- **Availability** — systems and data are accessible when needed. Broken by things like DDoS attacks, hardware failure, ransomware locking you out.

**My own way of remembering it:** if an attacker *reads* something they shouldn't — confidentiality. If they *change* something — integrity. If they *block access* to something — availability. Most real attacks actually hit more than one of these at once.

---

## ⚠️ Threats & Attacks

**Malware** — general term for malicious software. Sub-types worth knowing separately:
- Virus — attaches to a legitimate file/program, needs that program to run to spread
- Worm — spreads on its own across a network, no host file needed
- Trojan — disguised as something legitimate to trick you into running it
- Ransomware — encrypts your files, demands payment to unlock

**Social engineering** — manipulating people rather than exploiting technical systems. This is the one that stuck with me most — no matter how good the technical defenses are, humans are usually the easier target.
- Phishing — fake emails/messages trying to get you to click something or hand over credentials
- Pretexting — attacker invents a false scenario to get information out of someone
- Baiting — leaving something enticing (like a USB drive) to get a victim to compromise their own system

**DoS / DDoS** — Denial of Service / Distributed Denial of Service. Flooding a system with traffic so real users can't access it. "Distributed" means it's coming from many sources at once (usually a botnet), which makes it harder to block than a single source.

---

## 🔑 Cryptography Basics

- **Encryption** — converting readable data (plaintext) into unreadable data (ciphertext) so only someone with the right key can read it
- **Symmetric encryption** — same key used to encrypt and decrypt. Faster, but you have to securely share the key with the other party somehow
- **Asymmetric encryption** — uses a public key (encrypt) and private key (decrypt) pair. Slower, but solves the key-sharing problem since the public key can be shared openly
- **Hashing** — different from encryption. One-way — you can't reverse a hash back to the original data. Used to verify integrity (e.g. checking a downloaded file hasn't been tampered with) rather than to hide data

**Note to self:** encryption and hashing get mixed up a lot when talking casually about security — encryption is meant to be reversed (decrypted) by someone with the key, hashing isn't meant to be reversed at all.

---

## 🛡️ Network Security & Defense-in-Depth

Defense-in-depth = don't rely on one single security measure. Layer multiple defenses so if one fails, others still catch the problem.

Examples of layers:
- Firewalls — control what traffic is allowed in/out of a network
- Antivirus/endpoint protection — catches malware on individual devices
- Access controls — limiting who can reach what, even inside the network
- Monitoring/logging — so if something does get through, there's a record to investigate

This connects directly to what SOC analysts actually do day to day — the monitoring/logging layer is where a lot of the actual detection work happens, which is why this course made more sense once I started the hands-on labs afterward.

---

## 💼 Cybersecurity Career Paths (from the course)

Rough breakdown the course gave of common roles:
- **SOC Analyst** — monitors alerts, investigates incidents, first line of defense
- **Penetration Tester** — authorized attacker, finds vulnerabilities before real attackers do
- **Security Engineer** — builds and maintains security infrastructure/tools
- **GRC (Governance, Risk, Compliance)** — policy, audits, regulatory compliance side rather than hands-on technical work
- **Incident Responder** — handles active security incidents, containment and recovery

Useful mainly for getting the vocabulary straight — I already had a rough sense of these from research, but this laid it out more clearly.

---

## 🧠 Overall Takeaway

This course didn't teach anything technically difficult, but it gave me the shared vocabulary that made the hands-on labs afterward (HTB, LetsDefend) click faster — I wasn't stopping mid-lab to look up what a term meant. Worth doing early rather than skipping straight to hands-on work.
