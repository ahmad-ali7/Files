# Suraagh Nama — Production System

A repeatable pipeline for making one episode: **Pakistan's legends, mysteries and their real places.**
Built from Ep 1 (Saiful Malook). Reuse it; don't rebuild it.

## The core idea: think in the cloud, build on the machine

| Phase | Where | Why |
|---|---|---|
| Research, story, script, packaging (title/thumbnail/desc) | **Cloud session (Claude.ai)** | Cheap, fast reasoning. No files to move. |
| Rendering, images, music, assembly, captions, **upload** | **Local session (Claude Code on the Mac, Chrome access)** | Heavy CPU + browser work. Files never leave the Mac. No transfers. |

The cloud session ends each project by producing a **`BUILD_SPEC.md`** (see `templates/`). The local
session reads that spec, runs the **`toolkit/`** scripts, and produces the finished video — then sends back
small previews for the cloud to review. That review loop is what keeps quality high.

## What's in here

```
PRODUCTION_SYSTEM/
├── README.md            ← you are here
├── WORKFLOW.md          ← the cloud↔local division + the review loop + repo/branch rules
├── RUNBOOK.md           ← the LOCAL session's step-by-step: BUILD_SPEC + assets → finished video
├── toolkit/             ← the reusable scripts (the real asset — proven on Ep 1)
├── templates/
│   ├── BUILD_SPEC_TEMPLATE.md   ← fill one per episode in the cloud; hand to local
│   ├── IMAGE_GEN_GUIDE.md       ← generating illustrations via Gemini in Chrome
│   ├── AUDIO_GUIDE.md           ← music + SFX from the YouTube Audio Library
│   └── UPLOAD_GUIDE.md          ← YouTube upload steps (local session)
└── reference/
    └── EP1_RETROSPECTIVE.md     ← what worked, what broke, lessons baked into the toolkit
```

## The loop for every new episode

1. **Cloud:** research → story structure → Urdu script (ElevenLabs-ready) → packaging. Fill `BUILD_SPEC.md`.
2. **Local:** record VO → run the RUNBOOK (gather assets, render crafts, animate, assemble, mix, caption).
3. **Local → Cloud:** send a 480p preview reel + a few frames. **Cloud reviews, edits the spec.**
4. **Local:** apply notes, render Full HD, upload as Unlisted, send link.
5. **Cloud:** final packaging check → you publish.

## The one rule that saves the most pain
**Keep big files on the Mac.** Everything that went wrong on Ep 1 (1.6 GB transfers, GitHub throttling,
30-minute render babysitting) came from rendering in the cloud. Render where the file will live.
The cloud only ever needs to see **small previews**, never the master.
