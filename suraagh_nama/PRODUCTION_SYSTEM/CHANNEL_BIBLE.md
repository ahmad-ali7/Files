# CHANNEL BIBLE — Suraagh Nama
### The single source of truth. Both the cloud and local sessions read this FIRST, every time.

> Suraagh (سراغ) = a clue / trail. Suraagh Nama = "the book of clues." We take a legend everyone *thinks*
> they know and track it to its **real place and real evidence**. Story first, proof second, both true.

Everything else in `PRODUCTION_SYSTEM/` serves this file. If a choice isn't covered here, decide in the
**spirit** of this file and then write the rule down (see `EXTENDING.md`). This is a living document — version it.

---

## 1. Mission & promise
- **Mission:** make Pakistan's legends, mysteries and their real places unforgettable — and *credible*.
- **Promise to the viewer:** "You know the story. You don't know the truth behind it. In the next few minutes
  you'll get both — and I'll show you the receipts."
- **What we are not:** not a horror channel, not clickbait with no payoff, not a dry history lecture, not a
  reaction/compilation channel. Mystery + evidence, held in balance.

## 2. Audience
- Primarily **Urdu-speaking Pakistanis** (home + diaspora), mobile-first, evening/night viewing.
- They want **wonder + to feel smart afterwards**. They share things that are *beautiful* and things that make
  them go "I never knew that about our own place."
- They are quick to reject anything that feels **fake, foreign, or AI-sloppy**. Authenticity of place and craft
  is non-negotiable (Ep 1: drawn frames were rejected as "robotic").

## 3. Brand voice
- **Language:** Urdu narration; Roman-Urdu titles/description for reach. Warm, intimate, a storyteller by a lamp.
- **Register:** dastangoi craft — direct address (حاضرین), character voices, woven verse, pauses, "sittings" that
  end on آگے سنیے — **but never labelled** as dastangoi in packaging (the label underperforms; the craft sells).
- **Tone:** reverent toward the culture, curious, a little eerie, never mocking or sensational.
- **Signature beats:** a cold, fearful open grounded in a real moment → the legend → the hunt for proof →
  "the place is still here, and so is the danger/wonder" → a closing couplet → آگے/اگلی محفل teaser.

## 4. Visual identity
- **Real world = real footage / satellite / archives.** Landscapes, documents, maps, events: always real.
- **Legend world = painted illustration** (Persian/Mughal miniature → moonlit cinematic oil), used **only** in
  the story sections. Modest dress, real settings, no text/logos, watermark framed out. (See `IMAGE_GEN_GUIDE`.)
- **Motion:** nothing truly static — slow push-ins, write-on text, living light (flame, motes), map routes that
  grow then dissolve to real footage. Day-for-night for night scenes.
- **Type:** Nastaliq for Urdu; gold = wonder, red = threat, white = neutral. Safe margins; separate text/bg layers.
- **No channel badge on a thumbnail if it competes with the subject.**

## 5. Audio identity
- **The voice is king.** Music ≈15 dB under narration, effects ~10 dB under; beds swell only in pauses and on
  story beats. Whole mix to **-14 LUFS**. (See the voice-first rider in `audio_plan.py`.)
- **Character voices** are built from Ahmad's own VO (loudspeaker, astrologer, fairy, demon, verse) — not other actors.
- **Music:** instrumental, Pakistani/Persian, night-time; YouTube Audio Library only (monetisation-safe).
  Eastern instruments (sitar, bansuri, santoor, oud) for the dastan.

## 6. Storytelling doctrine
- **A hook or new question every ~60 seconds.** Map it before writing.
- **4–7 minutes** unless the story truly needs more.
- **Evidence is the spine:** every episode must land at least one real, checkable proof (a book, a record, an
  event, a map, a scientific fact). Myth without proof is not a Suraagh Nama episode.
- **Humanise and link** sections; natural spoken Urdu (the "fix Urdu sentences" pass from Ep 1); subject-first,
  connectors, no robotic "میں آپ کو بتاؤں گا".

## 7. Ethics & trust (hard rules — never break)
- **Never fabricate** documents, records, footage, reviews, or engagement. A "source note" summarising a real
  source is fine; an imitation newspaper/card presented as genuine is not.
- **Always disclose AI:** "Dastan illustrations created with AI; landscapes are real footage and satellite imagery."
- **Don't name** the women or children of real families tied to a tragedy. No real faces/bodies invented for real people.
- **Cite primary sources** with page numbers in a fact-check log; flag anything deliberately softened or cut.
- **Respect the culture and the dead.** Eerie, yes; exploitative, never.

## 8. Packaging rules (what the data taught us)
- **Title:** front-load the searchable name, then a curiosity gap, hide the payoff. Winning format:
  *"<Name>: the hidden truth / the part nobody tells."* Keep the hook in the first ~40 chars (mobile).
- **Thumbnail:** one clear subject + a threat + ≤3 big Urdu words; keep the face's eyes clear; beauty vs dread.
- **Description:** hook → chapters (timestamps) → sources → AI disclosure → hashtags. Tags mix Urdu/Roman/English.
- **A/B the title** in the first 48 h; keep the higher CTR.

## 9. North-star metrics
- **CTR** (thumbnail/title), **average view duration / % viewed** (story + pacing), **shares & saves** (wonder),
  **subscribes-per-view** (did the proof earn trust). Watch-time and trust over raw views.

## 10. How this scales without drifting
- Every episode starts from a **BUILD_SPEC** that inherits these rules.
- New creative ideas enter through `EXTENDING.md` → logged in `creative/` → graduate into `toolkit/` if they're code.
- Anything that contradicts §7 is rejected outright. Anything that stretches §3–§6 is allowed **as an experiment**,
  measured against §9, and then either adopted (write it here) or retired.
