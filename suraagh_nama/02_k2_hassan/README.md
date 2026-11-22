# 02 · Muhammad Hassan, K2 — "تو کیا آپ رُکتے؟"

Suraagh Nama episode 2. Urdu narration, Urdu/Hindi/English captions. About 9 minutes.
Research dossier, full script versions and the visual plan are in the Claude Doc:
https://claude.ai/artifact/3KsWxnv5xzoduLJVzr3AJD

## The story in one line
On 27 July 2023, a Pakistani porter lay dying in K2's Bottleneck while a line of climbers passed him on their way to a world record. One stranger stopped. A year later, five Pakistani climbers went back up and brought him home. The promises made to his family were never shown to be kept.

## Why this video works (the concept)
- **One image carries the film:** a single headlamp in the dark. It opens the video, it is the "still light" the line walks past, and in the last shot it goes out. The ending mirrors the opening, which pays off viewers who stay to the end.
- **A refrain instead of commentary:** "اور قطار چلتی رہی" lands twice, each time followed by two seconds of silence with only footsteps on snow. The silence carries the judgement; the narration doesn't moralise.
- **Three acts, one point of view each:**
  - رسّی (the rope): his cousin and the night.
  - اجنبی (the stranger): Gabriel and the record.
  - واپسی (the return): the family and the Pakistanis who brought him home.
- **The viewer is the jury:** three conflicting accounts (Steindl, Harila, the Russian cameraman), then "آپ کے خیال میں…" (comment prompt one). The film ends on "تو کیا آپ رُکتے؟" (comment prompt two).
- **Facts, attributed:** every claim is attributed ("…کے مطابق"). Where we could not verify a promise was kept, we say so ("ہمیں کوئی ثبوت نہیں مِلا"); we never say it was broken.

## Structure (final cut, from chapters.txt)
| Chapter | Starts | Ends on |
|---|---|---|
| ایک رات، ایک قطار (cold open + the three people) | 0:00 | "آئیے، آپ کو اُس رات میں واپس لے چلتے ہیں" |
| پہلا حصہ · رسّی | see 09_export/chapters.txt | "ایک اجنبی رُک گیا" |
| دوسرا حصہ · اجنبی | " | "…برف کے نیچے دبا رہا" |
| تیسرا حصہ · واپسی | " | "…خبر ہمیں آج تک نہیں مِلی" |
| Summit کی تصویر | " | "تو کیا آپ رُکتے؟", then the headlamp goes out |

Breathing pauses are inserted into the voice-over at the key beats (timeline.json → gaps). They also slow the fast ElevenLabs read without regenerating it.

## Look
| Part | Palette | Feeling |
|---|---|---|
| Night on the Bottleneck | Near-black navy; one warm headlamp is the only warm light | Alone, cold |
| Tisar and the family | Warm Earth Studio daylight | Home |
| Summit and record | Golden sunrise | Glory, the contrast with below |
| Drone morning | Flat grey | Too late |
| Inquiry, money, promises | Paper and navy cards, red stamps | Cold bureaucracy |
| The year, the return | White-grey, then evening gold | Grief, then release |

**Safety rules (keep these on every revision):**
- No real faces and no body.
- People appear only as lights, silhouettes or dots.
- Reconstructions carry the "منظر کشی / AI reconstruction" tag.
- 3D terrain carries "reconstruction · route approximate".
- Women and children of the family are not named.
- Disclaimer at 0:00.
- Tick YouTube's "altered or synthetic content" box at upload.

## Folder map
| Folder | What's inside |
|---|---|
| 01_voiceover | Final ElevenLabs voice-over, script, cue table (Urdu, English, Hindi per line), speech and word timings |
| 02_captions | Captions timed to the raw voice-over; `final/` holds captions re-timed to each cut (upload these) |
| 03_motion_graphics | 17 cards: map, chapter cards, wage, counter (alpha), record, three answers, claim, inquiry, price, promises, law, disclaimer, AI tag (alpha), end card |
| 04_scenes | 12 reconstruction scenes, named by shot number (S01 lone headlamp … S30b headlamp goes out) |
| 05_earth_studio | **Waiting on you:** see README inside |
| 06_music | **Waiting on you:** see README inside |
| 07_sfx | Sound effects are synthesized inside build.py (wind, snow steps, rope creak, impact, heartbeat, mask breathing, river, helicopter) |
| 08_edit | `timeline.json` (the edit: which clip under which line), `build.py` (renders the whole video), fonts |
| 09_export | Finished cuts, chapters.txt, edit_report_<version>.md (timeline table + what's still missing) |
| 10_news_footage | **Waiting on you:** see README inside |

## How to make a new cut
1. Drop files into 05 / 06 / 10 using the names in each folder's README.
2. Optionally change `08_edit/timeline.json`. Each segment is a voice-over cue number, a source clip and an "in" point.
3. Run `python3 08_edit/build.py v2`.
4. Check `09_export/edit_report_v2.md`. "Missing" should be empty before upload.

Needs Python 3 with numpy, and ffmpeg.

## Music cue sheet (what build.py does with 06_music)
- **No music in the cold open.** Wind only, then a dark drone under the arriving line.
- **Silence** at both "اور قطار چلتی رہی" and after "تو کیا آپ رُکتے؟".
- The **main piano theme** plays three times:
  - the story begins and Tisar;
  - "ایک اور بیٹا پیدا ہُوا";
  - the ending.
- **Warm strings** play only for Gabriel.
- A **cold bed** sits under the inquiry, the price and the promises.
- A **build** runs from the Sadpara recovery to "اپنے گھر واپس آ گیا", the emotional peak.
- Music sits about 17 dB under the voice and ducks a further 6 dB while he speaks. Final loudness is -14 LUFS (YouTube's target).

## Upload checklist
- [ ] Missing list in the edit report is empty: Earth Studio, news footage and music are all real files.
- [ ] Watch once on a phone at full volume, then once muted with captions.
- [ ] Upload `02_captions/final/*_<version>.srt` (Urdu, Hindi, English) via Subtitles → Upload file → With timing.
- [ ] Paste `09_export/chapters.txt` into the description.
- [ ] Credits in the description:
  - Google Earth.
  - Terrain: AWS Terrain Tiles (Mapzen / SRTM), route approximate.
  - The news channels whose footage is used.
  - Music, only if a track needs attribution.
- [ ] Studio → "Altered or synthetic content" → Yes.
- [ ] End screen elements on the two boxes of the end card (last 12 s).
