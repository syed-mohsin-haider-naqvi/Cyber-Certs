# LetsDefend

LetsDefend is a platform built around simulating actual SOC analyst work — instead of just rooms with quiz questions, it puts you in front of a monitoring dashboard with real alerts to triage, plus separate challenges with a specific scenario and log file to investigate.

I've used this alongside TryHackMe and HTB, but LetsDefend specifically is the closest to what day-to-day SOC L1 work actually feels like — checking a queue, pulling up an alert, deciding if its real or noise.

---

## What's In This Folder

```
letsdefend/
├── challenges/       Defined scenario + specific questions, one correct answer each
└── alerts/           Live alert triage — no predefined questions, I decide true/false positive myself
```

**[challenges/](./challenges/)** — scenario-based investigations with a specific log file or artifact and a set of questions to answer. Currently includes:
- [Investigate Web Attack](./challenges/01-investigate-web-attack/) — analyzing an access log to reconstruct a web reconnaissance and attack attempt

**[alerts/](./alerts/)** — pulled directly from LetsDefend's simulated SOC monitoring queue. No predefined questions here, just an alert and the job of deciding whether its a real threat or a false positive, same as actual shift work. See [alerts/README.md](./alerts/README.md) for the full list.

---

*More challenges and alerts get added here as I work through them — not trying to cover everything on the platform, just documenting the ones worth showing.*
