# Review request for Gemini Neon — holoen r02, packet B

> 給作者：把這整個檔案交給 Gemini Neon（桌面版），請它照下面的指示審查；它的回覆整段貼回給 Claude 即可。

You are the independent second reviewer of a Sudowrite story bible about hololive VTubers. Claude (an AI model) researched
and wrote the material below alone on 2026-11-27; nobody else has checked it yet. Your job is to find what is wrong,
unsupported, misattributed or out of scope, with evidence, so that Claude can fix it. Today is 2026-11-27. The project's
baseline date is 2026-09-30; facts after it are allowed when dated.

## Project rules (the material must follow these; flag any breach)
1. **Public persona only.** No private-life information about the performers: family, pets, home, health, daily
   routine, sleep, breaks or hiatuses and their reasons, travel, where they stream from. A stream title that mentions
   such a thing is still out of scope.
2. **Every important fact needs a source** (official hololive / COVER pages first: hololive.hololivepro.com profiles,
   music pages, news; then archived stream titles; then reputable news). Unverified items must be labelled as such.
   Fan wikis are secondary at best. Recent evidence outweighs old.
3. **Quoted speech from streams** may be quoted only where both speech-recognition models agree (see the audio-check
   reports in the materials: a "Partial (computed)" verdict approves only the quoted shared run; "Agrees (spelling)"
   approves the whole line; "Not confirmed" approves nothing). Written lines (official profile, the member's own
   titles or descriptions) may be quoted when labelled as written or official.
4. **Japanese members' spoken lines** are written in Japanese, with a romanization and an English gloss.
5. **Performance sheets** describe an original designed voice for ElevenLabs; they must never claim to imitate or
   clone the real member. Pitch and pace figures are research context, not targets.
6. The `## [SW] ...` sections are what Sudowrite receives; the rest of each dossier is the research behind them.
   Role is always "Protagonist" by author decision.

## What to check, in priority order
1. Factual errors: dates, names, song titles and release dates, unit membership, who took part in a collab, status
   (active, graduated, affiliate). Verify against the cited sources where you can open them.
2. Claims the cited source does not support, or that generalize too far from it ("always," "every," "known for").
3. Scope or privacy breaches (rule 1).
4. Misattributed lines: a chat response presented as the member's line, a game character's line presented as hers,
   an English official translation presented as her own words.
5. Inconsistencies: a dossier versus its own [SW] fields; one card versus another card about the same event; a card
   versus its performance sheet.
6. Japanese text: wrong kana/kanji, wrong romanization, wrong or misleading English gloss.
7. Important omissions a novelist would need, but only if you can give a source.

## Scope of packet B
Part 1: the outfit descriptions on all 40 character cards. Claude described each image in the member's official
profile gallery; open the image URLs listed with each card and check that every outfit description matches its image
(colours, garments, accessories, hair), that the labels are reasonable, and that any date given is supported by what
the description says it rests on (a reveal-stream title, hashtag, thumbnail or silhouette). Also check that the
[SW] Physical Description agrees with the dossier's outfit section. Galleries may omit seasonal outfits; that is a
known limitation, not an error.
Part 2: the relationship lines that r02 added to existing cards for the FLOW GLOW and GAMERS members (current
Relationships fields, the map rows added with their sources, and evidence notes). Check that each added tie is
supported by its source, names the right participants and dates, and does not overstate closeness. Archive video IDs
can be opened as https://www.youtube.com/watch?v=<ID>.


## Do not
- Rewrite style or restructure the files; suggest the smallest fix.
- Add facts without a source, or private details of any kind.
- Treat a fan wiki or a clip channel as official.
- Mark something wrong only because you cannot open its source; list it under "Could not verify" instead.

## Reply format (please follow exactly; Claude will merge it mechanically)
First line, exactly one of: `VERDICT: APPROVE` or `VERDICT: CHANGES`.

Then a Markdown table, one row per finding, most severe first:

| # | File | Section or field | Exact text (copy it) | Problem | Evidence (URL, or why) | Severity | Proposed fix |
|---|---|---|---|---|---|---|---|

Severity: **P0** = wrong or out of scope, must fix; **P1** = unsupported, misleading or inconsistent, should fix;
**P2** = suggestion. Then a section `## Could not verify` (claims you could not confirm or refute, with what you
tried), and `## Notes` (anything else, briefly). Reply in English; keep Japanese quotes as they are.

## Part 1. Outfits and Physical Description (all 40 character cards)

### Mori Calliope (`bible/characters/Mori-Calliope.md`)

**Official gallery images (open these to check the descriptions):**
- gallery 01: https://hololive.hololivepro.com/wp-content/uploads/2020/07/Mori-Calliope_pr-img_01.webp
- gallery 02: https://hololive.hololivepro.com/wp-content/uploads/2020/07/Mori-Calliope_pr-img_02.webp
- gallery 03: https://hololive.hololivepro.com/wp-content/uploads/2020/07/Mori-Calliope_pr-img_03.webp
- gallery 04: https://hololive.hololivepro.com/wp-content/uploads/2020/07/Mori-Calliope_pr-img_04.webp
- gallery 05: https://hololive.hololivepro.com/wp-content/uploads/2020/07/Mori-Calliope_pr-img_05.webp
- gallery 06: https://hololive.hololivepro.com/wp-content/uploads/2020/07/Mori-Calliope_pr-img_06.webp
- gallery 07: https://hololive.hololivepro.com/wp-content/uploads/2020/07/Mori-Calliope_pr-img_07.webp
- gallery 08: https://hololive.hololivepro.com/wp-content/uploads/2020/07/Mori-Calliope_pr-img_08.webp
- gallery 09: https://hololive.hololivepro.com/wp-content/uploads/2020/07/Mori-Calliope_pr-img_09.webp
- gallery 10: https://hololive.hololivepro.com/wp-content/uploads/2020/07/Mori-Calliope_pr-img_10.webp
- gallery 11: https://hololive.hololivepro.com/wp-content/uploads/2020/07/Mori-Calliope_pr-img_11.webp
- gallery 12: https://hololive.hololivepro.com/wp-content/uploads/2020/07/Mori-Calliope_pr-img_12.webp
- gallery 13: https://hololive.hololivepro.com/wp-content/uploads/2020/07/Mori-Calliope_pr-img_13.webp

**Dossier outfit section:**

````markdown
### Outfits in the official profile gallery (checked 2026-11-27)
Claude's reading of the gallery images on https://hololive.hololivepro.com/en/talents/mori-calliope/ (13 images (01 and 02 show the same original outfit)). Labels are descriptive
unless a date and its source are given; the gallery may not include every seasonal outfit shown only on stream.

- **Original reaper outfit** (gallery 01-02): a tattered black hooded cloak lined in red over a black dress with gold trim and a high slit, a chain belt with a red tassel, long black gloves with sheer sleeves, black heels, a small black crown and her scythe.
- **Streetwear** (gallery 03): a black cap, a red-and-black bomber jacket over a white crop top with a pink skull, a chain belt, black joggers with a red band and red-and-white high-tops.
- **Red evening dress** (gallery 04): a strapless red gown with a black sash and a ruffled side drape, a black lace choker with a pendant, red strappy heels and a glass of red wine.
- **Kimono** (gallery 05): hair up with a red flower, a black kimono with gold patterns and red lining whose hems dissolve into black wisps, a purple obi, a fox mask at her side and geta.
- **Loungewear** (gallery 06): twin tails with black bows, a sheer black lace slip dress and grey skull slippers.
- **Western outfit** (gallery 07): a black cowboy hat with a red band, a long fringed black duster, a corset vest, black shorts, tall boots and a long gun.
- **Bunny rocker** (gallery 08): a black bunny-ear headband, a navy fur-trimmed jacket over a black bodysuit, torn black tights, sneakers and a bass guitar shaped like a scythe.
- **Girly bob** (gallery 09): a short pink bob with a black headband, round glasses, a white frilled blouse with a ribbon tie, a pink pleated skirt and black strappy heels.
- **Punk coat** (gallery 10): a messy side updo with pins, sunglasses, a long black coat with a tattered hem and many pockets, ripped trousers, gloves and black boots.
- **Puffer streetwear** (gallery 11): a backwards black cap, a black puffer jacket with headphones around her neck, a red top, black cargo trousers and black boots.
- **Rock reaper** (gallery 12): a long high ponytail with a black bow, a black gothic dress with a garter, heeled lace-up boots and the scythe-bass.
- **Monster Hunter collaboration armor (©CAPCOM)** (gallery 13): spiked black armor with a white fur collar, a horned headpiece, spiked gauntlets and greaves over fishnet.
````

**[SW] Physical Description (what Sudowrite receives):**

````text
Calli's avatar is 167 cm tall, with long straight pink hair, red eyes and a small black crown. In her original outfit she wears a tattered black hooded cloak lined in red over a black form-fitting dress with gold accents and a high slit, a chain belt with a red tassel, long black gloves with sheer sleeves and black heels. A foldable scythe with pink accents, named Ricky, rides on her back. Other outfits in the official gallery: Streetwear: a black cap, a red-and-black bomber jacket over a white crop top with a pink skull, a chain belt; Red evening dress: a strapless red gown with a black sash and a ruffled side drape, a black lace choker with a pendant, red strappy heels and a glass of red wine; Kimono: hair up with a red flower, a black kimono with gold patterns and red lining whose hems dissolve into black wisps, a purple obi; Loungewear: twin tails with black bows, a sheer black lace slip dress and grey skull slippers; Western outfit: a black cowboy hat with a red band, a long fringed black duster, a corset vest; Bunny rocker: a black bunny-ear headband, a navy fur-trimmed jacket over a black bodysuit, torn black tights; Girly bob: a short pink bob with a black headband, round glasses, a white frilled blouse with a ribbon tie; Punk coat: a messy side updo with pins, sunglasses, a long black coat with a tattered hem and many pockets; Puffer streetwear: a backwards black cap, a black puffer jacket with headphones around her neck, a red top; Rock reaper: a long high ponytail with a black bow, a black gothic dress with a garter, heeled lace-up boots and the scythe-bass; Monster Hunter collaboration outfit: spiked black armor with a white fur collar, a horned headpiece, spiked gauntlets and greaves over fishnet.
````

### Takanashi Kiara (`bible/characters/Takanashi-Kiara.md`)

**Official gallery images (open these to check the descriptions):**
- gallery 01: https://hololive.hololivepro.com/wp-content/uploads/2020/07/Takanashi-Kiara_pr-img_01.webp
- gallery 02: https://hololive.hololivepro.com/wp-content/uploads/2020/07/Takanashi-Kiara_pr-img_02.webp
- gallery 03: https://hololive.hololivepro.com/wp-content/uploads/2020/07/Takanashi-Kiara_pr-img_03.webp
- gallery 04: https://hololive.hololivepro.com/wp-content/uploads/2020/07/Takanashi-Kiara_pr-img_04.webp
- gallery 05: https://hololive.hololivepro.com/wp-content/uploads/2020/07/Takanashi-Kiara_pr-img_05.webp
- gallery 06: https://hololive.hololivepro.com/wp-content/uploads/2020/07/Takanashi-Kiara_pr-img_06.webp
- gallery 07: https://hololive.hololivepro.com/wp-content/uploads/2020/07/Takanashi-Kiara_pr-img_07.webp
- gallery 08: https://hololive.hololivepro.com/wp-content/uploads/2020/07/Takanashi-Kiara_pr-img_08.webp
- gallery 09: https://hololive.hololivepro.com/wp-content/uploads/2020/07/Takanashi-Kiara_pr-img_09.webp
- gallery 10: https://hololive.hololivepro.com/wp-content/uploads/2020/07/Takanashi-Kiara_pr-img_10.webp
- gallery 11: https://hololive.hololivepro.com/wp-content/uploads/2020/07/Takanashi-Kiara_pr-img_11.webp

**Dossier outfit section:**

````markdown
### Outfits in the official profile gallery (checked 2026-11-27)
Claude's reading of the gallery images on https://hololive.hololivepro.com/en/talents/takanashi-kiara/ (11 images (01 and 02 show the same original outfit)). Labels are descriptive
unless a date and its source are given; the gallery may not include every seasonal outfit shown only on stream.

- **Original outfit** (gallery 01-02): an orange cap with a feather and badges, an orange vest-top with black buttons and a sailor collar, an orange miniskirt with a belt, white thigh-highs on garters and dark sneakers; a green-flamed sword and a blue shield.
- **Summer casual** (gallery 03): a straw hat, two braids, a white puff-sleeved crop blouse, a heart-shaped chocolate bag, denim shorts and white sandals.
- **Phoenix gown** (gallery 04): a gold leaf crown, a wrap of blue feathers at the shoulders, a dark red asymmetric gown with a feathered hem, patterned tights and red heels.
- **Furisode** (gallery 05): flowers and pink feathered wings in her hair and a white kimono printed with cranes and peonies.
- **Dirndl-style outfit** (gallery 06): hair up under a flower crown, a pink jacket over a white blouse, and a mint-green skirt and apron with folk patterns.
- **Armored outfit** (gallery 07): a long high ponytail with a blue feather ornament, sleek black-and-silver armor, dark blue feathered wings at her hips and armored boots.
- **Retro aerobics outfit** (gallery 08): short hair with a blue bow headband, a light-blue off-shoulder sweatshirt printed KFP, a white leotard, shiny pink leggings and leg warmers.
- **Loungewear** (gallery 09): short hair, a fluffy white jacket with heart pockets over a white top with orange lacing, frilled bloomers, white thigh-highs with orange bows and chick slippers.
- **Horned folk-festival outfit** (gallery 10): a crimson headdress with black ram horns, a red-and-white frilled dress with wide patterned sleeves, white tights, a long tail ending in a pom-pom and a winged microphone staff.
- **Monster Hunter collaboration outfit (©CAPCOM)** (gallery 11): very long straight hair with small horns and a black bodysuit with red accents.
````

**[SW] Physical Description (what Sudowrite receives):**

````text
Kiara's avatar is 165 cm tall, with medium-length coral hair fading to teal and magenta eyes. Shiny blue feathers grow behind her ears; they look like earrings but are phoenix down. In her original outfit she wears a mostly orange uniform with a greenish neck bow, a small white chef's hat and a red beret with a starred black bow, and she carries a sword that slots into her shield. Other outfits in the official gallery: Summer casual: a straw hat, two braids, a white puff-sleeved crop blouse; Phoenix gown: a gold leaf crown, a wrap of blue feathers at the shoulders, a dark red asymmetric gown with a feathered hem; Furisode: flowers and pink feathered wings in her hair and a white kimono printed with cranes and peonies; Dirndl-style outfit: hair up under a flower crown, a pink jacket over a white blouse, a mint-green skirt and apron with folk patterns; Armored outfit: a long high ponytail with a blue feather ornament, sleek black-and-silver armor, dark blue feathered wings at her hips and armored boots; Retro aerobics outfit: short hair with a blue bow headband, a light-blue off-shoulder sweatshirt printed KFP, a white leotard; Loungewear: short hair, a fluffy white jacket with heart pockets over a white top with orange lacing, frilled bloomers; Horned folk-festival outfit: a crimson headdress with black ram horns, a red-and-white frilled dress with wide patterned sleeves, white tights; Monster Hunter collaboration outfit: very long straight hair with small horns and a black bodysuit with red accents.
````

### Ninomae Ina'nis (`bible/characters/Ninomae-Inanis.md`)

**Official gallery images (open these to check the descriptions):**
- gallery 01: https://hololive.hololivepro.com/wp-content/uploads/2020/07/Ninomae-Inanis_pr-img_01.webp
- gallery 02: https://hololive.hololivepro.com/wp-content/uploads/2020/07/Ninomae-Inanis_pr-img_02.webp
- gallery 03: https://hololive.hololivepro.com/wp-content/uploads/2020/07/Ninomae-Inanis_pr-img_03.webp
- gallery 04: https://hololive.hololivepro.com/wp-content/uploads/2020/07/Ninomae-Inanis_pr-img_04.webp
- gallery 05: https://hololive.hololivepro.com/wp-content/uploads/2020/07/Ninomae-Inanis_pr-img_05.webp
- gallery 06: https://hololive.hololivepro.com/wp-content/uploads/2020/07/Ninomae-Inanis_pr-img_06.webp
- gallery 07: https://hololive.hololivepro.com/wp-content/uploads/2020/07/Ninomae-Inanis_pr-img_07.webp
- gallery 08: https://hololive.hololivepro.com/wp-content/uploads/2020/07/Ninomae-Inanis_pr-img_08.webp
- gallery 09: https://hololive.hololivepro.com/wp-content/uploads/2020/07/Ninomae-Inanis_pr-img_09.webp
- gallery 10: https://hololive.hololivepro.com/wp-content/uploads/2020/07/Ninomae-Inanis_pr-img_10.webp
- gallery 11: https://hololive.hololivepro.com/wp-content/uploads/2020/07/Ninomae-Inanis_pr-img_11.webp
- gallery 12: https://hololive.hololivepro.com/wp-content/uploads/2020/07/Ninomae-Inanis_pr-img_12.webp

**Dossier outfit section:**

````markdown
### Outfits in the official profile gallery (checked 2026-11-27)
Claude's reading of the gallery images on https://hololive.hololivepro.com/en/talents/ninomae-inanis/ (12 images (01 and 02 show the same original outfit)). Labels are descriptive
unless a date and its source are given; the gallery may not include every seasonal outfit shown only on stream.

- **Original outfit** (gallery 01-02): a golden halo, a black strapless dress trimmed with white feathers and orange accents, one white thigh-high, platform geta, a tome in her hands and a mass of purple tentacles with orange suckers behind her.
- **Artist outfit** (gallery 03): a black beret and glasses, a black pinafore dress over a dark shirt, a pink crossbody bag, patterned tights, a paintbrush and a palette.
- **White-coat outfit** (gallery 04): a small black top hat, long twin tails, a white frilled coat over a red-and-black kimono-print dress with a big bow, and black boots.
- **Kimono with haori** (gallery 05): hair in buns with a red flower, a black haori over a purple-and-red patterned kimono with a teal obi, and a small drawstring bag.
- **Loungewear** (gallery 06): a short bob, an oversized grey hoodie covered in pins and patches, and grey slippers.
- **Baker outfit** (gallery 07): wavy hair with a white headdress, a black dress with a white apron and a checkered hem, a whisk in hand and a doughnut in her mouth.
- **School outfit** (gallery 08): a side tail with clips, a white eye patch, a grey sweater with a black bow, a plaid skirt, black knee socks and loafers.
- **White battle gown** (gallery 09): tall tentacle ears in her buns, a white frilled coat over a black dress and lace skirt, white tights, a huge black flower-shaped gauntlet and glowing floating spears.
- **Monster Hunter collaboration outfit (©CAPCOM)** (gallery 10): a black monster-head hood with teal horns, an off-shoulder teal-and-black spiked sweater, black shorts, a teal tail and spiked boots.
- **Winged coat outfit** (gallery 11): a short bob, translucent insect wings, a long dark-grey coat with pink diamond motifs and huge patterned sleeves, a red-tipped staff and black boots.
- **Gothic lolita** (gallery 12): long twin tails under a black headdress, an eye patch, a black frilled flower dress, two plush creatures, lace socks and platform shoes.
````

**[SW] Physical Description (what Sudowrite receives):**

````text
Ina's avatar is 157 cm tall, with long purple hair falling below her knees, squishy tentacle-like side locks fading to yellow tips, purple flaps on her head like a dumbo octopus's fins, and bluish-purple eyes. In her original outfit she wears a golden tiara, a sleeveless purple-and-yellow dress and small white wings at her waist, and she can show a golden halo. Large purple tentacles float behind her, and her book AO-chan hovers nearby. Other outfits in the official gallery: Artist outfit: a black beret and glasses, a black pinafore dress over a dark shirt, a pink crossbody bag; White-coat outfit: a small black top hat, long twin tails, a white frilled coat over a red-and-black kimono-print dress with a big bow; Kimono with haori: hair in buns with a red flower, a black haori over a purple-and-red patterned kimono with a teal obi, a small drawstring bag; Loungewear: a short bob, an oversized grey hoodie covered in pins and patches, grey slippers; Baker outfit: wavy hair with a white headdress, a black dress with a white apron and a checkered hem, a whisk in hand and a doughnut in her mouth; School outfit: a side tail with clips, a white eye patch, a grey sweater with a black bow; White battle gown: tall tentacle ears in her buns, a white frilled coat over a black dress and lace skirt, white tights; Monster Hunter collaboration outfit: a black monster-head hood with teal horns, an off-shoulder teal-and-black spiked sweater, black shorts; Winged coat outfit: a short bob, translucent insect wings, a long dark-grey coat with pink diamond motifs and huge patterned sleeves; Gothic lolita: long twin tails under a black headdress, an eye patch, a black frilled flower dress.
````

### Gawr Gura (`bible/characters/Gawr-Gura.md`)

**Official gallery images (open these to check the descriptions):**
- gallery 01: https://hololive.hololivepro.com/wp-content/uploads/2024/05/Gawr-Gura_pr-img_01.png
- gallery 02: https://hololive.hololivepro.com/wp-content/uploads/2020/07/Gawr-Gura_pr-img_02.png
- gallery 03: https://hololive.hololivepro.com/wp-content/uploads/2020/07/Gawr-Gura_pr-img_03.png
- gallery 04: https://hololive.hololivepro.com/wp-content/uploads/2020/07/Gawr-Gura_pr-img_04.png
- gallery 05: https://hololive.hololivepro.com/wp-content/uploads/2020/07/Gawr-Gura_pr-img_05.png
- gallery 06: https://hololive.hololivepro.com/wp-content/uploads/2020/07/Gawr-Gura_pr-img_06.png
- gallery 07: https://hololive.hololivepro.com/wp-content/uploads/2020/07/Gawr-Gura_pr-img_07.png

**Dossier outfit section:**

````markdown
### Outfits in the official profile gallery (checked 2026-11-27)
Claude's reading of the gallery images on https://hololive.hololivepro.com/en/talents/gawr-gura/ (7 images (01 and 02 show the same original outfit)). Labels are descriptive
unless a date and its source are given; the gallery may not include every seasonal outfit shown only on stream.

- **Original outfit** (gallery 01-02): a blue shark hoodie whose hood has teeth and whose front has a toothy mouth, blue socks, white sneakers, her shark tail and a coral-blue trident.
- **Cat-ear outfit (#CatShark, revealed 2021-05-06; the cat ears match the hashtag)** (gallery 03): cat ears, a side ponytail, a white puff-sleeved blouse under a navy button dress, a blue shoulder bag and platform sandals.
- **Greek-style outfit** (gallery 04): a gold laurel wreath, braids, a white off-shoulder dress fading to blue, a sheer light-blue wrap, a gold belt, gladiator sandals and her trident.
- **Kimono-style outfit** (gallery 05): twin buns with leaf-and-berry ornaments, a short blue-and-white kimono dress with a fur collar and a navy obi, white socks and sandals.
- **Hoodie-and-skirt outfit** (gallery 06): a side tail, a light-blue zip hoodie over a white shirt with a blue tie, a blue pleated skirt, white socks and a bandage on one knee.
- **Winter outfit (#snowshark, revealed 2025-01-26; matched by the hashtag)** (gallery 07): an X-shaped hair clip, a navy coat with fluffy white trim and pom-poms, a red plaid scarf, grey socks and beige boots.
````

**[SW] Physical Description (what Sudowrite receives):**

````text
Gura's avatar is small, 141 cm, with white-silver hair streaked with blue, short pigtails tied with shark-face hair ties, cyan eyes and sharp shark teeth. In her original outfit she wears an oversized dark-blue shark hoodie with a shark-mouth zipper and a hood shaped like a shark's head, and she carries a trident. Her avatar's cyan shark tail is stitched up (in her lore, a rock fell on it). Other outfits in the official gallery: Cat-ear outfit (2021): cat ears, a side ponytail, a white puff-sleeved blouse under a navy button dress; Greek-style outfit: a gold laurel wreath, braids, a white off-shoulder dress fading to blue; Kimono-style outfit: twin buns with leaf-and-berry ornaments, a short blue-and-white kimono dress with a fur collar and a navy obi, white socks and sandals; Hoodie-and-skirt outfit: a side tail, a light-blue zip hoodie over a white shirt with a blue tie, a blue pleated skirt; Winter outfit (2025): an X-shaped hair clip, a navy coat with fluffy white trim and pom-poms, a red plaid scarf.
````

### Watson Amelia (`bible/characters/Watson-Amelia.md`)

**Official gallery images (open these to check the descriptions):**
- gallery 01: https://hololive.hololivepro.com/wp-content/uploads/2020/07/Watson-Amelia_pr-img_01.png
- gallery 02: https://hololive.hololivepro.com/wp-content/uploads/2020/07/Watson-Amelia_pr-img_02.png
- gallery 03: https://hololive.hololivepro.com/wp-content/uploads/2020/07/Watson-Amelia_pr-img_03.png
- gallery 04: https://hololive.hololivepro.com/wp-content/uploads/2020/07/Watson-Amelia_pr-img_04.png
- gallery 05: https://hololive.hololivepro.com/wp-content/uploads/2020/07/Watson-Amelia_pr-img_05.png
- gallery 06: https://hololive.hololivepro.com/wp-content/uploads/2020/07/Watson-Amelia_pr-img_06.png

**Dossier outfit section:**

````markdown
### Outfits in the official profile gallery (checked 2026-11-27)
Claude's reading of the gallery images on https://hololive.hololivepro.com/en/talents/watson-amelia/ (6 images (01 and 02 show the same original outfit)). Labels are descriptive
unless a date and its source are given; the gallery may not include every seasonal outfit shown only on stream.

- **Original detective outfit** (gallery 01-02): a checked deerstalker with a gear-decorated magnifying-glass hairpin, a white blouse with a short red tie, a checked skirt with her golden pocket watch, a detective coat with a stethoscope, syringes on her left leg, black thigh-highs and brown shoes.
- **Casual outfit** (gallery 03): a brown cap with Bubba sitting on top, round glasses, a brown plaid cardigan over a white top, black shorts, tan tights, a black handbag with a mustache emblem and strappy heels.
- **Black evening dress** (gallery 04): an updo with a tiara, a sheer black puff-sleeved dress with a white flower belt, a blue vine tattoo on one leg and gold heels.
- **Hakama** (gallery 05): a navy kimono printed with goldfish, a yellow-to-orange hakama with a big orange bow, and geta.
- **Astronaut suit** (gallery 06): a golden spacesuit with a MYTH patch, a clear bubble helmet with a bow, white boots, and Bubba floating in his own helmet.
````

**[SW] Physical Description (what Sudowrite receives):**

````text
Ame's avatar is 150 cm tall, with light-blonde hair falling below her shoulders and blue eyes. In her original outfit she wears a checked deerstalker with a gear-decorated magnifying-glass hairpin, a white blouse with a short red tie printed with a mustache, a checked skirt carrying her golden pocket watch, a detective coat with a stethoscope, and syringes of her concoction strapped to her left leg. Bubba, her dog mascot, appears in later outfit designs. Other outfits in the official gallery: Casual outfit: a brown cap with Bubba sitting on top, round glasses, a brown plaid cardigan over a white top; Black evening dress: an updo with a tiara, a sheer black puff-sleeved dress with a white flower belt, a blue vine tattoo on one leg and gold heels; Hakama: a navy kimono printed with goldfish, a yellow-to-orange hakama with a big orange bow, geta; Astronaut suit: a golden spacesuit with a MYTH patch, a clear bubble helmet with a bow, white boots.
````

### IRyS (`bible/characters/IRyS.md`)

**Official gallery images (open these to check the descriptions):**
- gallery 01: https://hololive.hololivepro.com/wp-content/uploads/2020/07/IRyS_pr-img_01.webp
- gallery 02: https://hololive.hololivepro.com/wp-content/uploads/2020/07/IRyS_pr-img_02.webp
- gallery 03: https://hololive.hololivepro.com/wp-content/uploads/2020/07/IRyS_pr-img_03.webp
- gallery 04: https://hololive.hololivepro.com/wp-content/uploads/2020/07/IRyS_pr-img_04.webp
- gallery 05: https://hololive.hololivepro.com/wp-content/uploads/2020/07/IRyS_pr-img_05.webp
- gallery 06: https://hololive.hololivepro.com/wp-content/uploads/2020/07/IRyS_pr-img_06.webp
- gallery 07: https://hololive.hololivepro.com/wp-content/uploads/2020/07/IRyS_pr-img_07.webp
- gallery 08: https://hololive.hololivepro.com/wp-content/uploads/2020/07/IRyS_pr-img_08.webp

**Dossier outfit section:**

````markdown
### Outfits in the official profile gallery (checked 2026-11-27)
Claude's reading of the gallery images on https://hololive.hololivepro.com/en/talents/irys/ (8 images (01 and 02 show the same original outfit)). Labels are descriptive
unless a date and its source are given; the gallery may not include every seasonal outfit shown only on stream.

- **Original outfit** (gallery 01-02): long magenta hair, small horns, pointed ears, a white spiked halo, one dark wing and one translucent wing; a white-and-black dress with red roses and ribbons, detached sleeves, a frilled skirt, purple thigh-highs with bows and red heels.
- **Furisode** (gallery 03): a purple-and-white kimono printed with planets, stars and flowers, a red obi with a decorative cord knot, ornaments in her twin tails and sandals.
- **Casual outfit** (gallery 04): a short bob under a checked cap, a cream cable-knit cardigan over a white dress, black tights and ankle boots.
- **School-sporty outfit** (gallery 05): two braids and headphones, a teal jacket with patches over a navy sailor uniform, slouchy white leg warmers and sneakers.
- **Maid outfit** (gallery 06): twin tails with a maid headdress and a red rose, a black-and-white maid dress with long frilled sleeves, garters, black thigh-highs and black boots.
- **Racing idol outfit** (gallery 07): a high ponytail with a visor, a cropped top under a white-and-teal racing jacket, a checkered skirt, a holographic ribbon tail and teal-and-pink boots.
- **Monster Hunter collaboration outfit (©CAPCOM)** (gallery 08): a flower in her hair, a pink-and-white kimono-style top with tassels and wide sleeves, a dark frilled skirt, white thigh-highs and platform sandals.
````

**[SW] Physical Description (what Sudowrite receives):**

````text
IRyS's avatar is 162 cm tall (166 cm in heels), with light brown skin, floor-length magenta hair, long pointed ears and two small black horns. Her eyes are heterochromatic, cyan on the right and purple on the left, and a halo of white crystal stars floats above her head. She has a small pair of iridescent wings at her shoulders and larger magenta ones at her lower back. Other outfits in the official gallery: Furisode: a purple-and-white kimono printed with planets, stars and flowers, a red obi with a decorative cord knot; Casual outfit: a short bob under a checked cap, a cream cable-knit cardigan over a white dress, black tights and ankle boots; School-sporty outfit: two braids and headphones, a teal jacket with patches over a navy sailor uniform, slouchy white leg warmers and sneakers; Maid outfit: twin tails with a maid headdress and a red rose, a black-and-white maid dress with long frilled sleeves, garters; Racing idol outfit: a high ponytail with a visor, a cropped top under a white-and-teal racing jacket, a checkered skirt; Monster Hunter collaboration outfit: a flower in her hair, a pink-and-white kimono-style top with tassels and wide sleeves, a dark frilled skirt.
````

### Ouro Kronii (`bible/characters/Ouro-Kronii.md`)

**Official gallery images (open these to check the descriptions):**
- gallery 01: https://hololive.hololivepro.com/wp-content/uploads/2020/07/Ouro-Kronii_pr-img_01.webp
- gallery 02: https://hololive.hololivepro.com/wp-content/uploads/2020/07/Ouro-Kronii_pr-img_02.webp
- gallery 03: https://hololive.hololivepro.com/wp-content/uploads/2020/07/Ouro-Kronii_pr-img_03.webp
- gallery 04: https://hololive.hololivepro.com/wp-content/uploads/2020/07/Ouro-Kronii_pr-img_04.webp
- gallery 05: https://hololive.hololivepro.com/wp-content/uploads/2020/07/Ouro-Kronii_pr-img_05.webp
- gallery 06: https://hololive.hololivepro.com/wp-content/uploads/2020/07/Ouro-Kronii_pr-img_06.webp

**Dossier outfit section:**

````markdown
### Outfits in the official profile gallery (checked 2026-11-27)
Claude's reading of the gallery images on https://hololive.hololivepro.com/en/talents/ouro-kronii/ (6 images (01 and 02 show the same original outfit)). Labels are descriptive
unless a date and its source are given; the gallery may not include every seasonal outfit shown only on stream.

- **Original outfit** (gallery 01-02): a giant clock-face halo with hands, a white sleeveless top with a light-blue bow, black pinstriped shorts, a black coat lined in blue with frilled cuffs, black thigh-highs, winged blue boots and two golden clock-hand blades.
- **Furisode** (gallery 03): blue and orange flowers in her hair, a light-blue kimono printed with gold clockwork, chrysanthemums and a white snake, a white fur stole, a folding fan and platform sandals.
- **Casual outfit** (gallery 04): long hair with a blue streak, round glasses, a tick-marked ring halo, a camel trench coat over a white top, a brown monogram crossbody bag, ripped skinny jeans and white heels.
- **Military uniform** (gallery 05): a navy uniform with a gold aiguillette and medals, a long caped coat, trousers with a thigh strap and boots.
- **Victorian maid dress** (gallery 06): braided hair under a white lace cap, a long white eyelet dress with black sleeves and hem, a pocket-watch pendant and Mary Jane shoes.
````

**[SW] Physical Description (what Sudowrite receives):**

````text
Kronii's avatar is 168 cm tall, with short dark-blue hair that falls in long locks at the sides and big blue eyes. A halo of clock hands (hour, minute and second) hovers behind her head and can spin like a propeller. In her original outfit she wears blue, white and black with gold trim, under a blue cape with a big ribbon, jewels and gold ornaments, and she carries two swords shaped like the long and short hands of a clock. Other outfits in the official gallery: Furisode: blue and orange flowers in her hair, a light-blue kimono printed with gold clockwork, chrysanthemums and a white snake; Casual outfit: long hair with a blue streak, round glasses, a tick-marked ring halo; Military uniform: a navy uniform with a gold aiguillette and medals, a long caped coat, trousers with a thigh strap and boots; Victorian maid dress: braided hair under a white lace cap, a long white eyelet dress with black sleeves and hem, a pocket-watch pendant and Mary Jane shoes.
````

### Ceres Fauna (`bible/characters/Ceres-Fauna.md`)

**Official gallery images (open these to check the descriptions):**
- gallery 01: https://hololive.hololivepro.com/wp-content/uploads/2023/10/Ceres-Fauna_pr-img_01.png
- gallery 02: https://hololive.hololivepro.com/wp-content/uploads/2023/09/Ceres-Fauna_pr-img_02.png
- gallery 03: https://hololive.hololivepro.com/wp-content/uploads/2023/09/Ceres-Fauna_pr-img_03.png
- gallery 04: https://hololive.hololivepro.com/wp-content/uploads/2023/09/Ceres-Fauna_pr-img_04.png
- gallery 05: https://hololive.hololivepro.com/wp-content/uploads/2020/07/Ceres-Fauna_pr-img_05.png

**Dossier outfit section:**

````markdown
### Outfits in the official profile gallery (checked 2026-11-27)
Claude's reading of the gallery images on https://hololive.hololivepro.com/en/talents/ceres-fauna/ (5 images (01 and 02 show the same original outfit)). Labels are descriptive
unless a date and its source are given; the gallery may not include every seasonal outfit shown only on stream.

- **Original outfit** (gallery 01-02): leafy antlers, a white blouse under a navy corset dress with gold trim and a flowered belt, a long sheer pink-to-peach train with a scalloped hem, a thigh ring, anklets and toe sandals; a golden fruit in her hand.
- **Kimono (#HoloENKimonoRelay, 2022-01-15)** (gallery 03): braids with a pink flower, a white kimono with red peonies, a white frilled apron, a teal obi bow, a drawstring bag and brown lace-up boots.
- **Casual outfit ("Casual Fauna," 2022-12-10)** (gallery 04): a choker, a cream cardigan over a lilac blouse with a ribbon, a dark plaid skirt with a sheer hem, frilled socks and black Mary Janes.
- **Goth outfit (#GothFauna, 2024-02-25)** (gallery 05): black ribbons in her hair, a black dress with lace sleeves, fishnet thigh-highs with a garter and chunky black boots.
````

**[SW] Physical Description (what Sudowrite receives):**

````text
Fauna's avatar is 164 cm tall, with wavy light-green hair that fades to blue-green at the tips and is decorated with small white five-petal flowers, and horns like leafy tree branches (kirin horns, not deer antlers). Her eyes are yellow, with a beauty mark under the right one. She wears a short blue dress with golden ornaments under a white overcoat lined with pink flowers and closed with a blue bow, a golden belt set with green roses and water-drop gems, one long white sock and a golden bangle on the other ankle, and she goes barefoot. A golden apple sometimes floats at her hand; her sleepy kirin mascot Nemu may be curled up nearby. Other outfits in the official gallery: Kimono (2022): braids with a pink flower, a white kimono with red peonies, a white frilled apron; Casual outfit (2022): a choker, a cream cardigan over a lilac blouse with a ribbon, a dark plaid skirt with a sheer hem; Goth outfit (2024): black ribbons in her hair, a black dress with lace sleeves, fishnet thigh-highs with a garter and chunky black boots.
````

### Nanashi Mumei (`bible/characters/Nanashi-Mumei.md`)

**Official gallery images (open these to check the descriptions):**
- gallery 01: https://hololive.hololivepro.com/wp-content/uploads/2023/10/Nanashi-Mumei_pr-img_01.png
- gallery 02: https://hololive.hololivepro.com/wp-content/uploads/2020/07/Nanashi-Mumei_pr-img_02.png
- gallery 03: https://hololive.hololivepro.com/wp-content/uploads/2020/07/Nanashi-Mumei_pr-img_03.png
- gallery 04: https://hololive.hololivepro.com/wp-content/uploads/2020/07/Nanashi-Mumei_pr-img_04.png
- gallery 05: https://hololive.hololivepro.com/wp-content/uploads/2020/07/Nanashi-Mumei_pr-img_05.png

**Dossier outfit section:**

````markdown
### Outfits in the official profile gallery (checked 2026-11-27)
Claude's reading of the gallery images on https://hololive.hololivepro.com/en/talents/nanashi-mumei/ (5 images (01 and 02 show the same original outfit)). Labels are descriptive
unless a date and its source are given; the gallery may not include every seasonal outfit shown only on stream.

- **Original outfit** (gallery 01-02): two owl-feather tufts, a brown hooded capelet over a white blouse with a black bow, a dark corset with belts and a dagger, a red pleated skirt, a long teal cloak, a lantern at her hip, gloves, mismatched black stockings and fur-trimmed brown boots; Friend, a paper-bag creature, floats beside her.
- **Winter kimono outfit** (gallery 03): a short bob under a brown beret, a red shawl over a white kimono, a basket with a little owl, and boots.
- **Casual outfit** (gallery 04): round glasses, a cream oversized sweatshirt with a ribbon, a long brown plaid skirt and sneakers.
- **Punk outfit** (gallery 05): a side tail, a black skull T-shirt with red-and-black striped sleeves, a black pleated skirt with a red plaid panel, a garter, fishnets, printed leg warmers and black shoes.
````

**[SW] Physical Description (what Sudowrite receives):**

````text
Mumei's avatar is 156 cm tall, with long light-brown hair in a high ponytail, tied with a black band and two brown feathers standing up in a V, and brown eyes with a yellow gradient. She dresses like a fantasy adventurer: a white puff-sleeved blouse under a brown, gold-trimmed corset, a short red ruffled skirt with a brown outer skirt, mismatched black stockings with thigh straps, a brown and beige feathered cape lined in teal, fingerless gloves, and a belt hung with a lantern, a pouch and a small dagger. Her paper-bag mascot Friend, with a drawn mouth and a cross-shaped plaster, sometimes floats beside her. Other outfits in the official gallery: Winter kimono outfit: a short bob under a brown beret, a red shawl over a white kimono, a basket with a little owl; Casual outfit: round glasses, a cream oversized sweatshirt with a ribbon, a long brown plaid skirt and sneakers; Punk outfit: a side tail, a black skull T-shirt with red-and-black striped sleeves, a black pleated skirt with a red plaid panel.
````

### Hakos Baelz (`bible/characters/Hakos-Baelz.md`)

**Official gallery images (open these to check the descriptions):**
- gallery 01: https://hololive.hololivepro.com/wp-content/uploads/2020/07/Hakos-Baelz_pr-img_01.webp
- gallery 02: https://hololive.hololivepro.com/wp-content/uploads/2020/07/Hakos-Baelz_pr-img_02.webp
- gallery 03: https://hololive.hololivepro.com/wp-content/uploads/2020/07/Hakos-Baelz_pr-img_03.webp
- gallery 04: https://hololive.hololivepro.com/wp-content/uploads/2020/07/Hakos-Baelz_pr-img_04.webp
- gallery 05: https://hololive.hololivepro.com/wp-content/uploads/2020/07/Hakos-Baelz_pr-img_05.webp
- gallery 06: https://hololive.hololivepro.com/wp-content/uploads/2020/07/Hakos-Baelz_pr-img_06.webp
- gallery 07: https://hololive.hololivepro.com/wp-content/uploads/2020/07/Hakos-Baelz_pr-img_07.webp

**Dossier outfit section:**

````markdown
### Outfits in the official profile gallery (checked 2026-11-27)
Claude's reading of the gallery images on https://hololive.hololivepro.com/en/talents/hakos-baelz/ (7 images (01 and 02 show the same original outfit)). Labels are descriptive
unless a date and its source are given; the gallery may not include every seasonal outfit shown only on stream.

- **Original outfit** (gallery 01-02): red twin tails with black and white streaks and mouse ears, a spiked choker, a white crop top printed RAT, mismatched sleeves (a teal flame glove and a yellow puff), a red-white-black skirt with a teal bear dice bag, mismatched leg warmers and a long red tail with a bow.
- **Kimono (#HoloENKimonoRelay, 2022-01-15)** (gallery 03): flowers in her hair, a short yellow kimono with red and blue checks and patterns, a big blue bow, one white and one black thigh-high and sandals.
- **Streetwear** (gallery 04): a holographic cropped jacket over a white crop top, black cargo trousers with straps, a knee pad, fishnets and chunky sneakers.
- **Black-and-red coat outfit** (gallery 05): a white peaked cap, an eye patch, an oversized black-and-red coat with an armband, black shorts and mismatched thigh-high boots.
- **Strawberry onesie** (gallery 06): a red strawberry-print hooded onesie with mouse ears and leaves, barefoot.
- **Edgy casual** (gallery 07): hair loose, earrings, a white cropped jacket over a black top, baggy white trousers with chains, a fishnet leg and black platform boots.
````

**[SW] Physical Description (what Sudowrite receives):**

````text
Bae's avatar is 149 cm tall, with bright red hair in two big pigtails and a white streak in the left bang, large pink mouse ears and a long thin tail tied with a blue ribbon; her little red-and-teal mouse mascot, Mr. Squeaks, rides on her head. She wears an off-shoulder white crop top reading "RAT," one red and one yellow oversized sleeve ending in teal paw mitts, a black, white and red panel skirt, mismatched legwear (a yellow-and-black stocking, a red sock), black platform shoes and a yellow "Chaos Toy" side bag. Other outfits in the official gallery: Kimono (2022): flowers in her hair, a short yellow kimono with red and blue checks and patterns, a big blue bow; Streetwear: a holographic cropped jacket over a white crop top, black cargo trousers with straps, a knee pad; Black-and-red coat outfit: a white peaked cap, an eye patch, an oversized black-and-red coat with an armband; Strawberry onesie: a red strawberry-print hooded onesie with mouse ears and leaves, barefoot; Edgy casual: hair loose, earrings, a white cropped jacket over a black top.
````

### Shiori Novella (`bible/characters/Shiori-Novella.md`)

**Official gallery images (open these to check the descriptions):**
- gallery 01: https://hololive.hololivepro.com/wp-content/uploads/2021/07/Shiori-Novella_pr-img_01.webp
- gallery 02: https://hololive.hololivepro.com/wp-content/uploads/2021/07/Shiori-Novella_pr-img_02.webp
- gallery 03: https://hololive.hololivepro.com/wp-content/uploads/2021/07/Shiori-Novella_pr-img_03.webp
- gallery 04: https://hololive.hololivepro.com/wp-content/uploads/2021/07/Shiori-Novella_pr-img_04.webp
- gallery 05: https://hololive.hololivepro.com/wp-content/uploads/2021/07/Shiori-Novella_pr-img_05.webp
- gallery 06: https://hololive.hololivepro.com/wp-content/uploads/2021/07/Shiori-Novella_pr-img_06.webp

**Dossier outfit section:**

````markdown
### Outfits in the official profile gallery (checked 2026-11-27)
Claude's reading of the gallery images on https://hololive.hololivepro.com/en/talents/shiori-novella/ (6 images (01 and 02 show the same original outfit)). Labels are descriptive
unless a date and its source are given; the gallery may not include every seasonal outfit shown only on stream.

- **Original outfit** (gallery 01-02): hair split white and black with a hash-mark clip, a black fur-trimmed jacket lined in purple whose hem drips like ink, a black corset dress with white lacing over a grey ruffled skirt, a striped thigh-high and spiked black platform boots.
- **Kimono** (gallery 03): hair up with a pink flower and black ornaments, a grey kimono with red and black peonies, a black fur stole, a giant calligraphy brush and frilled black platform sandals.
- **Red gothic outfit** (gallery 04): a black newsboy cap, a black capelet over a red-and-black strapped corset dress, patterned thigh-highs, fingerless gloves and black shoes.
- **Sleepwear** (gallery 05): braids under a pink frilled bonnet, a sheer pink nightgown and robe, white stockings and spiky black slippers.
- **Monster Hunter collaboration outfit (©CAPCOM)** (gallery 06): a short bob, a black high-collared dress with red accents, dark-blue scaled armor on her arms and legs and a bandaged thigh.
````

**[SW] Physical Description (what Sudowrite receives):**

````text
Shiori's avatar is 163 cm tall, with mid-length two-tone hair, black on one side and white on the other, held by sharp shuriken-like hairpins, and bright, glowing light-yellow eyes. She wears a dark purple and black jacket over a dress with "dripping" edges, long fingerless gloves and two rings on each hand. Yorick, a small, sad black sphere with long arms and four spikes on its head, rides on her right shoulder. Other outfits in the official gallery: Kimono: hair up with a pink flower and black ornaments, a grey kimono with red and black peonies, a black fur stole; Red gothic outfit: a black newsboy cap, a black capelet over a red-and-black strapped corset dress, patterned thigh-highs; Sleepwear: braids under a pink frilled bonnet, a sheer pink nightgown and robe, white stockings and spiky black slippers; Monster Hunter collaboration outfit: a short bob, a black high-collared dress with red accents, dark-blue scaled armor on her arms and legs and a bandaged thigh.
````

### Koseki Bijou (`bible/characters/Koseki-Bijou.md`)

**Official gallery images (open these to check the descriptions):**
- gallery 01: https://hololive.hololivepro.com/wp-content/uploads/2021/07/Koseki-Bijou_pr-img_01.webp
- gallery 02: https://hololive.hololivepro.com/wp-content/uploads/2021/07/Koseki-Bijou_pr-img_02.webp
- gallery 03: https://hololive.hololivepro.com/wp-content/uploads/2021/07/Koseki-Bijou_pr-img_03.webp
- gallery 04: https://hololive.hololivepro.com/wp-content/uploads/2021/07/Koseki-Bijou_pr-img_04.webp
- gallery 05: https://hololive.hololivepro.com/wp-content/uploads/2021/07/Koseki-Bijou_pr-img_05.webp
- gallery 06: https://hololive.hololivepro.com/wp-content/uploads/2021/07/Koseki-Bijou_pr-img_06.webp
- gallery 07: https://hololive.hololivepro.com/wp-content/uploads/2021/07/Koseki-Bijou_pr-img_07.webp

**Dossier outfit section:**

````markdown
### Outfits in the official profile gallery (checked 2026-11-27)
Claude's reading of the gallery images on https://hololive.hololivepro.com/en/talents/koseki-bijou/ (7 images (01 and 02 show the same original outfit)). Labels are descriptive
unless a date and its source are given; the gallery may not include every seasonal outfit shown only on stream.

- **Original outfit** (gallery 01-02): long lavender-grey hair with pink underneath, a gem tiara, filigree crystal wings, a white strapless dress with a dark red jeweled corset bodice, crystal boots and floating crystals.
- **Kimono-lolita outfit** (gallery 03): a purple flowered bonnet, braids with black bows, a lavender kimono printed with butterflies and roses with a frilled hem, and boots.
- **Streetwear** (gallery 04): a short bob with a patch on one cheek, an iridescent purple oversized jacket over a black crop top, a black pleated skirt with a garter, one leg warmer and purple sneakers.
- **Sleepwear** (gallery 05): a sleep mask with drawn eyes pushed up, an oversized white T-shirt with a doodle and the words "Don't talk to me, I'm sad," striped pink socks and purple slippers with eyes.
- **Monster Hunter collaboration outfit (©CAPCOM)** (gallery 06): a horned headdress, a purple-and-black demonic dress with spiked gauntlets, torn tights, laced thigh-high boots and torn purple trailing panels.
- **School outfit** (gallery 07): a high ponytail with a black bow, a black cardigan with red ribbons and patches over a white sailor uniform with a red bow, white leg warmers, a thigh strap and red loafers.
````

**[SW] Physical Description (what Sudowrite receives):**

````text
Bijou's avatar is 140 cm tall, with long silvery-purple hair, darker purple eyes and a dark purple crown. Metallic pink wings rise from her back, and purple gemstones grow on her body: a large jewel on her chest that changes color with her mood (blue when sad, rainbow when happy), small gems under her right eye and on the backs of her hands. Her feet are encased in gemstone shoes. Her avatar imagery includes floating crystals and a katana; crystal-to-weapon transformations belong to her lore and visual effects. Her small rabbit-like mascot GEOW has a jewel on its forehead. Other outfits in the official gallery: Kimono-lolita outfit: a purple flowered bonnet, braids with black bows, a lavender kimono printed with butterflies and roses with a frilled hem; Streetwear: a short bob with a patch on one cheek, an iridescent purple oversized jacket over a black crop top, a black pleated skirt with a garter; Sleepwear: a sleep mask with drawn eyes pushed up, an oversized white T-shirt with a doodle and the words "Don't talk to me, I'm sad; Monster Hunter collaboration outfit: a horned headdress, a purple-and-black demonic dress with spiked gauntlets, torn tights; School outfit: a high ponytail with a black bow, a black cardigan with red ribbons and patches over a white sailor uniform with a red bow, white leg warmers.
````

### Nerissa Ravencroft (`bible/characters/Nerissa-Ravencroft.md`)

**Official gallery images (open these to check the descriptions):**
- gallery 01: https://hololive.hololivepro.com/wp-content/uploads/2021/07/Nerissa-Ravencroft_pr-img_01.webp
- gallery 02: https://hololive.hololivepro.com/wp-content/uploads/2021/07/Nerissa-Ravencroft_pr-img_02.webp
- gallery 03: https://hololive.hololivepro.com/wp-content/uploads/2021/07/Nerissa-Ravencroft_pr-img_03.webp
- gallery 04: https://hololive.hololivepro.com/wp-content/uploads/2021/07/Nerissa-Ravencroft_pr-img_04.webp
- gallery 05: https://hololive.hololivepro.com/wp-content/uploads/2021/07/Nerissa-Ravencroft_pr-img_05.webp
- gallery 06: https://hololive.hololivepro.com/wp-content/uploads/2021/07/Nerissa-Ravencroft_pr-img_06.webp

**Dossier outfit section:**

````markdown
### Outfits in the official profile gallery (checked 2026-11-27)
Claude's reading of the gallery images on https://hololive.hololivepro.com/en/talents/nerissa-ravencroft/ (6 images (01 and 02 show the same original outfit)). Labels are descriptive
unless a date and its source are given; the gallery may not include every seasonal outfit shown only on stream.

- **Original outfit** (gallery 01-02): long black hair with blue streaks, a dark horn with feathers, black raven wings, a white striped shirt with a black tie under a belted black corset and skirt, feather-trimmed black sleeves, garters, heeled black thigh-high boots and a long forked staff.
- **Kimono** (gallery 03): a blue paper umbrella hung with wisteria, a black kimono with blue cranes and flowers, a white fur collar, trailing feathers and sandals.
- **Office outfit** (gallery 04): glasses, a plaid scarf, a navy coat over a white blouse, a black pencil skirt, black tights and heels.
- **Sleepwear** (gallery 05): a white-and-lavender babydoll nightdress with a ribbon and slippers with faces.
- **Summer outfit** (gallery 06): a long side braid, a white cropped jacket over a blue bikini top, a frilled plaid wrap skirt, a beaded thigh garter and sandals.
````

**[SW] Physical Description (what Sudowrite receives):**

````text
Nerissa's avatar is 175 cm tall, the tallest in hololive (197 cm counting heels and horns): long straight black hair with a blue inner layer and silver and gold ornaments, light purple eyes with a beauty mark under the left eye, and two horns layered black over blue, shaped like musical notes near the base and decorated with black flowers; one horn is broken. She wears a striped off-shoulder white shirt with a black bow and ruffled collar, feather-edged black sleeves and gloves, a layered sleeveless coat with three crossed belts, and asymmetrical high boots. Her staff is a giant flower-decorated tuning fork that can become a microphone, and her raven mascot Shadow can perch on her right shoulder. Other outfits in the official gallery: Kimono: a blue paper umbrella hung with wisteria, a black kimono with blue cranes and flowers, a white fur collar; Office outfit: glasses, a plaid scarf, a navy coat over a white blouse; Sleepwear: a white-and-lavender babydoll nightdress with a ribbon and slippers with faces; Summer outfit: a long side braid, a white cropped jacket over a blue bikini top, a frilled plaid wrap skirt.
````

### Fuwawa Abyssgard (`bible/characters/Fuwawa-Abyssgard.md`)

**Official gallery images (open these to check the descriptions):**
- gallery 01: https://hololive.hololivepro.com/wp-content/uploads/2021/07/Fuwawa-Abyssgard_pr-img_01.webp
- gallery 02: https://hololive.hololivepro.com/wp-content/uploads/2021/07/Fuwawa-Abyssgard_pr-img_02.webp
- gallery 03: https://hololive.hololivepro.com/wp-content/uploads/2021/07/Fuwawa-Abyssgard_pr-img_03.webp
- gallery 04: https://hololive.hololivepro.com/wp-content/uploads/2021/07/Fuwawa-Abyssgard_pr-img_04.webp
- gallery 05: https://hololive.hololivepro.com/wp-content/uploads/2021/07/Fuwawa-Abyssgard_pr-img_05.webp

**Dossier outfit section:**

````markdown
### Outfits in the official profile gallery (checked 2026-11-27)
Claude's reading of the gallery images on https://hololive.hololivepro.com/en/talents/fuwawa-abyssgard/ (5 images (01 and 02 show the same original outfit)). Labels are descriptive
unless a date and its source are given; the gallery may not include every seasonal outfit shown only on stream.

- **Original outfit** (gallery 01-02): blonde hair with blue streaks, blue-tipped dog ears, a blue hairband with clips, a black spiked collar with a chain, a white frilled dress, a cropped black jacket with blue flame patterns and blue claws, a blue belt, one fishnet thigh-high, chunky blue-and-white sneakers and a fluffy cream tail.
- **Kimono-style outfit** (gallery 03): hair up with a purple flower and blue ornaments, a one-sleeved blue floral kimono top over a white skirt, a big black-and-blue obi bow, paw gloves and fluffy paw boots.
- **Casual outfit** (gallery 04): wavy hair with black bows, a blue cropped cardigan with cut-out sleeves over a light-blue checked top, a white skirt, a small white dog bag, white thigh-highs and black heels.
- **Loungewear** (gallery 05): a fluffy light-blue hoodie with pom-pom strings, white stockings and light-blue slippers.
````

**[SW] Physical Description (what Sudowrite receives):**

````text
Fuwawa's avatar is 155 cm tall, with long blonde hair streaked light blue and gathered in small side pigtails, bright pink eyes, fluffy dog ears and a collar. She wears a pastel-blue headband and hairclips, one shaped like a white bandage with a blue center that mirrors her twin's pink one. Blue is always her color, so people can tell her from Mococo, who is otherwise her identical twin. Pero, "The Great Perroccino," their small, muscular fictional dog mascot, appears in their bits. Other outfits in the official gallery: Kimono-style outfit: hair up with a purple flower and blue ornaments, a one-sleeved blue floral kimono top over a white skirt, a big black-and-blue obi bow; Casual outfit: wavy hair with black bows, a blue cropped cardigan with cut-out sleeves over a light-blue checked top, a white skirt; Loungewear: a fluffy light-blue hoodie with pom-pom strings, white stockings and light-blue slippers.
````

### Mococo Abyssgard (`bible/characters/Mococo-Abyssgard.md`)

**Official gallery images (open these to check the descriptions):**
- gallery 01: https://hololive.hololivepro.com/wp-content/uploads/2021/07/Mococo-Abyssgard_pr-img_01.webp
- gallery 02: https://hololive.hololivepro.com/wp-content/uploads/2021/07/Mococo-Abyssgard_pr-img_02.webp
- gallery 03: https://hololive.hololivepro.com/wp-content/uploads/2021/07/Mococo-Abyssgard_pr-img_03.webp
- gallery 04: https://hololive.hololivepro.com/wp-content/uploads/2021/07/Mococo-Abyssgard_pr-img_04.webp
- gallery 05: https://hololive.hololivepro.com/wp-content/uploads/2021/07/Mococo-Abyssgard_pr-img_05.webp

**Dossier outfit section:**

````markdown
### Outfits in the official profile gallery (checked 2026-11-27)
Claude's reading of the gallery images on https://hololive.hololivepro.com/en/talents/mococo-abyssgard/ (5 images (01 and 02 show the same original outfit)). Labels are descriptive
unless a date and its source are given; the gallery may not include every seasonal outfit shown only on stream.

- **Original outfit** (gallery 01-02): blonde hair with pink streaks, pink-tipped dog ears, a pink hairband with clips, headphones around her neck, a cropped black jacket with pink flame patterns and pink claws over a white top, a pink belt, frilled white shorts, fishnet knee socks, chunky pink-and-white sneakers and a fluffy cream tail.
- **Kimono-style outfit** (gallery 03): hair up with pink flowers, a one-sleeved pink floral kimono top, a big purple obi bow, a garter, paw gloves and fluffy paw boots.
- **Casual outfit** (gallery 04): a pink jacket with bows over a white crop top printed with her name, a denim skirt, mismatched white and pink-striped socks and blue boots.
- **Loungewear** (gallery 05): a pink sleep mask pushed up, a sheer pink hoodie over a pink camisole with bows, white shorts, leg warmers and pink slippers.
````

**[SW] Physical Description (what Sudowrite receives):**

````text
Mococo's avatar is 155 cm tall, with short blonde hair streaked pink, pointed dog ears with white tufts and a collar. She wears a black and pink jacket and headphones, with light-pink X-shaped hairpins and a white-and-pink bandage clip that mirrors her twin's blue one. Pink is always her color, so people can tell her from Fuwawa, who is otherwise her identical twin. Pero, "The Great Perroccino," their small, muscular fictional dog mascot, appears in their bits. Other outfits in the official gallery: Kimono-style outfit: hair up with pink flowers, a one-sleeved pink floral kimono top, a big purple obi bow; Casual outfit: a pink jacket with bows over a white crop top printed with her name, a denim skirt, mismatched white and pink-striped socks and blue boots; Loungewear: a pink sleep mask pushed up, a sheer pink hoodie over a pink camisole with bows, white shorts.
````

### Elizabeth Rose Bloodflame (`bible/characters/Elizabeth-Rose-Bloodflame.md`)

**Official gallery images (open these to check the descriptions):**
- gallery 01: https://hololive.hololivepro.com/wp-content/uploads/2023/07/Elizabeth-Rose-Bloodflame_pr-img_01.webp
- gallery 02: https://hololive.hololivepro.com/wp-content/uploads/2023/07/Elizabeth-Rose-Bloodflame_pr-img_02.webp
- gallery 03: https://hololive.hololivepro.com/wp-content/uploads/2023/07/Elizabeth-Rose-Bloodflame_pr-img_03.webp
- gallery 04: https://hololive.hololivepro.com/wp-content/uploads/2023/07/Elizabeth-Rose-Bloodflame_pr-img_04.webp

**Dossier outfit section:**

````markdown
### Outfits in the official profile gallery (checked 2026-11-27)
Claude's reading of the gallery images on https://hololive.hololivepro.com/en/talents/elizabeth-rose-bloodflame/ (4 images (01 and 02 show the same original outfit)). Labels are descriptive
unless a date and its source are given; the gallery may not include every seasonal outfit shown only on stream.

- **Original outfit** (gallery 01-02): very long red hair with an ahoge, a blue flame gem at her chest, a white armored bodice with black accents and belts, a black skirt, a white coat of flowing cut-out panels edged in lace, white thigh-high heeled boots and a huge black-and-red executioner's sword.
- **Kimono** (gallery 03): hair up with blue roses, a red-and-navy kimono with blue roses and lace worn over a white off-shoulder top, long black gloves, a big red obi bow, a long frilled trailing hem and sandals.
- **Loungewear** (gallery 04): a pink bunny-ear hood topped with a cake, round glasses, a pink oversized cardigan, leg warmers, fluffy slippers and a game controller in her hands.
````

**[SW] Physical Description (what Sudowrite receives):**

````text
Elizabeth's avatar is 171 cm tall, the tallest of Justice, with red eyes, long red hair tinted blue underneath and a long ahoge. She wears a black and white outfit fastened with belts, red pauldrons and removable sleeves, and carries a black-and-red sword engraved with the scales of justice. A blue flame effect sits on her chest and can flare. Other outfits in the official gallery: Kimono: hair up with blue roses, a red-and-navy kimono with blue roses and lace worn over a white off-shoulder top, long black gloves; Loungewear: a pink bunny-ear hood topped with a cake, round glasses, a pink oversized cardigan.
````

### Gigi Murin (`bible/characters/Gigi-Murin.md`)

**Official gallery images (open these to check the descriptions):**
- gallery 01: https://hololive.hololivepro.com/wp-content/uploads/2023/07/Gigi-Murin_pr-img_01.webp
- gallery 02: https://hololive.hololivepro.com/wp-content/uploads/2023/07/Gigi-Murin_pr-img_02.webp
- gallery 03: https://hololive.hololivepro.com/wp-content/uploads/2023/07/Gigi-Murin_pr-img_03.webp
- gallery 04: https://hololive.hololivepro.com/wp-content/uploads/2023/07/Gigi-Murin_pr-img_04.webp
- gallery 05: https://hololive.hololivepro.com/wp-content/uploads/2023/07/Gigi-Murin_pr-img_05.webp

**Dossier outfit section:**

````markdown
### Outfits in the official profile gallery (checked 2026-11-27)
Claude's reading of the gallery images on https://hololive.hololivepro.com/en/talents/gigi-murin/ (5 images (01 and 02 show the same original outfit)). Labels are descriptive
unless a date and its source are given; the gallery may not include every seasonal outfit shown only on stream.

- **Original outfit** (gallery 01-02): twin tails under an orange monster hood marked with an X, fangs, an oversized orange jacket over a white top with a red scarf, black bike shorts, one orange-and-black striped stocking, red-and-white sneakers with paw soles, a long black tail with a round orange-and-white tip, giant mechanical gauntlets and a little green gremlin mascot.
- **New Year outfit (#GigiNewYear, 2025-01-01)** (gallery 03): a red flower in her hair, a white kimono top with orange and red flowers, a yellow pleated skirt with red ropes, fingerless gloves, bandages and white sandals.
- **Monster Hunter collaboration outfit (©CAPCOM)** (gallery 04): heart-shaped goggles on her head, a green-and-white patterned cropped jacket over a black top, white shorts with a belt, brown gloves, green thigh-highs and chunky boots.
- **Orange-and-navy outfit** (gallery 05): sunglasses, an oversized orange-and-navy jacket with a red cord knot, a small pouch, one orange stocking and sneakers.
````

**[SW] Physical Description (what Sudowrite receives):**

````text
Gigi's avatar is 153 cm tall, with pink eyes, sharp teeth and two-tone light-and-dark brown hair in bunches, a tall ahoge sticking out of her hood. She wears a bright orange hoodie decorated with fans, whose X-shaped eye blinks when she blinks, black cycle shorts and a single striped orange-and-black knee sock. Her lore weapons are huge gauntlets. Her mascot Popo, a small green kakapo with a propeller-like ahoge, often appears with her. Other outfits in the official gallery: New Year outfit (2025): a red flower in her hair, a white kimono top with orange and red flowers, a yellow pleated skirt with red ropes; Monster Hunter collaboration outfit: heart-shaped goggles on her head, a green-and-white patterned cropped jacket over a black top, white shorts with a belt; Orange-and-navy outfit: sunglasses, an oversized orange-and-navy jacket with a red cord knot, a small pouch.
````

### Cecilia Immergreen (`bible/characters/Cecilia-Immergreen.md`)

**Official gallery images (open these to check the descriptions):**
- gallery 01: https://hololive.hololivepro.com/wp-content/uploads/2023/07/Cecilia-Immergreen_pr-img_01.webp
- gallery 02: https://hololive.hololivepro.com/wp-content/uploads/2023/07/Cecilia-Immergreen_pr-img_02.webp
- gallery 03: https://hololive.hololivepro.com/wp-content/uploads/2023/07/Cecilia-Immergreen_pr-img_03.webp
- gallery 04: https://hololive.hololivepro.com/wp-content/uploads/2023/07/Cecilia-Immergreen_pr-img_04.webp

**Dossier outfit section:**

````markdown
### Outfits in the official profile gallery (checked 2026-11-27)
Claude's reading of the gallery images on https://hololive.hololivepro.com/en/talents/cecilia-immergreen/ (4 images (01 and 02 show the same original outfit)). Labels are descriptive
unless a date and its source are given; the gallery may not include every seasonal outfit shown only on stream.

- **Original outfit** (gallery 01-02): short silver hair with green streaks, a wind-up key on her head, doll joints, a white off-shoulder blouse with a red cravat, a green corset dress with gold gears and red gems, a gilded ring cage around the skirt with a musical staff, heeled boots and a spear with a glowing green tip.
- **Kimono** (gallery 03): a white lace parasol, a green-and-white harlequin kimono with roses and gears, a frilled white underskirt and white boots.
- **Casual outfit** (gallery 04): long hair, rose-tinted glasses, a black cropped jacket and top, a black-and-green frilled skirt, black tights with green ribbons, black flats with green bows and a black heart-shaped bag.
````

**[SW] Physical Description (what Sudowrite receives):**

````text
Cecilia's avatar is 162 cm tall: a clockwork automaton maiden with doll joints, green eyes and pale white-green neck-length hair, and a brass ribbon and wind-up key on her head; the key spins as an avatar effect when she is excited or thinking hard. She wears a gold-trimmed off-shoulder dress with a red neckerchief, a green skirt patterned with musical notes and clockwork, and ancient-looking sandals. She carries a white lance that transforms into a violin. Other outfits in the official gallery: Kimono: a white lace parasol, a green-and-white harlequin kimono with roses and gears, a frilled white underskirt and white boots; Casual outfit: long hair, rose-tinted glasses, a black cropped jacket and top.
````

### Raora Panthera (`bible/characters/Raora-Panthera.md`)

**Official gallery images (open these to check the descriptions):**
- gallery 01: https://hololive.hololivepro.com/wp-content/uploads/2023/07/Raora-Panthera_pr-img_01.webp
- gallery 02: https://hololive.hololivepro.com/wp-content/uploads/2023/07/Raora-Panthera_pr-img_02.webp
- gallery 03: https://hololive.hololivepro.com/wp-content/uploads/2023/07/Raora-Panthera_pr-img_03.webp
- gallery 04: https://hololive.hololivepro.com/wp-content/uploads/2023/07/Raora-Panthera_pr-img_04.webp
- gallery 05: https://hololive.hololivepro.com/wp-content/uploads/2023/07/Raora-Panthera_pr-img_05.webp

**Dossier outfit section:**

````markdown
### Outfits in the official profile gallery (checked 2026-11-27)
Claude's reading of the gallery images on https://hololive.hololivepro.com/en/talents/raora-panthera/ (5 images (01 and 02 show the same original outfit)). Labels are descriptive
unless a date and its source are given; the gallery may not include every seasonal outfit shown only on stream.

- **Original outfit** (gallery 01-02): long pink hair with a white streak, panther ears, goggles on a black cap, a white-and-black bodysuit with red accents under an oversized magenta-and-white coat trailing black straps, garters, white thigh-highs, white heeled ankle boots, a spotted pink tail, a drawing pen and a little blue mascot plush.
- **Kimono** (gallery 03): a fox mask on her head, twin tails, an off-shoulder white kimono with pink and gold patterns, a white fur stole, a blue flower obi ornament and sandals.
- **Monster Hunter collaboration outfit (©CAPCOM)** (gallery 04): a maid headdress, a white-and-black maid dress with red armored sleeves, tan cloth panels with heart designs, black tights and red armored boots.
- **School outfit** (gallery 05): glasses, very long braids tied with pink ribbons, a navy cardigan over a white shirt with a red bow, a blue plaid skirt, a thigh garter, leg warmers and loafers.
````

**[SW] Physical Description (what Sudowrite receives):**

````text
Raora's avatar is 155 cm tall, with long pink hair streaked white, pink cat ears, a long fuzzy tail, tiny fangs and yellow eyes; an aquamarine eye-glow effect marks her performed God Eyes bit. She wears a white-and-black outfit under a pink off-shoulder coat with a gap for her tail, white stockings, a round black hat, silver-tinted goggles on her head, an artist's glove on her right hand and an amulet with a blue gem. Other outfits in the official gallery: Kimono: a fox mask on her head, twin tails, an off-shoulder white kimono with pink and gold patterns; Monster Hunter collaboration outfit: a maid headdress, a white-and-black maid dress with red armored sleeves, tan cloth panels with heart designs; School outfit: glasses, very long braids tied with pink ribbons, a navy cardigan over a white shirt with a red bow.
````

### Hoshimachi Suisei (`bible/characters/Hoshimachi-Suisei.md`)

**Official gallery images (open these to check the descriptions):**
- gallery 01: https://hololive.hololivepro.com/wp-content/uploads/2020/06/Hoshimachi-Suisei_pr-img_01.png
- gallery 02: https://hololive.hololivepro.com/wp-content/uploads/2020/06/Hoshimachi-Suisei_pr-img_02.png
- gallery 03: https://hololive.hololivepro.com/wp-content/uploads/2020/06/Hoshimachi-Suisei_pr-img_03.png
- gallery 04: https://hololive.hololivepro.com/wp-content/uploads/2020/06/Hoshimachi-Suisei_pr-img_04.png
- gallery 05: https://hololive.hololivepro.com/wp-content/uploads/2020/06/Hoshimachi-Suisei_pr-img_05.png
- gallery 06: https://hololive.hololivepro.com/wp-content/uploads/2020/06/Hoshimachi-Suisei_pr-img_06.png
- gallery 07: https://hololive.hololivepro.com/wp-content/uploads/2020/06/Hoshimachi-Suisei_pr-img_07.png
- gallery 08: https://hololive.hololivepro.com/wp-content/uploads/2020/06/Hoshimachi-Suisei_pr-img_08.png

**Dossier outfit section:**

````markdown
### Outfits in the official profile gallery (checked 2026-11-27)
Claude's reading of the gallery images on https://hololive.hololivepro.com/en/talents/hoshimachi-suisei/ (8 images (01 and 02 show the same main outfit)). Labels are descriptive
unless a date and its source are given; the gallery may not include every seasonal outfit shown only on stream.

- **Main idol outfit** (gallery 01-02): a side ponytail with a blue bow under a grey plaid beret with a small gold crown, a grey plaid jacket with gold buttons and a blue tie, a plaid skirt with a big blue bow and a starry navy train, one black thigh-high and one blue knee sock, navy boots and a microphone.
- **Japanese-modern outfit** (gallery 03): a side braid with a blue bow, a blue floral kimono jacket with a red obi and a gold sash, a navy pleated skirt with wave patterns, purple tights, fishnet gloves and navy lace-up boots.
- **Streetwear** (gallery 04): a black beret, a teal-and-black jacket with lettering over a black dress, a garter, orange tights, green bows and black boots.
- **School outfit** (gallery 05): a bun with a white ribbon, a grey cardigan with a blue rosette over a white sailor uniform and skirt, white socks and loafers.
- **Black dress** (gallery 06): a small black hat, a black dress with sheer sleeves, a gold belt and a frilled grey hem, fingerless gloves and black shoes.
- **Black dragon coat** (gallery 07): a black fedora with red trim, red sunglasses, a long black coat with gold dragon embroidery and red lining over a black-and-red dress with tassels, and red-and-black platform shoes.
- **Casual outfit** (gallery 08): a red cropped jacket with bows over a beige knit top with a bear, a brown plaid skirt, red socks and white boots.
````

**[SW] Physical Description (what Sudowrite receives):**

````text
Suisei's avatar is 160 cm tall, with light blue hair in a side ponytail tied with a dark striped blue ribbon, blue eyes, and a black plaid cap topped with a small crown. She wears a grey plaid dress uniform with a ruffled dark-blue skirt panel, asymmetrical socks and black shoes. Her mark is a comet (☄️). (On her 2026 arena tour she wears a separate costume: a blue crop top with white see-through sleeves and a frilled white skirt.) Other outfits in the official gallery: Japanese-modern outfit: a side braid with a blue bow, a blue floral kimono jacket with a red obi and a gold sash, a navy pleated skirt with wave patterns; Streetwear: a black beret, a teal-and-black jacket with lettering over a black dress, a garter; School outfit: a bun with a white ribbon, a grey cardigan with a blue rosette over a white sailor uniform and skirt, white socks and loafers; Black dress: a small black hat, a black dress with sheer sleeves, a gold belt and a frilled grey hem; Black dragon coat: a black fedora with red trim, red sunglasses, a long black coat with gold dragon embroidery and red lining over a black-and-red dress with tassels; Casual outfit: a red cropped jacket with bows over a beige knit top with a bear, a brown plaid skirt, red socks and white boots.
````

### AZKi (`bible/characters/AZKi.md`)

**Official gallery images (open these to check the descriptions):**
- gallery 01: https://hololive.hololivepro.com/wp-content/uploads/2020/06/AZKi_pr-img_01.webp
- gallery 02: https://hololive.hololivepro.com/wp-content/uploads/2020/06/AZKi_pr-img_02.webp
- gallery 03: https://hololive.hololivepro.com/wp-content/uploads/2020/06/AZKi_pr-img_03.webp
- gallery 04: https://hololive.hololivepro.com/wp-content/uploads/2020/06/AZKi_pr-img_04.webp
- gallery 05: https://hololive.hololivepro.com/wp-content/uploads/2020/06/AZKi_pr-img_05.webp

**Dossier outfit section:**

````markdown
### Outfits in the official profile gallery (checked 2026-11-27)
Claude's reading of the gallery images on https://hololive.hololivepro.com/en/talents/azki/ (5 images). Labels are descriptive
unless a date and its source are given; the gallery may not include every seasonal outfit shown only on stream.

- **White shirt-dress outfit (main image)** (gallery 01): long dark hair with pink inner streaks and a pink flower clip, a white high-low shirt dress under a beige asymmetric wrap jacket with black buttons and a belt, and black ankle boots.
- **Diva gown** (gallery 02): a tiara and a blue ribbon in a very long side ponytail, a white-and-blue gown with puffed blue sleeves and a starry navy high-low skirt, white gloves and white heels.
- **New Year outfit (official New Year visual, announced 2023-12-19)** (gallery 03): a short bob under a flowered pink beret, a pink floral kimono top with a fur collar, a navy hakama with gold lines and peonies, and brown lace-up boots.
- **Loungewear** (gallery 04): a pink knit hoodie with bear ears over a white dress, and white boots.
- **Little-devil outfit** (gallery 05): twin tails with red horns, bat wings and a devil tail, a sleeveless white shirt with a black tie, black shorts, a thigh strap, one fishnet sock and black platform boots.
````

**[SW] Physical Description (what Sudowrite receives):**

````text
AZKi's avatar is 158 cm tall, with long dark hair streaked and lined with pink, light purple eyes and a floral hairpin. She wears a long dress with a partly pink skirt and a light beige half jacket on one side, with dark boots trimmed with pink triangle zippers. Her fan mark is ⚒️, for her fans, the Pioneers. Other outfits in the official gallery: Diva gown: a tiara and a blue ribbon in a very long side ponytail, a white-and-blue gown with puffed blue sleeves and a starry navy high-low skirt, white gloves and white heels; New Year outfit (2023): a short bob under a flowered pink beret, a pink floral kimono top with a fur collar, a navy hakama with gold lines and peonies; Loungewear: a pink knit hoodie with bear ears over a white dress, white boots; Little-devil outfit: twin tails with red horns, bat wings and a devil tail, a sleeveless white shirt with a black tie.
````

### Nakiri Ayame (`bible/characters/Nakiri-Ayame.md`)

**Official gallery images (open these to check the descriptions):**
- gallery 01: https://hololive.hololivepro.com/wp-content/uploads/2020/06/Nakiri-Ayame_pr-img_01.webp
- gallery 02: https://hololive.hololivepro.com/wp-content/uploads/2020/06/Nakiri-Ayame_pr-img_02.webp
- gallery 03: https://hololive.hololivepro.com/wp-content/uploads/2020/06/Nakiri-Ayame_pr-img_03.webp
- gallery 04: https://hololive.hololivepro.com/wp-content/uploads/2020/06/Nakiri-Ayame_pr-img_04.webp
- gallery 05: https://hololive.hololivepro.com/wp-content/uploads/2020/06/Nakiri-Ayame_pr-img_05.webp
- gallery 06: https://hololive.hololivepro.com/wp-content/uploads/2020/06/Nakiri-Ayame_pr-img_06.webp
- gallery 07: https://hololive.hololivepro.com/wp-content/uploads/2020/06/Nakiri-Ayame_pr-img_07.webp
- gallery 08: https://hololive.hololivepro.com/wp-content/uploads/2020/06/Nakiri-Ayame_pr-img_08.webp
- gallery 09: https://hololive.hololivepro.com/wp-content/uploads/2020/06/Nakiri-Ayame_pr-img_09.webp
- gallery 10: https://hololive.hololivepro.com/wp-content/uploads/2020/06/Nakiri-Ayame_pr-img_10.webp

**Dossier outfit section:**

````markdown
### Outfits in the official profile gallery (checked 2026-11-27)
Claude's reading of the gallery images on https://hololive.hololivepro.com/en/talents/nakiri-ayame/ (10 images (01 and 02 show the same original outfit)). Labels are descriptive
unless a date and its source are given; the gallery may not include every seasonal outfit shown only on stream.

- **Original oni outfit** (gallery 01-02): long white hair with red tips, two small horns, a red flower and bells in her hair, a short black-and-red frilled kimono with a green obi and red bow, two katana, a red-and-white sacred rope, white thigh-highs tied with red ribbons, black sandals and blue will-o'-wisps.
- **Western-style outfit** (gallery 03): a black frilled headband, a white blouse with a blue bow, detached frilled sleeves, a black corset skirt over a pale pleated skirt, black socks and shoes.
- **Furisode** (gallery 04): a red flower ornament, a purple-and-red furisode with plum blossoms and flowers, a gold obi and geta.
- **Streetwear** (gallery 05): twin tails, an oversized black jacket with red lining and printed lettering, a white shirt with a black tie, a black pleated skirt, black thigh-highs and black shoes with red bows.
- **Shrine-maiden-style outfit** (gallery 06): twin buns, a red-and-white outfit with pink arrow-feather sleeves and pom-pom tassels, a red skirt, pink thigh-highs and will-o'-wisps.
- **Gold-accented kimono** (gallery 07): gold hair ornaments, a dark brown-and-red kimono top with a short red skirt, one long white patterned sleeve, gold accents, tassels and sandals.
- **White uniform** (gallery 08): a white beret, a white jacket dress with a red tie and gold buckles, a black gauntlet and black boots.
- **Pink idol kimono** (gallery 09): twin buns with red bows, a pink frilled kimono dress with a black corset obi and pink ribbons, tassels and black lace-up boots.
- **Tracksuit** (gallery 10): a red tracksuit over a white T-shirt printed かわ余 and slippers with oni faces.
````

**[SW] Physical Description (what Sudowrite receives):**

````text
Ayame's avatar is 152 cm tall, an oni girl with long, loose white hair tinted pink, white horns, reddish-pink eyes, bell-ribbon hair ornaments and a red oni mask. She wears a black kimono with red and gold accents and spider lilies at the hem, a green obi with a gold flower motif, a large red-and-white bow, long white stockings and zori, with two swords on her back: the black-handled "Rasetsu" and the red-handled "Asura." Other outfits in the official gallery: Western-style outfit: a black frilled headband, a white blouse with a blue bow, detached frilled sleeves; Furisode: a red flower ornament, a purple-and-red furisode with plum blossoms and flowers, a gold obi and geta; Streetwear: twin tails, an oversized black jacket with red lining and printed lettering, a white shirt with a black tie; Shrine-maiden-style outfit: twin buns, a red-and-white outfit with pink arrow-feather sleeves and pom-pom tassels, a red skirt; Gold-accented kimono: gold hair ornaments, a dark brown-and-red kimono top with a short red skirt, one long white patterned sleeve; White uniform: a white beret, a white jacket dress with a red tie and gold buckles, a black gauntlet and black boots; Pink idol kimono: twin buns with red bows, a pink frilled kimono dress with a black corset obi and pink ribbons, tassels and black lace-up boots; Tracksuit: a red tracksuit over a white T-shirt printed かわ余 and slippers with oni faces.
````

### Nekomata Okayu (`bible/characters/Nekomata-Okayu.md`)

**Official gallery images (open these to check the descriptions):**
- gallery 01: https://hololive.hololivepro.com/wp-content/uploads/2020/06/Nekomata-Okayu_pr-img_01.png
- gallery 02: https://hololive.hololivepro.com/wp-content/uploads/2020/06/Nekomata-Okayu_pr-img_02.png
- gallery 03: https://hololive.hololivepro.com/wp-content/uploads/2020/06/Nekomata-Okayu_pr-img_03.png
- gallery 04: https://hololive.hololivepro.com/wp-content/uploads/2020/06/Nekomata-Okayu_pr-img_04.png
- gallery 05: https://hololive.hololivepro.com/wp-content/uploads/2020/06/Nekomata-Okayu_pr-img_05.png
- gallery 06: https://hololive.hololivepro.com/wp-content/uploads/2020/06/Nekomata-Okayu_pr-img_06.png
- gallery 07: https://hololive.hololivepro.com/wp-content/uploads/2020/06/Nekomata-Okayu_pr-img_07.png
- gallery 08: https://hololive.hololivepro.com/wp-content/uploads/2020/06/Nekomata-Okayu_pr-img_08.png
- gallery 09: https://hololive.hololivepro.com/wp-content/uploads/2020/06/Nekomata-Okayu_pr-img_09.png

**Dossier outfit section:**

````markdown
### Outfits in the official profile gallery (checked 2026-11-27)
Claude's reading of the gallery images on https://hololive.hololivepro.com/en/talents/nekomata-okayu/ (9 images (01 and 02 show the same original outfit)). Labels are descriptive
unless a date and its source are given; the gallery may not include every seasonal outfit shown only on stream.

- **Original outfit** (gallery 01-02): lavender hair, cat ears and tail, a black collar with a bell, a grey-and-purple cropped hoodie with an onigiri emblem and black straps, baggy white trousers with purple stripes and yellow sneakers.
- **Kimono-maid outfit** (gallery 03): a purple-to-white kimono top with wide sleeves, a black obi, a white frilled apron with an onigiri patch, white socks and geta.
- **Sailor-style outfit** (gallery 04): a black headband, a dark purple sailor crop top with a white tie, white shorts, black knee socks and sneakers.
- **Loungewear** (gallery 05): glasses, an oversized white shirt under a dark grey cardigan, and slippers.
- **Card-suit coat outfit** (gallery 06): a black beret, a white blouse with a purple ribbon, a long black coat patterned with white card suits, black shorts, mismatched striped stockings with purple wraps and black shoes.
- **Green-and-purple outfit** (gallery 07): a black beret with a green rose, a green cropped jacket with one fishnet purple sleeve, a purple skirt, garters, mismatched purple and green thigh-highs and black lace-up boots with a yellow bow.
- **Techwear** (gallery 08): twin tails, an oversized black coat with teal straps over a short grey-and-black dress with plated panels, a thigh strap, grey stockings and shoes.
- **Punk outfit** (gallery 09): long hair, a sheer grey cut-out top over a purple top, grey denim shorts, one purple stocking printed with hearts and one fishnet, and black boots.
````

**[SW] Physical Description (what Sudowrite receives):**

````text
Okayu's avatar is 152 cm tall, a cat girl with medium-length light purple hair, purple cat ears and a tail, and bright purple eyes. She wears an off-black, purple-tinted hoodie and a black collar. Her emoji is a rice ball (🍙). Other outfits in the official gallery: Kimono-maid outfit: a purple-to-white kimono top with wide sleeves, a black obi, a white frilled apron with an onigiri patch; Sailor-style outfit: a black headband, a dark purple sailor crop top with a white tie, white shorts; Loungewear: glasses, an oversized white shirt under a dark grey cardigan, slippers; Card-suit coat outfit: a black beret, a white blouse with a purple ribbon, a long black coat patterned with white card suits; Green-and-purple outfit: a black beret with a green rose, a green cropped jacket with one fishnet purple sleeve, a purple skirt; Techwear: twin tails, an oversized black coat with teal straps over a short grey-and-black dress with plated panels, a thigh strap; Punk outfit: long hair, a sheer grey cut-out top over a purple top, grey denim shorts.
````

### Houshou Marine (`bible/characters/Houshou-Marine.md`)

**Official gallery images (open these to check the descriptions):**
- gallery 01: https://hololive.hololivepro.com/wp-content/uploads/2020/06/Houshou-Marine_pr-img_01.webp
- gallery 02: https://hololive.hololivepro.com/wp-content/uploads/2020/06/Houshou-Marine_pr-img_02.webp
- gallery 03: https://hololive.hololivepro.com/wp-content/uploads/2020/06/Houshou-Marine_pr-img_03.webp
- gallery 04: https://hololive.hololivepro.com/wp-content/uploads/2020/06/Houshou-Marine_pr-img_04.webp
- gallery 05: https://hololive.hololivepro.com/wp-content/uploads/2020/06/Houshou-Marine_pr-img_05.webp
- gallery 06: https://hololive.hololivepro.com/wp-content/uploads/2020/06/Houshou-Marine_pr-img_06.webp
- gallery 07: https://hololive.hololivepro.com/wp-content/uploads/2020/06/Houshou-Marine_pr-img_07.webp
- gallery 08: https://hololive.hololivepro.com/wp-content/uploads/2020/06/Houshou-Marine_pr-img_08.webp
- gallery 09: https://hololive.hololivepro.com/wp-content/uploads/2020/06/Houshou-Marine_pr-img_09.webp
- gallery 10: https://hololive.hololivepro.com/wp-content/uploads/2020/06/Houshou-Marine_pr-img_10.webp
- gallery 11: https://hololive.hololivepro.com/wp-content/uploads/2020/06/Houshou-Marine_pr-img_11.webp

**Dossier outfit section:**

````markdown
### Outfits in the official profile gallery (checked 2026-11-27)
Claude's reading of the gallery images on https://hololive.hololivepro.com/en/talents/houshou-marine/ (11 images (01 and 02 show the same original outfit)). Labels are descriptive
unless a date and its source are given; the gallery may not include every seasonal outfit shown only on stream.

- **Original pirate captain outfit** (gallery 01-02): a black gold-trimmed tricorn with a plume, an eyepatch, a red cropped vest with gold buttons and a red collar bow, a long black captain's coat with gold trim and anchor-badged red cuffs, a red pleated miniskirt, dark thigh-highs and heeled boots.
- **Kimono-style outfit** (gallery 03): a white bow and a purple flower in her hair, a white-and-purple kimono with wave patterns and gold tassels, a white fur collar, a high slit, dark stockings and geta.
- **Gothic lolita** (gallery 04): ringlet twin tails under a small black top hat with roses, an eyepatch, a red-and-black frilled dress with a clock emblem, black gloves, white tights and ribbon-laced shoes.
- **Casual outfit** (gallery 05): a ponytail, a black officer's cap with heart-shaped sunglasses, a black zip hoodie, white shorts, a thigh strap and strappy sandals.
- **Captain's dress uniform** (gallery 06): a tall black shako with a plume, a black uniform with red-and-gold trim, a black-and-red coat with gold panels and thigh-high boots.
- **Office outfit** (gallery 07): a navy beret, a navy fur-trimmed coat over a sheer black top, a black pencil skirt, an ID badge, tights and heels.
- **Loungewear** (gallery 08): a fluffy white bear-ear hoodie, leg warmers and bear slippers.
- **Nun outfit** (gallery 09): a black veil with curled horns, a black dress with gold patterns and white ruffled sleeves, garters, white thigh-highs and black heels.
- **Japanese-style idol outfit** (gallery 10): a white sailor cap with a red flower, twin tails, a white-and-red kimono-style top with sweeping printed sleeves, a red pleated skirt, leg warmers and black platform shoes.
- **Summer outfit** (gallery 11): twin buns with a visor, a red bikini under a white cropped track jacket printed MARINE, white shorts, a sheer pink wrap, a thigh pouch and sandals.
````

**[SW] Physical Description (what Sudowrite receives):**

````text
Marine's avatar is 150 cm tall, with crimson-red twintails tied with ribbons, a black gold-trimmed pirate hat with a plume, an eyepatch and heterochromatic gold and red eyes. She wears a red cropped vest with gold buttons and a red collar bow, a long black captain's coat with gold trim and anchor-badged red cuffs slung over her shoulders, a red pleated miniskirt, dark thigh-highs and red-and-brown heeled boots. Kumarine, a bear, is her mascot. Other outfits in the official gallery: Kimono-style outfit: a white bow and a purple flower in her hair, a white-and-purple kimono with wave patterns and gold tassels, a white fur collar; Gothic lolita: ringlet twin tails under a small black top hat with roses, an eyepatch, a red-and-black frilled dress with a clock emblem; Casual outfit: a ponytail, a black officer's cap with heart-shaped sunglasses, a black zip hoodie; Captain's dress uniform: a tall black shako with a plume, a black uniform with red-and-gold trim, a black-and-red coat with gold panels and thigh-high boots; Office outfit: a navy beret, a navy fur-trimmed coat over a sheer black top, a black pencil skirt; Loungewear: a fluffy white bear-ear hoodie, leg warmers and bear slippers; Nun outfit: a black veil with curled horns, a black dress with gold patterns and white ruffled sleeves, garters; Japanese-style idol outfit: a white sailor cap with a red flower, twin tails, a white-and-red kimono-style top with sweeping printed sleeves; Summer outfit: twin buns with a visor, a red bikini under a white cropped track jacket printed MARINE, white shorts.
````

### Shirogane Noel (`bible/characters/Shirogane-Noel.md`)

**Official gallery images (open these to check the descriptions):**
- gallery 01: https://hololive.hololivepro.com/wp-content/uploads/2020/06/Shirogane-Noel_pr-img_01.webp
- gallery 02: https://hololive.hololivepro.com/wp-content/uploads/2020/06/Shirogane-Noel_pr-img_02.webp
- gallery 03: https://hololive.hololivepro.com/wp-content/uploads/2020/06/Shirogane-Noel_pr-img_03.webp
- gallery 04: https://hololive.hololivepro.com/wp-content/uploads/2020/06/Shirogane-Noel_pr-img_04.webp
- gallery 05: https://hololive.hololivepro.com/wp-content/uploads/2020/06/Shirogane-Noel_pr-img_05.webp
- gallery 06: https://hololive.hololivepro.com/wp-content/uploads/2020/06/Shirogane-Noel_pr-img_06.webp
- gallery 07: https://hololive.hololivepro.com/wp-content/uploads/2020/06/Shirogane-Noel_pr-img_07.webp
- gallery 08: https://hololive.hololivepro.com/wp-content/uploads/2020/06/Shirogane-Noel_pr-img_08.webp
- gallery 09: https://hololive.hololivepro.com/wp-content/uploads/2020/06/Shirogane-Noel_pr-img_09.webp
- gallery 10: https://hololive.hololivepro.com/wp-content/uploads/2020/06/Shirogane-Noel_pr-img_10.webp

**Dossier outfit section:**

````markdown
### Outfits in the official profile gallery (checked 2026-11-27)
Claude's reading of the gallery images on https://hololive.hololivepro.com/en/talents/shirogane-noel/ (10 images (01 and 02 show the same original outfit)). Labels are descriptive
unless a date and its source are given; the gallery may not include every seasonal outfit shown only on stream.

- **Original knight outfit** (gallery 01-02): short silver hair with a braid and a black headband, black-and-gold plate on her shoulders and arms over a white-and-black outfit, a white surcoat with a black crest, belts, black armored boots and a mace.
- **Furisode** (gallery 03): a braid with a blue flower ornament, a blue kimono with white peonies and arrow-feather patterns, a pale obi and geta.
- **Casual outfit** (gallery 04): round glasses, a choker, a white peasant blouse with laced sleeves, a brown plaid skirt, a crossbody bag, black socks and brown shoes.
- **Waitress outfit** (gallery 05): long hair, a brown capelet with a bow over a white blouse, a corset with a frilled apron, white thigh-highs, a garter holster, red shoes and her mace on her back.
- **School outfit** (gallery 06): a navy blazer over a light-blue zip hoodie with a blue bow, a pleated skirt, white socks and loafers.
- **Ponytail stage outfit** (gallery 07): a high ponytail, a white-and-black halter top with belts and wide detached sleeves, black shorts with a garter and brown boots.
- **Dark knight outfit** (gallery 08): curved black horns on her headband, a black armored dress with gold trim, long black gloves, garters, black boots and a huge black spiked mace.
- **Loungewear** (gallery 09): round glasses, a low bun, a cream cardigan over a light-blue camisole and bloomers, leg warmers, slippers and a cat plush in her arms.
- **Bridal-style idol dress** (gallery 10): a tiara and long braided hair, a white-and-navy off-shoulder ruffled dress with star-tipped panels, white gloves, white thigh-highs and navy heels.
````

**[SW] Physical Description (what Sudowrite receives):**

````text
Noel's avatar is 158 cm tall, with shoulder-length silver hair, a braid, a black-and-gold metal headband and green eyes. She wears black, gold-edged armor on one shoulder and both arms, a long white surcoat with navy trim and a heraldic panel, leather belts and pouches, and armored steel boots, and carries a flanged mace. Other outfits in the official gallery: Furisode: a braid with a blue flower ornament, a blue kimono with white peonies and arrow-feather patterns, a pale obi and geta; Casual outfit: round glasses, a choker, a white peasant blouse with laced sleeves; Waitress outfit: long hair, a brown capelet with a bow over a white blouse, a corset with a frilled apron; School outfit: a navy blazer over a light-blue zip hoodie with a blue bow, a pleated skirt, white socks and loafers; Ponytail stage outfit: a high ponytail, a white-and-black halter top with belts and wide detached sleeves, black shorts with a garter and brown boots; Dark knight outfit: curved black horns on her headband, a black armored dress with gold trim, long black gloves; Loungewear: round glasses, a low bun, a cream cardigan over a light-blue camisole and bloomers; Bridal-style idol dress: a tiara and long braided hair, a white-and-navy off-shoulder ruffled dress with star-tipped panels, white gloves.
````

### Yukihana Lamy (`bible/characters/Yukihana-Lamy.md`)

**Official gallery images (open these to check the descriptions):**
- gallery 01: https://hololive.hololivepro.com/wp-content/uploads/2020/06/Yukihana-Lamy_pr-img_01.webp
- gallery 02: https://hololive.hololivepro.com/wp-content/uploads/2020/06/Yukihana-Lamy_pr-img_02.webp
- gallery 03: https://hololive.hololivepro.com/wp-content/uploads/2020/06/Yukihana-Lamy_pr-img_03.webp
- gallery 04: https://hololive.hololivepro.com/wp-content/uploads/2020/06/Yukihana-Lamy_pr-img_04.webp
- gallery 05: https://hololive.hololivepro.com/wp-content/uploads/2020/06/Yukihana-Lamy_pr-img_05.webp
- gallery 06: https://hololive.hololivepro.com/wp-content/uploads/2020/06/Yukihana-Lamy_pr-img_06.webp
- gallery 07: https://hololive.hololivepro.com/wp-content/uploads/2020/06/Yukihana-Lamy_pr-img_07.webp
- gallery 08: https://hololive.hololivepro.com/wp-content/uploads/2020/06/Yukihana-Lamy_pr-img_08.webp

**Dossier outfit section:**

````markdown
### Outfits in the official profile gallery (checked 2026-11-27)
Claude's reading of the gallery images on https://hololive.hololivepro.com/en/talents/yukihana-lamy/ (8 images (01 and 02 show the same original outfit)). Labels are descriptive
unless a date and its source are given; the gallery may not include every seasonal outfit shown only on stream.

- **Original outfit** (gallery 01-02): long light-blue hair with a heart-shaped ahoge, elf ears, a white beret with a flower and feathers, a white blouse with a blue ribbon, a dark corset with a belt, a white skirt with snowflake patterns, a long light-blue fur-trimmed coat, frilled white thigh-highs and brown boots.
- **Kimono and hakama** (gallery 03): a blue flower ornament, a blue-and-white floral kimono, a red obi with a big bow and sash, a navy hakama with pink blossoms and black boots.
- **Casual outfit** (gallery 04): twin tails with black ribbons, a white cardigan with a black bow over a frilled brown plaid dress, lace-trimmed white socks and white lace-up shoes.
- **Loungewear** (gallery 05): a fluffy blue-and-white striped hoodie with snow-sprite pockets over a pink camisole, and fluffy blue slippers.
- **Green cape outfit** (gallery 06): a high ponytail with a green ribbon, a short green caped jacket with gold trim over a white blouse with a black ribbon, a short skirt, white socks and platform sandals.
- **Streetwear** (gallery 07): twin tails under a black cat-ear cap printed LAMY, a black jacket with pink and blue straps, a white sports top with a choker, black shorts, thigh straps, one fishnet stocking and black boots.
- **Swimsuit** (gallery 08): hair loose, a light-blue frilled bikini with a sheer skirt, a leg garter and platform sandals.
````

**[SW] Physical Description (what Sudowrite receives):**

````text
Lamy's avatar is 158 cm tall, with long light-blue hair, a heart-shaped ahoge, small side braids, pointed elf ears and golden eyes, under a white beret with a blue snow flower. She wears a white blouse with a blue ribbon, a light-blue fur-trimmed coat patterned with snowflakes worn off the shoulders, a brown belt, a white skirt fading to blue, snow-patterned white thigh-highs and brown boots. Daifuku, a tiny polar-bear-like snow spirit in a pot, keeps her company. Other outfits in the official gallery: Kimono and hakama: a blue flower ornament, a blue-and-white floral kimono, a red obi with a big bow and sash; Casual outfit: twin tails with black ribbons, a white cardigan with a black bow over a frilled brown plaid dress, lace-trimmed white socks and white lace-up shoes; Loungewear: a fluffy blue-and-white striped hoodie with snow-sprite pockets over a pink camisole, fluffy blue slippers; Green cape outfit: a high ponytail with a green ribbon, a short green caped jacket with gold trim over a white blouse with a black ribbon, a short skirt; Streetwear: twin tails under a black cat-ear cap printed LAMY, a black jacket with pink and blue straps, a white sports top with a choker; Swimsuit: hair loose, a light-blue frilled bikini with a sheer skirt, a leg garter and platform sandals.
````

### Shishiro Botan (`bible/characters/Shishiro-Botan.md`)

**Official gallery images (open these to check the descriptions):**
- gallery 01: https://hololive.hololivepro.com/wp-content/uploads/2020/07/Shishiro-Botan_pr-img_01.webp
- gallery 02: https://hololive.hololivepro.com/wp-content/uploads/2020/07/Shishiro-Botan_pr-img_02.webp
- gallery 03: https://hololive.hololivepro.com/wp-content/uploads/2020/07/Shishiro-Botan_pr-img_03.webp
- gallery 04: https://hololive.hololivepro.com/wp-content/uploads/2020/07/Shishiro-Botan_pr-img_04.webp
- gallery 05: https://hololive.hololivepro.com/wp-content/uploads/2020/07/Shishiro-Botan_pr-img_05.webp
- gallery 06: https://hololive.hololivepro.com/wp-content/uploads/2020/07/Shishiro-Botan_pr-img_06.webp
- gallery 07: https://hololive.hololivepro.com/wp-content/uploads/2020/07/Shishiro-Botan_pr-img_07.webp
- gallery 08: https://hololive.hololivepro.com/wp-content/uploads/2020/07/Shishiro-Botan_pr-img_08.webp

**Dossier outfit section:**

````markdown
### Outfits in the official profile gallery (checked 2026-11-27)
Claude's reading of the gallery images on https://hololive.hololivepro.com/en/talents/shishiro-botan/ (8 images (01 and 02 show the same original outfit)). Labels are descriptive
unless a date and its source are given; the gallery may not include every seasonal outfit shown only on stream.

- **Original outfit** (gallery 01-02): long silver-white hair with lion ears and tail, a gold choker, a sheer black top with white stripes, an oversized fur-trimmed black jacket, a grey miniskirt with a lettered belt, torn black tights on one leg and heeled black ankle boots.
- **Kimono** (gallery 03): buns with red ornaments, a white kimono top with red-and-gold decorations and a long red sash, a short black lace skirt, white socks and tall geta.
- **Vest suit** (gallery 04): a white shirt with a loose tie, a black vest, black shorts with straps, grey tights and black boots.
- **Streetwear** (gallery 05): a black-and-grey hooded jacket with neon-green stripes over a white T-shirt, shorts, one grey leg warmer and black-and-neon sneakers.
- **White veil dress** (gallery 06): a white veil with blue flowers, a white dress with black lacing and ribbons, a white cape lined with starry blue, white thigh-highs and white heels.
- **Gothic outfit** (gallery 07): twin tails with black ribbons, a sleeveless burgundy blouse with a black bow, a black skirt, strapped thigh-high stockings and black boots.
- **Grey uniform** (gallery 08): a small black hat, a grey pinstripe jacket with white flower motifs and a belt, a white pleated skirt, tights and black loafers.
````

**[SW] Physical Description (what Sudowrite receives):**

````text
Botan's avatar is 166 cm tall, with long silver-white hair, lion ears and a lion's tail, and grey eyes. She wears a black sleeveless top with three white stripes, a black choker with a gold chain, an oversized black jacket with a fur-lined hood slipping off her shoulders, a grey miniskirt with a lettered belt, one torn black stocking and black heeled ankle boots. Fans call the sporty stripes her "Adidas Lion" look. Other outfits in the official gallery: Kimono: buns with red ornaments, a white kimono top with red-and-gold decorations and a long red sash, a short black lace skirt; Vest suit: a white shirt with a loose tie, a black vest, black shorts with straps; Streetwear: a black-and-grey hooded jacket with neon-green stripes over a white T-shirt, shorts, one grey leg warmer and black-and-neon sneakers; White veil dress: a white veil with blue flowers, a white dress with black lacing and ribbons, a white cape lined with starry blue; Gothic outfit: twin tails with black ribbons, a sleeveless burgundy blouse with a black bow, a black skirt; Grey uniform: a small black hat, a grey pinstripe jacket with white flower motifs and a belt, a white pleated skirt.
````

### Kikirara Vivi (`bible/characters/Kikirara-Vivi.md`)

**Official gallery images (open these to check the descriptions):**
- gallery 01a: https://hololive.hololivepro.com/wp-content/uploads/2023/09/Kikirara-Vivi_pr-img_01_a.webp
- gallery 01b: https://hololive.hololivepro.com/wp-content/uploads/2023/09/Kikirara-Vivi_pr-img_01_b.webp
- gallery 02: https://hololive.hololivepro.com/wp-content/uploads/2023/09/Kikirara-Vivi_pr-img_02.webp
- gallery 03: https://hololive.hololivepro.com/wp-content/uploads/2023/09/Kikirara-Vivi_pr-img_03.webp

**Dossier outfit section:**

````markdown
### Outfits in the official profile gallery (checked 2026-11-27)
Claude's reading of the gallery images on https://hololive.hololivepro.com/en/talents/kikirara-vivi/ (4 images (01_a and 02 show the same original outfit)). Labels are descriptive
unless a date and its source are given; the gallery may not include every seasonal outfit shown only on stream.

- **Original outfit** (gallery 01_a, 02): pink-to-purple twin tails with black sparkle bows, a cream off-shoulder top with oversized purple sleeves over a black crop top, a black heart-shaped bag full of makeup brushes, baggy purple cargo pants with one leg pulled up over patterned tights and black lace-up boots with pink laces.
- **Stage outfit** (gallery 01_b): a high ponytail with a black bow, a black-and-pink studded dress with a pink puffed jacket, a garter, one black patterned stocking and chunky black boots.
- **New Year outfit (revealed 2026-01-02, her first)** (gallery 03): a side bun with flowers, a black-and-purple kimono with star patterns and a big pink bow, a short pink pleated skirt underneath and black sandals.
````

**[SW] Physical Description (what Sudowrite receives):**

````text
Vivi's avatar is 161 cm tall, with long twin tails that fade from pink to purple, black sparkle-patterned bows and blue eyes. She wears a cream off-shoulder top with oversized purple sleeves over a black crop top, baggy purple cargo pants with one leg pulled up over patterned tights, black lace-up boots with pink laces, and a quilted black heart-shaped bag full of makeup brushes at her hip. Other outfits in the official gallery: New Year outfit (2026): a side bun with flowers, a black-and-purple kimono with star patterns and a big pink bow, a short pink pleated skirt underneath and black sandals.
````

### Isaki Riona (`bible/characters/Isaki-Riona.md`)

**Official gallery images (open these to check the descriptions):**
- gallery 01a: https://hololive.hololivepro.com/wp-content/uploads/2023/09/Isaki-Riona_pr-img_01_a.png
- gallery 01b: https://hololive.hololivepro.com/wp-content/uploads/2023/09/Isaki-Riona_pr-img_01_b.png
- gallery 02: https://hololive.hololivepro.com/wp-content/uploads/2023/09/Isaki-Riona_pr-img_02.png
- gallery 03: https://hololive.hololivepro.com/wp-content/uploads/2023/09/Isaki-Riona_pr-img_03.png

**Dossier outfit section:**

````markdown
## Appearance Anchors (avatar)
160 cm; illustrator Shirabii (しらび). Long silver-grey hair and crimson eyes. Emoji 🎤👑. The official profile
gallery (checked 2026-11-27) shows three outfits; descriptions are Claude's reading of those images:
- **Original outfit (debut, 2024-11):** hair in a high side ponytail tied with a black ribbon; a cropped black
  jacket with red lining worn off the shoulders; a white cropped top with chain details and a black choker; a black
  belt; black-and-white panelled flared trousers with knee cutouts; black lace-up boots with white toes; a pink
  microphone topped with a small crown. [Official RI1 gallery 01_a, 02]
- **Black-and-pink stage outfit:** twin tails tied with pink ribbons and a tiny black crown; a black-and-magenta
  corset top with chains and detached sleeves; a black pleated skirt layered with pink and white and a long pink
  sash; one fishnet leg with a ribbon garter and one striped sock; chunky black boots trimmed with pink fur.
  [Official RI1 gallery 01_b]
- **New Year outfit (revealed 2026-01-02, her first):** a pale-pink floral kimono-style dress that falls in
  ruffled tiers, with a big pink bow at the waist; hair braided into a side ponytail with a cream bow; white
  lace-up boots. The gallery image matches the silhouette in the reveal stream's thumbnail. [Official RI1 gallery
  03] [RI4 HTHdI209UXU]
````

**[SW] Physical Description (what Sudowrite receives):**

````text
Riona's avatar is 160 cm tall, with long silver-grey hair and crimson eyes. Original outfit: a high side ponytail tied with a black ribbon, a cropped black jacket with red lining worn off the shoulders over a white crop top with chains and a black choker, black-and-white panelled flared trousers with knee cutouts, black lace-up boots and a pink microphone topped with a small crown. Stage outfit: twin tails with pink ribbons and a tiny black crown, a black-and-magenta corset top with chains and detached sleeves, a layered black-and-pink pleated skirt with a long pink sash, one fishnet leg and one striped sock, and chunky black boots trimmed with pink fur. New Year outfit (2026): a pale-pink floral kimono-style dress in ruffled tiers with a big pink bow at the waist, her hair braided into a side ponytail with a cream bow, and white lace-up boots.
````

### Koganei Niko (`bible/characters/Koganei-Niko.md`)

**Official gallery images (open these to check the descriptions):**
- gallery 01a: https://hololive.hololivepro.com/wp-content/uploads/2023/09/Koganei-Niko_pr-img_01_a.png
- gallery 01b: https://hololive.hololivepro.com/wp-content/uploads/2023/09/Koganei-Niko_pr-img_01_b.png
- gallery 02: https://hololive.hololivepro.com/wp-content/uploads/2023/09/Koganei-Niko_pr-img_02.png
- gallery 03: https://hololive.hololivepro.com/wp-content/uploads/2023/09/Koganei-Niko_pr-img_03.png

**Dossier outfit section:**

````markdown
## Appearance Anchors (avatar)
172 cm; illustrator TETSUKAZU (鉄一). Long blonde hair with a black streak along the crown and green eyes. Emoji
☺️🐅. The official profile gallery (checked 2026-11-27) shows three outfits; descriptions are Claude's reading of
those images:
- **Original outfit (debut, 2024-11):** round orange-tinted glasses; an oversized dark-grey varsity jacket with
  beige sleeves, orange lining and embroidered tiger paws with green claws; a black crop top with a sheer mesh hem;
  light-grey ripped drawstring sweatpants; a long thin dark strap hanging behind her like a tail; patterned lace-up
  boots; rings on her fingers. [Official NK1 gallery 01_a, 02]
- **Tiger stage outfit:** a high blonde ponytail; a black zip-up crop top with orange-patterned mesh sleeves and
  long black gloves; a studded belt with a tiger-head buckle, chains and claw charms; a torn khaki wrap over flowing
  black trousers printed with orange tiger stripes and a tiger. [Official NK1 gallery 01_b]
- **Japanese-style outfit:** a short bob with two round buns like ears, sunglasses pushed up on her head; a black
  kimono-style robe embroidered with a tiger and waves, a beige tiger-striped shawl, a green jade pendant and chains;
  black platform boots. Its reveal stream is not in the archive checked. [Official NK1 gallery 03]
````

**[SW] Physical Description (what Sudowrite receives):**

````text
Niko's avatar is 172 cm tall, with long blonde hair with a black streak along the crown and green eyes. Original outfit: round orange-tinted glasses, an oversized dark-grey varsity jacket with beige sleeves, orange lining and embroidered tiger paws with green claws, a black crop top with a sheer mesh hem, light-grey ripped drawstring sweatpants, a long thin dark strap hanging behind her like a tail and patterned lace-up boots. Tiger stage outfit: a high ponytail, a black zip-up crop top with orange-patterned mesh sleeves and long black gloves, a studded tiger-head belt with chains and claw charms, and a torn khaki wrap over flowing black trousers printed with orange tiger stripes. Japanese-style outfit: a short bob with two round buns like ears and sunglasses pushed up, a black kimono-style robe embroidered with a tiger and waves, a beige tiger-striped shawl, a green jade pendant and black platform boots.
````

### Mizumiya Su (`bible/characters/Mizumiya-Su.md`)

**Official gallery images (open these to check the descriptions):**
- gallery 01a: https://hololive.hololivepro.com/wp-content/uploads/2023/09/Mizumiya-Su_pr-img_01_a.png
- gallery 01b: https://hololive.hololivepro.com/wp-content/uploads/2023/09/Mizumiya-Su_pr-img_01_b.png
- gallery 02: https://hololive.hololivepro.com/wp-content/uploads/2023/09/Mizumiya-Su_pr-img_02.png
- gallery 03: https://hololive.hololivepro.com/wp-content/uploads/2023/09/Mizumiya-Su_pr-img_03.png

**Dossier outfit section:**

````markdown
## Appearance Anchors (avatar)
145 cm (official profile; an encyclopedia records 151 cm before 2025-11-26, secondary); illustrator Bukurote
(ぶくろて). Light-blue hair to the shoulders with pink streaks and a lightning-bolt ahoge, blue eyes and a small fang.
Emoji 💬🔁💙. The official profile gallery (checked 2026-11-27) shows three outfits; descriptions are Claude's
reading of those images:
- **Original outfit (debut, 2024-11):** two small pink-and-blue braids and a blue hair clip; a black choker; an
  oversized white zip-up jacket with black ribbon lacing down the sleeves and pom-pom drawstrings; a light-blue
  graphic T-shirt worn as a dress, torn at the hem; a pink smartphone on a chain across her body; a black thigh
  strap and ankle strap; light-blue slouch socks with white bows; chunky white sneakers. [Official SU1 gallery 01_a, 02]
- **Black-and-blue frilled outfit:** hair in two pink-and-blue buns under a black lace headdress hung with charms;
  a black off-shoulder ruffled top with gingham trim and light-blue lacing; frilly black shorts; fingerless gloves;
  striped leg warmers; black platform boots. [Official SU1 gallery 01_b]
- **Japanese-style candy outfit:** twin braided tails tied with pink bows and candy hair ornaments; a white frilled
  pinafore with a lightning-bolt brooch over light-blue and pink candy-patterned kimono sleeves and a tiered skirt;
  pink platform shoes. Its reveal stream is not in the archive checked. [Official SU1 gallery 03]
````

**[SW] Physical Description (what Sudowrite receives):**

````text
Su's avatar is 145 cm tall, with light-blue shoulder-length hair streaked with pink, a lightning-bolt ahoge, blue eyes and a small fang. Original outfit: two small pink-and-blue braids and a blue hair clip, a black choker, an oversized white zip-up jacket with black ribbon lacing down the sleeves, a torn light-blue graphic T-shirt worn as a dress, a pink smartphone on a chain across her body, black thigh and ankle straps, light-blue slouch socks with white bows and chunky white sneakers. Frilled outfit: two pink-and-blue buns under a black lace headdress hung with charms, a black off-shoulder ruffled top with gingham trim and blue lacing, frilly black shorts, striped leg warmers and black platform boots. Japanese-style candy outfit: twin braids with pink bows and candy ornaments, a white frilled pinafore over light-blue and pink candy-patterned kimono sleeves and a tiered skirt, and pink platform shoes.
````

### Rindo Chihaya (`bible/characters/Rindo-Chihaya.md`)

**Official gallery images (open these to check the descriptions):**
- gallery 01a: https://hololive.hololivepro.com/wp-content/uploads/2023/09/Rindo-Chihaya_pr-img_01_a.png
- gallery 01b: https://hololive.hololivepro.com/wp-content/uploads/2023/09/Rindo-Chihaya_pr-img_01_b.png
- gallery 02: https://hololive.hololivepro.com/wp-content/uploads/2023/09/Rindo-Chihaya_pr-img_02.png
- gallery 03: https://hololive.hololivepro.com/wp-content/uploads/2023/09/Rindo-Chihaya_pr-img_03.png

**Dossier outfit section:**

````markdown
## Appearance Anchors (avatar)
168 cm; illustrator toridamono (トリダモノ). Shoulder-length black hair with a teal streak and a white streak, and
crimson eyes. Emoji 🎧🔧. The official profile gallery (checked 2026-11-27) shows three outfits; descriptions are
Claude's reading of those images:
- **Original outfit (debut, 2024-11):** a black-and-grey checkered cap with a blue wrench clip; big DJ headphones
  around her neck; a black choker; an off-shoulder black dress with a teal flame emblem and white sleeves studded
  with spikes, with jagged hems; a belt with a pouch; a thigh harness; black chunky boots with spikes and leg
  warmers; a blue wrench in hand. [Official CH1 gallery 01_a, 02]
- **Racing stage outfit:** a black bustier with teal accents; an oversized white-and-black racing jacket with teal
  stripes slipping off her shoulders; a black studded mini skirt over bike shorts; one black thigh-high; black boots
  with teal soles; a silver microphone. [Official CH1 gallery 01_b]
- **Japanese-style outfit:** a white kimono top patterned with black-and-white checks like a racing flag, with red
  accents; a dark-green hakama with a high slit; a large white flower and gold ornaments in her hair; black gloves
  and black boots. Its reveal stream is not in the archive checked. [Official CH1 gallery 03]
````

**[SW] Physical Description (what Sudowrite receives):**

````text
Chihaya's avatar is 168 cm tall, with shoulder-length black hair streaked with teal and white, and crimson eyes. Original outfit: a black-and-grey checkered cap with a blue wrench clip, big DJ headphones around her neck, a black choker, an off-shoulder black dress with a teal flame emblem and white spiked sleeves with jagged hems, a belt with a pouch, a thigh harness and black chunky spiked boots; she carries a blue wrench. Racing stage outfit: a black bustier with teal accents under an oversized white-and-black racing jacket with teal stripes, a studded black mini skirt over bike shorts, one black thigh-high and black boots with teal soles. Japanese-style outfit: a white kimono top checked like a racing flag with red accents, a dark-green slit hakama, a large white flower in her hair, black gloves and black boots.
````

### Shirakami Fubuki (`bible/characters/Shirakami-Fubuki.md`)

**Official gallery images (open these to check the descriptions):**
- gallery 01: https://hololive.hololivepro.com/wp-content/uploads/2020/06/Shirakami-Fubuki_pr-img_01.webp
- gallery 02: https://hololive.hololivepro.com/wp-content/uploads/2020/06/Shirakami-Fubuki_pr-img_02.webp
- gallery 03: https://hololive.hololivepro.com/wp-content/uploads/2020/06/Shirakami-Fubuki_pr-img_03.webp
- gallery 04: https://hololive.hololivepro.com/wp-content/uploads/2020/06/Shirakami-Fubuki_pr-img_04.webp
- gallery 05: https://hololive.hololivepro.com/wp-content/uploads/2020/06/Shirakami-Fubuki_pr-img_05.webp
- gallery 06: https://hololive.hololivepro.com/wp-content/uploads/2020/06/Shirakami-Fubuki_pr-img_06.webp
- gallery 07: https://hololive.hololivepro.com/wp-content/uploads/2020/06/Shirakami-Fubuki_pr-img_07.webp
- gallery 08: https://hololive.hololivepro.com/wp-content/uploads/2020/06/Shirakami-Fubuki_pr-img_08.webp
- gallery 09: https://hololive.hololivepro.com/wp-content/uploads/2020/06/Shirakami-Fubuki_pr-img_09.webp
- gallery 10: https://hololive.hololivepro.com/wp-content/uploads/2020/06/Shirakami-Fubuki_pr-img_10.webp

**Dossier outfit section:**

````markdown
## Appearance Anchors (avatar)
155 cm; illustrator Nagishiro Mito (凪白みと). Long white hair with a small side braid, white fox ears with black
inner tufts, cyan eyes and a white fox tail that darkens to black at the tip, marked with a small star. The official
profile gallery (checked 2026-11-27) shows nine outfits; descriptions are Claude's reading of those images:
- **Original outfit** (gallery 01–02): a white open-front top with a black-lined sailor collar and a light-blue
  neckerchief with a round clasp; detached wide white sleeves tied with light-blue ribbons; a bare midriff; black
  belted shorts; a black thigh-high on one leg and a black thigh strap on the other; black slouch boots with gold
  buckles. [Official FB1 gallery]
- **First new outfit (announced 2019-12-22; the announcement thumbnail shows the same frilled green skirt)** (gallery
  03): a black headband with a small light-blue ribbon, an oversized off-white top with a lace-trimmed collar and a
  big white bow, a dark-green skirt with a white frilled hem, black tights and black boots. [Official FB1 gallery]
  [FB4 pra4uMLmucA]
- **Hakama outfit** (gallery 04): a red flower hair ornament with tassels, a white kimono top whose wide sleeves fade
  to light blue with white blossoms, a navy-and-blue hakama scattered with white blossoms, a navy obi with a ribbon
  and a gold chain, and black lace-up boots. [Official FB1 gallery]
- **"TEK" outfit (named in a 2024-08-05 stream that brought it back, whose thumbnail shows it)** (gallery 05): a white
  technical coat with a fur-trimmed hood, a white scarf, "FOX" lettering and orange accents on the sleeves, long
  blue-and-white ribbons, black shorts, a black thigh band and white-and-black high-top sneakers. [Official FB1
  gallery] [FB4 IDX0gKhahFg]
- **Western-style outfit (worn in a 2020-10-06 stream titled for her new outfit; a 2024-05-27 stream welcomed it back
  as her "Western-style outfit")** (gallery 06): a small black top hat with a gold ornament, a navy double-breasted
  coat dress trimmed in gold, a navy bow with a blue rose brooch, a grey frilled skirt, white tights and grey boots.
  [Official FB1 gallery] [FB4 ta-ajhcaz7Q, JPnG3WsdSp8]
- **Hoodie-and-glasses outfit** (gallery 07): a black headband with small cross-shaped pins, black-rimmed glasses, an
  oversized black zip hoodie with a small "xxx" logo, black socks and hamburger-shaped slippers. [Official FB1
  gallery]
- **Apron-and-pass outfit (revealed 2024-08-09; the reveal silhouette's looped braids and wide sleeves match)**
  (gallery 08): looped braids, a navy dress with wide teal sleeves patterned with gold clovers, a white frilled apron
  with an orange heart-shaped pouch, a lanyard pass, a round clear-window shoulder bag, white tights patterned with
  gold clovers and navy plaid boots. [Official FB1 gallery] [FB4 tnOsA0krATc]
- **Royal outfit (her first solo live, FBKINGDOM "ANTHEM," 2025; a 2025-03-06 watch-along of the live shows it)**
  (gallery 09): a small gold crown, braided hair, a navy coat with gold epaulettes and star chains over a white
  high-collared shirt, a white fur-trimmed mantle lined in red, a blue jewel brooch, a navy skirt with gold stars and
  white thigh-high boots with gold heart garters. [Official FB1 gallery] [FB4 Dc8pLckDSYQ]
- **School-style outfit** (gallery 10): a dark knit vest with brooches over a striped white shirt and a mustard tie, a
  navy plaid pleated skirt with a chain and a white flower charm, navy knee socks and brown loafers. [Official FB1
  gallery]
````

**[SW] Physical Description (what Sudowrite receives):**

````text
Fubuki's avatar is 155 cm, with long white hair and a small side braid, white fox ears with black inner tufts, cyan eyes and a white fox tail that darkens to black at the tip. Original outfit: a white open-front top with a black-lined sailor collar and a light-blue neckerchief, detached wide sleeves tied with blue ribbons, a bare midriff, black shorts, one black thigh-high and one thigh strap, and black slouch boots. Other outfits in the official gallery: First new outfit (2019): a black headband, an oversized off-white top with a big bow, a dark-green frilled skirt; Hakama outfit: a red flower ornament, blossom-patterned blue sleeves and hakama; "TEK" outfit: a white technical coat with a fur-trimmed hood, a white scarf, long blue ribbons; Western-style outfit: a tiny top hat, a navy gold-trimmed coat dress, a blue rose; Hoodie-and-glasses outfit: black glasses, a black zip hoodie, hamburger slippers; Apron-and-pass outfit (2024): looped braids, teal clover sleeves, a white apron, a lanyard pass; Royal outfit (2025): a small gold crown, a navy coat with epaulettes, a red-lined white fur mantle; School-style outfit: a knit vest, a mustard tie, a navy plaid skirt.
````

### Ookami Mio (`bible/characters/Ookami-Mio.md`)

**Official gallery images (open these to check the descriptions):**
- gallery 01: https://hololive.hololivepro.com/wp-content/uploads/2020/06/Ookami-Mio_pr-img_01.webp
- gallery 02: https://hololive.hololivepro.com/wp-content/uploads/2020/06/Ookami-Mio_pr-img_02.webp
- gallery 03: https://hololive.hololivepro.com/wp-content/uploads/2020/06/Ookami-Mio_pr-img_03.webp
- gallery 04: https://hololive.hololivepro.com/wp-content/uploads/2020/06/Ookami-Mio_pr-img_04.webp
- gallery 05: https://hololive.hololivepro.com/wp-content/uploads/2020/06/Ookami-Mio_pr-img_05.webp
- gallery 06: https://hololive.hololivepro.com/wp-content/uploads/2020/06/Ookami-Mio_pr-img_06.webp
- gallery 07: https://hololive.hololivepro.com/wp-content/uploads/2020/06/Ookami-Mio_pr-img_07.webp
- gallery 08: https://hololive.hololivepro.com/wp-content/uploads/2020/06/Ookami-Mio_pr-img_08.webp
- gallery 09: https://hololive.hololivepro.com/wp-content/uploads/2020/06/Ookami-Mio_pr-img_09.webp

**Dossier outfit section:**

````markdown
## Appearance Anchors (avatar)
160 cm; illustrator Izumi Sai (泉彩). Long black hair with a red streak and a yellow-orange hair clip, black wolf
ears with white inner fur, amber eyes and a large black wolf tail with a white tip. The official profile gallery
(checked 2026-11-27) shows eight outfits; descriptions are Claude's reading of those images:
- **Original outfit** (gallery 01–02): a red choker; a black sleeveless crop top with a white sailor collar and a
  red tie; detached black sleeves lined in red; a twisted white-and-red rope with gold bells; a black pleated skirt
  with red lacing and purple flower prints; white thigh-highs tied with red ribbons; black thong sandals with red
  straps. [Official MI1 gallery]
- **Hoodie outfit (room wear; a 2022-01-09 morning show revealed its "2.0" version, and the title and thumbnail
  art match)** (gallery 03): red-rimmed glasses, a black choker, a white-and-black split hoodie with white paw prints,
  black shorts, black tights and white sneakers with red laces. [Official MI1 gallery] [MI4 Wfp02kj-7Qk]
- **Japanese-style maid outfit** (gallery 04): a frilled white maid headdress, round glasses, a high ponytail tied
  with a red ribbon, a red kimono with pink cherry blossoms under a white frilled apron, cuffs tied with red cord,
  black tights and brown boots. [Official MI1 gallery]
- **Autumn casual outfit** (gallery 05): a navy beret, a single braid, a white lace-collared blouse, a beige knit
  cardigan, a navy skirt with a red stripe and brown ankle boots. [Official MI1 gallery]
- **Playing-card outfit (revealed 2022-12-06; the reveal silhouette's twin tails and bow match)** (gallery 06): twin
  tails with a red-and-white bow and a red rose, a red ruffled collar with a black lace choker, white puff sleeves, a
  red bustier and a black corset laced in gold, long black gloves, a skirt hem hung with playing cards and black
  thigh-high boots. [Official MI1 gallery] [MI4 Wjxkl2m9zro]
- **Hooded outfit** (gallery 07): a black hood with wolf ears lined in red, a black crop top with a white sailor
  collar and red neckerchief, a black jacket with wide sleeves and red-and-white tassels, black shorts with red
  lacing, a leg band, white slouch socks and black shoes. [Official MI1 gallery]
- **Green capelet outfit** (gallery 08): a green capelet with gold paw buttons and a black bow, a grey ruffled blouse
  with black ribbon ties on the sleeves, a green skirt with a grey plaid panel, black tights and black shoes.
  [Official MI1 gallery]
- **School-style outfit** (gallery 09): a brown cable-knit sweater with a crest badge and star pins over a white
  collar and mustard tie, a red plaid pleated skirt with a chain and a small purple plush charm, black tights and
  brown lace-up boots. [Official MI1 gallery]
````

**[SW] Physical Description (what Sudowrite receives):**

````text
Mio's avatar is 160 cm, with long black hair streaked red, a yellow-orange hair clip, black wolf ears with white inner fur, amber eyes and a big black wolf tail tipped white. Original outfit: a red choker, a black crop top with a white sailor collar and red tie, detached black sleeves lined red, a white-and-red rope with gold bells, a black pleated skirt with red lacing, white thigh-highs tied with red ribbons and black sandals with red straps. Other outfits in the official gallery: Hoodie outfit (room wear): red-rimmed glasses, a white-and-black hoodie with paw prints, black shorts; Japanese-style maid outfit: a frilled maid headdress, round glasses, a red cherry-blossom kimono under a white apron; Autumn casual outfit: a navy beret, a single braid, a beige cardigan over a white blouse; Playing-card outfit (2022): twin tails with a red-and-white bow and rose, a black corset laced in gold, a skirt hem hung with playing cards; Hooded outfit: a wolf-eared black hood, a sailor-collared crop top, a wide-sleeved jacket with tassels; Green capelet outfit: a green capelet with paw buttons over a grey blouse; School-style outfit: a brown sweater, a mustard tie, a red plaid skirt.
````

### Inugami Korone (`bible/characters/Inugami-Korone.md`)

**Official gallery images (open these to check the descriptions):**
- gallery 01: https://hololive.hololivepro.com/wp-content/uploads/2020/06/Inugami-Korone_pr-img_01.png
- gallery 02: https://hololive.hololivepro.com/wp-content/uploads/2020/06/Inugami-Korone_pr-img_02.png
- gallery 03: https://hololive.hololivepro.com/wp-content/uploads/2020/06/Inugami-Korone_pr-img_03.png
- gallery 04: https://hololive.hololivepro.com/wp-content/uploads/2020/06/Inugami-Korone_pr-img_04.png
- gallery 05: https://hololive.hololivepro.com/wp-content/uploads/2020/06/Inugami-Korone_pr-img_05.png
- gallery 06: https://hololive.hololivepro.com/wp-content/uploads/2020/06/Inugami-Korone_pr-img_06.png
- gallery 07: https://hololive.hololivepro.com/wp-content/uploads/2020/06/Inugami-Korone_pr-img_07.png
- gallery 08: https://hololive.hololivepro.com/wp-content/uploads/2020/06/Inugami-Korone_pr-img_08.png
- gallery 09: https://hololive.hololivepro.com/wp-content/uploads/2020/06/Inugami-Korone_pr-img_09.png
- gallery 10: https://hololive.hololivepro.com/wp-content/uploads/2020/06/Inugami-Korone_pr-img_10.png

**Dossier outfit section:**

````markdown
## Appearance Anchors (avatar)
156 cm; illustrator Fukahire (フカヒレ). Brown hair in two long braids, floppy brown dog ears, bone-shaped hair
clips, red eyes and a brown dog tail. The official profile gallery (checked 2026-11-27) shows nine outfits;
descriptions are Claude's reading of those images:
- **Original outfit** (gallery 01–02): a red dog collar with a bone tag; a yellow jacket worn open, with colourful
  bow buttons on the sleeves; a white button-front sundress with multicoloured buttons and a navy hem; red leg
  warmers; white sneakers with pink laces. [Official KO1 gallery]
- **Beret outfit** (gallery 03): a red beret, small yellow hair bows, an orange plaid bow at the collar, a white
  blouse, a dark-brown capelet trimmed in gold, a dark-red skirt with gold patterns and white frills, brown knee
  socks and brown loafers. [Official KO1 gallery]
- **Japanese-style outfit** (gallery 04): red-and-white cord bows in her hair, a floating lavender shawl, a short
  white kimono top trimmed navy under a long yellow over-kimono patterned with red flowers and checks, a red obi with
  a white flower knot, white socks with pom-poms and red-thonged geta. [Official KO1 gallery]
- **Dog-hood outfit** (gallery 05): a pink zip hoodie with a white dog-face hood, "DOGGO" lettering and bone
  patches, a black tank top with dog prints, denim shorts, pink-and-white striped leg warmers and slippers.
  [Official KO1 gallery]
- **Sonic collaboration outfit (shown 2022-06-24 in an ambassador-commemoration stream; the image carries ©SEGA)**
  (gallery 06): a blue Sonic hoodie with spines and ears on the hood and a yellow front, blue-tinted hair and green
  eyes, white gloves, red sneakers and a Knuckles plush in her arms. [Official KO1 gallery] [KO4 QeqfCtJ-chw]
- **Alice-style outfit (revealed 2023-07-07; the reveal silhouette's bow and skirt match)** (gallery 07): a black
  ribbon headband, twin tails, a choker with a heart-lock pendant, a light-blue puff-sleeved dress under a white
  frilled apron, black harness straps with a small bottle charm, fishnet tights and black lace-up boots. [Official
  KO1 gallery] [KO4 Lidmb9yq8d8]
- **Viking-style outfit** (gallery 08): a horned helmet trimmed in gold, a gem pendant, a brown leather top with a
  shoulder guard, fur-trimmed arm wraps, a belt with a pouch, a red fur-trimmed skirt with a zigzag border, black
  thigh-highs and fur-topped boots. [Official KO1 gallery]
- **Jumpsuit outfit (revealed 2024-10-01 for her birthday; the reveal silhouette and the next day's thumbnail
  match)** (gallery 09): a yellow hooded jumpsuit with dog ears on the hood, white sleeves, a red badge and a paw
  badge, a white buckled belt, dog-face patches on the legs and chunky white sneakers. [Official KO1 gallery] [KO4
  mEPiE7V0lxg, SwUnrugQ9VM]
- **Horror-parody outfit** (gallery 10): a hockey mask pushed to the side of her head, braids with red bows, a red
  choker, a yellow-and-white striped T-shirt, denim overall shorts, red socks, blue sneakers and a toy-like chainsaw
  lettered "DooG" and splashed red. [Official KO1 gallery]
````

**[SW] Physical Description (what Sudowrite receives):**

````text
Korone's avatar is 156 cm, with brown hair in two long braids, floppy brown dog ears, bone-shaped hair clips, red eyes and a brown dog tail. Original outfit: a red dog collar with a bone tag, an open yellow jacket with colourful bow buttons, a white button-front sundress with a navy hem, red leg warmers and white sneakers. Other outfits in the official gallery: Beret outfit: a red beret, a dark-brown capelet, a dark-red frilled skirt; Japanese-style outfit: a floating lavender shawl, a yellow over-kimono with red flowers, a red obi; Dog-hood outfit: a pink hoodie with a white dog-face hood, denim shorts, striped leg warmers; Sonic collaboration outfit (2022): a blue Sonic hoodie, green eyes, a Knuckles plush; Alice-style outfit (2023): a black ribbon, a light-blue dress under a white apron, fishnet tights; Viking-style outfit: a horned helmet, a leather top, a fur-trimmed red skirt; Jumpsuit outfit (2024): a yellow dog-eared hooded jumpsuit with white sleeves; Horror-parody outfit: a hockey mask on her head, denim overalls, a toy chainsaw lettered "DooG."
````

### La+ Darknesss (`bible/characters/Laplus-Darknesss.md`)

**Official gallery images (open these to check the descriptions):**
- gallery 01: https://hololive.hololivepro.com/wp-content/uploads/2020/07/La-Darknesss_pr-img_01.webp
- gallery 02: https://hololive.hololivepro.com/wp-content/uploads/2020/07/La-Darknesss_pr-img_02.webp
- gallery 03: https://hololive.hololivepro.com/wp-content/uploads/2020/07/La-Darknesss_pr-img_03.webp
- gallery 04: https://hololive.hololivepro.com/wp-content/uploads/2020/07/La-Darknesss_pr-img_04.webp
- gallery 05: https://hololive.hololivepro.com/wp-content/uploads/2020/07/La-Darknesss_pr-img_05.webp
- gallery 06: https://hololive.hololivepro.com/wp-content/uploads/2020/07/La-Darknesss_pr-img_06.webp
- gallery 07: https://hololive.hololivepro.com/wp-content/uploads/2020/07/La-Darknesss_pr-img_07.webp

**Dossier outfit section:**

````markdown
### Outfits in the official profile gallery (checked 2026-11-27)
Claude's reading of the gallery images on https://hololive.hololivepro.com/en/talents/la-darknesss/ (7 images (01 and 02 show the same original outfit)). Labels are descriptive
unless a date and its source are given; the gallery may not include every seasonal outfit shown only on stream.

- **Original outfit** (gallery 01-02): very long silver hair with a purple streak, huge purple-striped horns, a black oversized coat with purple cuffs, belts and a yellow-striped tie, purple stockings, heavy shackle cuffs at her ankles, black boots, a tail tipped with a star, and her crow perched on her head.
- **Kimono** (gallery 03): twin braided tails tied with big gold bells, a black-and-purple kimono with manga-panel prints and flowers, a purple obi, geta, and the crow on her head wearing a red flower.
- **Streetwear** (gallery 04): a cross-shaped clip, a black oversized jacket with purple flame patterns over a white shirt with a purple tie, a purple plaid skirt and black thigh-high boots.
- **Sporty outfit** (gallery 05): purple-tipped twin tails, a white-and-purple cropped jacket with a sailor collar over a white crop top, black shorts, leg straps and purple-and-white sneakers.
- **Shackled robe** (gallery 06): short twin tails, banded horns, a black tunic with a long patterned front panel, belts and chains, and shackle cuffs at her ankles.
- **Knit-and-plaid outfit** (gallery 07): a black cat-ear knit beanie under her horns, a black oversized cardigan with purple plaid bows over a black shirt-dress, a chain bag, black socks, ankle shackles and black platform boots.
````

**[SW] Physical Description (what Sudowrite receives):**

````text
La+'s avatar is 139 cm tall, with long silvery hair, a purple lock and a braided bang, large black horns striped in purple above pointed ears, yellow eyes and small fangs. She wears a dark purple dress with a yellow tie and oversized sleeves that swallow her hands, one purple legging and short boots, with a star-tipped purple tail and shackles at her neck, sleeves and ankles. A crow keeps her company. Other outfits in the official gallery: Kimono: twin braided tails tied with big gold bells, a black-and-purple kimono with manga-panel prints and flowers, a purple obi; Streetwear: a cross-shaped clip, a black oversized jacket with purple flame patterns over a white shirt with a purple tie, a purple plaid skirt and black thigh-high boots; Sporty outfit: purple-tipped twin tails, a white-and-purple cropped jacket with a sailor collar over a white crop top, black shorts; Shackled robe: short twin tails, banded horns, a black tunic with a long patterned front panel; Knit-and-plaid outfit: a black cat-ear knit beanie under her horns, a black oversized cardigan with purple plaid bows over a black shirt-dress, a chain bag.
````

### Takane Lui (`bible/characters/Takane-Lui.md`)

**Official gallery images (open these to check the descriptions):**
- gallery 01: https://hololive.hololivepro.com/wp-content/uploads/2020/07/Takane-Lui_pr-img_01.webp
- gallery 02: https://hololive.hololivepro.com/wp-content/uploads/2020/07/Takane-Lui_pr-img_02.webp
- gallery 03: https://hololive.hololivepro.com/wp-content/uploads/2020/07/Takane-Lui_pr-img_03.webp
- gallery 04: https://hololive.hololivepro.com/wp-content/uploads/2020/07/Takane-Lui_pr-img_04.webp
- gallery 05: https://hololive.hololivepro.com/wp-content/uploads/2020/07/Takane-Lui_pr-img_05.webp
- gallery 06: https://hololive.hololivepro.com/wp-content/uploads/2020/07/Takane-Lui_pr-img_06.webp
- gallery 07: https://hololive.hololivepro.com/wp-content/uploads/2020/07/Takane-Lui_pr-img_07.webp
- gallery 08: https://hololive.hololivepro.com/wp-content/uploads/2020/07/Takane-Lui_pr-img_08.webp

**Dossier outfit section:**

````markdown
### Outfits in the official profile gallery (checked 2026-11-27)
Claude's reading of the gallery images on https://hololive.hololivepro.com/en/talents/takane-lui/ (8 images (01 and 02 show the same original outfit)). Labels are descriptive
unless a date and its source are given; the gallery may not include every seasonal outfit shown only on stream.

- **Original outfit** (gallery 01-02): short pink hair with a black headband, a white blouse with a red tie, a black corset and shiny black shorts, a long dark-crimson cape with hawk feathers and buckled straps, fingerless gloves, sheer black tights with leg bands and black heels with wing ornaments.
- **Kimono** (gallery 03): long hair with a black bow and a white flower, a navy striped kimono with lace trim and wing patterns, a red obi bow with a pink checkered cord, a frilled underskirt and lace-up boots.
- **Retro outfit** (gallery 04): round glasses, a black blouse with a sheer yoke and a red ribbon, a long burgundy skirt with an orange ribbon, socks and loafers.
- **Gentleman outfit** (gallery 05): a small black top hat with a blue ribbon, a black jacket with silver embroidery and a blue brooch, black shorts with garters and black boots.
- **Chinese-style outfit** (gallery 06): a side braid, a black sleeveless high-collared dress with a red belt and toggles, a dark fringed shawl with red-and-gold patterns, a thigh garter and red boots.
- **Techwear** (gallery 07): a black top with red accents, a long black quilted coat that trails like a wing, red tights with garters and black platform boots.
- **Gothic outfit** (gallery 08): braided twin tails with black ribbons, an oversized black jacket with purple patterns over a black dress, patterned tights and black platform shoes.
````

**[SW] Physical Description (what Sudowrite receives):**

````text
Lui's avatar is 161 cm tall: a hawk girl with short pink hair, feather-like side locks, a black headband and blue eyes. She wears a white blouse with a red tie and a gold bird pin under a dark crimson cape with strap-and-buckle trim and bird emblems, black fingerless gloves, glossy black high-waisted shorts with a wide belt, dark tights with a thigh strap holding a riding crop, and black heels with silver wing ornaments; brown feathers hang at her side. Ganmo, a plump frogmouth with two white chicks on his head, is her secretary. Other outfits in the official gallery: Kimono: long hair with a black bow and a white flower, a navy striped kimono with lace trim and wing patterns, a red obi bow with a pink checkered cord; Retro outfit: round glasses, a black blouse with a sheer yoke and a red ribbon, a long burgundy skirt with an orange ribbon; Gentleman outfit: a small black top hat with a blue ribbon, a black jacket with silver embroidery and a blue brooch, black shorts with garters and black boots; Chinese-style outfit: a side braid, a black sleeveless high-collared dress with a red belt and toggles, a dark fringed shawl with red-and-gold patterns; Techwear: a black top with red accents, a long black quilted coat that trails like a wing, red tights with garters and black platform boots; Gothic outfit: braided twin tails with black ribbons, an oversized black jacket with purple patterns over a black dress, patterned tights and black platform shoes.
````

### Hakui Koyori (`bible/characters/Hakui-Koyori.md`)

**Official gallery images (open these to check the descriptions):**
- gallery 01: https://hololive.hololivepro.com/wp-content/uploads/2020/07/Hakui-Koyori_pr-img_01.webp
- gallery 02: https://hololive.hololivepro.com/wp-content/uploads/2020/07/Hakui-Koyori_pr-img_02.webp
- gallery 03: https://hololive.hololivepro.com/wp-content/uploads/2020/07/Hakui-Koyori_pr-img_03.webp
- gallery 04: https://hololive.hololivepro.com/wp-content/uploads/2020/07/Hakui-Koyori_pr-img_04.webp
- gallery 05: https://hololive.hololivepro.com/wp-content/uploads/2020/07/Hakui-Koyori_pr-img_05.webp
- gallery 06: https://hololive.hololivepro.com/wp-content/uploads/2020/07/Hakui-Koyori_pr-img_06.webp
- gallery 07: https://hololive.hololivepro.com/wp-content/uploads/2020/07/Hakui-Koyori_pr-img_07.webp

**Dossier outfit section:**

````markdown
### Outfits in the official profile gallery (checked 2026-11-27)
Claude's reading of the gallery images on https://hololive.hololivepro.com/en/talents/hakui-koyori/ (7 images (01 and 02 show the same original outfit)). Labels are descriptive
unless a date and its source are given; the gallery may not include every seasonal outfit shown only on stream.

- **Original outfit** (gallery 01-02): long pink hair with coyote ears and a fluffy pink tail, a frilled white lab coat over a white crop top with a pink tie, a navy skirt with test tubes at the belt, brown tights, a potion vial on her thigh and black Mary Janes with pink bows.
- **Kimono and hakama** (gallery 03): a side ponytail with flower ornaments, a pink-and-white floral kimono with a big pink obi bow, a patterned pink hakama, white socks, geta and a tiny pink coyote on her shoulder.
- **Short-hair casual outfit** (gallery 04): a short bob, a choker, a white zip hoodie dress with pink laced sleeves, and clear sandals.
- **School outfit** (gallery 05): twin side tails, a white blouse with a pink bow, a lavender plaid skirt, white knee socks and brown loafers.
- **Maid outfit** (gallery 06): twin tails with a maid headdress, a pink-and-white maid dress with a black corset and a frilled apron, and black boots.
- **Chinese-style outfit** (gallery 07): buns with red tassels, a red high-collared dress with gold trim, wide black frilled sleeves with tassels, a corset belt hung with potions, one white thigh-high and one fishnet, and red shoes.
````

**[SW] Physical Description (what Sudowrite receives):**

````text
Koyori's avatar is 153 cm tall, with long pink hair in braids and buns, an ahoge, lilac eyes, pink coyote ears, a fluffy pink tail and a hexagonal hair clip. She wears an open white lab coat with pink trim and a ruffled hem over a white crop top, a pink tie with a heart, a black choker and a pocket-watch chain, with a black pleated skirt hung with test tubes, flasks on a thigh strap, brown tights and black heels tied with pink ankle ribbons. Kokoro, a small pink coyote, peeks out of her coat pocket. Other outfits in the official gallery: Kimono and hakama: a side ponytail with flower ornaments, a pink-and-white floral kimono with a big pink obi bow, a patterned pink hakama; Short-hair casual outfit: a short bob, a choker, a white zip hoodie dress with pink laced sleeves; School outfit: twin side tails, a white blouse with a pink bow, a lavender plaid skirt; Maid outfit: twin tails with a maid headdress, a pink-and-white maid dress with a black corset and a frilled apron, black boots; Chinese-style outfit: buns with red tassels, a red high-collared dress with gold trim, wide black frilled sleeves with tassels.
````

### Sakamata Chloe (`bible/characters/Sakamata-Chloe.md`)

**Official gallery images (open these to check the descriptions):**
- gallery 01: https://hololive.hololivepro.com/wp-content/uploads/2024/09/Sakamata-Chloe_pr-img_01.png
- gallery 02: https://hololive.hololivepro.com/wp-content/uploads/2024/09/Sakamata-Chloe_pr-img_02.png
- gallery 03: https://hololive.hololivepro.com/wp-content/uploads/2024/09/Sakamata-Chloe_pr-img_03.png
- gallery 04: https://hololive.hololivepro.com/wp-content/uploads/2024/09/Sakamata-Chloe_pr-img_04.png
- gallery 05: https://hololive.hololivepro.com/wp-content/uploads/2024/09/Sakamata-Chloe_pr-img_05.png

**Dossier outfit section:**

````markdown
### Outfits in the official profile gallery (checked 2026-11-27)
Claude's reading of the gallery images on https://hololive.hololivepro.com/en/talents/sakamata-chloe/ (5 images (01 and 02 show the same original outfit)). Labels are descriptive
unless a date and its source are given; the gallery may not include every seasonal outfit shown only on stream.

- **Original outfit** (gallery 01-02): grey hair with a black streak under a black orca hood with red plaid bows, a white frilled camisole with black straps and red ribbons, a red plaid skirt, an oversized black jacket with belts and yellow tape, garters with torn black stockings and black platform boots with red soles.
- **Kimono** (gallery 03): hair up with red flowers and a dangling hairpin, a black-and-white kimono with gold wave patterns and a black fur collar, a red cord at her thigh and sandals.
- **Gothic outfit** (gallery 04): drill twin tails with black bows, a red jacket with black bows over a black-and-grey corset dress with a heart cut-out, one fishnet and one black stocking, and black platform shoes.
- **School outfit** (gallery 05): long hair with a clip, a pink cardigan with black bows over a white shirt with a red bow, a red plaid skirt, white leg warmers and loafers.
````

**[SW] Physical Description (what Sudowrite receives):**

````text
Chloe's avatar is 148 cm tall, with long wavy gray hair, a side braid, X-shaped hair pins, red eyes and a small fang, under a black orca hood with white "eyes" and red plaid bows. She wears an open, off-shoulder black jacket lined in quilted red and strapped with belts, a white ruffled top, a collar with a heart charm, a studded belt with chains, a red plaid skirt over black ruffles, torn black thigh-highs with garters and black boots with red laces and red platform soles, all marked with yellow "caution" tape. Inu, a tiny orca in a "Caution" life jacket, is her mascot. Other outfits in the official gallery: Kimono: hair up with red flowers and a dangling hairpin, a black-and-white kimono with gold wave patterns and a black fur collar, a red cord at her thigh and sandals; Gothic outfit: drill twin tails with black bows, a red jacket with black bows over a black-and-grey corset dress with a heart cut-out, one fishnet and one black stocking; School outfit: long hair with a clip, a pink cardigan with black bows over a white shirt with a red bow, a red plaid skirt.
````

### Kazama Iroha (`bible/characters/Kazama-Iroha.md`)

**Official gallery images (open these to check the descriptions):**
- gallery 01: https://hololive.hololivepro.com/wp-content/uploads/2020/07/Kazama-Iroha_pr-img_01.png
- gallery 02: https://hololive.hololivepro.com/wp-content/uploads/2020/07/Kazama-Iroha_pr-img_02.png
- gallery 03: https://hololive.hololivepro.com/wp-content/uploads/2020/07/Kazama-Iroha_pr-img_03.png
- gallery 04: https://hololive.hololivepro.com/wp-content/uploads/2020/07/Kazama-Iroha_pr-img_04.png
- gallery 05: https://hololive.hololivepro.com/wp-content/uploads/2020/07/Kazama-Iroha_pr-img_05.png
- gallery 06: https://hololive.hololivepro.com/wp-content/uploads/2020/07/Kazama-Iroha_pr-img_06.png
- gallery 07: https://hololive.hololivepro.com/wp-content/uploads/2020/07/Kazama-Iroha_pr-img_07.png

**Dossier outfit section:**

````markdown
### Outfits in the official profile gallery (checked 2026-11-27)
Claude's reading of the gallery images on https://hololive.hololivepro.com/en/talents/kazama-iroha/ (7 images (01 and 02 show the same original outfit)). Labels are descriptive
unless a date and its source are given; the gallery may not include every seasonal outfit shown only on stream.

- **Original samurai outfit** (gallery 01-02): a blonde ponytail with a teal ribbon, a cream haori with teal sleeves and wave patterns over a white top, a teal-and-black pleated skirt, fingerless gloves, a thigh strap, geta with red straps and her katana.
- **Kimono and hakama** (gallery 03): red-and-white flower ornaments, a pale kimono top with orange flowers, an orange-red hakama with cherry blossoms, a red obi and black boots.
- **Pastel casual outfit** (gallery 04): a white cap with flowers, long hair, a pastel holographic jacket over a crop top, denim shorts, a thigh band and white platform sneakers.
- **Sailor uniform** (gallery 05): braids with a black headband, a white sailor top with a light-blue tie, a navy pleated skirt, white socks and loafers.
- **Sporty outfit** (gallery 06): twin tails with black ribbons, a white cropped hoodie with quilted sleeves, a black miniskirt, fishnet tights, black leg warmers and boots.
- **Café outfit** (gallery 07): short hair, a black bow at the collar, a white apron with a brush in the pocket over a brown frilled dress with black lace and ribbons, yellow tights and brown lace-up boots.
````

**[SW] Physical Description (what Sudowrite receives):**

````text
Iroha's avatar is 156 cm tall, with short blonde hair in a ponytail tied with a green leaf-like ribbon and aqua-blue eyes. She wears a white top with gold fittings and a red cord with a bell at her waist, a teal pleated skirt with a cloud pattern, a black fingerless glove and, over everything, a long cream haori-like coat with teal-gradient sleeves and cloud motifs; she carries a katana with a teal scabbard and wears white thigh-highs with teal diamond accents and black-and-red thong sandals. Pokobee, a small tanuki, travels with her. Other outfits in the official gallery: Kimono and hakama: red-and-white flower ornaments, a pale kimono top with orange flowers, an orange-red hakama with cherry blossoms; Pastel casual outfit: a white cap with flowers, long hair, a pastel holographic jacket over a crop top; Sailor uniform: braids with a black headband, a white sailor top with a light-blue tie, a navy pleated skirt; Sporty outfit: twin tails with black ribbons, a white cropped hoodie with quilted sleeves, a black miniskirt; Café outfit: short hair, a black bow at the collar, a white apron with a brush in the pocket over a brown frilled dress with black lace and ribbons.
````

## Part 2. FLOW GLOW and GAMERS ties added to existing cards

### Mori Calliope (`bible/characters/Mori-Calliope.md`)

**[SW] Groups:** hololive, hololive -Myth-, Myth, CHADCast, hololive English (former branch name), Last Writes, LYRA ("III" cover)

**[SW] Relationships (current, whole field):**

````text
Takanashi Kiara: her TakaMori partner. Kiara's 2020 crush bit met Calli's "kusotori" rebuffs; today their banter has an old-married-couple rhythm. Calli deflects, then insists "I love Kiara!"; they sang "Fire N Ice" and play Mom and Dad to Kobo. Ninomae Ina'nis: Myth genmate who designed Death Sensei and drew her debut EP cover; Calli wrote lyrics for Ina's TAKO∞TAKOVER and is a recurring target of Ina's puns. Gawr Gura (graduated): her "Bone Bros" partner; they sang "Q," and Calli performed Gura's unreleased "Full Color" at Myth's 2024 anniversary concert. Watson Amelia (affiliate): Myth genmate and Clubhouse 51 opponent. IRyS and Hakos Baelz: her CHADCast cohosts ("BLUE CLAPPER" with Bijou, 2024; "Here Comes the CHADCast," 2026); Bae sang "R x R x R" with her (2025); IRyS joined her as the "Two Pink Women" of Silent Hill 2. Nerissa Ravencroft: Advent kouhai and singing partner (the 2025 duet "OVER//RIDE"; a guest spot at Nerissa's 3D concert; "Magia" with Koganei Niko, 2026). Gigi Murin ("Grem Reaper"): horror and job-simulator collabs, and Elden Ring Nightreign with Raora Panthera. Kobo Kanaeru: "Uncle Dad." Koseki Bijou ("Biboo," "TombStone"): a junior whose skill Calli admires; they played her Undertale mod starring Calli and ran a 24-hour charity stream (2025). Shiori Novella: her 2026 Serendipity partner, who calls her "Mor Mori"; Calli admits she is "a little obsessed with her." Ouro Kronii ("Kronster"): deadpan sparring partner in "Time and Death" horror co-ops and mock feuds. Hoshimachi Suisei: "Wicked" and "CapSule" (2022). Cecilia Immergreen: "Cloudy Sheep" at Serendipity. Nekomata Okayu: Mario Party (2024). Inugami Korone: bilingual Keep Talking (2020). Rikka (HOLOSTARS; ended activities 2026-06-09): "spiral tones" (MoRikka). Elizabeth, Koganei Niko, Ayunda Risu and Amane Kanata (graduated 2025-12-27): fellow LYRA vocalists ("III"). Nanashi Mumei (graduated 2025): "ANATOMY REVIEW" drawing streams (2022). FUWAMOCO: "FUWAMOCALLI," a pair name the twins favor. Isaki Riona (FLOW GLOW): calls her "my beloved Calli-senpai"; Clubhouse Games (2026). English-lesson guests Marine, Fubuki, AZKi, La+, Iroha, Lui and Chloe (2022); HOLOYOI guests Lui, Chloe, Noel and Botan (2023). Ceres Fauna: a five-player Dota 2 collab (2024). Yukihana Lamy: the Myth × fifth-generation Among Us collab (2020).
````

**Relationship Map rows added in r02 (with sources):**

| Isaki Riona, Koganei Niko (FLOW GLOW) | Kouhai; Riona's "beloved Calli-senpai" | Clubhouse Games on Riona's channel (2026-09-12); "Ring my name" dance shorts (2026); Niko in LYRA and in "Magia" with Calli and Nerissa (2026-08-28) | [Archive metadata hhOim_G0kns, rAR9fgHBKwI, 5ccqXCOshHc] |
| Inugami Korone (GAMERS) | JP senior | Keep Talking and Nobody Explodes in Japanese and English (2020-11-27) | [Korone channel yk2kdHkzI48] |

**Evidence notes added:**

- Ties to the FLOW GLOW cards (added 2026-11-27 by author order; Claude only, Gemini Neon review pending): archived titles on both channels where listed in the Relationship Map row; covers and dance shorts show that the upload happened, not how close the members are.
- GAMERS ties (author order 2026-11-27; Claude only, Gemini Neon review pending): Korone's bilingual Keep Talking (yk2kdHkzI48); Fubuki named among the English-lesson guests (already in the map, 2022-02-19). Relationships trimmed slightly to stay inside the soft limit.

### Hakos Baelz (`bible/characters/Hakos-Baelz.md`)

**[SW] Groups:** hololive -Promise-, Promise, hololive English -Promise- (former branch name), hololive English -Council- (former), Council, BaeRyS, CHADCast

**[SW] Relationships (current, whole field):**

````text
IRyS: her BaeRyS partner in a performed "married and divorced" routine that traces back to a Minecraft bento exchange; covers, off-collabs, "Here Comes the CHADCast" and "LUVATORRRRRY!" at Serendipity; Bae calls IRyS "the very first senpai I had ever met," and IRyS calls their dynamic "a can of worms." Mori Calliope and IRyS: her CHADCast cohosts; "BLUE CLAPPER" with them and Koseki Bijou (2024); "R x R x R" with Calli (2025); her nickname for Calli is "Cori Malliope." Ouro Kronii: Promise genmate; Sandwich Review, Digimon Survive, Fortnite; "Dance Monkey" in Sydney (2025). Ceres Fauna (graduated): genmate and horror partner (Amnesia, 2022–2023). Nanashi Mumei (graduated): genmate; BAE-CADEMY, off-collabs, Overwatch 2. Tsukumo Sana: a graduated Council genmate. Koseki Bijou: "BaeBi," a 2024 sleepover marathon, We Were Here. Cecilia Immergreen: "BratTea"; by Bae's account a coffee-versus-tea debate, a 2026 fes talk and Resident Evil together. Gigi Murin: "Countach" with Kureiji Ollie (2025); a Midsummer Night's Dream reading. Elizabeth Rose Bloodflame and Kobo Kanaeru: "HELP!!" at Serendipity. Raora Panthera: Mario Party on Bae's 24-hour stream. FUWAMOCO: Gigi's 2025 Spring Party; they danced to "SNAKE EYES." Takanashi Kiara: Keep Talking and Nobody Explodes (2021). Ninomae Ina'nis: a K/DA cover and an art lesson. Watson Amelia: bathroom reviews and Apex. Gawr Gura: the Urban Dictionary Challenge. Usada Pekora: "HIDE & SEEK" (2023). Ookami Mio and Ollie: her joking "moms." Natsuiro Matsuri: "Kakumei Dualism" at the 2026 fes. holoX: Sakamata Chloe ("Crazy Scary Holy Fantasy," 2023), Takane Lui (episode 5, with Chloe) and Hakui Koyori (episode 4, with Nene) on BAE-GEMITE DOMINATION. Houshou Marine: Mario Kart (2021) and Calli's house party (2023); Bae and Mumei played "Truth of Beauty Witch," the horror game featuring Marine. Kikirara Vivi: #holoREPO (2025). Shirogane Noel: a team Mario Kart event with FUWAMOCO (2023). Shishiro Botan: BAE-GEMITE DOMINATION #2 with Oozora Subaru (2023). Hoshimachi Suisei: "High Tide" with IRyS and Moona at Breaking Dimensions (2024) and Bae's "Moonlight" dance cover (2025). AZKi: GeoGuessr (2023). Nekomata Okayu: team kart events (2023, 2024). Inugami Korone: the duet "BITE! KAMU! BITE!" (2023).
````

**Relationship Map rows added in r02 (with sources):**

| Inugami Korone (GAMERS) | Duet partner | "BITE! KAMU! BITE!" (2023-11-21) | [Official music https://hololive.hololivepro.com/en/music/354/] |

**Evidence notes added:**

- GAMERS ties (author order 2026-11-27; Claude only, Gemini Neon review pending): the official music entry for "BITE! KAMU! BITE!" (354).

### Nerissa Ravencroft (`bible/characters/Nerissa-Ravencroft.md`)

**[SW] Groups:** hololive -Advent-, Advent, hololive English (former branch name), Bloodraven

**[SW] Relationships (current, whole field):**

````text
Shiori Novella: Advent genmate whom she calls her "wife" in a running public bit (ShioRaven); Shiori plays hard to get, and the two keep a joke lore of fictional "children." Fuwawa and Mococo Abyssgard (FUWAMOCO; "Sound Hounds"): she jokingly claims to be the third sister, "Mofufu"; Fuwawa calls her "Newissa." Koseki Bijou: the raven and the shiny rock girl (JewelBird); Bijou calls her "Nerizzler," and Nerissa named Bijou's evil twin "Oobib." Takanashi Kiara: her oshi (KiaRissa); in Nerissa's lore she worked at KFP; Kiara showed her around Minecraft, and they held a 2025 "BIRB GIRLS" GIRLSTALK. Mori Calliope: Baldur's Gate 3 party member, duet partner ("OVER//RIDE") and guest at her 3D concert; "Magia" with Koganei Niko (2026). IRyS: fellow singer who guested at that concert. Elizabeth Rose Bloodflame: her "mortal enemy" in their lore (a performed rivalry) and her 2026 Serendipity unit partner in Bloodraven ("Cruel Angel's Thesis"); they covered "Rondo Revolution," and Nerissa praises Elizabeth's kindness and encouragement ("She's always looking out for me, even though I'm the senpai"). Moona Hoshinova: sings on Moona's "100%" (2025). Houshou Marine: one of her oshis; Mario Party Superstars with FUWAMOCO (2024). Gigi Murin: duo partner with a joke "child," Nerigi. Nanashi Mumei (graduated 2025): "emo hours" partner (2023, 2025); with Kiara they sang "Beyond the way" at the 2024 English concert. Ceres Fauna (graduated 2025): "Fauna-senpai!!!" on her first day on X; with Shiori they sang "Lonely in Gorgeous" at the same concert. Cecilia Immergreen: Unravel Two (2024; "AutoTune"). Raora Panthera: Clubhouse Games (2024); with Moona, Raft and Monster Hunter Wilds as "V3LVET" (2025). Kobo Kanaeru (ID): "BLUE CLAPPER" with Kronii at Serendipity. Gawr Gura (graduated): "Scarlet Wand" guildmate in ENigmatic Recollection, with Shiori. La+ Darknesss: both in holoGTA (2024); a dance short to her "Onee-sama♡Love Call" (2026); Takane Lui: an animated "Soar" short on her channel (2026). Ninomae Ina'nis: on her Tomodachi Life island with IRyS. Hoshimachi Suisei: a "BIBIDEBA" dance short (2024). Shishiro Botan: Nerissa guested at Botan's birthday 3D live "Stray&Stay" (2026). Nakiri Ayame, Nanashi Mumei and Watson Amelia: the 2023 Sports Festival white team.
````

**Relationship Map rows added in r02 (with sources):**

| Koganei Niko, Isaki Riona (FLOW GLOW) | Kouhai | "Magia" with Calli and Niko (2026-08-28); a "Ring my name" dance short (2026-06-23) | [Archive metadata 5ccqXCOshHc, Ts1v3xM-YG8] |

**Evidence notes added:**

- Ties to the FLOW GLOW cards (added 2026-11-27 by author order; Claude only, Gemini Neon review pending): archived titles on both channels where listed in the Relationship Map row; covers and dance shorts show that the upload happened, not how close the members are.

### Fuwawa Abyssgard (`bible/characters/Fuwawa-Abyssgard.md`)

**[SW] Groups:** FUWAMOCO, hololive -Advent-, hololive English -Advent- (former branch name), Advent, B.F.F

**[SW] Relationships (current, whole field):**

````text
Mococo Abyssgard: her younger twin, whom she calls "Moco-chan" even in English; Mococo says Fuwawa is dependable and calms her down; they finish each other's sentences ("FUWAMOCO sync") and sometimes argue; Fuwawa loved being called "Fuwa-nee" once. Pero, "The Great Perroccino": their fictional dog mascot and self-proclaimed mentor; they call him "nasty" in their public bits. Advent: Shiori (Pen Pups), Bijou (Diamond Dogs), Nerissa (Sound Hounds; Fuwawa calls her "Newissa," and Nerissa claims to be the third sister, "Mofufu"). Mori Calliope: "FUWAMOCALLI." Watson Amelia: "Detective Dogs." Ouro Kronii: "WatchDog." Nanashi Mumei (graduated 2025): "Fuwamoomco" (Overwatch). Raora Panthera: their 2026 Serendipity unit partner in B.F.F. Gigi Murin and Mori Calliope: "2 Creatures + 1 Reaper," defusing bombs (2026). Houshou Marine: her oshi; a Touhou off-collab (2024). Shirakami Fubuki: horror and Lethal Company partner. Hakui Koyori: "FUWAMOKOYO" on FUWAMOCO MORNING (2024). Gigi Murin and Cecilia Immergreen: Justice kouhai who guest-hosted FUWAMOCO MORNING #167 as a FUWAMOCO impersonation bit; Gigi sang "Bright Tonight" with the twins (2025) and "MAKE IT, BREAK IT" with them and Vestia Zeta at Serendipity. Elizabeth Rose Bloodflame: the twins sang in her 2026 birthday cover "CHA-LA HEAD-CHA-LA." Ookami Mio (GAMERS): a mochi-pounding off-collab (2025) and, with Ina, "Dottabatta Chindouchuu" at Serendipity. Hakos Baelz: Gigi's 2025 Spring Party; FUWAMOCO danced to "bae-senpai's new song SNAKE EYES" (2026). IRyS, Gigi and Kronii: "Bright Tonight" (2025). Ceres Fauna (graduated): FUWAMOCO helped on the World Tree's last day (2024-12-31). AZKi: a FUWAMOCO-themed GeoGuessr collaboration ("FWMCAZ"); also a singing stream with Minato Aqua (graduated 2024-08-28) and the twins' guest appearance at her 2025 birthday live. Nekomata Okayu: her enthusiasm for FUWAMOCO and her appearance with Korone at their 3D debut; the twins' 2025 watch-along of her concert. Takane Lui: "TWIN DAY WITH LUI" (2023). Kazama Iroha: a cookie-quiz off-collab (2024). Shirogane Noel: a team Mario Kart event (2023). Kikirara Vivi: #holoREPO (2025). Hoshimachi Suisei: Puyo Puyo coaching (2026). Nakiri Ayame: the 7th fes. stage (2026). La+ Darknesss: a dance short to her song (2026). Sakamata Chloe: a "Gimme Chocolate!!" cover (2024).
````

**Relationship Map rows added in r02 (with sources):**

| Ookami Mio (GAMERS) | JP senior | A mochi-pounding off-collab on Mio's channel (2025-02-07); "Dottabatta Chindouchuu" with Ina at Serendipity (2026) | [Mio channel fQaE6-usUjg] [Official Serendipity report] |

**Evidence notes added:**

- GAMERS ties (author order 2026-11-27; Claude only, Gemini Neon review pending): Mio's mochi-pounding off-collab (fQaE6-usUjg).

### Mococo Abyssgard (`bible/characters/Mococo-Abyssgard.md`)

**[SW] Groups:** FUWAMOCO, hololive -Advent-, hololive English -Advent- (former branch name), Advent, B.F.F

**[SW] Relationships (current, whole field):**

````text
Fuwawa Abyssgard: her older twin, who calls her "Moco-chan"; Mococo has called her dependable, calls her plain "Fuwawa" (she refused to repeat "Fuwa-nee"), and is embarrassed by their "FUWAMOCO sync." Pero: the twins' fictional dog mascot; in the prison-break lore, Mococo throws Pero at the guards. Advent: Shiori (Pen Pups), Bijou (Diamond Dogs), Nerissa (Sound Hounds; Nerissa's "Mofufu" bit). Omaru Polka: her oshi (Phasmophobia with Fubuki and Polka; a guest at their birthday concert). Gigi Murin ("GigiMoco," "bauBau") and Cecilia Immergreen ("Cecemoco"): Justice kouhai who guest-hosted FUWAMOCO MORNING #167 as a FUWAMOCO impersonation bit; Cecilia is also Mococo's Chrono Trigger partner, including 2026 off-collabs; Gigi sang "Bright Tonight" and "MAKE IT, BREAK IT" with the twins. Raora Panthera: their 2026 Serendipity unit partner in B.F.F. Ouro Kronii: "WatchDog." Mori Calliope: "FUWAMOCALLI." Watson Amelia: "Detective Dogs." Nanashi Mumei (graduated 2025): "Fuwamoomco." Hakui Koyori: special guest on FUWAMOCO MORNING ("FUWAMOKOYO," 2024). La+ Darknesss: a dance short to her song (2026). Elizabeth Rose Bloodflame: the twins sang in her 2026 birthday cover "CHA-LA HEAD-CHA-LA." Ookami Mio (GAMERS): a mochi-pounding off-collab (2025) and, with Ina, "Dottabatta Chindouchuu" at Serendipity. Hakos Baelz: Gigi's 2025 Spring Party with FUWAMOCO and Bae; FUWAMOCO danced to "bae-senpai's new song SNAKE EYES" (2026). IRyS, Gigi and Kronii: "Bright Tonight" (2025). Ceres Fauna (graduated): FUWAMOCO helped on the World Tree's last day (2024-12-31). AZKi: a FUWAMOCO-themed GeoGuessr collaboration ("FWMCAZ"); also a singing stream with Minato Aqua (graduated 2024-08-28) and the twins' guest appearance at her 2025 birthday live. Nekomata Okayu: her enthusiasm for FUWAMOCO and her appearance with Korone at their 3D debut; the twins' 2025 watch-along of her concert. Houshou Marine: a Touhou off-collab and Mario Party with Nerissa (2024). Takane Lui: "TWIN DAY WITH LUI" (2023). Kazama Iroha: a cookie-quiz off-collab (2024). Kikirara Vivi: #holoREPO (2025). Shirogane Noel: a team Mario Kart event (2023). Hoshimachi Suisei: a "Chatter Chatter" dance short and Puyo Puyo Tetris 2 coaching (2026). Nakiri Ayame: the 7th fes. stage with Okayu and Ina (2026). Sakamata Chloe: a "Gimme Chocolate!!" cover (2024).
````

**Relationship Map rows added in r02 (with sources):**

| Ookami Mio (GAMERS) | JP senior | A mochi-pounding off-collab on Mio's channel (2025-02-07); "Dottabatta Chindouchuu" with Ina at Serendipity (2026) | [Mio channel fQaE6-usUjg] [Official Serendipity report] |

**Evidence notes added:**

- GAMERS ties (author order 2026-11-27; Claude only, Gemini Neon review pending): Mio's mochi-pounding off-collab (fQaE6-usUjg).

### Hoshimachi Suisei (`bible/characters/Hoshimachi-Suisei.md`)

**[SW] Groups:** hololive, hololive 0th Generation, Star Flower, miComet, Hoshimatic Project, Shiranui Kensetsu, Startend, AS_tar, MOMAS, Midnight Grand Orchestra

**[SW] Relationships (current, whole field):**

````text
Mori Calliope: collaborators on "CapSule" and "Wicked" (2022), including their performance at Calli's concert New Underworld Order, and Calli hosted a watch party of Suisei's first tour. AZKi: 0th-generation labelmate since INoNaKa Music ("AS_tar"); a 2026 horror off-collab and "Going My Way." IRyS: Star Flower with AZKi and Moona Hoshinova ("story time," 2022); "High Tide" with IRyS, Moona and Hakos Baelz at the 2024 English concert. Ninomae Ina'nis and Gawr Gura (graduated): "BIBBIDIBA" with Moona at that concert; Gura and Usada Pekora were fellow featured talents in the July 5, 2024 hololive night collaboration with the Los Angeles Dodgers. Takanashi Kiara: HOLOTALK #8 and a Tales of Arise discussion (2021); a dance-challenge short (2025). Hakos Baelz: a "Moonlight" dance cover (2025). FUWAMOCO: a "Chatter Chatter" dance short and Puyo Puyo Tetris 2 coaching (2026). Nanashi Mumei (graduated): a #bibbidibachallenge short (2024). Nerissa Ravencroft: a "BIBIDEBA" dance short (2024). Koseki Bijou: watched her Fortnite concert on stream (2026). Nekomata Okayu: "MOMAS"; Okayu's 2025 New Year Game Festival team with Nakiri Ayame, Ina, IRyS and Cecilia, among others. Sakura Miko: her miComet partner. Shiranui Flare: "Shiranui Kensetsu," where Suisei is the PR director. Hakui Koyori and Kazama Iroha: her Hoshimatic Project ("BEEP BEEP," 2026); Sakamata Chloe was in its earlier lineup; she coached Iroha at Puyo Puyo Tetris (2023). Houshou Marine: "Chatter Chatter" (2026). Shirogane Noel: a fellow Shiranui Kensetsu member. La+ Darknesss, Nakiri Ayame and Shishiro Botan: holoGTA (2024); La+, Botan and Shirakami Fubuki: featured with her in the m HOLD'EM poker collaboration (2024). Kikirara Vivi: taught her Tetris (2026). Shirakami Fubuki: a watch-along of Suisei's Budokan live (2025).
````

**Relationship Map rows added in r02 (with sources):**

| Shirakami Fubuki (GAMERS) | — | A watch-along of Suisei's Budokan live "SuperNova" on Fubuki's channel (2025-02-01) | [Fubuki channel XYztoXM9Xiw] |

**Evidence notes added:**

- GAMERS ties (author order 2026-11-27; Claude only, Gemini Neon review pending): Fubuki's watch-along (XYztoXM9Xiw).

### AZKi (`bible/characters/AZKi.md`)

**[SW] Groups:** hololive, hololive 0th Generation, Star Flower, SorAZ, AS_tar, AzuIro, KanatAZ, RosaMiA

**[SW] Relationships (current, whole field):**

````text
Hoshimachi Suisei: labelmate since INoNaKa Music and 0th-generation partner ("AS_tar"); a 2026 horror off-collab and "Going My Way." IRyS: Star Flower with Suisei and Moona Hoshinova ("story time," 2022); IRyS covered AZKi's "Inochi" (2021); R.E.P.O. (2025); "A Cruel Angel's Thesis" at AZKi's 2026 birthday live. FUWAMOCO: "FWMCAZ," a FUWAMOCO-themed GeoGuessr map (2024), a singing collab with Minato Aqua (graduated 2024-08-28), and an appearance at her 2025 birthday live. Takanashi Kiara: HOLOTALK's 13th guest (2021); the 2023 Sports Festival white team. Mori Calliope: her English lesson with IRyS and Tsunomaki Watame (2022); AZKi's "Orpheus" dance short (2025). Hakos Baelz: GeoGuessr (2023). Ouro Kronii and Elizabeth Rose Bloodflame: fellow members of Tokoyami Towa's 2025 New Year Game Festival team. Ninomae Ina'nis and Kronii: R.E.P.O. "JP & EN" (2025). Tokino Sora: her SorAZ partner. Amane Kanata (graduated 2025-12-27) and Kazama Iroha: collaborators associated with KanatAZ and AzuIro ("AZUIRO BESTIE DAYS," 2025). Nakiri Ayame: 2023 Sports Festival teammate. Hakui Koyori and Yukihana Lamy: "KoZMy" cover partners on "Ai♡Scream!" (2025). Koyori also joined AZKi, Isaki Riona and Koganei Niko for a four-person 3D karaoke (2026); Lamy is also in "KALAZ" with Amane Kanata. Sakamata Chloe: "Kanaken" with Kanata (Minecraft and a 3D live, 2024). La+ Darknesss: GeoGuessr for Tochigi Day and other games (2025). Nekomata Okayu: Mario Kart World practice for Team Wind (2026-01-16) and AZKi's pun-ASMR contest (2025), with Shirogane Noel also playing. Houshou Marine: AZKi supplied soothing commentary for Marine's Holo Koshien stream (2026). Kikirara Vivi: GeoGuessr on Vivi's channel (2026). Isaki Riona and Mizumiya Su (FLOW GLOW): RoARiS with Roboco (Momotetsu 2, 2026) and guest songs at AZKi's 2026 birthday live. Koganei Niko: holoRUST's "Team AZKi" (2025). Ookami Mio: RosaMiA with Aki Rosenthal ("Blossom Sinfonia," 2026), Mio's first GeoGuessr (2024) and a marshmallow chat (2025). Inugami Korone: School 666 with Lamy and Momosuzu Nene (2026). Shirakami Fubuki: Overcooked! 2 with Omaru Polka (2023).
````

**Relationship Map rows added in r02 (with sources):**

| Isaki Riona, Mizumiya Su, Koganei Niko (FLOW GLOW) | Kouhai | RoARiS (Roboco, AZKi, Su, Riona) in Momotetsu 2 (2026-06-07); Riona and Su as guests at AZKi's 2026 birthday 3D live; the 2026-02-03 self-3D karaoke with Riona, Niko and Koyori; Niko on "Team AZKi" in holoRUST (2025); AZKi's "Ring my name" dance short (2026) | [Archive metadata jG-EPYQ4V9g, M1mZrusy-xY, fqGI67bRcXQ, 1HQL3WJPBHA, 7UaG-JGAdIs, 83cZEqTVdOQ] |
| Ookami Mio, Inugami Korone, Shirakami Fubuki (GAMERS) | RosaMiA with Mio and Aki Rosenthal | GeoGuessr with Mio (2024-12-29); a marshmallow chat (2025-08-18); School 666 with Korone, Lamy and Nene (2026-05-27); Overcooked! 2 with Fubuki and Polka (2023-05-03) | [Mio channel GDOn9JNBAGA, cX-Wir_k3cE] [Korone channel ktEBw4nBpMs] [Fubuki channel iiBvt2jd8ro] [Official music 813] |

**Evidence notes added:**

- Ties to the FLOW GLOW cards (added 2026-11-27 by author order; Claude only, Gemini Neon review pending): archived titles on both channels where listed in the Relationship Map row; covers and dance shorts show that the upload happened, not how close the members are.
- GAMERS ties (author order 2026-11-27; Claude only, Gemini Neon review pending): Mio (GDOn9JNBAGA, cX-Wir_k3cE; RosaMiA, official music 813), Korone (ktEBw4nBpMs), Fubuki (iiBvt2jd8ro).

### Nakiri Ayame (`bible/characters/Nakiri-Ayame.md`)

**[SW] Groups:** hololive, hololive 2nd Generation, FAMS, AyaFubuMi, AyaSuba, Manji-gumi, OKFAMS

**[SW] Relationships (current, whole field):**

````text
Takanashi Kiara: her 23rd HOLOTALK guest (2022) and a 2023 Sports Festival white-team teammate. Nekomata Okayu: "OKFAMS"; Okayu's 2025 New Year Game Festival team, and 7th fes STAGE 1 together. Hoshimachi Suisei, Ninomae Ina'nis, IRyS and Cecilia Immergreen: listed among the members of Okayu's 2025 New Year Game Festival team; Ina and FUWAMOCO shared her 7th fes stage. AZKi, Nanashi Mumei, Watson Amelia and Nerissa Ravencroft: the 2023 Sports Festival white team. Shirakami Fubuki and Ookami Mio: AyaFubuMi (a 2025 anime opening; the originals "OniOniKonKonWaon," 2024, "Irowanioedomo" and "Gokuraku Gokigen Enbiyori," 2026); Fubuki created her companion Poyoyo; FAMS with Oozora Subaru (AyaSuba). Murasaki Shion and Minato Aqua (both graduated, 2025 and 2024): Manji-gumi. Inugami Korone: "Onigashima Combi" (a Clubhouse Games match, 2025; a ReGLOSS 3D-live watch-along with Lui, 2024). Houshou Marine: a third-generation junior whom Ayame admires. La+ Darknesss, Hoshimachi Suisei and Shishiro Botan: holoGTA (2024). Takane Lui: "Onikan" (2025). Shirogane Noel: an Audio-Technica sponsored stream (2025-07-11).
````

**Relationship Map rows added in r02 (with sources):**

| Shirakami Fubuki, Ookami Mio | "AyaFubuMi"; FAMS with Subaru | Their 2025 anime opening; Anime NYC 2026; originals "OniOniKonKonWaon" (2024-01-02), "Irowanioedomo" (2026-03-21) and "Gokuraku Gokigen Enbiyori" (2026-11-14) | [AY2] [Official AY7] [Official music 383, 705, 864] |
| Inugami Korone | "Onigashima Combi" | Clubhouse Games five-match as #鬼ヶ島コンビ (2025-01-16); a ReGLOSS 3D-live watch-along with Lui (2024-09-28) | [AY2] [Korone channel myqzgEEnV1I, 1Q48E6vFA6Y] |

**Evidence notes added:**

- GAMERS ties (author order 2026-11-27; Claude only, Gemini Neon review pending): AyaFubuMi originals (official music 383, 705, 864); #鬼ヶ島コンビ and the ReGLOSS watch-along (Korone channel myqzgEEnV1I, 1Q48E6vFA6Y).

### Nekomata Okayu (`bible/characters/Nekomata-Okayu.md`)

**[SW] Groups:** hololive, hololive GAMERS, OkaKoro, SMOK, OKFAMS, MOMAS, TakoNeko, SubaOka, NYANGUCORN

**[SW] Relationships (current, whole field):**

````text
Ninomae Ina'nis: their pairing is called "TakoNeko"; they released "Kurukuru Cruise" together (2025) and were teammates at the 2025 New Year Game Festival. FUWAMOCO: Okayu's enthusiasm for the twins, her appearance with Korone at their 3D debut (2024) and the twins' 2025 watch-along of her concert. Takanashi Kiara: HOLOTALK's 18th guest (2021). Nanashi Mumei (graduated): a guest at Mumei's 3D live (2024). Mori Calliope: a pop-up Mario Party with Anya and Ao (2024). Gigi Murin: public translation-based banter during the 2026 New Year Game Festival. IRyS and Cecilia Immergreen: members of her 2025 New Year Game Festival team. Hakos Baelz: kart events. Houshou Marine: gave her the nickname "Okanyan." Hoshimachi Suisei: "MOMAS." Nakiri Ayame: "OKFAMS." Inugami Korone: her OkaKoro collaborator and fellow GAMERS member ("Koro-san"). Shirakami Fubuki: her GAMERS and NYANGUCORN partner ("KemomomomomoMof！," 2026). Ookami Mio: GAMERS, OKFAMS and the cover "神或アルゴリズム" (2025). Hakui Koyori: a lateral-thinking puzzle collab (2025). La+ Darknesss: "Dorobo Kensetsu" and a 3D lie-detector challenge (2026). Takane Lui: Harry Potter watch-alongs (2025). AZKi: Mario Kart World practice for Team Wind (2026-01-16) and AZKi's pun-ASMR contest (2025), where Shirogane Noel also played. Kikirara Vivi: a 2026 collab on Vivi's channel. Sakamata Chloe: Okayu contributed chorus vocals to Chloe's "Bling-Bang-Bang-Born" cover (2025). Yukihana Lamy: a "Lukewarm" duet cover (2024). Rindo Chihaya (FLOW GLOW): Minecraft and a voice-impression game (2025) and the cover "打上花火" (2026); Okayu and Korone watched FLOW GLOW's debut (2024).
````

**Relationship Map rows added in r02 (with sources):**

| Shirakami Fubuki, Ookami Mio | GAMERS; "NYANGUCORN," "MiOKayu" | GAMERS fes; Fubuki and Okayu's April Fools furball models (2026); NYANGUCORN's original "KemomomomomoMof！" (2026-04-02); "神或アルゴリズム" with Mio (2025-08-21) | [OK2] [Official music 737] [Mio channel grN8TN-eLk4] |
| Rindo Chihaya (FLOW GLOW) | Kouhai | Minecraft on both channels (2025-02-20); a voice-impression game (2025-03-24); "打上花火" (2026-09-20); Okayu and Korone watched FLOW GLOW's debut (2024-11-09) | [Archive metadata ScqzxDtCIoY, IYBdcw4wWuA, DcfVi2rf1oc, UGQfq16yY1A, rlylHqns09w] |

**Evidence notes added:**

- Solo concerts, GAMERS concerts, two million in May 2025: secondary event histories. "Okayu Nyūmu!" star and supervisor: secondary coverage; the 2026 sequel's publisher supports her starring role.
- Ties to the FLOW GLOW cards (added 2026-11-27 by author order; Claude only, Gemini Neon review pending): archived titles on both channels where listed in the Relationship Map row; covers and dance shorts show that the upload happened, not how close the members are.
- GAMERS cohort (2026-11-27): NYANGUCORN added to Groups (official music credit, "KemomomomomoMof！," 2026-04-02, https://hololive.hololivepro.com/en/music/737/).
- GAMERS ties (author order 2026-11-27; Claude only, Gemini Neon review pending): NYANGUCORN's original (official music 737) and the Mio cover (grN8TN-eLk4) added to Relationships and the map.

### Houshou Marine (`bible/characters/Houshou-Marine.md`)

**[SW] Groups:** hololive, hololive 3rd generation, hololive Fantasy, UMISEA, holoWitches, Bara☆Dice, Yakamashi Musume, BABACORN, Blue Journey, MVP

**[SW] Relationships (current, whole field):**

````text
Usada Pekora: hololive Fantasy genmate ("PekoMari"); in 2026 Pekora coached her at Mario Tennis ("Pekoach"). Shirogane Noel: hololive Fantasy genmate; Bara☆Dice with Takane Lui, Shiranui Flare, Momosuzu Nene and Kazama Iroha; separately, Yakamashi Musume with Yukihana Lamy and Inugami Korone. Hoshimachi Suisei: "Chatter Chatter" (2026). Kikirara Vivi: the unit MVP with Pekora (2026). Yukihana Lamy: Yakamashi Musume, holoWitches and Blue Journey. Hakui Koyori: "#頭ピンク組," their "pink-haired pair" (a race and a talk testing whether they are alike, 2025); Blue Journey. La+ Darknesss: a sponsored collab billed #マリラプ and a cover with Koyori (2025). Takane Lui and Kazama Iroha: Bara☆Dice. Sakamata Chloe (affiliate): UMISEA and holoWitches. Nekomata Okayu: Marine gave her the nickname "Okanyan" (Okayu's official profile). Takanashi Kiara: her first HOLOTALK guest (2020) and dance shorts ("MIRAGE," "III," 2024). Mori Calliope: Calli's English lesson #01 (2022), Mario Kart (2021) and a house-party off-collab with Bae (2023). Hakos Baelz: that Mario Kart and house party; Bae and Mumei played the horror game featuring Marine (2023). Ninomae Ina'nis and Gawr Gura (graduated): UMISEA; English lesson #01 with Ina and a guest spot at Ina's "Pleides" (2024); "SHINKIRO" with Gura (2023). FUWAMOCO: a Touhou off-collab and Mario Party Superstars with Nerissa (2024). Nerissa Ravencroft: that Mario Party off-collab. Elizabeth Rose Bloodflame: "IT'S LOVE" with Korone for Elizabeth's 2026 birthday. Nakiri Ayame: a second-generation senior. AZKi: commentary for her Holo Koshien stream (2026). Mizumiya Su (FLOW GLOW): a 2025 collab on Marine's channel in which Su made her a "pet." Shirakami Fubuki: BABACORN (a 2023 call-in, Cubic Stars), Content Warning with Shishiro Botan and Oozora Subaru (2024) and "Kami-Tsumo Dora Dora Densetsu" with Aki Rosenthal and Ichijou Ririka (2026). Inugami Korone: a film talk after interviewing a director (2026).
````

**Relationship Map rows added in r02 (with sources):**

| Mizumiya Su (FLOW GLOW) | Kouhai | A collab framed as Su making Marine her "pet" (2025-06-29) | [Archive metadata zpG2xKGK_Jo] |
| Shirakami Fubuki, Inugami Korone (GAMERS) | "BABACORN" with Fubuki; Yakamashi Musume with Korone | A #BABACORN call-in (2023-03-16) and Cubic Stars (2023-06-07); Content Warning with Botan and Subaru (2024-04-23); "Kami-Tsumo Dora Dora Densetsu" (2026-11-05); a film talk with Korone after a director interview (2026-03-19) | [Fubuki channel pmMqFJm9bHc, LR9JXY2c7xI, U33SciUF0WQ] [Official music 839] [Korone channel x3V1BH5tT-4] |

**Evidence notes added:**

- Ties to the FLOW GLOW cards (added 2026-11-27 by author order; Claude only, Gemini Neon review pending): archived titles on both channels where listed in the Relationship Map row; covers and dance shorts show that the upload happened, not how close the members are.
- GAMERS cohort (2026-11-27): BABACORN (with Shirakami Fubuki) added to Groups: archived #BABACORN title on Fubuki's channel (pmMqFJm9bHc, 2023-03-16).
- GAMERS ties (author order 2026-11-27; Claude only, Gemini Neon review pending): Fubuki (pmMqFJm9bHc, LR9JXY2c7xI, U33SciUF0WQ; official music 839) and Korone (x3V1BH5tT-4).

### Shirogane Noel (`bible/characters/Shirogane-Noel.md`)

**[SW] Groups:** hololive, hololive 3rd generation, hololive Fantasy, NoeFure, Bara☆Dice, Shiranui Kensetsu, Yakamashi Musume, Blue Journey

**[SW] Relationships (current, whole field):**

````text
Houshou Marine: hololive Fantasy genmate; Bara☆Dice with Takane Lui, Shiranui Flare, Momosuzu Nene and Kazama Iroha; separately, Yakamashi Musume with Yukihana Lamy and Inugami Korone; 3rd-gen R.E.P.O. (2025). Shiranui Flare: hololive Fantasy genmate ("NoeFure," a label from Noel's own stream titles); any mock jealousy is on-stream comedy. Yukihana Lamy: Yakamashi Musume and drinking-talk collabs. Hoshimachi Suisei: "Shiranui Kensetsu" (Shiraken), the Minecraft construction company with Flare, Omaru Polka and Sakura Miko. Nakiri Ayame: an Audio-Technica sponsorship collab (2025). Hakui Koyori: "#ノエこよ," a Power Pros baseball exhibition (2025), and Blue Journey (2023). Takane Lui and Kazama Iroha: Bara☆Dice. Kikirara Vivi: Gartic Phone (2025). Takanashi Kiara: her 22nd HOLOTALK guest (2022). Mori Calliope: HOLOYOI #02 with Flare (2023). FUWAMOCO and Hakos Baelz: a team Mario Kart event (2023); FUWAMOCO danced to "TREVIAN KNIGHT" (2025). Nanashi Mumei (graduated), Ninomae Ina'nis, Ouro Kronii and Elizabeth Rose Bloodflame: Gartic Phone EN + ID + JP (2025). AZKi and Nekomata Okayu: fellow players in AZKi's 3D pun-ASMR contest (2025). Inugami Korone: a Star Wars club with Himemori Luna (2025). Shirakami Fubuki and Kazama Iroha: a cup-noodle tasting with Aki Rosenthal (2024).
````

**Relationship Map rows added in r02 (with sources):**

| Inugami Korone, Shirakami Fubuki (GAMERS) | Yakamashi Musume with Korone | #ホロライブスターウォーズ部 with Korone and Luna (2025-05-03); a cup-noodle tasting with Fubuki, Aki and Iroha (2024-05-17) | [Korone channel VNJNilMuHZk] [Fubuki channel fQmhewlBr80] |

**Evidence notes added:**

- GAMERS ties (author order 2026-11-27; Claude only, Gemini Neon review pending): Korone (VNJNilMuHZk), Fubuki (fQmhewlBr80).

### Yukihana Lamy (`bible/characters/Yukihana-Lamy.md`)

**[SW] Groups:** hololive, hololive 5th generation, NePoLaBo, KALAZ, KoZMy, Yakamashi Musume, holoWitches, NePoX, Blue Journey

**[SW] Relationships (current, whole field):**

````text
Shishiro Botan: 5th-gen genmate and NePoLaBo partner; horror runs where Lamy is scared and Botan stays calm. Momosuzu Nene and Omaru Polka: 5th-gen genmates and NePoLaBo (a 3D party, 2026); "Magamaga's" with Nene. AZKi: her KoZMy cover partner with Hakui Koyori on "Ai♡Scream!" (2025). Hakui Koyori: KoZMy (2025) and a March 2026 off-collab titled to name their duo. Houshou Marine and Shirogane Noel: "Yakamashi Musume" with Inugami Korone, and Blue Journey; Marine is also in holoWitches. La+ Darknesss, Takane Lui, Kazama Iroha and Hakui Koyori: NePoX, the 2026 NePoLaBo × holoX events. Ninomae Ina'nis: a Minecraft festival and a Minecraft collab billed as a "date" (2021), and a guest at Ina's 3D live "Pleides" (2024). Sakamata Chloe (affiliate): Rust with Amane Kanata (2022). Nekomata Okayu: a "Lukewarm" duet cover (2024). Gawr Gura, Watson Amelia and Mori Calliope: co-players in the Myth × fifth-generation Among Us collab (2020). Koganei Niko (FLOW GLOW): #にこらみ晩酌, an off-collab drinking stream (2024). Isaki Riona and Rindo Chihaya: Gang Beasts with Nene (2025). Inugami Korone: #やかまし娘 Cuphead and R.E.P.O. (2025) and School 666 with AZKi and Nene (2026). Shirakami Fubuki: White Cat Golf with Hakui Koyori (2022).
````

**Relationship Map rows added in r02 (with sources):**

| Koganei Niko, Isaki Riona, Rindo Chihaya (FLOW GLOW) | Kouhai | #にこらみ晩酌 with Niko (2024-12-22); Gang Beasts with Nene, Riona and Chihaya (2025-01-20) | [Archive metadata Ig_Ba2h9DZc, EsfZ7Ny4aPA] |
| Inugami Korone, Shirakami Fubuki (GAMERS) | Yakamashi Musume with Korone | #やかまし娘 Cuphead (2025-08-09) and R.E.P.O. (2025-07-14); School 666 with AZKi and Nene (2026-05-27); White Cat Golf with Fubuki and Koyori (2022-11-11) | [Korone channel Xx6XUFllIO8, RjIUPjfdhSY, ktEBw4nBpMs] [Fubuki channel Rfq9c8h3LPY] |

**Evidence notes added:**

- Ties to the FLOW GLOW cards (added 2026-11-27 by author order; Claude only, Gemini Neon review pending): archived titles on both channels where listed in the Relationship Map row; covers and dance shorts show that the upload happened, not how close the members are.
- GAMERS ties (author order 2026-11-27; Claude only, Gemini Neon review pending): Korone (Xx6XUFllIO8, RjIUPjfdhSY, ktEBw4nBpMs), Fubuki (Rfq9c8h3LPY).

### Shishiro Botan (`bible/characters/Shishiro-Botan.md`)

**[SW] Groups:** hololive, hololive 5th generation, NePoLaBo, holoFive, NePoX, InuTakaShishiRam, Usada Kensetsu, SubaChocoLunaTan

**[SW] Relationships (current, whole field):**

````text
Yukihana Lamy: 5th-gen genmate and NePoLaBo partner; horror "dates" where Botan stays calm and teases Lamy. Momosuzu Nene and Omaru Polka: 5th-gen genmates and NePoLaBo. Takane Lui: "InuTakaShishiRam" with Inugami Korone and Tsunomaki Watame; Left 4 Dead 2 (2022) and Overwatch 2 (2023) together. La+ Darknesss, Hakui Koyori and Kazama Iroha: NePoX (NePoLaBo × holoX, 2026). La+ Darknesss and Hoshimachi Suisei: holoGTA and, with Shirakami Fubuki, the m HOLD'EM poker collaboration (2024); Nakiri Ayame: holoGTA (2024). IRyS: Left 4 Dead 2 with Lui and Korone (2022) and an Overwatch 2 team with Lui, Sakamata Chloe and Tokoyami Towa (2023). Takanashi Kiara: a fellow member of the Minecraft "Usada Kensetsu" and an Among Us co-player in the Myth × fifth-generation collab (2020), with Watson Amelia. Gawr Gura (graduated): "Apex Predators." Mori Calliope: HOLOYOI #03 with Oozora Subaru (2023). Hakos Baelz: BAE-GEMITE DOMINATION #2 with Subaru (2023). Ninomae Ina'nis: a guest at Ina's birthday 3D live "EVERMORE" (2025), singing "storia" with Ina and Watame. Nerissa Ravencroft: credited as a guest in Botan's birthday 3D live "Stray&Stay" (2026). Shirakami Fubuki: Content Warning with Marine and Oozora Subaru (2024) and EDF5 with Koyori (2022). Inugami Korone: Machine Party as #いぬたかししらむ (2026) and a jump-scare game on Korone's channel (2025).
````

**Relationship Map rows added in r02 (with sources):**

| Shirakami Fubuki, Inugami Korone (GAMERS) | — | Content Warning with Fubuki, Marine and Subaru (2024-04-23); EDF5 with Fubuki and Koyori (2022-05-06); Jumpscare Scare Jump on Korone's channel (2025-05-26); #いぬたかししらむ Machine Party (2026-09-29) | [Fubuki channel U33SciUF0WQ, KtzsKY807hY] [Korone channel Xq43wV29LW8, Wc1kJDN-xtQ] |

**Evidence notes added:**

- GAMERS ties (author order 2026-11-27; Claude only, Gemini Neon review pending): Fubuki (U33SciUF0WQ, KtzsKY807hY), Korone (Xq43wV29LW8, Wc1kJDN-xtQ).

### Kikirara Vivi (`bible/characters/Kikirara-Vivi.md`)

**[SW] Groups:** hololive, FLOW GLOW, MVP

**[SW] Relationships (current, whole field):**

````text
Usada Pekora: "PekoVivi"; co-op games (2025) and a gifted Getting Over It (2026); Pekora rescued her in Minecraft and Vivi calls her the "legendary hero." Houshou Marine: MVP with Pekora (2026). Shirogane Noel: Mumei's Gartic Phone collab (2025). FLOW GLOW (Isaki Riona, Koganei Niko, Mizumiya Su, Rindo Chihaya): her unit, led by Riona. Mizumiya Su: duets "らぶきゅん♡うぉんてっど" and "クリームで会いにいけますか" and a Forza Horizon 6 drive (2026). Rindo Chihaya: the duet "Bridal Dream" (2025). Koganei Niko: SuperBunnyMan (#ヴィヴィガー, 2024) and Minecraft (2025). FUWAMOCO: watched FLOW GLOW's debut with Bijou (2024); R.E.P.O. with Bae (2025-05-25). Hakos Baelz: that R.E.P.O. session. Ninomae Ina'nis: a separate R.E.P.O. session on Ina's stream (2025-06-02) and the Gartic Phone collab. Ouro Kronii and Elizabeth Rose Bloodflame: Gartic Phone (2025). Nanashi Mumei (graduated): hosted that Gartic Phone collab. Koseki Bijou: watched FLOW GLOW's debut with FUWAMOCO. AZKi: GeoGuessr (2026). Hoshimachi Suisei: taught her Tetris on Vivi's channel (2026). Nekomata Okayu: a 2026 collab billed with a mock-scandalized "やーらし." Inugami Korone: Vivi gave her the game SPAGHET (2026).
````

**Relationship Map rows added in r02 (with sources):**

| 2025 | FLOW GLOW songs "24K GOLD" (03-14), "LOAD" (07-09), "good enough" (09-21, official release date); 500,000 subscribers (11-30, secondary) | [Observed VI2] |
| 2026 | FLOW GLOW's self-titled album (01-21, including "PUNISHER" and "the light"); first on-stream Super Mario Bros. 3 and Super Mario World playthroughs; Getting Over It, a gift from Pekora (07-25); 700,000 subscribers during an endurance karaoke (08-11, secondary); FLOW GLOW's "magic summer" (08-19, official release date); MVP's "Hatsukoi Cider" with Marine and Pekora (09, secondary record) | [Official music 024] [VI4] [Observed VI2] [MVP upload record] |
| Inugami Korone (GAMERS) | Senpai | Korone played SPAGHET, a game Vivi gave her (2026-08-05) | [Korone channel LriXEkMQGAc] |

**Evidence notes added:**

- EN-cast items: archived metadata. FUWAMOCO and Bijou watching FLOW GLOW's debut: a secondary archive.
- Ties to the FLOW GLOW cards (added 2026-11-27 by author order; Claude only, Gemini Neon review pending): archived titles on both channels where listed in the Relationship Map row; covers and dance shorts show that the upload happened, not how close the members are.
- GAMERS ties (author order 2026-11-27; Claude only, Gemini Neon review pending): Korone's SPAGHET stream (LriXEkMQGAc).

### La+ Darknesss (`bible/characters/Laplus-Darknesss.md`)

**[SW] Groups:** hololive, Secret Society holoX, holoX, NePoX

**[SW] Relationships (current, whole field):**

````text
Takane Lui: holoX's executive officer, who actually runs things and reins her in. Hakui Koyori and Kazama Iroha: holoX; her pairing with Iroha is called "Irohasu." Sakamata Chloe (affiliate since 2025): the former intern; covers together (2022, 2025). Takanashi Kiara: "Glow in the Dark" (Mythmash) and "FAKE HEART" (2025), and a nostalgic-games off-collab (2023). Mori Calliope and Gawr Gura (graduated): Calli's English lesson #02 (2022). FUWAMOCO: shorts of them performing to "Onee-sama♡Love Call" (2026). Cecilia Immergreen: an "ONEE-SAMA!" short about her (2026). Nerissa Ravencroft, Nakiri Ayame, Hoshimachi Suisei and Shishiro Botan: fellow holoGTA participants (2024). Suisei, Botan and Shirakami Fubuki: featured with her in the m HOLD'EM poker collaboration (2024). Nekomata Okayu: a 3D lie-detector challenge (2026); grouped in "Dorobo Kensetsu." AZKi: games in 2025; an animated short on La+'s channel uploaded in 2026 depicts her reaction to AZKi's ASMR. Houshou Marine: a sponsored collab billed #マリラプ and a cover with Koyori (2025). Yukihana Lamy and Shishiro Botan: NePoX (2026). Shirakami Fubuki: "インターネットサバイバー," a Touhou PV song featuring La+ (2023).
````

**Relationship Map rows added in r02 (with sources):**

| Shirakami Fubuki (GAMERS) | — | "インターネットサバイバー（白上フブキ feat.ラプラス・ダークネス）" (2023-03-21) | [Fubuki channel g_6-sM3t760] |

**Evidence notes added:**

- GAMERS ties (author order 2026-11-27; Claude only, Gemini Neon review pending): Fubuki's song featuring La+ (g_6-sM3t760).

### Takane Lui (`bible/characters/Takane-Lui.md`)

**[SW] Groups:** hololive, Secret Society holoX, holoX, HOLOTORI, Bara☆Dice, Blue Journey, InuTakaShishiRam, NePoX

**[SW] Relationships (current, whole field):**

````text
La+ Darknesss: holoX's founder, whom Lui reins in and covers for. Sakamata Chloe (affiliate since 2025): the intern she used to keep in line. Hakui Koyori and Kazama Iroha: holoX; Iroha calls her "Lui-nee." Takanashi Kiara: HOLOTORI; a Wario off-collab (2023). Nanashi Mumei (graduated): HOLOTORI; "Q&A With Bird Sisters" (2025). Mori Calliope: English practice (2021), lesson #04 (2022), "HOLOYOI" (2023). FUWAMOCO: "TWIN DAY WITH LUI" (2023). Hakos Baelz: "BAE-GEMITE DOMINATION" (2023) and a "FEAST" dance short (2025). IRyS and Ouro Kronii: Minecraft with Kaela (2022). Watson Amelia (affiliate): Apex with Iofi (2022). Nekomata Okayu: Harry Potter watch-alongs (2025); both are in "Dorobo Kensetsu." Nakiri Ayame: "Onikan" (2025). Shishiro Botan: "InuTakaShishiRam" with Inugami Korone and Tsunomaki Watame (2023); Left 4 Dead 2 with IRyS and Korone (2022); Blue Journey. Houshou Marine, Shirogane Noel and Kazama Iroha: Bara☆Dice (with Flare and Nene). Yukihana Lamy: NePoX (2026). Nerissa Ravencroft, Koseki Bijou, Gigi Murin and Raora Panthera: animated "Soar" shorts (2026). Koganei Niko (FLOW GLOW): Minecraft and horror runs Lui watched over (2025). Isaki Riona: Minecraft (2025). Rindo Chihaya: a horse-racing stream (2025). Shirakami Fubuki: Virtual-On and mahjong off-collabs (2025), Galaxy Burger with Mio and Okayu (2024) and a ZIGZAG dance short. Ookami Mio: holoGTA (2024) and a ZIGZAG dance short (2025). Inugami Korone: #ルイころ (2025) and Machine Party as #いぬたかししらむ (2026).
````

**Relationship Map rows added in r02 (with sources):**

| Koganei Niko, Isaki Riona, Rindo Chihaya (FLOW GLOW) | Kouhai | Minecraft with Niko (2025-03-02) and with Riona (2025-03-17); Lui watched over Niko's Shadow Corridor runs (2025-04); a February Stakes horse-racing stream with Chihaya (2025-02-23) | [Archive metadata IvzEZcBdmNk, pB3e3SzBjJ8, hlb4XXjpf4M, Lh7LPWpmCEI] |
| Shirakami Fubuki, Ookami Mio, Inugami Korone (GAMERS) | — | Virtual-On (2025-03-14) and mahjong (2025-04-01) off-collabs with Fubuki; Galaxy Burger with Fubuki, Mio and Okayu (2024-12-03); ZIGZAG dance shorts with Fubuki and with Mio (2025); holoGTA with Mio (2024-09-20); #ルイころ (2025) and #いぬたかししらむ Machine Party (2026-09-29) with Korone | [Fubuki channel AnhxVnLpGR0, 80Se1st9Zyk, YT4yL2_3-Rw, 7cseBNYCrkM] [Mio channel UX52XaorEfY, Rjwd8WGH2kY] [Korone channel Wc1kJDN-xtQ] [GAMERS card 4LDafBjiNdg] |

**Evidence notes added:**

- Ties to the FLOW GLOW cards (added 2026-11-27 by author order; Claude only, Gemini Neon review pending): archived titles on both channels where listed in the Relationship Map row; covers and dance shorts show that the upload happened, not how close the members are.
- GAMERS ties (author order 2026-11-27; Claude only, Gemini Neon review pending): Fubuki (AnhxVnLpGR0, 80Se1st9Zyk, YT4yL2_3-Rw, 7cseBNYCrkM), Mio (UX52XaorEfY, Rjwd8WGH2kY), Korone (Wc1kJDN-xtQ, 4LDafBjiNdg).

### Hakui Koyori (`bible/characters/Hakui-Koyori.md`)

**[SW] Groups:** hololive, Secret Society holoX, holoX, Hoshimatic Project, KoZMy, NePoX, Blue Journey

**[SW] Relationships (current, whole field):**

````text
La+ Darknesss: holoX's founder; a sponsored "#stons" collab (2024) and a cover with Marine (2025). Takane Lui and Kazama Iroha: holoX; Lui: Blue Journey (2023). Sakamata Chloe (affiliate since 2025): "KoyoChlo," a running "disband!" gag from their co-op games; their last collab before Chloe's graduation and the duet cover 「一番の宝物」 (January 2025). AZKi and Yukihana Lamy: "KoZMy" (2025); a self-3D karaoke with AZKi, Isaki Riona and Koganei Niko (2026); a #ラミこよ off-collab with Lamy (2026). Houshou Marine: billed as the "pink-haired pair"; Blue Journey; Marine backseats her Pikachu game (2025). Shirogane Noel: Blue Journey and "NoeKoyo" baseball (2025). Hoshimachi Suisei: Hoshimatic Project. Shishiro Botan: NePoX and Blue Journey. Nekomata Okayu: a lateral-thinking puzzle collab she hosted (2025). FUWAMOCO: "FUWAMOKOYO" on FUWAMOCO Morning (2024), Lethal Company with them and Shirakami Fubuki (2024), their birthday concert (2025). Hakos Baelz: BAE-GEMITE DOMINATION with Nene and a KHAOS KITCHEN tasting (2023). Nanashi Mumei (graduated): a guest at her first 3D live (2024). IRyS: Splatoon 3 (2022) and Among Us (2023). Takanashi Kiara: a "MIRAGE" dance short (2024). Mizumiya Su (FLOW GLOW): #こよすう, their first one-on-one collab (2025). Isaki Riona: holoRUST together (2025). Shirakami Fubuki: #こんこんこよーて New Year card-pack openings (2024, 2025), EDF5 with Shishiro Botan (2022) and White Cat Golf with Lamy (2022). Inugami Korone: a manzai (2022).
````

**Relationship Map rows added in r02 (with sources):**

| Mizumiya Su, Isaki Riona, Koganei Niko (FLOW GLOW) | Kouhai | #こよすう with Su (2025-02-02); holoRUST with Riona (2025); the 2026-02-03 self-3D karaoke with AZKi, Riona and Niko | [Archive metadata f4K54Fc-ghM, l50dJY8DxqM, 1HQL3WJPBHA] |
| Shirakami Fubuki, Inugami Korone (GAMERS) | #こんこんこよーて with Fubuki | Card-pack openings (2024-01-04, 2025-01-04); EDF5 with Fubuki and Botan (2022-05-06); White Cat Golf with Fubuki and Lamy (2022-11-11); a manzai with Korone (2022-12-15) | [Fubuki channel cFwsRVbUQaQ, 8dZ9atjf4WA, KtzsKY807hY, Rfq9c8h3LPY] [Korone channel hNqFWgDcvXM] |

**Evidence notes added:**

- Ties to the FLOW GLOW cards (added 2026-11-27 by author order; Claude only, Gemini Neon review pending): archived titles on both channels where listed in the Relationship Map row; covers and dance shorts show that the upload happened, not how close the members are.
- GAMERS ties (author order 2026-11-27; Claude only, Gemini Neon review pending): Fubuki (cFwsRVbUQaQ, 8dZ9atjf4WA, KtzsKY807hY, Rfq9c8h3LPY), Korone (hNqFWgDcvXM).

### Sakamata Chloe (`bible/characters/Sakamata-Chloe.md`)

**[SW] Groups:** hololive, Secret Society holoX (until 2025), holoX, KoyoChlo, Kanaken, holoWitches, UMISEA

**[SW] Relationships (current, whole field):**

````text
Takane Lui: holoX's executive officer; Lui reins her in; "LuiChlo" collabs, Calli's English lesson and HOLOYOI together. Hakui Koyori: "KoyoChlo," a duo with a running "disband!" gag; their last collab and two covers in January 2025. La+ Darknesss: covers together (2022, 2025). Kazama Iroha: holoX; the duet cover "Gehenna" on her last day (2025-01-26). AZKi: "Kanaken" with Amane Kanata (graduated 2025-12-27) (Minecraft, Chained Together, a 3D live, 2024). Houshou Marine: UMISEA (official 2023 roster) and holoWitches. Hoshimachi Suisei: the original Hoshimatic Project lineup; a farewell video together (2025). Yukihana Lamy: Rust with Kanata (2022). Shishiro Botan: an Overwatch 2 team (2023). Takanashi Kiara: "WILDCARD," performed at the 2024 fes and released as a cover in her final week (2025), and an origami off-collab (2023). Hakos Baelz: the EN Minecraft tour (2022), BAE-GEMITE DOMINATION and "Crazy Scary Holy Fantasy" (2023). Mori Calliope: HOLO ENGLISH LESSON #04 (2022) and HOLOYOI #01 (2023). Nanashi Mumei (graduated): the EN Minecraft tour (2022). IRyS: Overwatch 2 and Among Us (2023). Ninomae Ina'nis and Gawr Gura (graduated): UMISEA (official 2023 roster). Nekomata Okayu: chorus on her "Bling-Bang-Bang-Born" cover (2025). Fuwawa and Mococo Abyssgard: a "Gimme Chocolate!!" cover together (2024). Rindo Chihaya (FLOW GLOW): a talk collab on Chihaya's channel (2024).
````

**Relationship Map rows added in r02 (with sources):**

| Rindo Chihaya (FLOW GLOW) | Kouhai | A talk collab on Chihaya's channel (2024-12-12) | [Archive metadata FgSn_JCgKyk] |

**Evidence notes added:**

- Ties to the FLOW GLOW cards (added 2026-11-27 by author order; Claude only, Gemini Neon review pending): archived titles on both channels where listed in the Relationship Map row; covers and dance shorts show that the upload happened, not how close the members are.

### Kazama Iroha (`bible/characters/Kazama-Iroha.md`)

**[SW] Groups:** hololive, Secret Society holoX, holoX, AzuIro, Hoshimatic Project, NePoX, Bara☆Dice

**[SW] Relationships (current, whole field):**

````text
AZKi: "AzuIro," her steady duo (covers, "AZUIRO BESTIE DAYS" in 2025, Cuphead and off-collabs billed as summer camps). La+ Darknesss: holoX's founder; a cover together (2024). Takane Lui: a cover together (2024); she calls Lui "Lui-nee." Hakui Koyori: holoX genmate. Sakamata Chloe (affiliate since 2025): the duet cover "Gehenna" on Chloe's last day (2025). Hoshimachi Suisei: Hoshimatic Project ("BEEP BEEP," 2026); coached her at Puyo Puyo Tetris (2023). Yukihana Lamy and Shishiro Botan: NePoX. Houshou Marine and Shirogane Noel: fellow Bara☆Dice vocalists (distributor credits). Takanashi Kiara: a credited guest at Kiara's 2024 and 2025 lives; #TASTYchallenge shorts with Nene (2025). Watson Amelia (affiliate): a VALORANT collab with Kobo Kanaeru (2022; the trio "KoMeHa"). Mori Calliope and Gawr Gura (graduated): Calli's English lesson #02 (2022). FUWAMOCO: challengers in the cookie battle she and AZKi presented (2024). Elizabeth Rose Bloodflame: "CHA-LA HEAD-CHA-LA" from her 2026 birthday show, with FUWAMOCO. Shirakami Fubuki: a cup-noodle tasting with Noel and Aki Rosenthal (2024) and a #めぇぷるしろっぷう collab with Tsunomaki Watame (2023).
````

**Relationship Map rows added in r02 (with sources):**

| Shirakami Fubuki (GAMERS) | — | A cup-noodle tasting with Fubuki, Aki and Noel (2024-05-17); #めぇぷるしろっぷう with Fubuki and Watame (2023-11-22) | [Fubuki channel fQmhewlBr80, s18jJY5MbzM] |

**Evidence notes added:**

- GAMERS ties (author order 2026-11-27; Claude only, Gemini Neon review pending): Fubuki (fQmhewlBr80, s18jJY5MbzM).
