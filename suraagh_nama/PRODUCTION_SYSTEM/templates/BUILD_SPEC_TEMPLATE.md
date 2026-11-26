# BUILD SPEC — <EPISODE NAME>

> Filled in the **cloud session** after the story + script + packaging are final.
> Handed to the **local session**, which builds the video per `RUNBOOK.md` using `toolkit/`.
> Everything the local session needs should be in here or in the linked files. Keep it self-contained.

## 0. Snapshot
- **Series / Ep #:**
- **Working title (search name):**
- **One-line hook:**
- **Runtime target:** ~X min
- **Status of VO:** (recorded? who? file path)

## 1. Final script
- Link/path to `SCRIPT_vFINAL.md` (the human-readable cut) and `vo_parts/` (ElevenLabs-ready part files P01…Pn).
- Note the storytelling style in use (e.g. dastangoi: حاضرین, character voices, verse, sittings).

## 2. Voice parts → roles (for the mixer's character FX)
| Part | Role | FX treatment |
|---|---|---|
| P01 | Narrator | dry |
| P02 | Loudspeaker | PA band-pass + valley echo |
| … | Astrologer / Fairy / Prince / Demon / Verse | (see audio_plan FX map) |

## 3. Illustrations to generate (Gemini) — see IMAGE_GEN_GUIDE
- **Style block:** (paste the episode's style line — keep Persian/Mughal realism, modest, real settings, no text)
- **Character bible:** (each recurring character's locked description)
- **Shot list:** table of `file name | prompt | format | used in part`. Mark which need a reference image for consistency.

## 4. Real footage / stock to gather
- List each clip/photo, the search terms, the source (Pexels/Pixabay/Openverse/archive.org), and the license note.
- Flag anything that must be real (landscapes, documents, maps) vs illustrated (dastan scenes).

## 5. Scene list & edit order (drives assemble.py PLAN)
Ordered beats with the clip(s) per voice part and the sound under each. Mirror Ep 1's EDIT_PLAN table:
`Part | clips (with @offset / weights) | SFX/music | cut-or-dissolve`. Note any beat cuts (e.g. demon line on lightning).

## 6. Audio plan — see AUDIO_GUIDE
- **Music slots** M1…Mn: where each plays + mood/instrument + search terms.
- **SFX** S01…: filename + search terms + where used.
- **Rider notes:** which beats may rise near the voice (title boom, thunder, flood, cards); default music ≈15 dB under speech.

## 7. Packaging (final)
- **Title (Roman Urdu):**
- **Description:** (hook + chapters + sources + AI disclosure + hashtags)
- **Tags:** (comma-separated)
- **Thumbnail:** concept + text + which assets. (Cloud usually delivers the PNG.)
- **Chapters:** (from the sitting-card / section times)

## 8. Scene-specific build notes
Anything non-obvious: a day-for-night shot, a flood map, a map-route animation, a composited figure, a tricky mix moment.
Point to the toolkit script that handles it.

## 9. Sources / fact-check log
Primary sources with page numbers, and any claim deliberately softened or cut. (Protects the brand: legend + real evidence.)
