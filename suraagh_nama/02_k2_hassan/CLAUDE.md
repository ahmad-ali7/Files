# K2 Hassan episode: handoff for the local editing session

Read this whole file before touching anything. It is the complete context from the cloud session that researched, wrote and pre-built this video. The goal of this session: produce the **final cut** with the fewest possible revisions.

---

## 0. First 10 minutes (do these in order)

1. **Find the episode folder.** It's the repo folder `suraagh_nama/02_k2_hassan/` (from github.com/ahmad-ali7/Files, branch `claude/eloquent-dirac-5kmw24`). Ahmad may also have dropped loose media files next to it.
2. **Check the tools:**
   - `ffmpeg -version`
   - `python3 -c "import numpy"`
   - If missing: `brew install ffmpeg python` and `pip3 install numpy`.
3. **Inventory the media and move each file into its slot** with the exact names in section 6. Report anything you can't place, and anything that's missing.
4. **Build:** `python3 08_edit/build.py v2`, run from the episode folder. It takes about 5–15 minutes.
5. **Read** `09_export/edit_report_v2.md`. The "Missing" list must be empty, and every music role must show a real file, not "INTERIM".
6. **Make a review copy** and give it to Ahmad (section 9). Ask for notes by timestamp only.

Don't redesign the film. The story, script, structure, look and timings below were decided with Ahmad over many rounds. Only change what he asks for, or what's clearly broken.

---

## 1. Who and what

- **Channel:** Suraagh Nama (سُراغ نامہ). Urdu / Roman-Urdu documentaries for Pakistani, Indian and Bangladeshi viewers.
- **Owner:** Ahmad. The editor is Hassan (not the subject of this film). The voice-over was made in ElevenLabs.
- **Episode:** Muhammad Hassan (محمد حسن), a porter from Tisar (تِسر), Shigar, Gilgit-Baltistan.
  - On 27 July 2023 he fell and died in the Bottleneck on K2 while dozens of climbers passed him on the day of a world record.
  - A Brazilian cameraman, Gabriel, stopped and stayed with him.
  - A year later, five climbers from Sadpara village brought his body home.
  - None of the government's promises to the family could be shown to have been kept.
- **Working title idea:** "تو کیا آپ رُکتے؟" (the final line).
- **Research dossier, script history and visual plan:** https://claude.ai/artifact/3KsWxnv5xzoduLJVzr3AJD (a Claude Doc). Everything needed here is in this file.

## 2. Ahmad's standing rules (non-negotiable)

**Language and story**
- Story-first, spoken and humanised Urdu, built with proper Urdu joining words. No childish or broken sentences.
- Verified facts only, always attributed ("…کے مطابق", "US officials believe" style).
- **Never name the women or children** of Hassan's family on screen or in text.
- No real faces generated. No body shown. Death and recovery are shown only through lights, rope, snow and distant shots, so YouTube doesn't age-restrict the video.

**Disclosure**
- Every AI or reconstruction shot carries the "منظر کشی / AI reconstruction" tag (`03_motion_graphics/aitag_alpha.mov`). The build adds it automatically.
- At upload, tick Studio → **Altered or synthetic content → Yes**.
- A disclaimer card opens the video (0:00–0:04).

**Footage**
- Use only footage shown on public channels or free to use.
- Keep news clips short, wide, and credited in the description.
- Don't fabricate documents. The inquiry card is labelled "our summary, not the original document".

**Working style**
- Ahmad wants depth, correctness and speed.
- Be concise, recommend rather than list options, and check before claiming.

## 3. The film (concept)

- **The central image:** a single headlamp in the dark.
  - It opens the film (S01).
  - It is the "still light" the line of headlamps walks past (S03).
  - In the last shot it goes out (S30b), in the same framing as the opening.
- **The refrain:** "اور قطار چلتی رہی" lands twice (VO cues 9 and 91). Each time, music cuts and there are 2 seconds of silence with only footsteps on snow.
- **Three acts, one point of view each:**
  - رسّی (the rope): the cousin and the night.
  - اجنبی (the stranger): Gabriel and the record.
  - واپسی (the return): the family and the Sadpara climbers.
- **Viewer as jury:** three conflicting accounts (Steindl / Harila / the Russian cameraman), then "آپ کے خیال میں اِن میں سے کس کی بات سچ ہے؟" (comment prompt). The film ends on "تو کیا آپ رُکتے؟".

### Chapters (in the v1 cut; build.py recomputes them)
```
0:00 Ek raat, ek qatar | ایک رات، ایک قطار
1:01 Pehla hissa: Rassi | رسّی
3:19 Doosra hissa: Ajnabi | اجنبی
5:36 Teesra hissa: Wapsi | واپسی
8:13 Summit ki tasveer | Summit کی تصویر
```
Total length is about 8:57. The voice-over is 8:10, plus the 4.6 s intro, 35 s of inserted pauses and a 12 s end card.

### Key facts used (already in the script; don't change wording without a source)
- **Wage and insurance:**
  - The daily wage for porters is about Rs 1,700.
  - At the time, the death compensation was about Rs 2 lakh. Hassan had no insurance.
  - The law now requires Rs 20–30 lakh of insurance per porter.
- **Rescue and fundraising:**
  - A helicopter rescue costs about $20,000.
  - Steindl's fundraiser raised about $170,000.
- **The night:**
  - 30 to 80 people passed him (witness accounts differ).
  - Gabriel stayed about 2.5 hours (per Harila).
- **The record:** Harila and Tenjen Sherpa climbed all 14 peaks over 8,000 m in 92 days.
- **The inquiry (September 2023):**
  - It ruled the death accidental.
  - The company didn't provide full equipment, didn't check his experience and didn't insure him.
  - It recommended a two-year ban on the company.
  - The 70-page report doesn't mention the people who passed him.
- **The recovery:** July 2024, by five Sadpara climbers. The Alpine Club of Pakistan calls it the first recovery of its kind from that altitude on K2. An Army helicopter flew the body free of charge, and he was buried in his village in Shigar.
- **The promises:** the tourism minister promised free schooling, a job for the widow, and treatment for his mother. No proof of delivery was found in public records or official websites (checked November 2026).
- **What the family has:** a house, land and children's bank accounts, via Steindl's fund (per Naila Kiani).
- **2025:** another porter died on K2. The GB advisory said his claim was "being processed", and no payout report was found.

## 4. Folder map

| Path | Contents |
|---|---|
| `01_voiceover/k2_hassan_voiceover.m4a` | **Final voice-over** (8:10). Ahmad's file may be named `k2_hassan_full_voiceover.m4a`; rename it. |
| `01_voiceover/script_urdu.txt` | Exact voice-over text |
| `01_voiceover/cues_ur_en_hi.tsv` | 174 caption cues: Urdu / English / Hindi per line (0-based index = "cue") |
| `01_voiceover/cue_speech_times.json` | Speech start and end per cue in voice-over seconds (from forced alignment, accurate to about 0.1 s) |
| `01_voiceover/word_timings_asr.json` | Word-level timestamps (faster-whisper) |
| `02_captions/*.srt` | Captions on raw voice-over timing; `final/` holds captions re-timed per build (**upload these**) |
| `03_motion_graphics/` | 17 clips (section 5) |
| `04_scenes/` | 12 reconstruction scenes (section 5) |
| `05_earth_studio/` | Google Earth Studio renders (section 6) |
| `06_music/` | Music tracks with role prefixes (section 7) |
| `07_sfx/` | (empty) Sound effects are synthesized inside build.py |
| `08_edit/timeline.json` | **The edit**: segments, gaps, overlays, music ranges |
| `08_edit/build.py` | Renders the whole video and audio mix, captions, chapters and report |
| `08_edit/fonts/` | Inter, used for placeholder slides |
| `09_export/` | Cuts, review copies, chapters.txt, edit_report_<ver>.md |
| `10_news_footage/` | `recovery.mp4`, `funeral.mp4` |

## 5. Generated assets (all 1920×1080, 30 fps, no audio)

**Motion graphics (`03_motion_graphics/`):**

| File | Length | What it shows |
|---|---|---|
| `map.mp4` | 15 s | Pakistan at 0 s → GB label at 5 s → Shigar at 8 s → route Skardu→Askoli at about 11 s → K2 at 14 s. Real terrain, no borders drawn. |
| `ch1–ch4.mp4` | 4.5 s each | Chapter cards: رسّی / اجنبی / واپسی / Summit کی تصویر |
| `wage.mp4` | 6 s | Rs 1,700 daily wage (counts up from 0) |
| `counter_alpha.mov` | 6 s | Transparent lower third: "30 - 80 لوگ اُس کے پاس سے گزرے" |
| `record.mp4` | 5.5 s | 14 peaks / 92 days |
| `answers.mp4` | 10 s | Three answers (Steindl / Harila / cameraman), "summaries, not direct quotes" |
| `claim.mp4` | 6 s | Company "چند لمحوں میں" vs witnesses "کئی گھنٹے زندہ" |
| `inquiry.mp4` | 9 s | Our typed summary of the inquiry with a "گزرنے والوں کا ذکر؟ نہیں" stamp |
| `price.mp4` | 9 s | Rs 2 lakh / $20,000 / Rs 1,700 |
| `promises.mp4` | 10 s | Three promises appear (1–3 s), "ثبوت نہیں مِلا" stamps (about 4 s), stranger line (about 6 s) |
| `law.mp4` | 7 s | Rs 20–30 lakh insurance law; "ادائیگی کی تصدیق: ابھی تک نہیں" |
| `disclaimer.mp4` | 4 s | Opening disclaimer |
| `aitag_alpha.mov` | 8 s | Transparent "AI reconstruction · منظر کشی" pill |
| `endcard.mp4` | 12 s | End card with two boxes for YouTube end-screen elements |

**Reconstruction scenes (`04_scenes/`):**
- K2 shots are rendered on real K2 elevation data at 15 m resolution, with a moonlit or dawn look and an approximate Abruzzi route.
- They carry "Terrain: AWS Terrain Tiles (SRTM) · reconstruction · route approximate".

| ID | Length | Shot |
|---|---|---|
| S01 | 9 s | Lone headlamp in blowing snow on the fixed rope (fades up from black) |
| S02 | 9 s | Two lights: a cool moving light kneeling beside the warm still light (cousin / Gabriel) |
| S03 | 12 s | K2 at night: a line of headlamps climbs past one still light |
| S06 | 12 s | K2 summit pyramid at sunrise |
| S07 | 12 s | Summit "photos" on a table (backlit climbers with flags), ending on an empty print with a dotted maroon outline |
| S17 | 10 s | K2 at blue dawn, push-in; "Bottleneck · تقریباً 8,200 میٹر" label at about 3 s |
| S18 | 6 s | The fall: the beam whips round, the rope snaps, the light hangs swaying |
| S20 | 10 s | One light leaves the line and goes to the still light (stops at about 1 s, arrives at about 6.5 s) |
| S24 | 10 s | Grey morning, looking down on the route: dark dots pass one maroon dot |
| S27 | 10 s | Time-lapse: the rope is buried by snow until only the anchor ring is left |
| S30a | 9 s | The empty print, slow push-in, fade to black |
| S30b | 8 s | The same framing as S01; the headlamp flickers and dies at about 5.5 s, then black |

## 6. Media Ahmad is adding: required names

**Google Earth Studio → `05_earth_studio/`**
- Use .mp4 or .mov. If he has a JPEG frame zip, convert it:
  `ffmpeg -framerate 30 -i <dir>/<prefix>_%03d.jpeg -c:v libx264 -crf 17 -pix_fmt yuv420p out.mp4` (check the frame-number padding).
- Keep the Google Earth credit visible.

| Name | Shot | Ideal length | Used at (v1) |
|---|---|---|---|
| `tisar_zoom.mp4` | From about 60 km into Tisar (35.6665, 75.4502), centred on the houses | 12–14 s | 1:28 (family, his dream); 6:34 (Steindl reaches Tisar, starts 4 s in) |
| `tisar_orbit.mp4` | Half orbit around the village, about 800 m above ground, late-afternoon light | 15–20 s | 5:36 (son born); 6:27 (promises made, 5 s in); 7:29 (home at last, 6 s in) |
| `k2_basecamp.mp4` | Base Camp (35.8345, 76.5093) rising toward the summit pyramid | 20 s | 1:41 (first time above Base Camp); 6:48 (family pleads, 8 s in) |

If his Earth Studio files have other names or contents, map them by what they show, and tell Ahmad which file went where.

**News → `10_news_footage/`:**
- `recovery.mp4` (used at 7:02): July 2024 recovery, wide or distant shots.
- `funeral.mp4` (used at 7:21): helicopter in the valley, crowd seen from behind.

Only wide shots, no close-ups of the body, no faces of the widow or children. Note each source channel for the description credits. If unusable, ask Ahmad, then replace those two timeline segments with S24 / S17 / S06.

**Music → `06_music/`**, YouTube Audio Library, "attribution not required" only. Prefix each file with its role; anything after `__` is ignored. Example: `1_main_theme__Title.mp3`.

| Role | Character |
|---|---|
| `1_main_theme` | Slow, sparse solo piano. Restarts from the top each time it's used. |
| `2_dark_drone` | Low ambient drone or pulse, no melody |
| `3_warm_strings` | Gentle, hopeful strings (Gabriel only) |
| `4_cold_bed` | Sparse, cold ambient (inquiry, price, promises, law) |
| `5_build` | Slow build to a peak and release (summit swell, record, recovery → "home at last") |

If Ahmad gave a music table from the other local session (title, artist, licence), keep it in `06_music/MUSIC_CREDITS.md`. Any track needing attribution needs its credit line in the description.

## 7. How the build works (08_edit/build.py + timeline.json)

- **Time model.** Everything is anchored to **voice-over cue numbers** (0–173). A segment `{"cue": N, "src": X, "in": s}` starts at cue N's speech start minus 0.15 s and runs until the next segment.
- **Sources:**
  - `S##` = `04_scenes`.
  - `MG:<name>` = `03_motion_graphics`.
  - `MAP` = the map clip.
  - `GES:<name>` = `05_earth_studio/<name>.mp4`.
  - `NEWS:<name>` = `10_news_footage/<name>.mp4`.
  - A missing GES or NEWS file becomes a labelled placeholder slide.
- **Gaps** insert silence into the voice-over after a cue: 12 gaps, 35 s in total. Gaps with a `card` show a chapter card. The key gaps:

  | After cue | Length | Shows |
  |---|---|---|
  | 9 | 2 s | Silence after the first refrain |
  | 21 | 4.5 s | ch1 card |
  | 67 | 1.5 s | Silence before the stranger |
  | 68 | 8 s | S20 finishes, then the ch2 card |
  | 91 | 2 s | Silence after the second refrain |
  | 114 | 4.5 s | ch3 card |
  | 150 | 2 s | Pause after "home at last" |
  | 161 | 4.5 s | ch4 card |
  | 171 | 2.5 s | The headlamp dies |

- **Intro:** disclaimer 4.0 s plus black 0.6 s. The voice-over starts at 4.6 s.
- **Overlays:**
  - The AI tag is added automatically at the start of every segment from `ai_tag_sources` that's at least 4 s long.
  - The 30–80 counter is placed at cue 66 minus 0.5 s.
- **Fading clips:** for MG clips (except the end card), MAP and S27, the build never holds a faded-out last frame. It holds the last fully visible frame (clip end minus 1 s).
- **Audio:**
  - Sound effects are synthesized: wind beds, snow footsteps at both refrains, rope creaks, the impact and slowing heartbeat at the fall (cue 53), mask breathing (cues 73–77), river at Tisar, helicopter (cue 148).
  - Music roles play over the `music_roles` cue ranges.
  - Music level is the voice RMS minus 17 dB, ducked a further 6 dB while he speaks. It fades in over 1.5 s and out over 2.2 s.
  - The master is soft-limited, then loudness-normalised (`loudnorm=I=-14:TP=-1.5`).
- **Outputs:**
  - `09_export/K2_Hassan_<ver>.mp4`.
  - `02_captions/final/K2_Hassan_{ur,hi,en}_<ver>.srt` (re-timed through the same time map).
  - `09_export/chapters.txt`.
  - `09_export/edit_report_<ver>.md` (timeline table, missing list, music sources).
- **Making a change:**
  1. Edit `timeline.json`, for example change a segment's `src` or `in`, add or remove a gap, or adjust `music_roles` ranges.
  2. Run `python3 08_edit/build.py v3`.
  3. The intermediate `08_edit/_work/` is rebuilt every run. Delete it if switching versions.
- **Speed:** most time goes on rendering pieces with ProRes alpha overlays. On a Mac it should be well under 15 minutes.

## 8. Music cue sheet (the intent behind `music_roles`)

All ranges are [first cue, end cue).

| Cues | Music | Moment |
|---|---|---|
| 0–6 | None (wind) | Cold open |
| 6–9 | dark drone | The line arrives |
| 9 | **Silence** | First "اور قطار چلتی رہی" |
| 10–14 | build ("victorious", ironic) | Summit and flags; cuts out on "…تصویر میں بھی نہیں" |
| 15–48 | **main theme** | "یہ کہانی…", Tisar, the family, the dream |
| 48–67 | dark drone | The night, the fall, the line not stopping |
| 67 | **Silence** | Before "اور پھر، اندھیرے میں، ایک اجنبی رُک گیا" |
| 68–79 | warm strings | Gabriel |
| 79–84 | build (quiet reprise) | The summit and the record |
| 84–90 | dark drone (thin) | Drone footage, last breath |
| 91 | **Silence** | Second refrain |
| 92–111 | dark drone (investigative) | Three answers |
| 111–115 | Wind only | A year in the ice |
| 115–117 | **main theme** | "ایک اور بیٹا… باپ کا چہرہ کبھی نہیں دیکھا" |
| 117–137 | cold bed | Inquiry, price, promises |
| 137 | **Hard stop** | "لیکن حسن ابھی تک برف میں تھا" |
| 138–151 | build to peak | Recovery → funeral → "اپنے گھر واپس آ گیا" |
| 151–162 | cold bed | Promises, law, the unpaid claim |
| 162–171 | **main theme**, thinning | The ending |
| After 171 | **Total silence** | The headlamp dies; end card |

## 9. Quality gate before giving Ahmad any cut

1. `edit_report`: Missing is empty and no music role is "INTERIM". If something is still missing, say so plainly.
2. **Contact sheet:** grab about 24 frames across the cut with ffmpeg and look for:
   - black or faded frames under speech;
   - placeholder slides;
   - wrong-looking shots.
3. **Spot-check these beats:**
   - The counter appears on "تیس سے اسّی لوگ".
   - The Bottleneck label appears on "Bottleneck کہتے ہیں".
   - The headlamp dies right after "تو کیا آپ رُکتے؟".
   - The chapter cards are at the chapter times.
4. **Loudness:** `ffmpeg -i out.mp4 -af ebur128 -f null -` should give about -14 LUFS integrated.
5. **Review copy** (Ahmad watches on his phone):
   `ffmpeg -i K2_Hassan_<ver>.mp4 -vf scale=1280:720 -c:v libx264 -b:v 700k -preset medium -c:a aac -b:a 96k K2_Hassan_<ver>_REVIEW_720p.mp4`
6. Ask Ahmad for notes as "time → change". Apply them all in one pass, rebuild once.

## 10. Upload package (after Ahmad approves the final cut)

- **Video:** `09_export/K2_Hassan_<final>.mp4` (1080p master).
- **Captions:** `02_captions/final/*_<final>.srt` → Subtitles → Upload file → With timing (Urdu, Hindi, English). Hindi captions matter for Indian reach.
- **Description:**
  - A hook line.
  - Chapters from `chapters.txt`.
  - Sources (Dawn, the Alpine Club of Pakistan, and others, per the Doc).
  - Credits: Google Earth; "Terrain: AWS Terrain Tiles (Mapzen / SRTM), route approximate"; news channels used; any music needing attribution.
- **Studio:** "Altered or synthetic content" → Yes. Not made for kids.
- **End screen:** place the elements on the two boxes of the end card (last 12 s).
- **Pinned comment:** ask the closing question, "اگر آپ اُس قطار میں ہوتے، تو کیا آپ رُکتے؟". Don't create fake engagement; Ahmad posts from his own account only.
- **Material moved out of the voice-over** (use for the pinned comment, Shorts or community posts):
  - The two clocks: 11 p.m. vs 2:15 a.m.
  - The separate passer-by counts: 30–40, about 50, about 80.
  - The government website's $500 helicopter-insurance rule, with nothing listed for porters.
  - The survey income data.

## 11. Decisions already made (don't reopen these)

- **Removed from the script at Ahmad's request:**
  - The death-threats line.
  - "We'll answer at the end".
  - The twist and the Tisar 2026 sections.
  - The witness-count clause.
- **Spelling and wording:**
  - "Summit" is written in Latin letters.
  - انشورنس is treated as feminine; the voice-over says "insurance".
  - "رُکنے کے بجائے" is correct.
- **The voice-over is final.** It reads fast, about 205 words per minute; that's why the gaps exist. Don't regenerate it unless Ahmad asks.
- **Reconstructions are stylised (lights and terrain), not photoreal AI people.** This is deliberate: it's safe, honest and consistent.
- **No borders drawn** on maps (the Kashmir dispute).
- **Don't compare runtimes** with Ahmad's own earlier videos. Judge against top-performing documentaries.

## 12. Troubleshooting

- **`missing motion graphic`:** a file in `03_motion_graphics` has a different name. Rename it to the names in section 5.
- **ProRes alpha overlays look opaque in some players:** that's normal in QuickTime previews. The build composites them correctly.
- **The build fails on a GES clip:** check it with `ffprobe` and re-encode to H.264 1080p30.
- **Earth Studio clip shorter than its segment:** the build holds the last frame. Better: re-render the clip longer, or set `in` lower.
- **A different look is wanted for one moment:** change only that segment's `src`/`in` in `timeline.json`. Every other timing stays locked to the voice-over automatically.
