# RUNBOOK — building an episode on the local session

For a **Claude Code session on the Mac** (Chrome access, signed in to Gemini + YouTube).
Input: a filled **`BUILD_SPEC.md`** + the recorded voice-over. Output: finished HD video, captions, thumbnail, uploaded.

Work inside the episode's folder, e.g. `~/Video Work/<Series>/<episode>/`. Keep a `prod/` subfolder for the toolkit run.
Copy `PRODUCTION_SYSTEM/toolkit/` into `prod/` so scripts and assets sit together.

> **Environment:** Chromium + Playwright are expected. `pip install numpy pillow scipy faster-whisper playwright`,
> `npm i playwright`. ffmpeg must be on PATH. The Mac already has python3, node, ffmpeg.

---

## Step 0 — Fonts & folders
Put the Nastaliq/Inter/Anton fonts under `prod/sm/web/fonts/` (same names `real.html` expects:
`Nastaliq700.ttf`, `Nastaliq400.ttf`, `Inter600.ttf`, `Anton.ttf`, …). Reuse Ep 1's font set.
Make `prod/more/` (stock video/photos), `prod/paris/` (illustrations), `prod/audio/{music,sfx}/`, `prod/out/`, `prod/clips/`.

## Step 1 — Voice-over → part timings  (toolkit/asr.py, vo_align.py, refine.py)
1. Export the VO to `prod/vo/vo16.wav` (16 kHz mono) and `vo48.wav` (48 kHz) with ffmpeg.
2. `python3 asr.py vo16.wav medium asr.json` — Urdu transcription with word timestamps.
3. Point `vo_align.py` at the BUILD_SPEC's `vo_parts/*.txt` (the ElevenLabs part files). It fuzzy-matches the
   transcript to each part and writes `parts.json` (start/end per part). `refine.py` snaps boundaries to the
   quietest gaps and hand-fixes any verse lines the ASR missed. **Check the printed table against the script.**

## Step 2 — Illustrations  (templates/IMAGE_GEN_GUIDE.md)
Generate the episode's paintings via **Gemini in Chrome** per the BUILD_SPEC's shot list + character bible.
Save to `prod/paris/`. Reuse Ep 1's style block (Persian/Mughal, modest dress, real settings, no text).

## Step 3 — Music & SFX  (templates/AUDIO_GUIDE.md)
Download the BUILD_SPEC's music slots (M1…Mn) and SFX (S01…) from the **YouTube Audio Library** in Chrome.
Save to `prod/audio/music/` and `prod/audio/sfx/` with the exact names the spec lists. Write `LOG.md` + `CREDITS.md`.

## Step 4 — Scene crafts & stills  (toolkit/real.html, produce.py, layers.js, a_*.py, craft.py, flood2d.py)
`real.html` holds every scene (titles, cards, document frames, maps, the demon, etc.) as HTML.
- `layers.js` renders each scene's text layer (`T_*.png`) and background layer (`B_*.png`).
- `produce.py JOB…` renders real-footage grades, day-for-night, the flood, the evidence stills.
- `a_lamp.py`, `a_paris.py`, `a_fairies.py` render the living diya, the pari composites, the fairy scenes.
- `anim.js SCENE out.mp4 DUR` renders the **animated** scenes (sitting cards write-on, the astrologer chart,
  the map route) driven by `anim_scenes.js`.
Output clips land in `prod/clips/`. Spot-check a frame from each (`ffmpeg -ss T -i clip -frames:v 1 x.jpg`).

## Step 5 — Assemble + mix  (toolkit/assemble.py, audio_plan.py, anim_core.py)
`assemble.py` reads the edit plan (the `PLAN` list — update it from the BUILD_SPEC's shot order) and:
- fits each clip to its voice part (slows/pans long ones, ping-pongs if still short),
- adds 0.5 s dissolves, cuts on beats (e.g. the demon line on a lightning flash),
- builds the voice track with the **character-voice FX** (loudspeaker/astrologer/fairy/demon/verse),
- lays the **music beds + SFX** (`audio_plan.py`) under a **voice-first rider** (music ≈15 dB under speech,
  swells only in pauses and on story beats), and normalizes to **-14 LUFS**.

Run order:
```
export PV=1 && python3 assemble.py video && python3 assemble.py audio && python3 assemble.py mux   # 480p PREVIEW
```
`PV=1` renders a fast **854×480 preview** — always make this first and review it before HD.

> **Memory:** the blender loads only the slice of each clip it needs (fixed after Ep 1's OOM). Keep it that way;
> never cache whole clips at 1080p.

## Step 6 — Review loop (send small files to the cloud)
Send the cloud session: `deliver/..._preview_480p.mp4`, a contact sheet of ~12 frames, and (if audio is in doubt)
a 30-sec WAV of a tricky section. The cloud returns notes → edit the spec/PLAN → re-render the preview.
**Never send the HD master to the cloud.**

## Step 7 — Final HD + captions + chapters
```
unset PV && python3 assemble.py video && python3 assemble.py mux    # 1080p master
```
- `python3 captions.py` → `*_ur.srt` (script spelling, English words written back in Urdu).
- Chapters come from the sitting-card times → paste into the description.
- **Verify the file plays** before trusting it: `ffmpeg -v error -i master.mp4 -f null -` must exit clean.
  (Ep 1 produced a corrupt file once; a "done" flag is not proof.) Check loudness: `ffmpeg -i master.mp4 -af ebur128 -f null -` ≈ -14 LUFS.

## Step 8 — Thumbnail
Use `templates/` thumbnail approach (an HTML canvas screenshotted at 1280×720) or the cloud-provided PNG.

## Step 9 — Upload  (templates/UPLOAD_GUIDE.md)
Upload in Chrome/YouTube Studio with the BUILD_SPEC's title/description/tags, the thumbnail, and the SRT as
Urdu subtitles. **Unlisted first**, send Ahmad the link, publish on his OK.

---

### Fast checklist
`VO → asr/align → images → audio → scenes(layers+produce+anim+a_*) → assemble(PV=1 preview) → REVIEW → HD → captions/chapters → verify → thumbnail → upload(unlisted)`
