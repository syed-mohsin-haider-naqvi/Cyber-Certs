# Python Projects

Small scripts and tools I've built with Python, split by what they're actually for. This isn't tied to one course — its where stuff from the Python Crash Course (see `courses/python-crash-course/`) actually gets put to use, plus anything else I build going forward as I get into cloud automation and security tooling specifically.

Not trying to make these look bigger or more advanced then they are. Some of these are genuinely small, first-attempt scripts. The point is showing real progression over time, not pretending to be more advanced then I actually am right now.

---

## Structure

```
python-projects/
├── basics/            starter scripts from working through the Python Crash Course itself
├── security/           scripts related to SOC/security work
└── cloud/               scripts related to AWS/cloud work, mostly Boto3
```

---

## basics/

Small scripts written while actually going through the Python Crash Course — not polished projects, just practice code from working through functions, loops, and data structures. Keeping these separate from the security/cloud folders since theyre learning exercises, not real tools built for an actual purpose. Worth having here anyway since it shows the actual starting point rather then only showing the more advanced stuff and skipping the part where I was still figuring out basic syntax.

---

## security/

See [`security/README.md`](./security/README.md) for details. Scripts here are mostly things that support SOC-style work — log analysis, OSINT lookups, that kind of thing. Built as I go through SOC labs and figure out what would actually be useful to automate instead of doing manually every time.

---

## cloud/

See [`cloud/README.md`](./cloud/README.md) for details. Scripts here use Boto3 (AWS's python library) to interact with AWS directly instead of clicking through the console every time. Built alongside the AWS Cloud Practitioner material and the hands-on projects in `cloud-projects/`.

---

## Why Split It This Way

This maps onto the same two-pillar thing the rest of this repo is built around — security and cloud, converging toward cloud security specifically. Keeping the python scripts split the same way instead of dumping everything in one flat folder makes it obvious which skill each script is actually demonstrating.

---

*Updated as I build more of these — starting small and adding real scripts over time rather then trying to fill every folder immediately.*
