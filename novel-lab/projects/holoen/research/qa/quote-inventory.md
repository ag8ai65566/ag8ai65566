# Spoken lines resting only on secondary transcriptions (quotation pass, Claude, 2026-10-04)

Source of the finding: jp:JP-QUOTE-001 (P0 before release), which follows P1's rule that a spoken quotation needs the
two-model gate: both ASR models, the same window, a contiguous shared span and the member as the speaker. Claude
traced every quoted string in the exported speech fields (Personality, Dialogue Style, Catchphrases, Voice & Delivery,
Audio Tags) to its dossier evidence tags and source records. Nicknames, pair names, fan names, titles, posts and
official wording are out of scope (labels and written text, not speech). The five holoX cards wait for voice audit v4.

## Two-model checks run for this pass

New windows (stream openings and endings) and existing windows were run through both models. Results are recorded in the audio reports
(rows marked "quotation pass"):
- **Confirmed and upgraded on the cards and sheets:**
  - Marine's "Shukkō!" sign-off, at the end of two streams.
  - Noel's "Ohamassuru".
  - Bae's "Bruh.".
- **Not confirmed:**
  - Noel's "Konbanmassuru": the second model hears 「こんばんは」.
  - Lamy's "Konlamy desu": the opening five minutes are the waiting screen.
  - Ayame's "Yo da yo!": not heard.
  - AZKi's 「この野郎」: both models hear it, but the speaker is the game's voiced narrator.
  - Bae's full self-introduction: the two models share only "I'm Chaos, the end of" and "your best friend". span_check now flags the wiki version, which is correct.

## The decision (author)

The lines below are exported verbatim with a "secondary"/"wiki" label, or with no label, and their only evidence is a
fan wiki or other secondary transcription. Every one is kept in its dossier with its label; the question is only the
exported fields that Sudowrite reads.
- **A. Strict (the P1 rule as written):** paraphrase each line out of the exported fields. For example, "Mococo
  builds Pup Talks to a cheer" instead of quoting the cheer. Release check V13 can then pass.
- **B. Keep labelled:** leave them in the exports with their secondary label, as voice audits v1–v3 accepted. V13
  then attests an author exception for these lines.
- **C. Mixed:** keep short stock catchphrases and greetings (five words or fewer) labelled. Paraphrase the longer
  sentences.

Until the author decides, nothing below is removed. V13 stays blocked.

## Inventory (93 lines, 25 cards; approximate, from the tracer)

| Card | Line | Exported in |
|---|---|---|
| AZKi | kono yarō | Catchphrases |
| Cecilia-Immergreen | Ew! Get away from me, you FREAK! | Catchphrases |
| Cecilia-Immergreen | For Justice! | Catchphrases |
| Cecilia-Immergreen | I hate… | Catchphrases, Dialogue Style |
| Cecilia-Immergreen | I'm not a hag. I'm ancient, it's different | Catchphrases |
| Cecilia-Immergreen | Let's wind you up! | Catchphrases |
| Cecilia-Immergreen | when people say 'I guess' | Personality |
| Ceres-Fauna | four and a half billion | Catchphrases |
| Elizabeth-Rose-Bloodflame | By royal decree, my sweet Rosarians… | Catchphrases |
| Elizabeth-Rose-Bloodflame | Oh, you mothertrucker… | Dialogue Style |
| Elizabeth-Rose-Bloodflame | Roses are red, the fire of my heart is blue… | Catchphrases |
| Elizabeth-Rose-Bloodflame | What the Frigg! | Dialogue Style |
| Fuwawa-Abyssgard | Bau bau! | Catchphrases |
| Fuwawa-Abyssgard | I'm not a chihuahua, I'm Fuwawa! | Catchphrases |
| Fuwawa-Abyssgard | No support is small | Catchphrases |
| Fuwawa-Abyssgard | Oh my gosh! | Catchphrases |
| Fuwawa-Abyssgard | Refridgator! | Catchphrases, Dialogue Style, Personality |
| Fuwawa-Abyssgard | Wuffians | Audio Tags |
| Fuwawa-Abyssgard | Zero is where the math stops | Catchphrases |
| Gawr-Gura | (when teased about being flat); | Catchphrases |
| Gawr-Gura | Ka-chow! | Audio Tags, Dialogue Style |
| Gawr-Gura | Parkour! | Dialogue Style |
| Gigi-Murin | Boat goes binted! | Catchphrases |
| Gigi-Murin | DON'T TELL LIZ! | Dialogue Style |
| Gigi-Murin | MORI CALLIOPE! | Dialogue Style, Catchphrases |
| Gigi-Murin | Ouchi! | Catchphrases |
| Gigi-Murin | PPEEWEASEEEEE | Dialogue Style |
| Gigi-Murin | What do you meaaaaaan? | Catchphrases |
| Gigi-Murin | Why?! WHY, WHY, WHY?! | Catchphrases |
| Hakos-Baelz | BIG BRAIN! | Catchphrases |
| Hakos-Baelz | Bae is stoopid | Catchphrases |
| Hakos-Baelz | I am Chaos the end of ends, a steel rose trapped in a cage of ice, your best friend Baelz Hakos | Catchphrases |
| Hakos-Baelz | JDON MY SOUL | Catchphrases |
| Hakos-Baelz | ORA ORA ORA | Catchphrases |
| Hakos-Baelz | SARABA DA! | Catchphrases |
| Hoshimachi-Suisei | Hi, honey! | Catchphrases, Audio Tags |
| IRyS | Yoisho~ | Audio Tags, Catchphrases |
| IRyS | a hundred percent seiso | Catchphrases, Dialogue Style |
| Koseki-Bijou | dang it! | Audio Tags, Catchphrases, Dialogue Style, Personality |
| Mococo-Abyssgard | Bau bau! | Catchphrases |
| Mococo-Abyssgard | Haeh? | Dialogue Style |
| Mococo-Abyssgard | I'm not Fuwawa, I'm Mococo! | Catchphrases |
| Mococo-Abyssgard | I'm the danger! | Catchphrases, Dialogue Style |
| Mococo-Abyssgard | Mococo Pup Talks | Personality |
| Mococo-Abyssgard | Not tomorrow! Today! | Dialogue Style, Personality |
| Mococo-Abyssgard | That means you're unstoppable! | Catchphrases, Dialogue Style |
| Mococo-Abyssgard | This is good! | Dialogue Style |
| Mococo-Abyssgard | What about Mococo? | Catchphrases, Dialogue Style |
| Mococo-Abyssgard | Whæt? | Audio Tags, Catchphrases, Dialogue Style, Voice & Delivery |
| Mococo-Abyssgard | hashtag hashtag FWMCMORNING | Catchphrases, Dialogue Style, Personality |
| Mococo-Abyssgard | one step forward a day | Personality |
| Mori-Calliope | Cringe is like, my brand | Catchphrases |
| Mori-Calliope | Curse you, muscle memory! | Catchphrases |
| Mori-Calliope | If you quit when you suck, you'll suck forever | Dialogue Style |
| Mori-Calliope | Let me kill him | Catchphrases |
| Mori-Calliope | WAIT A MINUTE, WAIT A MINUTE! | Catchphrases |
| Mori-Calliope | Well... listen. Listen | Audio Tags, Catchphrases |
| Nakiri-Ayame | Why don't you humans have horns? | Personality, Catchphrases |
| Nakiri-Ayame | 余だよ！ / Yo da yo! | Catchphrases |
| Nanashi-Mumei | Civilization is temporary | Catchphrases |
| Nanashi-Mumei | Today we moom | Catchphrases |
| Nerissa-Ravencroft | Nerissa Ravencroft, at your service~ | Catchphrases |
| Ninomae-Inanis | Forgetty Beam! | Catchphrases, Personality |
| Ninomae-Inanis | I'll bonk you. With a crowbar. Don't do it | Catchphrases |
| Ninomae-Inanis | Live without regrets | Catchphrases, Personality |
| Ninomae-Inanis | Tomorrow! | Catchphrases |
| Ouro-Kronii | Dinner? A bath? Or… me? | Catchphrases |
| Ouro-Kronii | Flower | Catchphrases |
| Ouro-Kronii | GWAK! | Catchphrases |
| Ouro-Kronii | God, I can't get over how amazing I am. Narcissus would be so jealous | Catchphrases |
| Ouro-Kronii | I'm like, the hottest dumpster fire | Catchphrases |
| Ouro-Kronii | I'm not a happy person. But I would like to be happy | Catchphrases |
| Ouro-Kronii | Sorry, I just don't understand things from a CLANKER | Catchphrases |
| Ouro-Kronii | Tea is leaf juice | Catchphrases |
| Ouro-Kronii | You're looking at the ribbon, right? | Catchphrases |
| Ouro-Kronii | ご飯にする？お風呂にする？それとも…わ・た・し？ | Catchphrases |
| Raora-Panthera | Doya! | Catchphrases |
| Raora-Panthera | Here to capture (you)r hearts! ~ | Catchphrases |
| Raora-Panthera | No break-a da pasta! | Catchphrases |
| Shiori-Novella | Aw, it's okay! There, there! | Catchphrases |
| Shiori-Novella | Oh nyo | Catchphrases |
| Shirogane-Noel | Konbanmassuru~ | Catchphrases |
| Shishiro-Botan | ぽい / Poi! | Catchphrases, Audio Tags |
| Takanashi-Kiara | exquisite | Dialogue Style |
| Watson-Amelia | Don't look, stahp! | Catchphrases |
| Watson-Amelia | I'm gonna do it my way! | Catchphrases |
| Watson-Amelia | It's just like Minecraft! | Catchphrases |
| Watson-Amelia | It's not cheating, I got stuck, what do you want me to do? | Catchphrases |
| Watson-Amelia | Make money, get bitches | Catchphrases |
| Watson-Amelia | NEHEHEHEHE! | Catchphrases |
| Watson-Amelia | Wadyameeeeean? | Catchphrases |
| Watson-Amelia | Wait, why did I say that out loud? | Catchphrases |
| Yukihana-Lamy | Konlamy desu | Catchphrases |
