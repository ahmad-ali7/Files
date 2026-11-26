# WORKFLOW — how cloud and local work together

## Roles

**Cloud session (here, Claude.ai) — the writers' room + art director**
- Deep research and fact-checking (primary sources, cross-checks).
- Story structure, the per-minute hook map, the storytelling style (dastangoi, etc.).
- Urdu scripting, humanising, and splitting into ElevenLabs-ready parts.
- Packaging strategy: titles, thumbnail concepts, description, tags.
- **Authoring and improving the `toolkit/` scripts.**
- **Reviewing the local session's previews** and revising the BUILD_SPEC.
- Produces one `BUILD_SPEC.md` per episode.

**Local session (Mac, Claude Code + Chrome) — the studio**
- Records/handles the VO, generates images (Gemini), downloads music/SFX and stock footage.
- Runs the toolkit: renders crafts, animations, assembly, the mix, captions, chapters.
- Builds the thumbnail, uploads to YouTube (Unlisted first).
- Sends previews back up; applies the cloud's notes.

## The review loop (the quality guardrail)
Do **not** fire-and-forget. After the first assembly the local session sends the cloud:
- a **480p preview reel** (small),
- a **contact sheet** of ~12 frames,
- optionally a **30-sec audio clip** of a doubtful section.

The cloud reviews, edits the BUILD_SPEC / the `assemble.py` PLAN, and the local session re-renders.
Iterate on the **preview**, not the master. Only render Full HD once the preview is approved.

## File discipline (why Ep 1 hurt, and the fix)
- **Masters and raw assets live on the Mac. Always.** Rendering happens where the file will stay.
- The cloud only ever receives **small** files (previews, frames, short audio). Never the HD master.
- If a file truly must move cloud→Mac, prefer: **a GitHub Release asset** (no size cap, CDN-fast) created by
  the **local** session, or a direct browser download. Avoid `git clone` of >100 MB blobs (throttled) and the
  Contents API (truncates big files). Avoid pushing masters through the public repo at all.

## Repo layout
- **`ahmad-ali7/Files` (public):** scripts, specs, docs, captions, metadata — **no video, no raw audio, no AI face assets** you don't want public.
- **Private repo / local disk:** masters, VO, illustrations, music.
- Per-episode folder on the Mac: `~/Video Work/<series>/<episode>/` with a `prod/` work area.

## Branch & commit rules (cloud)
- Develop on the branch the session is given; push only there.
- Commit toolkit/spec/doc changes with the session's attribution trailer.
- Never commit `.env`/credentials, masters, or large binaries to the public repo.

## When to update the toolkit vs the spec
- **Spec** = what changes per episode (script, shots, assets, packaging).
- **Toolkit** = how we build (the scripts). Improve it when a technique recurs; keep it episode-agnostic.
  A new reusable trick from one episode should graduate into `toolkit/` with a note in the retrospective.
