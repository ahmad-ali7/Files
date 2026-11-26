# AUDIO GUIDE (template) — music + SFX from the YouTube Audio Library

For the local session (Chrome, signed in to YouTube Studio → Audio library). Fill specifics from BUILD_SPEC §6.

## Rules
1. **Only the YouTube Audio Library** (cleared for monetised videos). Prefer "No attribution required"; if a
   track needs attribution, copy its exact line into `CREDITS.md`.
2. **Instrumental only** — no vocals/lyrics (the VO carries the words).
3. Preview the first 20–30 s. It must feel **Pakistani / Persian, mysterious, night-time** — not upbeat/EDM/pop.
4. Pick the best per slot + a runner-up `_alt`. Keep exact file names from the spec.
5. Write `LOG.md` (slot, title, artist, length, licence, why) and `CREDITS.md`.

## Music slots (typical shape — the spec lists the episode's actual set)
`M1` mystery/opening · `M2` romantic/dastan (sitar, bansuri, santoor, oud) · `M3` tension/storm ·
`M4` calm documentary bed (evidence sections) · `M5` emotional/mystic ending. Save to `prod/audio/music/`.

## SFX (typical — the spec lists the episode's list)
wind, river/stream, thunder (close + distant), heavy rain, flood/rushing water, night crickets, water drop,
candle/fire, page turn, magic shimmer, whoosh, deep boom, footsteps, distant dog, snow/blizzard wind, small bells.
Save to `prod/audio/sfx/` with the spec's exact `S01…` names. **Don't** fetch a mosque-loudspeaker voice — the
mixer makes that from Ahmad's own line.

## How the mixer uses it (for reference)
`audio_plan.py` places each bed over its section and ducks it with a **voice-first rider** (music ≈15 dB under
speech, effects ~10 dB under), letting beds swell only in pauses and on chosen beats (title boom, thunder on the
demon line, the flood, sitting cards). Whole mix normalised to **-14 LUFS** (YouTube target).

## Note
Neither Claude session can *hear* audio — picks are made from the library's tags/titles/duration + the brief.
**Ahmad should listen** to the first 20–30 s of each pick before the final mix.
