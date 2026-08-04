# Notes — Python Crash Course (Google / Coursera)

Module by module, same format as my other course notes. This one moves fast — 5 modules covering actual programming from scratch, so more concept-dense then some of the cisco stuff even though each individual video is short.

---

## Module 1 — Introduction to Programming and Automation

Started right at the beginning basically — what programming even is, what automation actually means (getting computers to do repetitive stuff for u instead of doing it manually every time), and why that matters practically. Then a first look at python syntax specifically, some basic arithmetic operations, and a rundown of code editors/IDEs u can actually use to write python.

Module ends with a "Hello Python" challenge — first actual graded thing in the course, basic as it sounds but its the first time actually writing something instead of just watching/reading.

Nothing here was hard exactly, more just orientation before the real content starts in module 2.

---

## Module 2 — Basic Python Syntax

This is where it gets real.

- **Data types** — int, string, boolean, etc, and how to identify which is which
- **Variables** — assigning data, referencing variables later
- **Type conversion** — implicit (python does it automatically) vs explicit (u tell it to convert, like using `int()` or `str()`)
- **Functions** — defining them, passing parameters, returning values
- **Code reuse and code style** — writing functions so u dont repeat yourself, and keeping code readable
- **Comparison and logical operators** — `==`, `!=`, `and`, `or`, etc
- **Branching** — if statements, else statements, elif for more complex branching

Got 80% on the "expressions and variables" quiz and 80% on "functions" too — nothing failed but these were the two spots where i clearly hadnt fully locked things in yet on first pass. Went back over type conversion specifically (kept mixing up when python converts automatically vs when u have to do it yourself) and functions/parameters before it felt solid.

Got 100% on conditionals though, if/elif/else made intuitive sense pretty much right away, probably cause its close to how u'd naturally think through a decision anyway.

---

## Module 3 — Loops

- **While loops** — the anatomy of one, why initializing variables before the loop matters (otherwise u can get errors or unexpected behavior), and how infinite loops happen plus how to actually break out of them
- **For loops** — what they are, more examples, the `range()` function specifically, nested for loops, looping over strings, and a dedicated section on common for-loop errors and how to fix them

Got 80% on the while loops quiz, 100% on for loops. While loops took a bit more care mainly around the initializing variables thing — forgot to set a starting value a couple times early on and got confused why the loop wasnt behaving right, which is exactly the mistake the course warned about, just had to actually make it myself once before it really stuck.

The common-for-loop-errors lesson specifically was more useful then i expected going in. Stuff like off-by-one issues with `range()`, or messing up what your looping over — having these named and explained ahead of time meant when i hit similar bugs later i recognized the pattern faster instead of being stuck confused.

---

## Module 4 — Basic Structures

Biggest module content wise.

- **Strings** — parts of a string, indexing and slicing, creating new strings, basic and more advanced string methods, formatting strings multiple ways
- **Lists and tuples** — what a list is, modifying contents, lists vs tuples (tuples being immutable is the key difference), iterating over both, iterating with `enumerate()`, and list comprehensions specifically — covered both how to write them and when to actually use one instead of a normal for loop
- **Dictionaries** — what one is, iterating over contents, using while loops and if/else with dictionaries, dictionaries vs lists (key-value pairs vs just ordered items)
- **OOP intro (optional)** — methods, constructors, special methods, instance methods — kept this section lighter since it was marked optional, but useful to have seen the basic vocabulary even briefly

Got 100% on strings and dictionaries, 83.33% on lists specifically. List comprehensions were the part that took the most repetition — the compact syntax `[x for x in something]` looked confusing compared to writing the equivalent for loop out normally, took writing a bunch of small examples myself before it stopped feeling like a weird shortcut and started feeling like something i'd actually reach for.

---

## Module 5 — Final Project

Pulls everything from modules 1-4 together into one actual project instead of isolated exercises:

- Problem statement — being given (or defining) an actual problem to solve
- Research — figuring out what youd actually need before writing any code
- Planning — mapping out the approach before jumping straight into typing
- Writing the script — actually building it
- Putting it all together — the final combined submission

This module was less about learning new syntax and more about actually using everything from the earlier modules in one place, which honestly felt like a good test of whether stuff had actually stuck or if id just been passing quizzes without really absorbing it.

---

## Overall

Went from knowing basically nothing formal about python to being able to write functions, work with all three core data structures (strings/lists/dictionaries), use loops properly, and handle basic branching logic confidently. Not advanced by any means, but a real foundation.

Weakest spots based on the quiz grades were expressions/variables and functions early on (both 80%), and list comprehensions specifically within module 4 (83%) — went back and did extra practice on all three rather then just moving on with a lower score. Strongest were conditionals and for loops, both 100%, probably cause the logic maps closely to how id naturally think through those problems anyway even before learning the actual syntax.

This is the base everything else python related builds from — Boto3 for cloud automation, log parsing scripts, eventual OSINT tooling. Actual scripts and small projects using this stuff live in the separate `python-projects/` folder, not here — this folder's just the course notes.
