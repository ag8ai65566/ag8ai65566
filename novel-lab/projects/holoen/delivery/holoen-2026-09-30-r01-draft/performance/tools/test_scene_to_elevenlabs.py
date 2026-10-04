#!/usr/bin/env python3
"""Offline smoke/regression test; no files or network."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from scene_to_elevenlabs import compile_script, sheet_policy  # noqa: E402

voice_map = {"Mori Calliope": "original_voice_A", "AZKi": "original_voice_B"}
sheets = [
    "# ElevenLabs v4 Performance Sheet: Mori Calliope\n"
    "## 4. Tag palette by situation\n[hesitant]\n"
    "## 5. Signature sounds\n[laughs]\n"
    "## 7. Don't\n[angry]\n",
    "# ElevenLabs v4 Performance Sheet: AZKi\n"
    "## 4. Tag palette by situation\n[mock-dignified]\n"
]
palettes = dict(sheet_policy(text) for text in sheets)
script = """@@scene demo
@@date 2026-09-30
# Style demo: invented lines, not quotations.
STAGE :: A game map appears.
Mori Calliope :: [hesitant] Okay, whose map is this?
AZKi :: [mock-dignified] これは練習です。
ROMAJI :: Kore wa renshū desu.
GLOSS :: This is practice.
PAUSE :: 0.4
narrator :: The cursor stops.
Mori Calliope :: [laughs]
"""
expected = {
    "model_id": "eleven_v4",
    "inputs": [
        {"text": "[hesitant] Okay, whose map is this?", "voice_id": "original_voice_A"},
        {"text": "[mock-dignified] これは練習です。", "voice_id": "original_voice_B"},
        {"text": "[laughs]", "voice_id": "original_voice_A"}
    ]
}
result, warnings = compile_script(script, voice_map, palettes)
assert result["demo"][0] == expected
assert not warnings
assert "Kore wa renshū desu." in result["demo"][1]
assert "PAUSE :: 0.4" in result["demo"][1]
assert "angry" not in palettes["Mori Calliope"]
for broken in (
    script.replace("[hesitant]", "[unknown]"),
    script.replace("Mori Calliope ::", "Calli ::"),
    script.replace("ROMAJI :: Kore wa renshū desu.\n", ""),
    script.replace("@@scene demo", "@@scene ../../escape"),
):
    try:
        compile_script(broken, voice_map, palettes)
    except ValueError:
        pass
    else:
        raise AssertionError("Invalid script was accepted")
_, warnings = compile_script(
    script.replace("[laughs]", "[laughs] Ha ha!"), voice_map, palettes)
assert any("duplicate nonverbal" in warning for warning in warnings)
# any listed sound tag can stand alone; a non-sound tag cannot (Claude, 2026-10-03)
sneeze = {"Mori Calliope": {"hesitant", "sneezes", "dramatic gasp"}, "AZKi": {"mock-dignified"}}
for alone in ("[sneezes]", "[dramatic gasp]"):
    compile_script(script.replace("[laughs]", alone), voice_map, sneeze)
_, warnings = compile_script(script.replace("[laughs]", "[sneezes] Achoo!"), voice_map, sneeze)
assert any("duplicate nonverbal" in warning for warning in warnings)
try:
    compile_script(script.replace("[laughs]", "[hesitant]"), voice_map, sneeze)
except ValueError:
    pass
else:
    raise AssertionError("A delivery-only turn without a sound tag was accepted")
print("PASS")
