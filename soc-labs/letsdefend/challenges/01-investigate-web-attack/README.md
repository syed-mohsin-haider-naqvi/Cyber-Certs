# Investigate Web Attack — LetsDefend Challenge

## Scenario

LetsDefend flagged web attack activity and the task was to dig through the provided `access.log` file to reconstruct what actually happened — from initial reconnaissance through to whatever the attacker ended up doing once they got in. No SIEM here, just a raw access log and a text editor, so this one was pure manual log reading rather then querying a platform.

Attacker IP throughout: `192.168.199.2`
Target: `192.168.199.5` (running bWAPP, a deliberately vulnerable web app)

---

## Investigation

### Question 1 — Which automated scan tool did the attacker use for web reconnaissance?

First thing I did was search the whole log for the attacker's IP specifically, since I figured whatever they did would be clustered together once filtered down. That immediately narrowed things out from thousands of irrelevant lines to just their activity.

Didn't take long to spot it — the requests from that IP had a distinct user-agent string sitting right in the log line, not something I had to dig for:

```
"Mozilla/5.00 (Nikto/2.1.6) (Evasions:None) (Test:Port Check)"
```

**Answer: Nikto**

Nikto's a pretty well known automated web scanner, and it doesn't really try to hide itself in the user-agent, which honestly made this first question the easiest one of the whole challenge.

![Nikto user-agent visible in log](./screenshots/q1-nikto-useragent.png)

---

### Question 2 — After web reconnaissance, which technique did the attacker use for directory listing discovery?

After confirming Nikto was the recon tool, I kept scrolling through the same filtered IP and started noticing a pattern — a huge run of requests hitting different paths one after another, all coming back 404, with random-looking filenames like `4RaXX5Ac.exe`, `4RaXX5Ac.show`, `4RaXX5Ac.java`, `4RaXX5Ac.x-shop` and so on, all in the same second-ish window.

That pattern — rapid-fire requests to a long list of guessed paths/filenames — is basically the textbook signature of directory brute forcing. The tool's throwing a wordlist at the server trying to find directories/files that exist by brute forcing the names rather then actually knowing them ahead of time.

**Answer: Directory brute force**

![Rapid sequential requests showing brute force pattern](./screenshots/q2-directory-bruteforce.png)

---

### Question 3 — What was the third attack type after directory listing discovery?

This one took a bit more scrolling to actually locate. After the brute force activity died down, I kept moving further down the log looking for the next distinct cluster of activity, and eventually landed on a big block of POST requests all hitting `/bWAPP/login.php`, back to back, dozens of them in quick succession.

Once I saw it was specifically POST requests repeatedly targeting a login page, that narrowed down what kind of attack this actually was pretty fast — that pattern is the signature of someone trying to guess login credentials by throwing repeated attempts at the same endpoint.

**Answer: Brute force (login/credential brute force)**

![Repeated POST requests to login.php](./screenshots/q3-login-bruteforce.png)

---

### Question 4 — Was the third attack successful?

Since the third attack was targeting the login page, the natural next question was whether it actually worked. Instead of just assuming, I kept reading forward past the burst of failed POST attempts to see what happened right after.

Right after the repeated login attempts stopped, the log showed a request to `/bWAPP/portal.php` returning a 200 status — portal.php being the kind of page you'd only land on after actually authenticating successfully on a login form like this. Before that point every login attempt was just POSTing back to login.php itself; the switch to portal.php loading successfully was the tell that one of those attempts actually worked.

**Answer: Yes**

![Successful redirect to portal.php after brute force attempts](./screenshots/q4-successful-login.png)

---

### Question 5 — What was the fourth attack?

With the attacker now authenticated and browsing around (`portal.php`, then `phpi.php`), I kept following the log forward looking for anything that looked like it was doing more then just normal navigation.

Found it in a request like:

```
GET /bWAPP/phpi.php?message=%22%22;%20system(%27whoami%27)
```

URL-decoded, that's `message="";system('whoami')` — the attacker was injecting a system command directly through the `message` parameter. That's textbook remote code execution via a vulnerable parameter, PHP specifically letting the injected `system()` call execute directly on the server.

**Answer: Code injection (command injection / RCE via the `message` parameter)**

I want to be honest that I had to look up what a payload like this actually does before I was confident calling it code injection specifically rather then just "some kind of injection attack" — the `system()` function wrapped inside the URL parameter wasn't something I immediately recognized on sight.

![Code injection payload in message parameter](./screenshots/q5-code-injection.png)

---

### Question 6 — What was the first payload for the fourth attack?

Following directly from question 5 — same request, same parameter, the actual command being executed inside that first `system()` call was `whoami`. Simple recon command, attacker checking what user context they'd landed in after getting code execution.

```
GET /bWAPP/phpi.php?message=%22%22;%20system(%27whoami%27)
```

**Answer: `whoami`**

---

### Question 7 — Is there any persistence clue in the log file, and what's the related payload?

Last question, and this took the longest. Persistence means the attacker trying to make sure they can get back in later even if their current access gets cut off, so I specifically looked for anything after the initial `whoami` recon that looked like account creation, backdoor setup, or user modification — commands that survive past the current session.

A few lines down from the `whoami` call, found this:

```
GET /bWAPP/phpi.php?message=%22%22;%20system(%27net%20user%20hacker%20Asd123!!%20/add%27)
```

I tried to decode/read through it and honestly wasn't 100% sure I was reading the encoded version correctly at first, so I submitted it in its encoded form rather then risk mis-transcribing it:

**Answer: `%27net%20user%20hacker%20asd123!!%20/add%27`**

Decoded, that's a Windows `net user` command creating a new local account named `hacker` with the password `Asd123!!` — a classic way to plant a persistent backdoor account on a compromised machine so the attacker can log back in later through a completely legitimate-looking user account instead of relying on the original exploit still being open.

![Persistence payload creating backdoor user account](./screenshots/q7-persistence-payload.png)

---

## Putting It Together

Full attack chain, start to finish: the attacker ran Nikto against the target for initial reconnaissance, then brute forced directories/filenames to map out what existed on the server. From there they moved to brute forcing the login page itself and got a successful authentication. Once inside, they found a vulnerable parameter on `phpi.php` and used it for command injection — first running `whoami` to check their access level, then using the same injection point to create a new local user account (`hacker`) as a persistence mechanism, so they'd have a way back in later even without relying on the original login brute force working again.

This is a pretty clean example of a full attack progression — recon, discovery, initial access, then post-exploitation persistence — all visible just from reading through one access log carefully in order.

---

## What Tripped Me Up

Question 5 specifically — recognizing the `system()` call as code injection wasn't immediate for me, I had to actually look into what that PHP function does when it's reachable through a URL parameter like that before I felt confident in the answer rather then just guessing based on the word "system" showing up.

Question 7 also slowed me down a bit, mostly just from scrolling through a long log carefully enough not to miss the persistence attempt, since it wasn't immediately next to the code injection discovery — had to keep reading a good chunk further down before it showed up.

---

## Tools Used

- Text editor with search (GNOME Text Editor) — filtering the log by attacker IP first made everything after that much more manageable then trying to read the raw file top to bottom
