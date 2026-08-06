# SOC Labs

Hands-on writeups from actual investigations — TryHackMe, LetsDefend, and HackTheBox. This is the part of the repo I care most about being solid. Anyone can complete a course and get a certificate; this is where I actually try to show I can think through a problem, not just follow steps.

---

## How These Are Different From `courses/`

`courses/` shows I sat through material and understood the concepts. This folder is different — each writeup here is me actually investigating something: an alert, a log file, a compromised system, a phishing email. I'm documenting my real process, including the parts where I got confused or had to backtrack, not just the clean final answer.

If a writeup here looks too smooth, thats probably a sign I cleaned it up too much. Real investigation has dead ends.

---

## Structure

```
soc-labs/
├── tryhackme/
│   ├── 01-tempest/                   SIEM/incident investigation (capstone-level)
│   └── 02-the-greenholt-phish/        Phishing analysis
│
├── letsdefend/
│   ├── challenges/
│   │   └── 01-investigate-web-attack/   Web attack log analysis
│   └── alerts/                          Live alert triage — true/false positive calls
│       ├── 01-.../
│       ├── 02-.../
│       └── 03-.../
│
└── htb/
    ├── 01-windows-event-logs-finding-evil/   Windows log forensics
    └── 02-intro-to-malware-analysis/          Malware analysis
```

---

## Why Only A Handful Of Writeups

Ive done alot more labs/rooms then what's documented here across all three platforms. Deliberately not writing up every single one — a handful of these done properly, with real reasoning and screenshots, is worth more then twenty rushed summaries that just say "completed X, got the flag." Quality over checklist.

Each writeup here was picked specifically to show a different skill, not just more of the same thing:

- **SIEM/incident investigation** — Tempest
- **Phishing analysis** — The Greenholt Phish
- **Web attack analysis** — Investigate Web Attack
- **Live alert triage** — LetsDefend alerts (x3)
- **Windows log forensics** — Windows Event Logs & Finding Evil
- **Malware analysis** — Intro to Malware Analysis

---

## Format

Most writeups follow roughly this structure, though it varies slightly by platform since challenges, alerts, and rooms don't all work the same way:

- **Scenario** — what I was given / what the situation was
- **Investigation** — my actual process, what I checked and why, including wrong turns
- **Findings** — what I actually found, with real queries/commands/screenshots
- **Conclusion** — what happened, and for alerts specifically, whether it was a true or false positive and why

---

*Updated as I work through more labs — this is a slow-growing section, not something I'm trying to fill quickly.*
