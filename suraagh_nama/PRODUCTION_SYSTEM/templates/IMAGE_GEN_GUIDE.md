# IMAGE GEN GUIDE (template) — illustrations via Gemini in Chrome

For the local session. Fill the bracketed bits from the episode's BUILD_SPEC (§3).

## Rules (keep these every episode)
1. **House style:** Persian/Mughal miniature reimagined as a moonlit cinematic oil painting. Painted realism,
   rich but restrained colour. **Not** Disney/Western, no European castles, no modern objects, no butterflies.
2. **Modest dress** for a Pakistani audience: covered shoulders/chest, dupatta/veil, long sleeves.
3. **Real settings** of the place the episode is about (lake, valley, peaks, night/moonlight).
4. **No text, letters, logos, frames** in any image.
5. **Consistency:** generate the lead character's portrait first; **upload it as a reference** for every later
   image showing that face. State "same woman/man as the reference, same face".
6. Don't remove Gemini's watermark; frame shots so the compositor can crop around it.
7. **2–3 variations each**, keep the best + save the runner-up as `_alt`. Reject extra fingers, melted hands,
   >2 eyes, distorted faces, text, immodest clothing, modern objects.
8. Download the largest size; 16:9 unless a shot needs portrait (e.g. a figure to composite on a black bg).

## Prompt skeleton
`[CHARACTER BIBLE block]` + the shot description + `[STYLE BLOCK]`. Paste the blocks from the BUILD_SPEC.
For figures to be composited over real footage, request **"isolated on a pure solid black background, nothing else"**.

## Steps
1. Create `prod/paris/` (or the episode's art folder).
2. gemini.google.com → image model → generate the portrait first → save as the spec's P01 name.
3. For reference-dependent shots, attach the portrait and note the sameness.
4. Generate the rest; keep best + `_alt`; write `LOG.md` (file, prompt, date, any regen reason).
5. QC each against the rules before saving. Tell Ahmad when the folder is complete.

## For the cloud compositor's reference
Black-bg figures get keyed and placed into real footage with wind-warp, glowing motes, parallax.
Other paintings become dastan "paintings" with slow push-in, moving mist, candle flicker. Paintings appear
only in the story/dastan sections; evidence sections stay real footage + real documents. YouTube description
must say "Dastan illustrations created with AI; landscapes are real footage and satellite imagery."
