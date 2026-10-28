# 14. 標籤一覽

在要念的文字裡寫 `[標籤]`，可以指定**情緒、說話方式、說話習慣、角色、聲音和停頓**。文字轉語音、長文、劇本配音都能用；中文、英文、日文的寫法效果一樣（`[害羞]` = `[embarrassed]` = `[照れて]`）。不用背：文字框下面按「**標籤**」，可以搜尋、點一下插入。

## 標籤怎麼作用

- **管它後面的字，到下一個標籤為止**：`[開心] やった！[難過] でも、明日はもう会えないんだ。` 前半開心、後半難過。平台會在換標籤的地方分段，每段用自己的語氣和參考片段合成，再接起來。
- **說話方式會延續**：`[緊張]`、`[悄悄話]`、`[慢慢說]` 這類會一直用到下一個說話方式標籤；長文裡寫在段落開頭的，會套用到整段。
- **聲音和停頓只出現一次**：`[嘆氣]`、`[笑聲]`、`[咳嗽]`、`[停頓]` 只在寫的位置出現，不會延續。
- **停頓是真的靜音**：`[停頓]` 0.5 秒、`[短停頓]` 0.25 秒、`[長停頓]` 1.2 秒，也可以寫秒數：`[停頓 1.5秒]`、`[pause 2s]`、`[間 0.8秒]`、`[1秒]`（最多 10 秒）。
- **聲音用你的原音最像**：聲音類標籤（呼吸、笑聲、哭聲、其他聲音）在聲音頁的「聲音標籤」放進你自己錄到的那個聲音後，會在那個位置播你的原音；沒有原音時只是「那句話的語氣」，不會真的發出那個聲音。登記時用任何一個名字都可以：登記 `[喘氣]` 之後，文字裡寫 `[panting]`、`[はぁはぁ]` 也會播它。
- **情緒靠參考片段最有效**：每個標籤會挑一種情緒的參考片段（表格最後一欄）。在模型頁為常用情緒各加一段你自己那種語氣的片段，再用「參考音色」模式，效果比只寫標籤好很多。
- **同一個位置寫好幾個標籤**（`[開心, 快速]`）：描述會合在一起，參考片段用第一個有情緒的。
- **沒有的標籤**也可以直接寫英文描述：`[like a pirate]`、`[slowly, thoughtfully]`，會照寫的內容當風格提示。
- **優先順序**：那一句自己選的情緒（介面上的選單）＞ 標籤 ＞ 預設情緒。

## 做不到的

- **唱歌**：模型只學說話。
- **換成別人的聲音、年齡或性別、方言口音**：標籤只改語氣，聲音還是你的。
- 訓練資料裡完全沒有的語氣（例如從來沒大喊過），標籤只能稍微推一下；要更像，就錄一些那種語氣的素材，或用原音。

## 全部標籤

<!-- tags:start -->
### 情緒標籤（24 種）

片段、參考片段、原音都用這些標情緒；標籤會挑對應情緒的參考片段。沒有那種情緒的參考片段時，依序改用相近的情緒，最後用平靜。

| 代碼 | 中文 | 沒有時改用 |
|---|---|---|
| `neutral` | 平靜 | — |
| `happy` | 開心 | 興奮、平靜 |
| `excited` | 興奮 | 開心、平靜 |
| `angry` | 生氣 | 不耐煩、平靜 |
| `sad` | 難過 | 哭著說、小聲／溫柔、平靜 |
| `soft` | 小聲／溫柔 | 悄悄話、平靜 |
| `laughing` | 笑著說 | 開心、平靜 |
| `surprised` | 驚訝 | 興奮、平靜 |
| `scared` | 害怕 | 緊張、平靜 |
| `whisper` | 悄悄話 | 小聲／溫柔、平靜 |
| `teasing` | 撒嬌／調皮 | 開心、平靜 |
| `narration` | 念稿／旁白 | 平靜 |
| `annoyed` | 不耐煩 | 生氣、平靜 |
| `crying` | 哭著說 | 難過、平靜 |
| `nervous` | 緊張 | 害怕、平靜 |
| `embarrassed` | 害羞 | 小聲／溫柔、撒嬌／調皮、平靜 |
| `disgusted` | 嫌棄 | 不耐煩、生氣、平靜 |
| `tired` | 疲倦／想睡 | 小聲／溫柔、難過、平靜 |
| `shouting` | 大喊 | 興奮、生氣、平靜 |
| `serious` | 認真 | 念稿／旁白、平靜 |
| `cold` | 冷淡 | 認真、平靜 |
| `smug` | 得意 | 撒嬌／調皮、開心、平靜 |
| `sarcastic` | 諷刺 | 撒嬌／調皮、冷淡、平靜 |
| `confused` | 疑惑 | 驚訝、平靜 |

### 開心・正面

| 中文 | 英文 | 也可以寫 | 效果 | 參考片段 |
|---|---|---|---|---|
| `[開心]` | `[happy]` | `cheerful` `glad` `joyful` `高興` `快樂` `愉快` `嬉しい` `うれしい` `嬉しそうに` `楽しい` `楽しそうに` | happy, cheerful | 開心 |
| `[興奮]` | `[excited]` | `energetic` `hyped` `pumped` `enthusiastic` `high energy` `激動` `亢奮` `嗨` `興奮して` `ワクワク` `わくわく` `ハイテンション` `テンション高め` | excited, energetic | 興奮 |
| `[驚喜]` | `[delighted]` | `overjoyed` `thrilled` `欣喜` `大喜び` `歓喜` | delighted, overjoyed | 開心 |
| `[笑著說]` | `[laughing]` | `laughing while talking` `邊笑邊說` `帶笑` `笑いながら` `笑って` | laughing while speaking | 笑著說 |
| `[微笑著說]` | `[smiling]` | `with a smile` `微笑` `笑咪咪` `ニコニコ` `にこにこ` `微笑みながら` `笑顔で` | smiling, warm | 開心 |
| `[調皮]` | `[playful]` | `mischievous` `impish` `cheeky` `頑皮` `淘氣` `いたずらっぽく` `おちゃめ` `茶目っ気たっぷりに` | playful, mischievous | 撒嬌／調皮 |
| `[親切]` | `[warm]` | `friendly` `kind` `溫暖` `友善` `和善` `親しげに` `フレンドリー` | warm, friendly | 開心 |
| `[溫柔]` | `[gentle]` | `tender` `柔和` `輕柔` `優しく` `やさしく` `優しい声で` | gentle, tender | 小聲／溫柔 |
| `[深情]` | `[loving]` | `affectionate` `fond` `寵溺` `疼愛` `愛おしそうに` `愛情を込めて` | loving, affectionate | 小聲／溫柔 |
| `[感謝]` | `[grateful]` | `thankful` `heartfelt` `感激` `感動` `感謝を込めて` `心を込めて` | grateful, heartfelt | 小聲／溫柔 |
| `[驕傲]` | `[proud]` | `自豪` `誇らしげに` `誇らしく` | proud | 得意 |
| `[放心]` | `[relieved]` | `安心` `安心して` `ほっとして` | relieved, tension leaving | 平靜 |
| `[期待]` | `[hopeful]` | `eager` `expectant` `盼望` `期待して` `楽しみそうに` | hopeful, eager | 開心 |
| `[讚嘆]` | `[amazed]` | `impressed` `in awe` `awestruck` `佩服` `驚嘆` `感心して` `感嘆して` | amazed, in awe | 驚訝 |
| `[懷念]` | `[nostalgic]` | `wistful` `懷舊` `懐かしそうに` `しみじみ` | nostalgic, wistful | 小聲／溫柔 |
| `[平靜]` | `[calm]` | `neutral` `steady` `relaxed` `composed` `冷靜` `平常` `放鬆` `淡定` `落ち着いて` `穏やか` `穏やかに` `普通に` `リラックス` | calm, steady | 平靜 |

### 生氣・不滿

| 中文 | 英文 | 也可以寫 | 效果 | 參考片段 |
|---|---|---|---|---|
| `[生氣]` | `[angry]` | `mad` `憤怒` `怒` `怒って` `怒り` `怒った` `ムカついて` | angry, sharp | 生氣 |
| `[暴怒]` | `[furious]` | `enraged` `livid` `raging` `大怒` `抓狂` `激怒` `ブチギレ` `キレて` | furious, seething | 生氣 |
| `[不耐煩]` | `[annoyed]` | `irritated` `impatient` `煩躁` `惱火` `イライラ` `いらいら` `イラついて` | annoyed, irritated | 不耐煩 |
| `[懊惱]` | `[frustrated]` | `挫折` `もどかしそうに` | frustrated | 不耐煩 |
| `[不甘心]` | `[vexed]` | `不甘` `悔しい` `悔しそうに` `くやしい` | vexed, bitterly frustrated | 不耐煩 |
| `[不爽]` | `[grumpy]` | `sullen` `cranky` `臭臉` `不機嫌` `不機嫌そうに` `ぶすっと` | grumpy, sullen | 不耐煩 |
| `[賭氣]` | `[sulking]` | `pouting` `鬧彆扭` `嘟嘴` `拗ねて` `すねて` `ふくれっ面` | sulking, pouting | 不耐煩 |
| `[抱怨]` | `[complaining]` | `whining` `whiny` `grumbling` `發牢騷` `愚痴っぽく` `ぼやいて` `文句を言って` | complaining, whiny | 不耐煩 |
| `[嫌棄]` | `[disgusted]` | `grossed out` `repulsed` `噁心` `厭惡` `嫌悪` `気持ち悪そうに` `ドン引き` `引いて` | disgusted, repulsed | 嫌棄 |
| `[鄙視]` | `[contemptuous]` | `disdainful` `scornful` `輕蔑` `不屑` `見下して` `軽蔑して` | contemptuous, looking down on them | 冷淡 |
| `[威脅]` | `[threatening]` | `menacing` `兇狠` `凶狠` `脅すように` `凄んで` `ドスの効いた声で` | low, menacing, threatening | 生氣 |
| `[吃醋]` | `[jealous]` | `envious` `嫉妒` `羨慕` `ヤキモチ` `嫉妬して` `羨ましそうに` | jealous, pouty | 不耐煩 |
| `[無奈]` | `[fed up]` | `exasperated` `resigned` `受不了` `沒轍` `呆れて` `あきれて` `やれやれ` `うんざり` | resigned, exasperated | 不耐煩 |

### 難過・哭腔

| 中文 | 英文 | 也可以寫 | 效果 | 參考片段 |
|---|---|---|---|---|
| `[難過]` | `[sad]` | `unhappy` `down` `傷心` `悲傷` `悲しい` `悲しそうに` | sad, subdued | 難過 |
| `[憂鬱]` | `[melancholy]` | `gloomy` `depressed` `低落` `沮喪` `落ち込んで` `しょんぼり` `どんより` | melancholy, gloomy | 難過 |
| `[寂寞]` | `[lonely]` | `forlorn` `孤單` `寂しそうに` `さみしい` `寂しい` | lonely, forlorn | 難過 |
| `[失望]` | `[disappointed]` | `let down` `失落` `がっかり` `残念そうに` | disappointed, let down | 難過 |
| `[後悔]` | `[regretful]` | `remorseful` `悔恨` `後悔して` | regretful, remorseful | 難過 |
| `[道歉]` | `[apologetic]` | `sorry` `抱歉` `愧疚` `申し訳なさそうに` `謝りながら` | apologetic, sorry | 小聲／溫柔 |
| `[哀求]` | `[pleading]` | `begging` `imploring` `懇求` `拜託` `懇願して` `すがるように` | pleading, begging | 難過 |
| `[哭腔]` | `[tearful]` | `teary` `on the verge of tears` `要哭了` `淚眼汪汪` `涙声` `泣きそう` `うるうる` | tearful, close to tears | 哭著說 |
| `[哭著說]` | `[crying]` | `weeping` `邊哭邊說` `泣きながら` `泣いて` | crying while speaking | 哭著說 |
| `[哽咽]` | `[choked up]` | `voice breaking` `声を詰まらせて` `涙をこらえて` | choked up, voice breaking | 哭著說 |
| `[心碎]` | `[heartbroken]` | `devastated` `despairing` `grief-stricken` `心痛` `崩潰` `悲痛` `絕望` `絶望して` `打ちひしがれて` | heartbroken, devastated | 哭著說 |

### 害怕・緊張・驚訝

| 中文 | 英文 | 也可以寫 | 效果 | 參考片段 |
|---|---|---|---|---|
| `[害怕]` | `[scared]` | `afraid` `frightened` `fearful` `恐懼` `怖い` `怖がって` `怯えて` `びくびく` | scared, frightened | 害怕 |
| `[驚恐]` | `[terrified]` | `panicked` `panicking` `horrified` `嚇壞` `恐慌` `驚慌` `パニック` `慌てて` `取り乱して` | terrified, panicked | 害怕 |
| `[緊張]` | `[nervous]` | `tense` `uneasy` `jittery` `忐忑` `緊張して` `ドキドキ` `どきどき` | nervous, tense | 緊張 |
| `[不安]` | `[anxious]` | `worried` `concerned` `擔心` `焦慮` `心配そうに` `不安そうに` | anxious, worried | 緊張 |
| `[發抖]` | `[trembling]` | `shaky` `shaking` `quivering` `顫抖` `聲音發抖` `震え声` `震えて` `ぶるぶる` | shaky, trembling voice | 害怕 |
| `[驚訝]` | `[surprised]` | `意外` `驚いて` `びっくり` `びっくりして` `驚き` | surprised | 驚訝 |
| `[震驚]` | `[shocked]` | `stunned` `astonished` `傻眼` `嚇一跳` `呆然` `愕然` `ショック` `唖然` | shocked, stunned | 驚訝 |
| `[疑惑]` | `[confused]` | `puzzled` `baffled` `困惑` `疑問` `不解` `一頭霧水` `困惑して` `戸惑って` `きょとん` | confused, puzzled | 疑惑 |
| `[好奇]` | `[curious]` | `inquisitive` `intrigued` `感興趣` `興味津々` `興味深そうに` | curious, intrigued | — |
| `[懷疑]` | `[suspicious]` | `doubtful` `skeptical` `sceptical` `狐疑` `半信半疑` `疑って` `怪しむように` `ジト目` | suspicious, doubtful | 疑惑 |

### 害羞・撒嬌・調情

| 中文 | 英文 | 也可以寫 | 效果 | 參考片段 |
|---|---|---|---|---|
| `[害羞]` | `[embarrassed]` | `bashful` `shy` `不好意思` `難為情` `臉紅` `恥ずかしそうに` `照れて` `照れながら` `恥ずかしい` | embarrassed, bashful | 害羞 |
| `[慌張]` | `[flustered]` | `手忙腳亂` `慌亂` `あたふた` `あわあわ` `動揺して` | flustered | 害羞 |
| `[尷尬]` | `[awkward]` | `uncomfortable` `気まずそうに` `気まずい` | awkward, uncomfortable | 害羞 |
| `[傲嬌]` | `[tsundere]` | `ツンデレ` `ツンツン` | acting cold and annoyed while secretly pleased | 害羞 |
| `[裝可愛]` | `[cute]` | `adorable` `可愛` `賣萌` `萌` `かわいく` `可愛く` `ぶりっ子` `きゃぴきゃぴ` | cute, sweet and bright | 撒嬌／調皮 |
| `[撒嬌]` | `[coaxing]` | `clingy` `sweet-talking` `撒嬌地` `甘えて` `甘え声` `あまえて` | sweet, coaxing, clingy | 撒嬌／調皮 |
| `[調侃]` | `[teasing]` | `ribbing` `逗` `捉弄` `開玩笑` `からかって` `からかうように` `いじって` | teasing, playful | 撒嬌／調皮 |
| `[調情]` | `[flirty]` | `flirtatious` `coy` `曖昧` `撩` `撩人` `誘うように` | flirtatious, charming | 撒嬌／調皮 |
| `[性感]` | `[sultry]` | `seductive` `alluring` `魅惑` `嫵媚` `色っぽく` `艶っぽく` `妖艶` | sultry, low and alluring | 撒嬌／調皮 |

### 冷淡・認真・自信

| 中文 | 英文 | 也可以寫 | 效果 | 參考片段 |
|---|---|---|---|---|
| `[認真]` | `[serious]` | `earnest` `sincere` `嚴肅` `正經` `真剣` `真面目` `まじめに` `真剣に` | serious, earnest | 認真 |
| `[嚴厲]` | `[stern]` | `strict` `嚴格` `厳しく` `厳しい口調で` | stern, strict | 認真 |
| `[堅定]` | `[determined]` | `resolute` `decisive` `firm` `果斷` `決心` `決意を込めて` `きっぱり` `力強く` | determined, resolute | 認真 |
| `[自信]` | `[confident]` | `assertive` `self-assured` `自信滿滿` `篤定` `自信満々` `堂々と` | confident, self-assured | 認真 |
| `[得意]` | `[smug]` | `cocky` `boastful` `得意洋洋` `臭屁` `ドヤ` `ドヤ顔` `得意げ` `自慢げ` | smug, self-satisfied | 得意 |
| `[諷刺]` | `[sarcastic]` | `ironic` `snarky` `酸` `嘲諷` `挖苦` `陰陽怪氣` `皮肉っぽく` `嫌味っぽく` | sarcastic, dry irony | 諷刺 |
| `[嘲弄]` | `[mocking]` | `derisive` `taunting` `取笑` `挑釁` `あざ笑うように` `煽るように` `馬鹿にして` | mocking, taunting | 諷刺 |
| `[冷淡]` | `[cold]` | `cool` `distant` `aloof` `icy` `冷漠` `高冷` `冷たく` `クール` `そっけなく` `素っ気なく` | cold, distant | 冷淡 |
| `[無所謂]` | `[indifferent]` | `uninterested` `nonchalant` `不在乎` `隨便` `無関心` `どうでもよさそうに` `興味なさそうに` | indifferent, uninterested | 冷淡 |
| `[面無表情]` | `[deadpan]` | `expressionless` `無表情` `真顔で` | deadpan, flat | 冷淡 |
| `[無聊]` | `[bored]` | `unenthusiastic` `沒勁` `退屈そうに` `つまらなそうに` | bored, unenthusiastic | 疲倦／想睡 |

### 疲倦・想睡・身體狀況

| 中文 | 英文 | 也可以寫 | 效果 | 參考片段 |
|---|---|---|---|---|
| `[疲倦]` | `[tired]` | `exhausted` `weary` `worn out` `累` `好累` `疲憊` `疲れて` `疲れた` `ぐったり` `へとへと` | tired, low energy | 疲倦／想睡 |
| `[想睡]` | `[sleepy]` | `drowsy` `睏` `睡意` `眠そうに` `眠い` `うとうと` `ねむい` | sleepy, drowsy | 疲倦／想睡 |
| `[剛睡醒]` | `[groggy]` | `just woke up` `half asleep` `睡眼惺忪` `迷迷糊糊` `寝起き` `寝ぼけて` | groggy, just woke up | 疲倦／想睡 |
| `[懶洋洋]` | `[lazy]` | `sluggish` `listless` `懶散` `有氣無力` `だるそうに` `けだるく` | lazy, listless | 疲倦／想睡 |
| `[微醺]` | `[drunk]` | `tipsy` `喝醉` `醉醺醺` `酔っ払って` `ほろ酔い` | tipsy, slightly slurred | — |
| `[生病]` | `[sick]` | `under the weather` `stuffy nose` `感冒` `鼻音重` `風邪声` `鼻声` `体調悪そうに` | sick, weak and stuffy-nosed | 疲倦／想睡 |
| `[痛苦]` | `[in pain]` | `hurt` `pained` `好痛` `吃痛` `痛そうに` `苦しそうに` | in pain, strained | — |

### 音量・距離

| 中文 | 英文 | 也可以寫 | 效果 | 參考片段 |
|---|---|---|---|---|
| `[悄悄話]` | `[whispers]` | `whisper` `whispering` `耳語` `低語` `說悄悄話` `ささやき` `ささやいて` `囁いて` `ひそひそ` | whispering | 悄悄話 |
| `[氣音]` | `[breathy]` | `airy` `吐息` `吐息まじり` `ウィスパーボイス` | breathy, airy voice | 悄悄話 |
| `[小聲]` | `[soft]` | `quiet` `quietly` `softly` `hushed` `輕聲` `輕輕地` `小声` `小声で` `静かに` | soft, quiet | 小聲／溫柔 |
| `[呢喃]` | `[murmurs]` | `murmur` `murmuring` `喃喃` `喃喃自語` `つぶやく` `つぶやいて` | murmuring softly, half to themself | 小聲／溫柔 |
| `[大聲]` | `[loud]` | `loudly` `projecting` `大聲說` `大声で` `声を張って` | loud, projecting | — |
| `[大喊]` | `[shouts]` | `shout` `shouting` `yells` `yelling` `吼` `喊` `叫喊` `叫んで` `叫ぶ` `怒鳴って` | shouting | 大喊 |
| `[呼喚遠處的人]` | `[calling out]` | `calling` `呼喚` `喊人` `呼びかけて` `遠くに呼びかけて` | calling out to someone far away | 大喊 |
| `[耳邊]` | `[asmr]` | `close to the mic` `close-mic` `貼耳` `耳元で` `耳元` `ASMR風に` | very close to the mic, intimate | 悄悄話 |
| `[遠處]` | `[far away]` | `distant voice` `遠くから` | distant, as if from across the room | — |
| `[悶聲]` | `[muffled]` | `捂著嘴` `こもった声で` | muffled | — |

### 速度・節奏・音調

| 中文 | 英文 | 也可以寫 | 效果 | 參考片段 |
|---|---|---|---|---|
| `[快速]` | `[fast]` | `quickly` `rapidly` `快` `講很快` `早口` `早口で` `速く` | fast, quick pace | — |
| `[急促]` | `[rushed]` | `hurried` `hasty` `in a hurry` `急忙` `趕時間` `慌ただしく` `急いで` | rushed, hurried | 緊張 |
| `[慢慢說]` | `[slow]` | `slowly` `unhurried` `慢` `慢慢地` `ゆっくり` `ゆっくりと` | slow, unhurried | — |
| `[一字一句]` | `[deliberate]` | `measured` `word by word` `enunciating` `咬字清楚` `一言一言` `はっきりと` `区切って` | deliberate, word by word | 認真 |
| `[拖長音]` | `[drawn out]` | `drawl` `drawling` `elongated` `拖音` `語尾を伸ばして` `伸ばして` `間延びして` | drawn-out vowels, drawling | — |
| `[唱歌似的]` | `[sing-song]` | `singsong` `lilting` `melodic` `歌うように` `ルンルン` | sing-song, melodic | 開心 |
| `[平板]` | `[monotone]` | `平淡` `沒起伏` `棒読み` `抑揚なく` | monotone, flat | 冷淡 |
| `[強調]` | `[emphatic]` | `emphasis` `emphasizing` `加重語氣` `強調して` `力を込めて` | emphatic, stressing the words | — |
| `[疑問語氣]` | `[questioning]` | `rising intonation` `問句` `尻上がりに` `疑問形で` | questioning, rising intonation | 疑惑 |
| `[低沉]` | `[low voice]` | `deep voice` `low-pitched` `低音` `壓低聲音` `低い声で` `声を低くして` | low, deep voice | — |
| `[高音]` | `[high voice]` | `high-pitched` `尖細` `拔高` `高い声で` | high-pitched | — |
| `[假音]` | `[falsetto]` | `假聲` `裏声` | falsetto | — |

### 說話習慣

| 中文 | 英文 | 也可以寫 | 效果 | 參考片段 |
|---|---|---|---|---|
| `[結巴]` | `[stutters]` | `stuttering` `stammers` `stammering` `口吃` `結結巴巴` `どもって` `どもりながら` `噛みながら` | stuttering, tripping over the first sounds | 緊張 |
| `[猶豫]` | `[hesitant]` | `hesitating` `hesitates` `unsure` `吞吞吐吐` `支支吾吾` `欲言又止` `ためらいがちに` `言いよどんで` `もじもじ` | hesitant, unsure | 緊張 |
| `[越說越小聲]` | `[trails off]` | `trailing off` `fading out` `聲音漸弱` `語尾を濁して` `尻すぼみ` `消え入るように` | trailing off at the end | 小聲／溫柔 |
| `[含糊]` | `[mumbles]` | `mumbling` `mumble` `嘟囔` `口齒不清` `もごもご` `ぼそぼそ` | mumbling, unclear | 小聲／溫柔 |
| `[嘀咕]` | `[mutters]` | `muttering` `mutter` `under the breath` `碎碎念` `小聲抱怨` `ぶつぶつ` `ボソッと` `ぼそっと` | muttering under the breath | 不耐煩 |
| `[邊想邊說]` | `[thinking]` | `thinking aloud` `pondering` `思考` `想一想` `考えながら` | thinking aloud, pausing to think | — |
| `[自言自語]` | `[to themself]` | `to oneself` `to herself` `to himself` `self-talk` `aside` `獨白` `独り言` `ひとりごと` | talking to themself | 小聲／溫柔 |
| `[滔滔不絕]` | `[rambling]` | `rattling on` `talking nonstop` `嘮叨` `碎嘴` `まくし立てて` `マシンガントーク` | rambling, talking nonstop | 興奮 |
| `[話說一半]` | `[cut off]` | `interrupted` `被打斷` `途中で遮られて` | cut off abruptly at the end | — |
| `[隨性聊天]` | `[casual]` | `conversational` `chatty` `隨性` `口語` `聊天` `輕鬆` `雑談風に` `砕けた感じで` `タメ口` | casual, conversational | 平靜 |
| `[禮貌]` | `[polite]` | `formal` `courteous` `禮貌地` `客氣` `正式` `丁寧に` `敬語で` `かしこまって` | polite, formal | 平靜 |

### 角色・用途

| 中文 | 英文 | 也可以寫 | 效果 | 參考片段 |
|---|---|---|---|---|
| `[旁白]` | `[narration]` | `narrator` `narrating` `念稿` `ナレーション` `ナレーター` `語り` | narrating, clear storytelling voice | 念稿／旁白 |
| `[說故事]` | `[storytelling]` | `story time` `telling a story` `講故事` `読み聞かせ` `昔話風に` | storytelling, engaging and expressive | 念稿／旁白 |
| `[朗讀]` | `[reading aloud]` | `reading` `recitation` `唸稿` `朗読` `音読` | reading aloud, clear and even | 念稿／旁白 |
| `[新聞播報]` | `[news]` | `newscaster` `news anchor` `播報` `主播` `ニュース風に` `アナウンサー風に` `キャスター風に` | news anchor, crisp and neutral | 念稿／旁白 |
| `[廣播]` | `[announcer]` | `announcement` `廣播` `場內廣播` `宣布` `アナウンス` `場内アナウンス` | announcer, clear and projecting | 念稿／旁白 |
| `[實況]` | `[commentator]` | `play-by-play` `sportscaster` `解說` `実況` `実況風に` | lively play-by-play commentary | 興奮 |
| `[客服]` | `[customer service]` | `receptionist` `店員` `接待` `接客` `店員風に` `営業スマイル` | polite customer-service tone | 平靜 |
| `[老師講解]` | `[teacher]` | `lecturing` `explaining` `講課` `解釋` `先生っぽく` `説明口調` | explaining patiently like a teacher | 念稿／旁白 |
| `[廣告]` | `[commercial]` | `advertisement` `ad read` `業配` `CM風に` `宣伝` | upbeat commercial voice | 興奮 |
| `[預告片]` | `[trailer]` | `movie trailer` `epic` `史詩` `予告編風に` | dramatic movie-trailer voice | 認真 |
| `[戲劇化]` | `[dramatic]` | `theatrical` `over the top` `誇張` `浮誇` `芝居がかって` `大げさに` `オーバーに` | dramatic, theatrical | 興奮 |
| `[反派]` | `[villain]` | `villainous` `sinister` `evil` `邪惡` `陰險` `悪役風に` `悪そうに` | villainous, sinister | 冷淡 |
| `[熱血]` | `[heroic]` | `rousing` `inspiring` `英雄` `激勵` `鼓舞するように` `ヒーロー風に` | heroic, rousing | 認真 |
| `[孩子氣]` | `[childlike]` | `childish` `innocent` `童聲` `天真` `子供っぽく` `あどけなく` | childlike, innocent | 開心 |
| `[成熟]` | `[mature]` | `grown-up` `穩重` `大人っぽく` | mature, composed | 平靜 |
| `[機器人]` | `[robotic]` | `mechanical` `robot` `機械` `ロボット風に` `機械的に` | robotic, mechanical | 冷淡 |
| `[開場招呼]` | `[streamer greeting]` | `greeting` `idol` `開場` `打招呼` `偶像` `配信開始` `アイドル風に` `挨拶` | bright, high-energy streamer greeting | 興奮 |

### 笑聲（只在寫的位置出現一次）

| 中文 | 英文 | 也可以寫 | 效果 | 參考片段 |
|---|---|---|---|---|
| `[笑聲]` | `[laughs]` | `laugh` `laughter` `笑` `笑い` `笑い声` `哈哈` `haha` | with a laugh | 笑著說 |
| `[輕笑]` | `[chuckles]` | `chuckle` `低笑` `笑一下` `くすっと` `クスッ` `ふふっ` | with a soft chuckle | 笑著說 |
| `[咯咯笑]` | `[giggles]` | `giggle` `giggling` `嘻嘻` `くすくす` `クスクス` `うふふ` `えへへ` | giggling | 笑著說 |
| `[偷笑]` | `[snickers]` | `snicker` `sniggers` `竊笑` `憋笑` `ぷぷっ` `にやにや` `ニヤニヤ` | snickering | 撒嬌／調皮 |
| `[噴笑]` | `[bursts out laughing]` | `bursts into laughter` `cracks up` `pfft` `笑出來` `笑場` `噗哧` `吹き出して` `噴き出して` `ぷっ` | bursting into laughter | 笑著說 |
| `[大笑]` | `[laughs hard]` | `laughs heartily` `laughing out loud` `guffaws` `belly laugh` `哈哈大笑` `爆笑` `笑到不行` `大爆笑` | laughing heartily | 笑著說 |
| `[笑到喘]` | `[wheezes]` | `wheezing laugh` `笑到岔氣` `笑到無法呼吸` `引き笑い` `笑いすぎて` | wheezing with laughter | 笑著說 |
| `[狂笑]` | `[cackles]` | `cackle` `evil laugh` `maniacal laugh` `怪笑` `奸笑` `高笑い` `悪役笑い` | cackling | 笑著說 |
| `[乾笑]` | `[nervous laugh]` | `laughs nervously` `awkward laugh` `尷尬地笑` `愛想笑い` `照れ笑い` | with a nervous laugh | 緊張 |
| `[苦笑]` | `[bitter laugh]` | `laughs bitterly` `wry laugh` `自嘲` `苦笑い` `自嘲気味に` | with a wry, bitter laugh | 諷刺 |
| `[冷笑]` | `[scoffs]` | `scoff` `sneers` `嗤笑` `哼笑` `鼻で笑う` `鼻笑い` | with a scoff | 冷淡 |

### 哭聲（只在寫的位置出現一次）

| 中文 | 英文 | 也可以寫 | 效果 | 參考片段 |
|---|---|---|---|---|
| `[抽泣]` | `[sobs]` | `sobbing` `啜泣` `嗚咽` `しゃくり上げて` `すすり泣き` | sobbing | 哭著說 |
| `[哭聲]` | `[cries]` | `cry` `wails` `大哭` `嚎啕大哭` `泣き声` `号泣` `うわーん` | crying | 哭著說 |
| `[吸鼻子]` | `[sniffles]` | `sniffle` `sniffling` `鼻をすする` `ぐすっ` `グスッ` `ぐすん` | sniffling | 哭著說 |
| `[嗚嗚]` | `[whimpers]` | `whimper` `whimpering` `小聲哭` `めそめそ` | whimpering | 哭著說 |

### 呼吸（只在寫的位置出現一次）

| 中文 | 英文 | 也可以寫 | 效果 | 參考片段 |
|---|---|---|---|---|
| `[嘆氣]` | `[sighs]` | `sigh` `sighing` `嘆息` `唉聲嘆氣` `ため息` `ため息まじり` | with a sigh | — |
| `[鬆一口氣]` | `[sigh of relief]` | `relieved sigh` `鬆口氣` `ほっと一息` `安堵のため息` | with a sigh of relief | 平靜 |
| `[吐氣]` | `[exhales]` | `exhale` `breathes out` `呼氣` `息を吐いて` | with a slow exhale | — |
| `[吸氣]` | `[inhales]` | `inhale` `breathes in` `breath` `吸一口氣` `息を吸う` `息を吸って` | with a quick intake of breath | — |
| `[大口吸氣]` | `[deep breath]` | `takes a deep breath` `深呼吸` `深吸一口氣` `深呼吸して` `大きく息を吸って` | taking a deep breath first | — |
| `[倒抽一口氣]` | `[gasps]` | `gasp` `sharp inhale` `倒吸一口氣` `抽氣` `息をのむ` `息を呑んで` `はっと` | with a gasp | 驚訝 |
| `[喘氣]` | `[panting]` | `pants` `breathless` `out of breath` `heavy breathing` `breathing heavily` `huffing` `喘` `喘息` `氣喘吁吁` `上氣不接下氣` `息切れ` `息を切らして` `はぁはぁ` `ハァハァ` `ぜえぜえ` | breathless, panting | — |
| `[嬌喘]` | `[soft panting]` | `喘ぎ` `甘い吐息` | breathy, softly panting | 小聲／溫柔 |
| `[屏息]` | `[holds breath]` | `holding breath` `憋氣` `息を止めて` `息を殺して` | holding the breath, then speaking tightly | 緊張 |

### 其他聲音（只在寫的位置出現一次）

| 中文 | 英文 | 也可以寫 | 效果 | 參考片段 |
|---|---|---|---|---|
| `[咳嗽]` | `[coughs]` | `cough` `coughing` `咳` `咳咳` `咳き込んで` `ゴホッ` `けほっ` | with a cough | — |
| `[清喉嚨]` | `[clears throat]` | `clear throat` `ahem` `清嗓子` `咳払い` `んんっ` | clearing the throat first | — |
| `[打噴嚏]` | `[sneezes]` | `sneeze` `achoo` `噴嚏` `哈啾` `くしゃみ` `くしゅん` `ハクション` | with a sneeze | — |
| `[嗅]` | `[sniffs]` | `sniff` `聞聞看` `すんすん` `匂いを嗅いで` | sniffing | — |
| `[打哈欠]` | `[yawns]` | `yawn` `yawning` `哈欠` `呵欠` `あくび` `あくびしながら` | yawning | 疲倦／想睡 |
| `[哼歌]` | `[hums]` | `humming` `鼻歌` `鼻歌まじり` `ふんふん` | humming | 開心 |
| `[思考的嗯]` | `[hmm]` | `thinking hmm` `嗯` `うーん` `んー` `ふむ` | with a thoughtful hmm | — |
| `[呻吟]` | `[groans]` | `groan` `groaning` `唉唷` `うめき` `うめいて` `うなって` | groaning | — |
| `[低吟]` | `[moans]` | `moan` `moaning` | moaning softly | — |
| `[悶哼]` | `[grunts]` | `grunt` `うっ` `ぐっ` | with a grunt | — |
| `[不屑地哼]` | `[hmph]` | `huffs` `哼` `哼一聲` `ふんっ` `フン` | with a dismissive hmph | 不耐煩 |
| `[嘖]` | `[tsk]` | `tch` `tuts` `clicks tongue` `tongue click` `咂嘴` `舌打ち` `ちっ` `チッ` | with a tongue click | 不耐煩 |
| `[吞口水]` | `[gulps]` | `gulp` `swallows` `嚥口水` `ごくり` `ゴクリ` `唾を飲んで` | with a nervous gulp | 緊張 |
| `[打嗝]` | `[hiccups]` | `hiccup` `しゃっくり` `ひっく` | with a hiccup | — |
| `[尖叫]` | `[screams]` | `scream` `screaming` `shrieks` `shriek` `慘叫` `悲鳴` `悲鳴を上げて` `きゃー` `キャー` `ぎゃー` | screaming | 害怕 |
| `[驚叫]` | `[yelps]` | `yelp` `嚇到叫出來` `ひゃっ` `ひゃあ` `きゃっ` | with a startled yelp | 驚訝 |
| `[興奮尖叫]` | `[squeals]` | `squeal` `歡呼尖叫` `黄色い声` | squealing with delight | 興奮 |
| `[歡呼]` | `[cheers]` | `cheering` `好耶` `歓声` `やったー` | cheering | 興奮 |
| `[吹口哨]` | `[whistles]` | `whistle` `口笛` | whistling | 開心 |
| `[親親聲]` | `[kisses]` | `kiss` `smooch` `親親` `啾` `ちゅっ` `チュッ` | with a kiss sound | 撒嬌／調皮 |

### 停頓（只在寫的位置出現一次）

| 中文 | 英文 | 也可以寫 | 效果 | 參考片段 |
|---|---|---|---|---|
| `[停頓]` | `[pause]` | `beat` `停一下` `間` `ポーズ` `一拍` `一拍置いて` | 停 0.5 秒 | — |
| `[短停頓]` | `[short pause]` | `brief pause` `頓一下` `少し間` `短い間` | 停 0.25 秒 | — |
| `[長停頓]` | `[long pause]` | `silence` `停很久` `沉默` `長い間` `沈黙` | 停 1.2 秒 | — |
<!-- tags:end -->
