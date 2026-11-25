# Paris for Ep 1 (Saiful Malook): image-generation guide for a local Claude session

**For:** a Claude Code session running on Ahmad's Mac with **Claude in Chrome**.
**Tool:** **Google Gemini** (gemini.google.com) in Ahmad's own Chrome, signed in.
**Save to:** `/Users/ahmadnawazali/Video Work/Saif ul malook lake/03_paris/` (create it if missing).
**Then:** tell Ahmad it's done. The cloud session composites these into the real lake footage and animates them.

---

## 0. Rules (read first)
1. **Style: Persian/Mughal Peri.** Painted realism, like a Mughal miniature turned into a cinematic oil painting. **Not** a Western or Disney princess, **not** a European castle, **not** butterflies.
2. **Modest dress for a Pakistani audience:** long sleeves, covered shoulders and chest, a dupatta or veil, gold embroidery. **No off-shoulder or low-cut clothes, no bare midriff.**
3. **Real Kaghan settings:** a glacial lake at 3,200 m surrounded by snow peaks, a rocky moraine shore, a mountain stream, alpine grass. Night and moonlight. **No castles, palaces, cities or modern objects.**
4. **No text, letters, logos or frames** in any image.
5. **Consistency:** Badal Jamal must look like the same woman in every image. Generate her portrait (P01) first, then **upload P01 as a reference** for every later image that shows her face.
6. **Gemini's watermark:** don't use watermark-removal tools. The cloud session will frame shots around it.
7. **Make 2–3 variations of each image.** Keep the best one, and also save the runner-up as `_alt`.
8. **Quality check every image before saving.** Reject any with:
   - extra or missing fingers, or melted hands;
   - more than two eyes, or a distorted face;
   - text or symbols;
   - immodest clothing;
   - modern objects.
9. **Download the largest size Gemini offers.** Landscape 16:9 unless the shot says otherwise.

## 1. Character bible (paste the matching block into every prompt that includes that character)

**BADAL JAMAL (queen of the paris).**
> a young Persian-Kashmiri fairy queen in her early twenties, serene and otherworldly, luminous moon-pale skin with a faint inner glow, large almond-shaped amber-green eyes, softly arched dark brows, long black hair in a loose braid threaded with tiny pearls, a delicate gold and emerald jeweled taj (small crown) with a hanging teardrop emerald on the forehead, emerald drop earrings, a flowing moon-white translucent silk gown with long sleeves and a high neckline, an ivory dupatta veil with fine gold zari embroidery falling over her head and shoulders, faint shimmering light motes around her, no wings or only very faint translucent light-wings

**THE PARIS (her 360 attendants).**
> graceful veiled fairy maidens in pale white, silver and soft gold silk with long sleeves and dupattas, faces mostly hidden by veils or turned away, each surrounded by a soft golden glow, so many that in the distance they look like a river of tiny lights

**THE PRINCE (of Delhi, Mughal).**
> a young Mughal prince in his twenties, slim, dark short beard, wearing a cream angarkha with gold embroidery, a dark green shawl, and a white turban with a single feather plume and a ruby pin, calm and devoted expression

**THE DEV (demon).**
> a colossal demon formed out of black storm clouds and broken mountain rock, never fully solid, two curved horns made of cloud, two small glowing ember-red eyes, lightning crawling inside its body, so huge that the mountains reach only its chest

**STYLE BLOCK (add to the END of every prompt).**
> cinematic painted realism in the style of a Mughal-Persian miniature reimagined as a moonlit oil painting, rich but restrained colour, deep indigo night, moonlight from the upper right, warm gold highlights, fine detail, soft atmospheric haze, film grain, 16:9 landscape, no text, no watermark, no frame

## 2. Shot list
Save each image with exactly the file name shown.

| # | File name | Used in script | Format |
|---|---|---|---|
| P01 | `P01_badal_portrait.png` | P04, the dream ("چہرہ ایسا کہ چودھویں کا چاند شرمائے…") | 16:9 |
| P02 | `P02_badal_fullfigure_black.png` | Composited over the real lake (P06) | **Portrait 9:16, pure black background** |
| P03 | `P03_descent.png` | P06, the 360 paris coming down to the stream | 16:9 |
| P04 | `P04_paris_group_black.png` | Composited over the real stream (P06) | 16:9, **pure black background** |
| P05 | `P05_stolen_clothes.png` | P06–P08 | 16:9 |
| P06 | `P06_prince_devotion.png` | P06, twelve years of devotion | 16:9 |
| P07 | `P07_dev.png` | P09–P10 | 16:9 |
| P08 | `P08_lovers_escape.png` | P11 | 16:9 |
| P09 | `P09_paris_dance.png` | P19, "still of nights they come to dance…" | 16:9 |

### Prompts (copy exactly; replace [BADAL], [PARIS], [PRINCE], [DEV], [STYLE] with the blocks above)

**P01, Badal Jamal portrait (the dream).**
> Portrait of [BADAL], head and shoulders, three-quarter view, looking slightly past the viewer with a gentle mysterious half-smile, the veil lifting slightly in a night breeze, a full moon and faint stars behind her, the edges of the image dissolving into soft dreamlike mist as if seen in a dream, [STYLE]

**P02, Badal Jamal full figure for compositing.**
*(Upload P01 as a reference.)*
> Full-body standing figure of [BADAL], the same woman as in the reference image, floating slightly above the ground, gown and dupatta flowing gently, one hand raised softly, isolated on a pure solid black background with nothing else in the frame, her own soft glow lighting her, 9:16 portrait, [STYLE without the 16:9 words]

**P03, the descent of the 360 paris.**
*(Upload P01 as a reference.)*
> Wide night landscape of a turquoise glacial lake high in the Himalayas (Saiful Malook, Kaghan Valley), snow-covered peaks under a full moon, a mountain stream flowing out of the lake over rocks in the foreground. From the night sky a long curving river of hundreds of golden lights descends toward the stream; at the front of it, [BADAL] glides down, the same woman as in the reference image, followed by [PARIS], seen at a distance, [STYLE]

**P04, group of paris for compositing.**
> A procession of about thirty [PARIS] walking and floating in a gentle curve, seen from a slight distance, isolated on a pure solid black background with nothing else in the frame, each figure glowing softly, [STYLE]

**P05, the stolen clothes.**
*(Modest and tasteful: only a hand is visible, no bathing body.)*
> Close-up at night by a moonlit mountain stream: an ivory silk dupatta with gold zari embroidery and a small emerald-and-gold taj lie folded on a wet dark rock at the water's edge, while from the dark water a slender woman's hand with henna patterns and a thin gold bangle reaches toward them; tiny golden lights scatter away into the night, glints on the water, [STYLE]

**P06, the prince's twelve years of devotion.**
> [PRINCE], seen from behind and slightly to the side, sitting in prayer on a flat rock at the shore of a frozen glacial lake in deep winter, snow falling, snow on his shawl and turban, his hair and beard grown long from years of devotion, snow-covered Himalayan peaks around him, a small oil lamp beside him, moonlight on the snow, quiet and lonely, [STYLE]

**P07, the dev breaks the dam.**
> [DEV] rising behind snow peaks above a glacial lake at night during a violent thunderstorm, its cloud-hand smashing a natural wall of boulders (a moraine) at the end of the lake, a huge wave of water bursting out and rushing down the valley, lightning lighting the scene, rain and spray, terrifying and epic, the lake in the middle ground, [STYLE]

**P08, the lovers escape.**
*(Upload P01 as a reference.)*
> On a rocky hilltop at night, [PRINCE] holds [BADAL]'s hand, the same woman as in the reference image, both seen from behind as silhouettes edged with moonlight, looking down into a valley where a raging flood of dark water sweeps away a small old town, storm clouds clearing, [STYLE]

**P09, the paris dance on the grass.**
> Wide view of an alpine meadow beside a glacial lake at night under a full moon, a circle of [PARIS] dancing slowly on the grass, their movement leaving soft trails of golden light, seen from a distance so no faces are clear, mist over the water, a lone small stone and a shepherd's path in the foreground, eerie and beautiful, [STYLE]

## 3. Steps for the local session (Claude in Chrome)
1. Create the folder `03_paris/` inside `/Users/ahmadnawazali/Video Work/Saif ul malook lake/`.
2. Open gemini.google.com in a new Chrome tab and start a new chat. Use the image-generation model Gemini offers.
3. Generate **P01** first: paste the full prompt with the blocks filled in, make 2–3 variations, pick the best, download it, rename it `P01_badal_portrait.png`, and save it to the folder.
4. For P02, P03 and P08, **attach P01 as a reference image** and add: "the same woman as in the reference image, same face, same crown and jewellery".
5. Generate P04–P09 the same way: 2–3 variations each, keep the best, and save the runner-up as `_alt`.
6. Write `03_paris/LOG.md`. For each image, record the file name, the prompt used, the date, and any problems (for example "regenerated twice: extra fingers").
7. Check each kept image against the rules in section 0 before saving.
8. When all 9 are saved, tell Ahmad: "Pari images are ready in 03_paris". He'll pass them to the cloud session.

## 4. How the cloud session will use them (for reference)
- P02 and P04 (black backgrounds) are keyed out and placed **into the real Saiful Malook drone footage**. Their veils and hair are animated with a gentle wind warp, glowing motes drift around them, and a slow parallax camera moves through the scene.
- P01, P03 and P05–P09 become dastan "paintings" with a slow push-in, moving mist and light particles, and candle flicker on the frame edges.
- **Rule for the edit:** paintings appear only in the dastan sections. The evidence sections stay real footage and real documents.
- **YouTube:** the description will say "Dastan illustrations created with AI; landscapes are real footage and satellite imagery."
