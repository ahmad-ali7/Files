# Ep 1 retrospective — lessons baked into the system

What worked, what broke on Saiful Malook, so Ep 2 doesn't re-learn it.

## What worked
- **Dastangoi as the style, not the label.** Market check: dastangoi-titled videos underperform (median ~179
  views), so we used the *craft* (حاضرین, character voices, verse, sittings) without naming it in packaging.
- **Legend + real evidence** is the brand's edge: the 1907 Gazetteer, Mian Muhammad Bakhsh's verse, the
  1893/2005/2025 floods turned a fairy tale into a documentary hook.
- **Real footage for evidence, AI paintings only for the dastan.** Viewers rejected the first drawn frames as
  "robotic/AI". Fix: real lake/valley/satellite for the real world; painted scenes only inside the story.
- **Voice-first mix.** The win was a rider that keeps narration ~15–18 dB over beds and lets music swell only in
  pauses/beats. Do this from the start, not as a fix.
- **Animate the static bits.** Living diya, write-on sitting cards, a drawing astrologer chart, a map route that
  grows then dissolves to real footage — these lifted the v1→v2 jump.

## What broke (and the guardrails now in the toolkit/runbook)
- **Rendering in the cloud → 1.6 GB file → GitHub throttling + API truncation.** Root cause of hours of pain.
  → **Render on the Mac.** Cloud sees only small previews. (WORKFLOW "file discipline".)
- **OOM at 1080p.** The blender cached whole clips in RAM (fine at 480p, killed at 1080p in a ~6.5 GB cgroup).
  → `assemble.py` now loads only the clip **slice** each segment needs. Never revert that.
- **A "done" flag on a corrupt render.** A truncated MP4 still reported a duration.
  → Always `ffmpeg -v error -i master -f null -` must exit clean before trusting a render.
- **Text cropping on panned stills.** Baking text into a zoomed still clipped edges/descenders.
  → Separate `B_` (background, panned) and `T_` (text, fixed, scaled 0.94) layers; `.gold` gets padding-bottom.
- **Gemini refuses some prompts** (it refused the demon figure 5×). → Have an atmospheric fallback (storm +
  glowing eyes) and don't block the episode on one image.
- **Can't hear audio.** Both Claude sessions are deaf to audio; music is chosen by tags + brief. → Ahmad auditions
  the first 20–30 s of each pick.

## Numbers to reuse
- Loudness target **-14 LUFS**, true peak ≤ -1 dB.
- 0.5 s dissolves; beat cuts on action (demon line on a lightning flash).
- Preview at **854×480** (`PV=1`); master at **1920×1080**; ~8–12 Mbps is plenty for upload (YouTube re-encodes).
- Thumbnail 1280×720; face + threat + short Urdu; no channel badge if it competes; keep the subject's eyes clear.

## Packaging that landed
- Title format that won: **name + "the hidden truth / the part nobody tells"** (searchable + curiosity).
- Thumbnail: real lake, lovers one side, demon (red eyes) the other, pari prominent, 3-word title in the middle.
