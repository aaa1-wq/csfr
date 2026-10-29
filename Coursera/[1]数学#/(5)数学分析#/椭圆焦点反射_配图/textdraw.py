# -*- coding: utf-8 -*-
"""逐字符渲染，缺字形时自动回退到带该字形的字体。Draw 包装器版本。"""
import os
from PIL import Image, ImageDraw, ImageFont

FONT_DIR = os.path.join(os.environ.get("WINDIR", r"C:\Windows"), "Fonts")
CACHE = {}


def _load(fn, size):
    key = (fn, size)
    if key not in CACHE:
        p = os.path.join(FONT_DIR, fn)
        CACHE[key] = ImageFont.truetype(p, size) if os.path.exists(p) else ImageFont.load_default()
    return CACHE[key]


FALLBACK = ["msyh.ttc", "simhei.ttf", "segoeui.ttf", "arial.ttf"]


def has_glyph(fnt, ch):
    try:
        m = fnt.getmask(ch)
        return m.size[0] > 0 and m.size[1] > 0
    except Exception:
        return False


class TextDraw:
    """包装 ImageDraw：text() 会按字符回退字体，返回整体 bounding box。"""

    def __init__(self, draw):
        self.d = draw

    def text(self, xy, text, font=None, fill=None, anchor="la", spacing=0):
        if not text:
            return
        x, y = xy
        base_path = getattr(font, "path", None)
        base_size = getattr(font, "size", 24)
        pen = 0
        for ch in text:
            if ch == " ":
                pen += base_size * 0.32
                continue
            fnt = font
            if base_path and not has_glyph(font, ch):
                for fn in FALLBACK:
                    cand = _load(fn, base_size)
                    if has_glyph(cand, ch):
                        fnt = cand
                        break
            try:
                w = self.d.textlength(ch, font=fnt)
            except Exception:
                w = fnt.getlength(ch) if hasattr(fnt, "getlength") else base_size * 0.6
            self.d.text((x + pen, y), ch, font=fnt, fill=fill, anchor=anchor)
            pen += w
        return (x, y, x + pen, y + base_size)
