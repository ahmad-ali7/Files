# SCENE LIBRARY — the catalog of reusable scene types

Every scene type we can already build, and which `toolkit/` piece builds it. The BUILD_SPEC's scene list should
reference these by name. **To add a new scene type:** prototype it, add a row here (status `experimental`), and
once it's used in a shipped episode mark it `adopted`. Keep it consistent with CHANNEL_BIBLE §4.

| Scene type | What it is | Built by | Status |
|---|---|---|---|
| Title card | Episode title over a graded plate, gold/red type | `real.html` + `layers.js` | adopted |
| Sitting card | "نشست" chapter card, title writes on, real candle, glint | `anim_scenes.js` (card) | adopted |
| Document frame | A real archival page/photo on a lamp-lit desk | `real.html` (desk/doc) + `produce.py still` | adopted |
| Map (static→route) | Old map; a glowing route grows stop-by-stop, then dissolves to real footage | `anim_scenes.js` (R06b route) | adopted |
| Astrologer chart | Zodiac chart draws itself, signs ink in, stars wake, line of fate | `anim_scenes.js` (R03) | adopted |
| Living flame / diya | Real lamp footage with animated flicker, breathing light, sparks, heat shimmer | `a_lamp.py` | adopted |
| Day-for-night landscape | Real daytime footage graded to moonlit night, sky-masked | `produce.py` (naran_night) + `craft.py` | adopted |
| Painted dastan scene | AI painting with push-in, moving mist, motes, candle flicker | `a_paris.py` (painting) | adopted |
| Composited figure | Black-bg AI figure keyed into real footage, wind-warp, reflection, glow | `a_paris.py` (key_black/place) | adopted |
| Storm-demon | Storm clouds form a demon, revealed on lightning; red eyes | `produce.py` (demon) + `f_demon.py` | adopted |
| Flood map | 2D satellite flood spread (HAND/least-cost), front eases down-valley | `flood2d.py` + `produce.py` (flood) | adopted |
| Verse over footage | A couplet in gold over real lake water / plate | `real.html` (V1_water) + `anim_scenes.js` | adopted |
| Evidence timeline | Dated cards (e.g. 1893/2005/2025) over a plate | `real.html` (R21_events) | adopted |
| Fog / belief scene | Real fog footage with drifting lights | `produce.py` (belief) | adopted |

## Ideas not yet built (candidates — pass the brand test in EXTENDING first)
- Parallax 2.5D on a single still (depth map → slow dolly) for archive photos.
- Ken-Burns + particle embers reusable macro for any lamp/fire scene.
- A recurring "map of Pakistan → zoom to the place" opener motif.
- Hand-drawn ink annotations appearing on a real document (circle, underline) to point at evidence.
- A signature 3-second "Suraagh Nama" sting (audio + mark) for open/close.

> Each new scene type should end up callable from `assemble.py`'s PLAN like the rest, so episodes stay data-driven.
