# Pari image log (Gemini / Nano Banana, gemini.google.com, Ahmad's account)

Generated on 25 November 2026. Native download size from Gemini: 1376 x 768 for 16:9, saved as PNG.
Candidates (every variation downloaded) are kept in `_candidates/`.

## P01_badal_portrait.png
- Prompt: the guide's P01 prompt with [BADAL] and [STYLE] filled in. For v3 (kept) two changes: "translucent" removed from the gown, "no wings or only very faint translucent light-wings" replaced by "no wings at all", and "Important: no wings of any kind, the gown is opaque and modest." added.
- Variations: 3. v1 had visible insect-like wings and a sheer bodice (runner-up, saved as `_alt`). v2 had large butterfly-style wings (rejected: rule 1). v3 kept: no wings, opaque high-neck gown, clear face.
- Check: 2 eyes, no hands in frame, no text, modest, no modern objects. Pass.

## P02_badal_fullfigure_black.png (9:16, 768 x 1376)
- Prompt: the guide's P02 prompt with [BADAL] (wording as kept P01: no wings, opaque gown) and [STYLE] without the 16:9 words, P01 attached as reference, plus "the same woman as in the reference image, same face, same crown and jewellery" and "Important: no wings, the gown is opaque and modest, the background is pure flat black."
- Variations: 2. Both passed. v2 kept: one hand raised as asked, whole figure inside the frame with margin (best for keying). v1 saved as `_alt` (fuller flowing dupatta).
- Check: same face/taj as P01, hands 5 fingers, modest, pure black background, no text. Pass.

## P04_paris_group_black.png
- Prompt: the guide's P04 prompt with [PARIS] and [STYLE] (without "deep indigo night"), plus "No wings." For v3 (kept) also: "Every maiden fully covered: long sleeves, covered midriff, covered chest. The background must be completely flat pure black everywhere, with no moon, no glow, no light source and no gradient in the background." (the style block's "moonlight from the upper right" was dropped for this shot only).
- Variations: 3. v1 rejected: bare midriffs on the front figures (rule 2) and blank faces. v2 modest but a moon glow in the top-right corner (corner brightness 59/255), saved as `_alt`. v3 kept: pure black (corners ~1/255), all fully covered and veiled.
- Check: no wings, no text, modest, pure black background. Pass.
- Note: P03 failed twice in the first long chat ("I'm having a hard time fulfilling your request" / "encountering an error"); every later image was made in its own new chat.

## P03_descent.png
- Prompt: the guide's P03 prompt with [PARIS] and [STYLE], P01 attached as reference. Because the full-length version failed twice in the first chat, [BADAL] was condensed to "the fairy queen from the reference image (same face, same gold and emerald taj, same ivory dupatta with gold zari, moon-white long-sleeved high-neck gown, no wings)"; "no buildings" added.
- Variations: 2 (in a new chat). v2 kept: Badal leads at the front coming down to the stream, river of lights behind. v1 saved as `_alt` (Badal in the middle of the group, holding hands).
- Check: zoomed on Badal: hands natural, face consistent with P01, all figures covered and veiled, no text, no buildings. Pass.

## P05_stolen_clothes.png
- Prompt: the guide's P05 prompt with [STYLE], plus "Only the hand and wrist are visible, no body."
- Variations: 2. Both passed. v2 kept: the taj reads clearly as a small emerald-and-gold crown. v1 saved as `_alt` (jewel looks more like a forehead pendant).
- Check: one hand, natural fingers, henna and gold bangle, no body, no text. Pass.

## P06_prince_devotion.png
- Prompt: the guide's P06 prompt exactly, with [PRINCE] and [STYLE] filled in.
- Variations: 2. Both passed. v2 kept: hands raised in dua, long hair and beard grown out, snow on turban and shawl (best fit for "twelve years"). v1 saved as `_alt` (hands clasped, short beard).
- Check: zoomed on the raised hands: natural fingers. Face side-on, no text, no modern objects. Pass.

## P09_paris_dance.png
- Prompt: the guide's P09 prompt with [PARIS] and [STYLE], plus "No wings."
- Variations: 2. Both passed. v2 kept: a true circle of dancers with golden light trails, lone stone and shepherd's path in the foreground. v1 saved as `_alt` (a long winding line rather than a circle).
- Check: distant, no faces readable, all covered, no text, no modern objects. Pass.

## P08_lovers_escape.png
- Prompt: the guide's P08 prompt with [PRINCE] and [STYLE], P01 attached as reference; [BADAL] condensed to "the fairy queen from the reference image (same woman, same face, same gold and emerald taj, ivory dupatta with gold zari, moon-white long-sleeved high-neck gown, no wings)".
- Variations: 2. Both passed. v1 kept: both seen from behind as the prompt asks. v2 saved as `_alt` (both in profile; Badal's face visible and consistent with P01).
- Check: joined hands natural, both fully covered, flooded old town as the prompt asks, no text. Pass.

## P07_dev.png — NOT GENERATED
- Gemini refused or errored on every attempt, 5 tries in 3 separate new chats ("I'm having a hard time fulfilling your request" / "I seem to be encountering an error"):
  1. The guide's P07 prompt exactly ([DEV] + [STYLE]), plus one Try again.
  2. Softened: "a colossal storm giant (a dev from Persian legend)", "breaks open" instead of "smashing", "dramatic" instead of "terrifying", "empty valley", "no people".
  3. Reframed as "an enormous storm cloud shaped like a giant horned figure" with the flood in an empty valley.
  4. Same, without the red eyes.
- Other images succeeded right before and after these attempts (P09, P08), so this is a content block on this scene, not a quota limit. Likely trigger: a horned giant figure plus a destructive flood.
- Needs another tool, or a version Ahmad approves that drops the horned figure (for example only the storm and the bursting moraine).
- Decision (Ahmad, 25 Nov 2026): skip P07 for now.
