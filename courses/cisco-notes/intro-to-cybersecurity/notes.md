# Notes — Introduction to Cybersecurity (Cisco Networking Academy)

Notes from working through this course. Writing these mostly for myself so I actually remember the stuff later, not trying to make it sound impressive.

---

## CIA Triad

This is the thing basically every other security topic gets measured against, so worth actually understanding not just memorizing.

- **Confidentiality** — only the right people can see the data
- **Integrity** — data hasn't been changed by someone who shouldn't have touched it
- **Availability** — the system/data is actually there when you need it

The way I actually remember which is which: if someone *reads* something they shouldn't = confidentiality broken. If they *change* something = integrity broken. If they *block* access = availability broken. A lot of real attacks hit more than one of these at the same time, which is something the course didn't really explain but I figured out later doing labs — like ransomware hits availability obviously (you can't get your files) but also kind of touches integrity depending on how you look at it.

---

## Threats/Attacks

**Malware types:**
- Virus — needs a host file to spread, attaches to something legit
- Worm — spreads on its own, no host needed
- Trojan — pretends to be something legit
- Ransomware — locks your files, wants money

**Social engineering** — this is the one I actually think about the most. Doesn't matter how good the firewall is if someone just calls and asks nicely, or sends a fake email that looks real enough. Course covered:
- Phishing (fake emails/messages)
- Pretexting (making up a fake reason to get info out of someone)
- Baiting (leaving a USB drive somewhere hoping someone plugs it in)

**DoS/DDoS** — flooding something with traffic so real users can't use it. DDoS = distributed, meaning it's coming from a bunch of different sources at once (botnet usually), which is why it's harder to just block one IP and be done with it.

---

## Basic Crypto

- Encryption = turning readable data into unreadable data, need the right key to read it again
- Symmetric = same key both ways, faster but you gotta share the key safely somehow first
- Asymmetric = public key to encrypt, private key to decrypt, slower but solves the key sharing problem
- Hashing = NOT the same as encryption, this one you can't reverse. used to check if a file got tampered with, not to hide it

I mixed up hashing and encryption a few times before this clicked. Encryption you're supposed to be able to undo (with the key). Hashing you're not supposed to be able to undo at all, ever.

---

## Network Security / Defense in Depth

Basically: don't rely on one single thing to keep you safe, stack multiple layers so if one fails something else catches it.

- Firewalls
- Antivirus/endpoint stuff
- Access controls (who's allowed to touch what)
- Logging/monitoring — this is the layer that actually connects to what SOC analysts do day to day, which I didn't really get until after I started the labs on HTB and LetsDefend and realized half of what I was doing there was literally just this

---

## Career Paths (from the course)

- SOC Analyst — watches alerts, investigates stuff
- Pentester — gets paid to break in before real attackers do
- Security Engineer — builds/maintains the actual security tools and setup
- GRC — more policy/audit/compliance side, less hands on technical
- Incident Responder — handles stuff when it's already going wrong

Honestly already knew roughly what these were from reading around online before this course, but having them actually laid out clearly helped.

---

## What I Actually Got Out Of This

Nothing here was hard exactly, it's an intro course. But it gave me the vocabulary so when I jumped into HTB and LetsDefend labs after, I wasn't stopping every five minutes to google what a term meant. That part mattered more than I expected going in — I thought the course itself would feel kind of pointless since it's not hands on, but not having to look up basic terms mid-lab later on was worth it.
