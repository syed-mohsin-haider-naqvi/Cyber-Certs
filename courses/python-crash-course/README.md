# Python Crash Course — Google / Coursera

## About This Course

This is part of Google's IT Automation with Python track on Coursera, first course in that series. Did this alongside the cisco stuff, wanted an actual programming foundation rather then just picking up bits and pieces from random tutorials. 5 modules total — starts from literally nothing (what is programming, what is automation) and builds up through syntax, functions, conditionals, loops, and then data structures (strings, lists, dictionaries, brief optional intro to classes/OOP), finishing with an actual final project pulling everything together.

Didnt have any real programming background going in besides messing around with basic scripts here and there, so this was genuinely starting from scratch for me, not a refresher.

**Status:** Completed

---

## What It Covered

**Module 1 — Introduction to programming and automation**
What programming actually is, what automation means and why it matters, basic python syntax intro, some arithmetic, and a look at code editors/IDEs. Ends with a "Hello Python" challenge.

**Module 2 — Basic Python syntax**
Data types, variables, type conversion (implicit vs explicit), defining functions and returning values, code reuse and code style, then into comparison/logical operators and branching with if/elif/else statements.

**Module 3 — Loops**
While loops first (including why initializing variables matters and how to avoid infinite loops), then for loops — nested loops, looping over strings, and a section specifically on common errors in for loops and how to fix them.

**Module 4 — Basic structures**
Strings in depth (indexing, slicing, string methods, formatting), then lists and tuples (modifying lists, iterating, list comprehensions), then dictionaries (iterating, dictionaries vs lists), and an optional intro to classes/methods/OOP concepts at the end.

**Module 5 — Final Project**
An actual project pulling together everything from the previous 4 modules — problem statement, doing research, planning it out, writing the script, then putting it all together as one graded final challenge.

---

## What Actually Took Time

For loops vs while loops took some getting used to at first, mostly just knowing when to reach for which one. The course actually has a whole section specifically on common for-loop errors which was more useful then id expected — things like off-by-one type mistakes, or forgetting `range()` behaves the way it does. Having those mistakes actually named and explained ahead of time meant i recognized them faster when i hit them myself later.

List comprehensions in module 4 also took a couple passes. The syntax is compact enough that it looked confusing at first compared to just writing a normal for loop, but once it clicked it became one of the things i actually reach for now instead of avoiding.

Grades on the practice assignments were mostly solid (100% on a few, 80-83% on a couple like the "expressions and variables" and "lists" quizzes) — nothing failed, but the ones i didnt get 100% on were good markers for what i needed to go back and actually solidify rather then just clicking through.

---

## Why This One Matters For What Im Building Toward

This is the actual foundation everything else python-related builds on — Boto3 scripts for AWS automation, log parsing for SOC work, eventually OSINT tooling for the OT/ICS side of things. Doesnt look flashy on its own compared to a security course, but its the base layer the more interesting stuff sits on top of.

---

## Notes

- [`notes.md`](./notes.md) — module by module notes

Real Python scripts and small projects built using what I learned here live separately in [`python-projects/`](../../python-projects/), split between security-focused and cloud-focused scripts.

---

*First real programming course completed, foundation for everything python-related going forward.*
