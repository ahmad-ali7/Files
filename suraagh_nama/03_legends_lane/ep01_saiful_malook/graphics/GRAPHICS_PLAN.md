# Ep 1 graphics plan: "Dastan Night"

## Style system
| Token | Value | Use |
|---|---|---|
| Night | `#0A0F24` → `#18204A` | Every background |
| Moon | `#E9EDF7` | Body text, moonlight |
| Lamp amber | `#F4B35E` | Highlights, the route, dates, the moraine glow |
| Gold leaf | `#D9A441` / `#F6E3B0` | Ornamental frames, titles, verse |
| Paper | `#E8DBBE` with ink `#2A2016` | Archive cards (1907, 1895, UNESCO) |

**Fonts:**
- **Noto Nastaliq Urdu:** all Urdu and the Shahmukhi verse.
- **IM Fell English:** quotes from the old printed records.
- **Special Elite:** source tags.
- **Amiri:** Arabic and Persian labels.
- **Noto Sans Bengali:** Alaol's title.
- **Inter:** small English labels.

**Rules:**
- **No faces.** People appear only as silhouettes or light. The fairies are lights.
- Each sitting opens with a gold-framed card ("پہلی نشست"…).
- **No music under the dastan sections**; only natural sound.
- Archive quotes are **typed reproductions**, each with its source tag. No fake scans.

## Shot list (v3.1 script)
| # | Sitting / time | Graphic | Method | Status |
|---|---|---|---|---|
| SM01 | Opening, 0:00 | Lamp and silver bowl; the water ripples, then dissolves into the lake | Canvas 2D (style frame done). Add hands in white sleeves as silhouette | 🟡 style frame |
| — | 0:00–0:40 | Naran at night, the river, the loudspeaker | **Earth Studio (Ahmad)**: Naran town, night-graded, plus our sound | ⬜ |
| SM-src | 0:25 | `Dawn · June 2005` source tag | Small card | ⬜ |
| SM02 | 0:55 | Title: "سیف الملوک · ایک پری، ایک دیو… اور ڈوبتا ہوا ناران" | Canvas and HTML | 🟡 style frame |
| SM03 | Before each sitting | Sitting cards I–VI | HTML | 🟡 style frame (I) |
| SM04 | The dastan, 1:05–2:20 | 2D dastan scenes: (a) the dream, the fairy as a silhouette of light; (b) the astrologers' horoscope chart; (c) the prince through the seasons; (d) **360 lights descending to the river below the lake**; (e) clothes on the rock; (f) the demon's shadow over the ridge; (g) the dam bursting | Canvas 2D | 🟡 (d) done |
| SM-flood | 2:10 | The flood running down the real valley from the lake to Naran | three.js on the real terrain model (same pipeline as K2) | ⬜ |
| SM05 | Second sitting | 1907 record cards: "It is an enchanted lake" · "Naran… a collection of huts" · "marked only by a few huts and by the boulders" | Typed paper card | 🟡 (1 of 3) |
| SM-unesco | Second sitting | UNESCO/Hazara University 2007 card: same story, plus the cave under the graves | Typed paper card | ⬜ |
| SM06 | Third sitting | **The journey map**: Arabian Nights → Persian → Golconda → Arakan → Khari Sharif → Kaghan, each in its own script | Canvas and Natural Earth | 🟡 style frame |
| SM07a | Third sitting | Verse 1: "سدا نہیں مرگائیاں بہناں، سدا نہیں سر پانی", plus the side-remark card "سیف الملوک سر = سیف الملوک کی جھیل (1883–84)" | HTML | ⬜ |
| SM-fairy | Fourth sitting | Mountain fairy belief (Acta Orientalia 2014 card) | Card over mist | ⬜ |
| SM08 | Fifth sitting | **The real demon**: lake cross-section, moraine dam, depth about 34 m (reported) | Canvas (style frame). Final version on the real terrain profile | 🟡 style frame |
| SM09 | Fifth sitting | "یہ دیو سوتا نہیں": 1893 · 2005 · 2025 | HTML | 🟡 style frame |
| SM07 | Last sitting | Verse 2: "لوئِ لوئِ بھر لے کڑیئے…" | HTML | 🟡 style frame |
| SM-end | Last sitting | Tents today, then night; the fairy lights go out one by one; the 1907 "woe is it to the mortal" line; the lamp goes out | Canvas plus Earth Studio | ⬜ |
| SM-next | End | "اگلی محفل: سسی پنوں" end card | HTML | ⬜ |
| SM10 | Thumbnail | "جھیل کا دیو · 1907 RECORD · سچ یا داستان؟" | Canvas (concept) | 🟡 concept |

## Earth Studio shots for Ahmad
Coordinates are approximate.

| Shot | Where | Move |
|---|---|---|
| ES1 | Naran town (34.909, 73.650) | Slow descending orbit (we grade it to night) |
| ES2 | **Lake to Naran** (from 34.877, 73.694 down the outflow valley to Naran) | Follow the water's path, low and fast. This is the flood path |
| ES3 | Lake Saiful Malook (34.877, 73.694) | Wide reveal over the moraine, then push in |
| ES4 | Malika Parbat, the peak south of the lake | Slow tilt-up (no fairy claim) |

## How to render
- **Stills:** `node stills.js <abs path>/web <outdir> SM04_fairies@8 …`
- **Video:** use the K2 `render.js` with `HTML=scenes.html`. It uses the same API (`setup`, `renderFrame`, `sceneList`).

---

# v2 direction: "real craft" (replaces the drawn look above)
Ahmad's feedback: the drawn frames looked machine-made. **Every frame now starts from something real**, and the craft is in how we treat it.

| Element | v1 (drawn) | v2 (real) |
|---|---|---|
| Night lake | Drawn mountains | **Real drone footage of the lake** (Pixabay), graded to night by hand ("day-for-night", a classic film technique): sky masked along a hand-traced skyline, moonlit snow, film grain, halation (the warm glow around bright light on film) |
| Fairies | Dots over drawn hills | Light points with halo and **reflection on the real water** |
| 1907 record | Typed card | **The real scan of page 205** (archive.org, public domain) under lamp light, with a pencil underline on "enchanted lake" |
| 1907 evidence | — | **A real 1907 photograph** from the same book: "THE SAFR MALUK RIDGE, TO THE NORTH OF THE LAKE" |
| The real demon | Diagram | **Real footage of the rocky moraine** with a hand-drawn line |
| Thumbnail | Drawn eyes | Real night lake, plus a **torn strip of the real 1907 page**: "The inhabitants of Naran, then a big city…" |

## New finds in the 1907 book (public domain)
- Page 205 says it directly: **"(sar meaning lake)"**. This backs up the side-remark about "سیف الملوک سر".
- **Photo plates:** "The Safr Maluk ridge, to the north of the lake"; "The Manur peak"; "Flowers in Kagan"; "The Kagan road, a little above Kagan village".

## Still to build in v2
- **Opening (needs Ahmad):** film a real clay diya and a steel or silver bowl of water on a white cloth at night, on a phone, 4K if possible. Hands only, in a white sleeve, no face. **The most human-crafted shot in the episode.**
- **Dastan scenes:**
  - The dream and the astrologers, as real candle and paper textures with shadow-play (hands only).
  - The demon as real weather: storm clouds and an avalanche or debris flow, from stock footage.
- **The flood:** real terrain plus free satellite imagery (Sentinel-2) in 3D, water running down the valley to Naran.
- **Journey map:** a **real public-domain old map** of Asia (for example, the 1909 Imperial Gazetteer atlas) with an ink route.
- **Moraine label:** confirm on satellite imagery and the terrain model which ridge is the damming moraine before the label says "it holds the lake". It currently says only "گلیشیئر کا لایا ہوا پتھر اور مٹی".

**Code:** `real/craft.py` (grading and light compositing), `real/f_fairies.py`, `real/real.html` (layouts). **Frames:** `style_frames_real/`.
