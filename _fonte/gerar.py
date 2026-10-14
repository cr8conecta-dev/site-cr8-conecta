# -*- coding: utf-8 -*-
"""Gera todas as páginas HTML do site na raiz do repositório.

Uso (de qualquer pasta):  python3 _fonte/gerar.py
Só usa a biblioteca padrão do Python 3. Não mexe em CSS, JS nem imagens:
  - textos e estrutura das páginas: _fonte/data.py e _fonte/build.py
  - ilustrações em HTML: _fonte/art.py
  - visual: assets/css/style.css (editado direto)
  - comportamento: assets/js/site.js (editado direto)
"""
import glob
import os
import re
import struct
import subprocess
import sys

FONTE = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(FONTE)
PREVIEW = "--preview" in sys.argv

# 1) páginas, sitemap, robots, llms.txt e 404
subprocess.run([sys.executable, os.path.join(FONTE, "build.py"), RAIZ] + (["--preview"] if PREVIEW else []), check=True)

# 2) ajustes finais nas páginas geradas
HEX = {
    "0a101a": "0d2743", "0e1626": "112f52", "131e33": "163861", "223049": "2a4a6f", "19243a": "1c395b",
    "18284a": "1a3a63", "1b2942": "1f3d63", "34476a": "3d5a7f", "0f2145": "0f2e52", "1b3a73": "2a4f7a",
    "13203a": "17395f", "0d1626": "0d2743", "07101f": "0d2743", "eaf0fa": "f4f2ef", "9aa9c2": "a9b9c7",
    "d8e1f1": "e4e0db", "cbd6e8": "e4e0db", "dbe5f6": "e4e0db", "cdd8ea": "e4e0db",
    "4285f5": "8c9eac", "6da3ff": "c5d1db", "5b97ff": "a9bac8", "3a74e0": "7a8e9d", "7fb0ff": "d3dce4",
    "2c58b8": "5a7389", "6a3df0": "6f8496", "4c2a8a": "3a566f", "3a1a66": "24415f", "2b1b4d": "1f3a58",
    "9f00ff": "dad5cf", "c486ff": "ece8e3", "3a4f78": "3d5a7f", "28406f": "2a4a6f", "2a3a58": "2f4a6b",
}
RGBA = {"66, 133, 245": "140, 158, 172", "159, 0, 255": "218, 213, 207", "109, 163, 255": "197, 209, 219", "10, 16, 26": "13, 39, 67"}

with open(os.path.join(RAIZ, "assets/logos/cr8-mark.png"), "rb") as f:
    mw, mh = struct.unpack(">II", f.read(24)[16:24])
marca_w = round(42 * mw / mh)

mapa = open(os.path.join(FONTE, "map_snip.html"), encoding="utf-8").read()
HASMAP = '"hasMap":"https://www.google.com/maps?cid=13746290579143037967",'

for f in glob.glob(os.path.join(RAIZ, "**/*.html"), recursive=True):
    if os.sep + "_fonte" + os.sep in f:
        continue
    s = open(f, encoding="utf-8").read()
    o = s
    s = re.sub(r"#([0-9a-fA-F]{6})\b", lambda m: "#" + HEX.get(m.group(1).lower(), m.group(1)), s)
    for a, b in RGBA.items():
        s = s.replace("rgba(%s" % a, "rgba(%s" % b)
    s = re.sub(r'<meta name="theme-color" content="#[0-9a-fA-F]{6}">', '<meta name="theme-color" content="#0d2743">', s)
    s = re.sub(r'(cr8-mark\.png"[^>]*?)width="\d+" height="\d+"', r'\g<1>width="%d" height="42"' % marca_w, s)
    s = s.replace('"width":480,"height":468', '"width":512,"height":512')
    if '"hasMap"' not in s:
        s = s.replace('"logo":{"@type":"ImageObject"', HASMAP + '"logo":{"@type":"ImageObject"', 1)
    if f.endswith(os.path.join("contato", "index.html")) and 'id="mapa"' not in s:
        s = s.replace("</main>", mapa + "\n</main>", 1)
    if s != o:
        open(f, "w", encoding="utf-8").write(s)

print("Site gerado em", RAIZ)
