# Ep 2 — Sassi-Punnu — BUILD SPEC (handoff to the local session)

**Read first:** `../../PRODUCTION_SYSTEM/CHANNEL_BIBLE.md`, then `RESEARCH.md` + `SOURCES.md` here, then this file.
**Final script:** `SCRIPT_v5_READ.md` (locked). **Runtime:** ~9–9.5 min.
**Build with:** `PRODUCTION_SYSTEM/toolkit/` (same pipeline as Ep 1: `real.html`, `produce.py`, `anim_scenes.js`, `a_paris.py`, `assemble.py`, `audio_plan.py`, `captions.py`).

## The two visual worlds (Bible §4 — keep them separate)
- **DASTAN (the legend)** = **painted AI scenes** (Gemini), Persian/Mughal-miniature → moonlit oil, *immersive present*. Used for: the living port, little Sassi, the birth, the box on the Indus, Punnu, the wedding, the theft, the desert death.
- **REAL (the evidence)** = **real footage / satellite / the Cousens 1929 page / excavation photos / maps**. Used for: the dead ruins today, the dig, the river moving, the three-name mystery, Bhit Shah.
- The **pivot** ("یہ سب صدیوں پرانی بات ہے۔ اور آج؟") is the hard cut from painted world → real world. Make it land.

## On-screen document (our 1907-Gazetteer equivalent)
- **Henry Cousens, *The Antiquities of Sind* (1929)** — PUBLIC DOMAIN. Download the Bhambor pages (pp. 80–81) from
  archive.org and show the real page where it reads the site is **"also called Sassui-jo-Takar."**
  - Scan: https://archive.org/details/in.ernet.dli.2015.36039  (plain text: add `/…_djvu.txt`)
  - On the Mac: pull the page image (pdftoppm/screenshot of the archive.org page) → `assets/docs/cousens_1929_bhambor.png`.
- **DO NOT** show or redistribute the Parthica 2016 PDF or the Kot Diji booklet (copyright). Their *facts* are used in narration only.

---

## SHOT LIST — each beat: the line → the visual → how to build it → research basis

> Numbers are scene IDs for `assemble.py`'s PLAN. "Gen" = generate in Gemini (see `IMAGE_GEN_GUIDE_EP2.md`).
> "Real" = real footage/photo/satellite. Keep the legend painted, the evidence real.

| # | Script beat (cue) | On screen | Build | Research basis |
|---|---|---|---|---|
| **S01** | "آج سے ہزار سال پہلے… بندرگاہ کھچاکھچ بھری ہے" | The **living port at dusk** — ships, crowds, 47-tower wall, ivory being carved | **Gen** `P01_port_alive` (wide, golden dusk, dhows, bustle) + slow push-in | Peak port 8th–12th c.; 47 towers; trade Syria/Iran/Iraq/China; ivory workshops (RESEARCH §Parthica) |
| **S02** | "ایک گھاٹ پر… ایک ننھی سی بچی… ہنستی ہوئی" | **Little Sassi (child)** helping the dhobi at the ghat, splashing, laughing | **Gen** `P02_child_sassi_ghat` | the warm open (user direction) |
| **S03** | "اِس بچی کا نام ہے — سسی… یہ ہے سراغ نامہ" | hold on the child → title | title plate (`real.html` R02-style) | — |
| **TITLE** | **سسی پنوں: ریت میں کھویا شہر** | title over the port/ghat | `real.html` title scene | — |
| **S04** | "اوپری سندھ… راجا اور رانی کی گود برسوں سے سونی" | a small **palace in upper Sindh** by the river; the longing couple | **Gen** `P03_raja_palace` | user direction; Indus geography |
| **S05** | "نجومی… اچانک چپ ہو جاتے ہیں" + Astrologer line | the **astrologers over the baby's chart**, falling silent; the old najumi speaks | **Gen** `P04_astrologers` (candlelit court, a chart) | the fate premonition (legend) |
| **S06** | "آنسو پیتے ہوئے… صندوق… دریا کے حوالے" | the **father, weeping, setting the box on the night river** | **Gen** `P05_box_on_river_night` | legend |
| **S07** | "صندوق بہتا ہے… سمندر کی طرف… بھنبھور کے گھاٹ پر" | the **box drifting down the Indus**, upper Sindh → the delta; a map/satellite of the river's course helps | **Gen** `P06_box_drift` + optional **Real** satellite of the Indus delta | geography: upper Sindh → river mouth at Bhambore |
| **S08** | "ڈھکن کھولتا ہے… نام رکھتے ہیں — سسی" | the **dhobi opens the box**, the smiling baby; adoption | **Gen** `P07_dhobi_finds_baby` | legend |
| **S09** | "سسی جوان ہوتی ہے… حُسن کے چرچے… کیچ، مکران تک" | **young Sassi** at the ghat; her fame travelling with caravans across desert to Kech | **Gen** `P08_young_sassi` + `P09_caravan_desert` | legend; Kech/Makran; the port's trade links the lovers |
| **S10** | "پنوں… تاجر کا بھیس بدلے… اُسی ایک جھلک میں سب کچھ ہار بیٹھتا ہے" | **Punnu** (disguised trader) sees Sassi — the glimpse | **Gen** `P10_punnu_glimpse` | legend; Punnu = Hoth chief's son, Kech |
| **S11** | "شرط… دھوبی بن کر دکھائے… پنوں گھاٹ پر" | **the prince washing clothes** at the ghat, blistered hands | **Gen** `P11_prince_washerman` | legend (the test) |
| **S12** | "شہنائیاں بجتی ہیں… سسی اپنے پنوں کی ہو جاتی ہے" | **the wedding** in Bhambore, lights, joy | **Gen** `P12_wedding` | legend |
| **S13** | "ہم اِسے بھنبھور کہتے ہیں، مگر… باربریکون… دیبل… تین نام" | **the three names** over the city — Barbarikon / Debal / Bhambore; an old map | **Real/graphic** name-cards + old map (Imperial Gazetteer Atlas 1908 style) | Barbarikon (Periplus), Debal (Qasim 711), the debate |
| **S14** | "مگر آج رات… کیچ سے، پنوں کے بھائی آ پہنچے ہیں" | **the brothers arrive at the night gate** — ominous | **Gen** `P13_brothers_gate` | legend |
| **S15** | "دھوکے سے… اتنی شراب… بے ہوش… اونٹ پر ڈال کر کیچ" | **the drugged feast; Punnu carried off on a camel** into the dark | **Gen** `P14_feast_abduction` | legend |
| **S16** | "صبح… جگہ خالی… اونٹوں کے نشان" | **Sassi wakes to the empty bed / camel tracks** in the sand | **Gen** `P15_sassi_wakes` | legend |
| **S17** | "ننگے پاؤں… صحرا میں… پنوں… پنوں" + Sassi line | **Sassi running barefoot in the burning desert**, calling; collapses; prayer | **Gen** `P16_sassi_desert` (the hero image; reuse for the cold-open flash) | legend |
| **S18** | "زمین پھٹتی ہے، سسی اُس میں سما جاتی ہے" | **the earth opens / swallows her** (suggestive, not gory) | **Gen** `P17_earth_opens` | legend |
| **S19** | "پنوں کی آنکھ کھلتی ہے… قیامت… دوڑ پڑتا ہے… وہی گڈریا… قبر" | **Punnu wakes, escapes, races back; the shepherd shows the grave; the earth takes him too** | **Gen** `P18_punnu_grave` | legend |
| **S20** | "لسبیلہ… ایک قبر دکھائی جاتی ہے… کیا یہ سچ ہے؟" | **the alleged grave at Lasbela** (tradition) | **Real** photo of the Lasbela shrine/tomb (credit) OR `Gen` tasteful | tradition; Lasbela, ~45 mi W of Karachi |
| **PIVOT** | "یہ سب صدیوں پرانی بات ہے۔ اور آج؟… خاموش ٹیلہ" | **HARD CUT: painted world → the real dead ruins today**, wind, broken walls | **Real** footage/photos of Bhambore ruins (archaeology reports / stock); satellite | the ruins today; 30 km from the sea |
| **S21** | "دریا خود چھوڑ گیا… سمندر تیس کلومیٹر دُور… خاموش ٹیلہ" | **satellite: the Indus swings away, the creek silts, the sea retreats**; a 'one-night' storm plate for the destruction legend | **Real** satellite/map animation (toolkit flood/map style) | Indus shift, creek silt, decline 13th c. (UNESCO, Cousens) |
| **S22** | "سو سال پہلے… ہینری کزنز… 'سسئی جو تڑ'… دھوبی کی بیٹی کے نام سے لکھا" | **the real Cousens 1929 page on screen**, highlight "Sassui-jo-Takar" | **Real** `cousens_1929_bhambor.png` on a lamp-lit desk (`real.html` doc scene) | Cousens 1929, pp. 80–81 |
| **S23** | "پچاس اور ساٹھ کے عشرے میں… ریت اپنے راز اُگلنے لگتی ہے… پورا شہر… ہاتھی دانت… برتن اور دھات" | **the dig**: archaeologists, trenches; finds — the wall & towers, ivory, foreign pottery | **Real** excavation photos (F.A. Khan era / mission report images, credited) + satellite of the 65-ha site | F.A. Khan 1958–65; 47 towers, lake, ivory, Syria/Iran/Iraq/China goods |
| **S24** | "شہر کے بیچوں بیچ ایک دیوار… مندر… مسجد… سات سو ستائیس، نو سو چھ عیسوی" | **the dividing wall; temple side & mosque side; the dated Kufic stones (727 & 906 CE)** | **Real** photos of the Partition Wall + mosque + Kufic inscription (credited); a graphic of the two dates | the Partition Wall; temple(west)/mosque(east); Kufic 727 & 906 CE |
| **S25** | "آخر یہ شہر ہے کون؟… کزنز: دیبل نہیں… خان و بلوچ: یہی دیبل ہے… نام آج بھی نہیں جانتے" | **the century-old debate** — the two camps, the question unresolved | **Real/graphic** the name-debate card; portraits/names of Cousens vs Khan/Baloch | the Debal dispute (RESEARCH §Parthica) |
| **S26** | "سسی کو زندہ کس نے رکھا؟… قاضی قادن… شاہ عبداللطیف بھٹائی… بھٹ شاہ… فقیر گاتے ہیں" | **Bhittai / Bhit Shah / faqeers singing** — honour in Urdu, NO on-screen Sindhi verse | **Real** Bhit Shah footage/photos + a Sindhi manuscript plate | Qazi Qadan (1500s), Bhittai, Seven Queens, Bhit Shah urs |
| **CLOSE** | "صحرا نے نگلا کیا تھا؟… سسی کا ٹیلہ… [CTA]… مکلی… سراغ نامہ" | dusk over the ruins / the hill; subscribe; Makli teaser | `real.html` close + teaser plate | — |

## Audio plan (see `PRODUCTION_SYSTEM/templates/AUDIO_GUIDE.md`)
- **Music beds:** M1 mystery/港 opening · M2 romantic (sitar/bansuri) for the love · M3 tension for the theft/desert · M4 calm documentary for the dig/evidence · M5 mystic for Bhittai/close. Instrumental, Pakistani/Persian, YouTube Audio Library only.
- **SFX:** harbour crowd/gulls, desert wind, camel, footsteps on sand, a heartbeat under the desert run, a deep boom on "زمین پھٹتی ہے", trowel/brush on stone for the dig, paper for the Cousens page, faqeer bells/ektara feel for Bhit Shah.
- **Voice-first rider** (music ≈15 dB under narration), −14 LUFS. Character lines: the **Astrologer** (older, grave) and **Sassi** (the desert cry) — from Ahmad's own recording with FX, as Ep 1.

## Voice-over
- Ahmad records the narration himself (as Ep 1). Recording script + pronunciation guide: `VO_SCRIPT.md` (in this folder).
- Mark the two character lines (Astrologer, Sassi) to read in a different tone; the mixer adds the FX.

## Packaging (cloud will finalise; placeholder)
- **Title (Roman Urdu):** e.g. *"Sassi Punnu: Woh Dooba Hua Sheher Jiska Naam Bhi Hum Nahi Jante"* (to be locked).
- **Thumbnail concept:** Sassi in the desert / the ruins + "سسی کا ٹیلہ" or "ریت میں کھویا شہر"; the three-name mystery.
- **Chapters, description, tags:** cloud writes from the final cut.

## Build order (RUNBOOK)
VO → asr/align → **images (Gemini)** → **real footage/archive gather (incl. Cousens page)** → music/SFX → scenes (layers+produce+anim+a_paris) → assemble (480p preview) → **send preview to cloud for review** → HD → captions/chapters → thumbnail → upload (unlisted).
