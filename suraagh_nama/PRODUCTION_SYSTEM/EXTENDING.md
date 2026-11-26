# EXTENDING — how to add new ideas without breaking the brand

The system is deliberately **two-layer**: a stable **core** (CHANNEL_BIBLE + toolkit) and a growing **creative
library** (`creative/`) where new things are tried. You add to the library freely; you change the core rarely and
on purpose. That's what keeps us consistent *and* flexible.

## The three kinds of "new"
| New thing | Where it goes | Gate |
|---|---|---|
| A new **episode idea** | `creative/IDEA_BACKLOG.md` | Score it against the brand rubric (below). |
| A new **creative item** (scene type, motif, transition, audio trick, thumbnail style) | `creative/SCENE_LIBRARY.md` / `MOTIFS.md` | Must respect CHANNEL_BIBLE §4–§7. Prototype on a preview first. |
| A new **capability in code** | `toolkit/` (graduates from a creative experiment) | Must be episode-agnostic, documented, and proven on one episode. |
| A new **rule or format** | edit `CHANNEL_BIBLE.md` (version bump) | Only after an experiment beat the north-star metrics. |

## The rule for any new creative idea (the brand test)
Before building it, it must pass all of these (from the BIBLE):
1. **Real-place anchored** — is there a real place/evidence this ties to? (If no → it's not Suraagh Nama.)
2. **Wonder + credibility** — does it add awe *and* keep trust? (No fabrication, §7.)
3. **On-voice** — does it fit the lamp-lit dastango tone, in Urdu, for a mobile Pakistani viewer?
4. **Buildable** — can the toolkit make it, or is it a bounded new script?
5. **Measurable** — if it's a bet, what metric (§9) tells us it worked?

Fails 1–3 → reject. Passes 1–3 but new to build → prototype it as an **experiment** on a 480p preview, measure, then
adopt (write it into the library/bible) or retire. Never ship an untested new technique straight to a master.

## The experiment loop
`idea → brand test → prototype on a preview → cloud review → measure on one real episode → adopt or retire`
Log the outcome in the creative library so we don't re-try dead ends (like Ep 1's three.js flood that looked CG).

## Versioning
- `CHANNEL_BIBLE.md` carries a version note when a rule changes; keep a one-line changelog at its bottom over time.
- Creative items are dated and marked `experimental` / `adopted` / `retired`.
- Code changes to `toolkit/` ride the normal commit history with a line in `reference/` when a technique is new.

## Starting a brand-new series (not just an episode)
A new series (e.g. "Mysteries of the Coast") inherits the BIBLE, then adds a short `SERIES_<name>.md` that states
only what differs (setting, recurring motifs, any palette shift). It never overrides §7 (ethics) or the core voice.
