# Missing Person — TryHackMe (OSINT)

> **repo path suggestion:** `soc-labs/tryhackme/04-missing-person-osint/README.md`
> *(placeholder numbering — line it up with wherever tempest/greenholt-phish/ai-threat-modeling land)*

## Scenario

"My friend went on holiday in 2025 and shared some photos, but I haven't heard from him since. Can you help me track him down for the police report?"

Classic OSINT room — you're only given a handful of photos he shared and have to reconstruct his movements using nothing but publicly available info. Covers image metadata, reverse image search, geolocation, social media profiling, and business record lookup.

## Investigation

**Photo 1 — what circuit is this?**
Reverse image searched the racetrack photo. Google's AI overview pulled it straight up: the Pertamina Mandalika International Street Circuit in Kuta Mandalika, Lombok, Indonesia — a 4.31km FIA Grade 2/FIM Grade A circuit that hosts the MotoGP Indonesian Grand Prix.

`![circuit reverse image search](circuit-reverse-image-search.png)`

**When did the event take place?**
Pulled the EXIF data off the image — Create Date and Date Time Original both showed `2025:10:05`. That's the date the photo itself was taken, not necessarily the whole event, so I cross-referenced it against the official MotoGP schedule page for Indonesia and found the full event window: **03-05/10/2025**.

`![exif event date](exif-event-dates.png)`
`![motogp schedule page](moto-gp-schedule.png)`

**What's the restaurant with the Mexican food?**
Reverse image searched the restaurant photo (the one with the colorful papel picado banners hanging from the ceiling). Came back as Cantina Mexicana Kuta Lombok — matched not just the search result but the actual table numbers visible in the original photo too.

`![restaurant reverse image search](restaurant-reverse-image-search.png)`

**What time was the restaurant photo taken?**
Back to EXIF — Date Time Original this time gave a full timestamp: `2025-10-05T14:55:30.000Z`, which converts to **19:55:30** local time.

`![exif photo time](exif-photo-time.png)`

**Full address of the bar (from the last message he sent about the after-party)?**
No photo to work off here, just a text description. Searched for MotoGP after-parties happening in Lombok around those dates and got a handful of bar results. One of them — Surfers' Bar — matched the visual style/vibe described. Address came back as: Jl. Raya Kuta, Kuta, Kec. Pujut, Kabupaten Lombok Tengah, Nusa Tenggara Barat.

`![bar search results](bar-search-results.png)`

**The DJ's stage name?**
Found his Instagram through the bar's social presence — not posting that screenshot here out of privacy/respect, since he's a real person and not actually part of the "case." Stage name: **Bong Leleh**.

**What cave does he take tourists to?**
This one took a while — no direct name given anywhere, so I pulled up Google Maps and just scanned the area around the bar for anything tagged as a cave. Found Gua Sumur nearby and cross-checked it against the DJ's other social accounts to confirm the connection.

`![cave google maps search](cave-google-maps.png)`

**What number did the DJ list for his tour business?**
Searched his name directly and a Facebook page for "Gua Sumur Lombok" came up with a listed contact number: +62 853-3313-7345. Stripped the country code per the question's format requirement — final answer: **085333137345**.

`![dj tour business facebook page](dj-tour-business-facebook.png)`

## Findings / Verdict

Full timeline reconstructed from public info alone: friend was in Lombok, Indonesia for the MotoGP Indonesian Grand Prix (03-05 Oct 2025) at the Pertamina Mandalika circuit, ate at Cantina Mexicana on the evening of the 5th, went to an after-party at Surfers' Bar where he met a local DJ (stage name Bong Leleh), and was planning to visit the Gua Sumur cave with him the next day — which lines up with the DJ's tour business, contactable at 085333137345. That's the last confirmed lead for the report.

## What I'd Do Next

- Call the tour business number directly to confirm whether the cave trip actually happened and if he was seen after
- Check for any check-ins, reviews, or geotagged posts from Gua Sumur around the relevant date
- Cross-reference flight/departure records out of Lombok around that week if accessible through proper channels
- Reach out to Surfers' Bar directly — staff or other patrons that night might remember him

## What Tripped Me Up

*(these are my guesses at what would trip someone up here — swap these for what actually happened to you before this goes public)*

- Realizing the EXIF timestamp on a single photo only tells you when that photo was taken, not the full date range of the event — needed the official schedule page to fill that gap
- Narrowing down the right bar out of several similar-looking venues near Mandalika based on vibe/description alone, with no name given upfront
- The cave question specifically — no name to search, had to go visual-first on Google Maps instead of the usual text-search approach

## Tools Used

- exiftool (image metadata extraction)
- Google Reverse Image Search
- Google Maps
- Facebook / Instagram (social media enumeration)
- Google Search (business/phone number lookup)
