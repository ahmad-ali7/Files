# Ep 2 — Sassi-Punnu — Image-generation guide (Gemini, local session)

Follow `PRODUCTION_SYSTEM/templates/IMAGE_GEN_GUIDE.md` rules. Save to `assets/paris/` (keep the name). 2–3 variations each,
keep best + `_alt`, write `LOG.md`, QC against the rules, 16:9 unless noted. **No text/logos/watermark removal.**

## STYLE block (paste at the END of every prompt)
> cinematic painted realism in the style of a Mughal-Persian miniature reimagined as a moonlit/golden oil painting,
> rich but restrained colour, fine detail, soft atmospheric haze, film grain, dramatic natural light, 16:9, no text, no watermark, no frame

## Setting rule
Real **Sindh / Indus-delta** world ~1000 years ago: a mud-brick river **port city** (Bhambore) where the Indus meets the sea; dhows,
bustling bazaars, 47-tower walls; and the **Thar/Makran desert** for the pursuit. Dress: early-medieval Sindhi/Baloch, modest. **No modern objects.**

## Character bible (paste the matching block into each prompt)
- **SASSI (child):** a little girl ~6, bright-eyed, simple clean peasant clothes, a thin dupatta, by a river washing-ghat, joyful.
- **SASSI (young):** a strikingly beautiful young Sindhi woman, early 20s, long dark hair, modest long-sleeved ajrak-patterned dress + dupatta, barefoot, luminous but natural — not a European face.
- **PUNNU:** a handsome young Baloch prince of Kech, early 20s, short beard, turban, embroidered robe + shawl; later disguised as a plain trader with camels.
- **THE RAJA & RANI:** a modest Sindhi raja and rani of a small upriver kingdom, careworn, royal but not opulent.
- **THE ASTROLOGER:** an old court najumi, white beard, robe, with a star-chart, grave and fearful.
- **THE DHOBI:** a poor, kind washerman, middle-aged, simple clothes, at the river ghat.

## Prompts (file name → prompt + which block)
| File | Prompt (add the STYLE block) |
|---|---|
| `P01_port_alive` | Wide view at golden dusk of a great medieval Sindhi river port where the Indus meets the sea — mud-brick city with a long wall of many round towers, wooden sailing dhows crowding the harbour, crowds of traders of many races, bales of silk and carved ivory on the docks, smoke from workshops; alive and wealthy |
| `P02_child_sassi_ghat` | [SASSI child] a little girl helping a poor washerman father at a riverside washing-ghat, splashing water and laughing, warm morning light, the port city behind |
| `P03_raja_palace` | A modest river-side palace of a small kingdom in upper Sindh at night, a careworn [RAJA & RANI] holding a newborn, lamplight, tender and uneasy |
| `P04_astrologers` | [ASTROLOGER] old court astrologers bent over a baby's star-chart in a cand-lit hall, one looking up in fear, the raja watching, shadows, dread |
| `P05_box_on_river_night` | A grieving father at the dark river's edge at night, setting a small wooden box upon the water, moonlight on the Indus, tears, sorrow |
| `P06_box_drift` | A small wooden box drifting down a wide moonlit river past sleeping villages toward a distant sea, lonely and small on the vast water |
| `P07_dhobi_finds_baby` | [DHOBI] a poor washerman at a river ghat at dawn opening a wet wooden box to find a smiling baby wrapped in cloth, wonder and joy |
| `P08_young_sassi` | [SASSI young] a beautiful young woman washing clothes at the river-ghat of the bustling port city, modest ajrak dress and dupatta, luminous, a crowd noticing her |
| `P09_caravan_desert` | A camel caravan of traders crossing a vast golden desert at dusk toward distant blue mountains, carrying bales, long shadows |
| `P10_punnu_glimpse` | [PUNNU] a young Baloch prince disguised as a plain trader with camels, frozen mid-step in the bazaar, stunned, gazing off — love at first sight |
| `P11_prince_washerman` | [PUNNU] a prince who has removed his finery, kneeling at a washing-ghat clumsily washing clothes, blistered hands, half-ashamed half-smiling, the port behind |
| `P12_wedding` | A joyful night wedding in a medieval Sindhi port city, lamps and marigolds, music, [SASSI young] as a bride — warm, festive |
| `P13_brothers_gate` | Three stern Baloch horsemen arriving at the torch-lit night gate of a walled river city, cloaked, ominous, unwelcome guests pretending friendship |
| `P14_feast_abduction` | Night: a feast with wine; a young man slumped unconscious; men lifting him onto a waiting camel and slipping into the dark desert, secretive and cruel |
| `P15_sassi_wakes` | [SASSI young] a young woman waking at dawn in an empty room, reaching to an empty bedside, fear dawning; through the door, camel tracks in the sand |
| `P16_sassi_desert` | [SASSI young] a young woman alone, barefoot, running and stumbling across a vast burning desert under a white sun, hair wild, crying a name, tiny against the dunes — heartbreaking (HERO image; also used for the cold-open flash) |
| `P17_earth_opens` | A woman sinking as the desert ground opens around her in soft light, suggestive and poetic not gory, a distant shepherd watching, mystical |
| `P18_punnu_grave` | [PUNNU] a young man collapsed over a fresh desert grave, clutching the earth, hands raised to a pale sky in grief, a shepherd nearby, the empty desert |

*(The real-world evidence shots — ruins, dig, Cousens page, mosque, Bhit Shah — are REAL footage/photos/archive, not generated. See BUILD_SPEC.)*
