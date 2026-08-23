"""Chinese names for the Hololive cast, so a Chinese-named file finds its member.

The reference-art matcher was built against romaji and kana filenames, because
those are what a booru scrape produces. A collection organised by a Chinese
speaker is not named that way - the folders and files carry names like
`星街彗星`, `兔田佩克拉`, `寶鐘瑪琳` - and the matcher scored all of them zero.

**None of these are translations written here.** Every name came out of the
zh.wikipedia article `Hololive production`, rendered twice through the API's own
script converter: once with `variant=zh-tw` and once with `variant=zh-cn`. That
gives the traditional and the simplified spelling of each name from the source,
so nothing had to be inferred. Where the two variants disagree on more than
script - Watson Amelia is `華生·艾米莉亞` in one and `沃森·阿米莉亞` in the other,
which is two different *translations* - both are kept, because a file could be
named either way.

Two members have no entry, and guessing would be worse than missing:

  * **AZKi** - written in Latin letters in Chinese too, so the existing romaji
    matching already covers her.
  * **Pekomama** (`ぺこらマミー`) - no zh.wikipedia article, and the community
    uses several spellings. Her Japanese name is already in the character pack.

A wrong alias here is not dangerous the way a wrong *match* is - an alias that
matches nothing simply never fires - but it is dead weight, and dead weight in a
table like this is how a table stops being trustworthy.

Source: https://zh.wikipedia.org/wiki/Hololive_production, read 2026-08-23,
both `variant=zh-tw` and `variant=zh-cn`. Three names the article's member table
does not carry in that form (Roboco-san, A-Chan, Harusaki Nodoka) came from the
same article's prose and its Japanese-link templates.
"""

from __future__ import annotations

# character key -> the Chinese names that character is filed under
ZH_NAMES: dict[str, tuple[str, ...]] = {
    "a-chan": ("A酱", "A醬",),
    "airani-iofifteen": ("艾拉妮·伊歐菲芙婷",),
    "akai-haato": ("赤井心",),
    "aki-rosenthal": ("亚绮·罗森塔尔", "亞綺·羅森塔爾",),
    "amane-kanata": ("天音彼方",),
    "anya-melfissa": ("阿妮娅·梅尔菲莎", "阿妮婭·梅爾菲莎",),
    "ayunda-risu": ("阿芸達·栗絲",),
    "cecilia-immergreen": ("塞西莉亚·伊默格林", "塞西莉亞·伊默格林",),
    "ceres-fauna": ("塞莱希·法娜", "塞萊希·法娜",),
    "elizabeth-rose-bloodflame": ("伊丽莎白·露丝·布拉德弗雷姆", "伊麗莎白·露絲·布拉德弗雷姆",),
    "fuwawa-abyssgard": ("軟軟·阿比斯加德", "软软·阿比斯加德",),
    "gawr-gura": ("噶呜·古拉", "噶嗚·古拉",),
    "gigi-murin": ("琪琪·沐林",),
    "hakos-baelz": ("哈珂斯·貝爾絲", "哈珂斯·贝尔丝",),
    "hakui-koyori": ("博衣小夜璃",),
    "harusaki-nodoka": ("春先和香",),
    "himemori-luna": ("姬森璐娜",),
    "hiodoshi-ao": ("火威青",),
    "hoshimachi-suisei": ("星街彗星",),
    "houshou-marine": ("宝钟玛琳", "寶鐘瑪琳",),
    "ichijou-ririka": ("一条莉莉华", "一條莉莉華",),
    "inugami-korone": ("戌神沁音",),
    "irys": ("埃莉丝", "埃莉絲",),
    "juufuutei-raden": ("儒乌风亭螺钿", "儒烏風亭螺鈿",),
    "kaela-kovalskia": ("卡埃拉·科瓦尔斯基亚", "卡埃拉·科瓦爾斯基亞",),
    "kazama-iroha": ("風真伊呂波", "风真伊吕波",),
    "kiryu-coco": ("桐生可可",),
    "kobo-kanaeru": ("可波·卡娜埃露",),
    "koseki-bijou": ("古石碧珠",),
    "kureiji-ollie": ("克蕾西·奥莉", "克蕾西·奧莉",),
    "la-darknesss": ("拉普拉斯·暗黑",),
    "mano-aloe": ("魔乃阿蘿耶",),
    "minato-aqua": ("湊阿库娅", "湊阿庫婭",),
    "mococo-abyssgard": ("茸茸·阿比斯加德",),
    "momosuzu-nene": ("桃鈴音音", "桃铃音音",),
    "moona-hoshinova": ("暮娜·惑星諾瓦", "暮娜·惑星诺瓦",),
    "mori-calliope": ("森美声", "森美聲",),
    "murasaki-shion": ("紫咲詩音", "紫咲诗音",),
    "nakiri-ayame": ("百鬼綾目", "百鬼绫目",),
    "nanashi-mumei": ("七詩無銘", "七诗无铭",),
    "natsuiro-matsuri": ("夏色祭",),
    "nekomata-okayu": ("猫又小粥", "貓又小粥",),
    "nerissa-ravencroft": ("納瑞莎·雷文克羅夫特", "纳瑞莎·雷文克罗夫特",),
    "ninomae-ina-nis": ("一伊那尔栖", "一伊那爾栖",),
    "omaru-polka": ("尾丸波尔卡", "尾丸波爾卡",),
    "ookami-mio": ("大神澪",),
    "oozora-subaru": ("大空昴",),
    "otonose-kanade": ("音乃濑奏", "音乃瀨奏",),
    "ouro-kronii": ("奥罗·克洛尼", "奧羅·克洛尼",),
    "pavolia-reine": ("帕沃莉亚·蕾内", "帕沃莉亞·蕾內", "帕沃莉亞·蕾内",),
    "raora-panthera": ("拉欧拉·潘特拉", "拉歐拉·潘特拉",),
    "roboco-san": ("萝卜子", "蘿蔔子",),
    "sakamata-chloe": ("沙花叉克萝伊", "沙花叉克蘿伊",),
    "sakura-miko": ("樱巫女", "櫻巫女",),
    "shiori-novella": ("詩織·諾薇拉", "诗织·诺薇拉",),
    "shirakami-fubuki": ("白上吹雪",),
    "shiranui-flare": ("不知火芙蕾雅",),
    "shirogane-noel": ("白銀諾艾爾", "白银诺艾尔",),
    "shishiro-botan": ("狮白牡丹", "獅白牡丹",),
    "takanashi-kiara": ("小鳥遊琪亞拉", "小鸟游琪亚拉",),
    "takane-lui": ("鷹嶺琉依", "鹰岭琉依",),
    "todoroki-hajime": ("轟一", "轰一",),
    "tokino-sora": ("时乃空", "時乃空",),
    "tokoyami-towa": ("常暗永远", "常闇永遠",),
    "tsukumo-sana": ("九十九佐命",),
    "tsunomaki-watame": ("角卷綿芽", "角卷绵芽",),
    "uruha-rushia": ("润羽露西娅", "潤羽露西婭",),
    "usada-pekora": ("兔田佩克拉",),
    "vestia-zeta": ("維斯提亞·澤塔", "维斯提亚·泽塔",),
    "watson-amelia": ("沃森·阿米莉亚", "華生·艾米莉亞", "華生·阿米莉亞",),
    "yozora-mel": ("夜空梅露",),
    "yukihana-lamy": ("雪花菈米",),
    "yuzuki-choco": ("愈月巧可", "癒月巧可",),}

# Members deliberately absent, and why. Kept as data so a test can assert the
# list is complete rather than merely long.
NO_ZH_NAME = {
    "azki": "名字本來就是拉丁字母，羅馬字比對已經涵蓋",
    "pekomama": "zh.wikipedia 沒有條目，社群譯名不只一種，猜不如不猜",
}


def names_for(key: str) -> tuple[str, ...]:
    return ZH_NAMES.get(key, ())
