# -*- coding: utf-8 -*-
"""Re-build: 'Will There Be Shopping Malls in the Future?' — 4 pages.
Style: Riso / editorial print — cream paper, heavy black linework, one accent,
geometric vector illustrations drawn as native shapes (editable, crisp).
"""
from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE
import math

# ---- Riso palette ----
PAPER  = RGBColor(0xF3, 0xEE, 0xE4)   # cream paper
INK    = RGBColor(0x12, 0x12, 0x12)   # near-black ink
BLUE   = RGBColor(0x1D, 0x4E, 0xD8)   # riso blue accent
CORAL  = RGBColor(0xE6, 0x53, 0x3C)   # riso coral (secondary accent)
MUTE   = RGBColor(0x6B, 0x66, 0x5C)   # muted grey-brown for body
GREEN  = RGBColor(0x1F, 0x7A, 0x4E)

FONT_H = "Arial"
FONT_B = "Arial"

prs = Presentation()
prs.slide_width = Inches(13.333)
prs.slide_height = Inches(7.5)
SW, SH = 13.333, 7.5
BLANK = prs.slide_layouts[6]

def sl():
    return prs.slides.add_slide(BLANK)

def shape(s, x, y, w, h, fill=None, line=INK, lw=2.0, geom=MSO_SHAPE.RECTANGLE, rot=0):
    sp = s.shapes.add_shape(geom, Inches(x), Inches(y), Inches(w), Inches(h))
    if fill is None: sp.fill.background()
    else: sp.fill.solid(); sp.fill.fore_color.rgb = fill
    if line is None: sp.line.fill.background()
    else: sp.line.color.rgb = line; sp.line.width = Pt(lw)
    sp.shadow.inherit = False
    if rot: sp.rotation = rot
    return sp

def line(s, x1, y1, x2, y2, color=INK, w=2.5):
    from pptx.enum.shapes import MSO_CONNECTOR
    ln = s.shapes.add_connector(MSO_CONNECTOR.STRAIGHT, Inches(x1), Inches(y1), Inches(x2), Inches(y2))
    ln.line.color.rgb = color; ln.line.width = Pt(w)
    ln.shadow.inherit = False
    return ln

def tb(s, x, y, w, h, anchor=MSO_ANCHOR.TOP):
    b = s.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    tf = b.text_frame; tf.word_wrap = True; tf.vertical_anchor = anchor
    tf.margin_left = tf.margin_right = Inches(0.03)
    tf.margin_top = tf.margin_bottom = Inches(0.02)
    return tf

def para(tf, text, size=18, color=INK, bold=False, first=False, align=PP_ALIGN.LEFT,
         before=0, after=6, italic=False, font=FONT_B, spacing=1.0):
    p = tf.paragraphs[0] if first else tf.add_paragraph()
    p.alignment = align; p.space_before = Pt(before); p.space_after = Pt(after)
    p.line_spacing = spacing
    r = p.add_run(); r.text = text
    f = r.font; f.size = Pt(size); f.bold = bold; f.italic = italic
    f.color.rgb = color; f.name = font
    return p

def kicker(s, text, x=0.85, y=0.7, color=BLUE):
    tf = tb(s, x, y, 11, 0.4); para(tf, text.upper(), 14, color, bold=True, first=True)

def bigtitle(s, text, x=0.85, y=1.15, w=11.6, size=40, color=INK):
    tf = tb(s, x, y, w, 1.6)
    para(tf, text, size, color, bold=True, first=True, spacing=1.02, font=FONT_H)

def bg(s, color=PAPER):
    shape(s, 0, 0, SW, SH, fill=color, line=None)

def footer(s, num, dark=False):
    c = RGBColor(0xAF,0xAA,0xA0) if dark else MUTE
    tf = tb(s, 0.85, 6.95, 10, 0.35); para(tf, "Will There Be Shopping Malls in the Future?", 10, c, first=True)
    tf2 = tb(s, 11.5, 6.95, 1.2, 0.35); para(tf2, num, 10, c, first=True, align=PP_ALIGN.RIGHT)

def notes(s, t): s.notes_slide.notes_text_frame.text = t

# ============ ILLUSTRATIONS (native vector) ============

def illo_mall_wall(s, x, y, scale=1.0, accent=BLUE):
    """A flat, stylised mall facade: awning stripes, door, sign — riso poster look."""
    W, H = 5.4*scale, 3.4*scale
    # frame
    shape(s, x, y, W, H, fill=PAPER, line=INK, lw=3)
    # roof band
    shape(s, x, y, W, 0.55*scale, fill=accent, line=INK, lw=3)
    # title strip on roof
    tf = tb(s, x+0.15*scale, y+0.08*scale, W-0.3*scale, 0.45*scale)
    para(tf, "M A L L", 16*scale, PAPER, bold=True, first=True, align=PP_ALIGN.CENTER)
    # awning (striped) — alternating blocks
    ax, ay = x+0.35*scale, y+0.95*scale
    aw, ah = W-0.7*scale, 0.55*scale
    n = 7
    for i in range(n):
        c = INK if i % 2 == 0 else PAPER
        shape(s, ax + i*(aw/n), ay, (aw/n)+0.01, ah, fill=c, line=INK, lw=1.4)
    # scalloped bottom of awning — small circles
    for i in range(n):
        shape(s, ax + i*(aw/n)+0.12*scale, ay+ah-0.10*scale, aw/n-0.12*scale, 0.22*scale,
              fill=(INK if i%2==0 else PAPER), line=INK, lw=1.2, geom=MSO_SHAPE.OVAL)
    # two windows / doors
    shape(s, ax+0.25*scale, ay+0.85*scale, 1.1*scale, 1.2*scale, fill=accent, line=INK, lw=2.5)
    shape(s, ax+1.7*scale, ay+0.85*scale, 1.1*scale, 1.2*scale, fill=accent, line=INK, lw=2.5)
    # door
    dx = ax + aw - 1.15*scale
    shape(s, dx, ay+0.85*scale, 0.95*scale, 1.2*scale, fill=INK, line=INK, lw=2.5)
    shape(s, dx+0.62*scale, ay+1.4*scale, 0.1*scale, 0.1*scale, fill=PAPER, line=None, geom=MSO_SHAPE.OVAL)
    # sign plate
    shape(s, x+W*0.5-0.9*scale, y+H-0.55*scale, 1.8*scale, 0.42*scale, fill=CORAL, line=INK, lw=2.5)
    tf = tb(s, x+W*0.5-0.9*scale, y+H-0.55*scale, 1.8*scale, 0.42*scale, anchor=MSO_ANCHOR.MIDDLE)
    para(tf, "OPEN?", 13*scale, PAPER, bold=True, first=True, align=PP_ALIGN.CENTER)

def illo_phone_cart(s, x, y, scale=1.0):
    """Floating phone with a shopping cart — e-commerce eating retail."""
    # phone
    shape(s, x, y, 1.7*scale, 2.9*scale, fill=PAPER, line=INK, lw=3, geom=MSO_SHAPE.ROUNDED_RECTANGLE)
    shape(s, x+0.12*scale, y+0.28*scale, 1.46*scale, 2.34*scale, fill=BLUE, line=INK, lw=2)
    # inside: cart icon made of lines
    cx, cy = x+0.85*scale, y+1.35*scale
    shape(s, cx-0.5*scale, cy-0.35*scale, 0.62*scale, 0.42*scale, fill=None, line=PAPER, lw=3)
    line(s, cx-0.5*scale, cy-0.35*scale, cx-0.68*scale, cy-0.6*scale, color=PAPER, w=3)
    for wx in (cx-0.30*scale, cx+0.02*scale):
        shape(s, wx, cy+0.12*scale, 0.16*scale, 0.16*scale, fill=PAPER, line=None, geom=MSO_SHAPE.OVAL)
    # signal top
    shape(s, x+0.62*scale, y+0.05*scale, 0.46*scale, 0.14*scale, fill=INK, line=None, geom=MSO_SHAPE.ROUNDED_RECTANGLE)

def illo_burst(s, x, y, scale=1.0, color=CORAL):
    """A starburst 'explosion' for the dead-mall / pessimist idea."""
    cx, cy = x, y
    pts = 12
    outer, inner = 1.15*scale, 0.55*scale
    import math
    for i in range(pts):
        a1 = (2*math.pi*i/pts) - math.pi/2
        x1 = cx + outer*math.cos(a1); y1 = cy + outer*math.sin(a1)
        a2 = a1 + math.pi/pts
        x2 = cx + inner*math.cos(a2); y2 = cy + inner*math.sin(a2)
        # draw triangles
        a3 = a1 + 2*math.pi/pts
        line(s, cx, cy, cx + outer*math.cos(a1), cy + outer*math.sin(a1), color=color, w=3)

def illo_signpost(s, x, y, scale=1.0):
    """A signpost with two arrow-shaped boards: 'A PLACE' vs 'FUNCTION'."""
    # post
    post_w = 0.14*scale
    shape(s, x-post_w/2, y-0.2*scale, post_w, 3.4*scale, fill=INK, line=INK, lw=1)
    # top board: blue arrow pointing RIGHT (rect + triangle tip)
    bx, by, bw, bh = x, y+0.15*scale, 2.0*scale, 0.62*scale
    shape(s, bx, by, bw, bh, fill=BLUE, line=INK, lw=2.5)
    tipx = bx+bw
    tx = [tipx, tipx+0.42*scale, tipx]
    ty = [by, by+bh/2, by+bh]
    from pptx.util import Emu
    fb = s.shapes.build_freeform(Inches(tx[0]), Inches(ty[0]), scale=Emu(1))
    fb.add_line_segments([(Inches(tx[1]), Inches(ty[1])), (Inches(tx[2]), Inches(ty[2])), (Inches(tx[0]), Inches(ty[0]))], close=True)
    tri = fb.convert_to_shape()
    tri.fill.solid(); tri.fill.fore_color.rgb = BLUE
    tri.line.color.rgb = INK; tri.line.width = Pt(2.5); tri.shadow.inherit = False
    tf = tb(s, bx+0.1*scale, by, bw-0.15*scale, bh, anchor=MSO_ANCHOR.MIDDLE)
    para(tf, "A PLACE", 15*scale, PAPER, bold=True, first=True, align=PP_ALIGN.CENTER)
    # bottom board: coral arrow pointing LEFT (triangle tip on left)
    bx2, by2, bw2, bh2 = x-1.4*scale, y+1.15*scale, 2.0*scale, 0.62*scale
    shape(s, bx2, by2, bw2, bh2, fill=CORAL, line=INK, lw=2.5)
    tipx2 = bx2
    tx2 = [tipx2, tipx2-0.42*scale, tipx2]
    ty2 = [by2, by2+bh2/2, by2+bh2]
    fb2 = s.shapes.build_freeform(Inches(tx2[0]), Inches(ty2[0]), scale=Emu(1))
    fb2.add_line_segments([(Inches(tx2[1]), Inches(ty2[1])), (Inches(tx2[2]), Inches(ty2[2])), (Inches(tx2[0]), Inches(ty2[0]))], close=True)
    tri2 = fb2.convert_to_shape()
    tri2.fill.solid(); tri2.fill.fore_color.rgb = CORAL
    tri2.line.color.rgb = INK; tri2.line.width = Pt(2.5); tri2.shadow.inherit = False
    tf = tb(s, bx2+0.15*scale, by2, bw2-0.2*scale, bh2, anchor=MSO_ANCHOR.MIDDLE)
    para(tf, "FUNCTION", 15*scale, PAPER, bold=True, first=True, align=PP_ALIGN.CENTER)

# ============ SLIDE 1 — Cover ============
s = sl(); bg(s)
# left text block
kicker(s, "THE BUSINESS QUESTION", x=0.85, y=1.4)
bigtitle(s, "Will there be\nshopping malls\nin the future?", x=0.85, y=1.95, w=6.4, size=46)
shape(s, 0.9, 4.55, 1.7, 0.10, fill=BLUE, line=None)
tf = tb(s, 0.85, 4.8, 6.2, 1.4)
para(tf, "A test case for a bigger question: is business a place we go \u2014 or a function that finds us?",
     20, MUTE, italic=True, first=True)
# right illustration: mall + floating phone
illo_mall_wall(s, 7.15, 1.35, scale=1.0)
illo_phone_cart(s, 11.4, 2.1, scale=0.62)
footer(s, "01")
notes(s, "[0:00-0:20] Open with the question. Looks like retail; really about whether business still needs a physical place.")

# ============ SLIDE 2 — Why good vs evil ============
s = sl(); bg(s)
kicker(s, "WHY THIS IS A \u2018GOOD VS EVIL\u2019 QUESTION", y=0.6)
bigtitle(s, "Strip away the mask \u2014 same question", y=1.02, size=34)
shape(s, 0.9, 1.85, 1.5, 0.09, fill=BLUE, line=None)
# body column left
tf = tb(s, 0.85, 2.15, 6.6, 3.4)
para(tf, "A mall is the most physical form business ever took \u2014 a place whose only original job was to sell things.",
     18, INK, first=True, after=10)
para(tf, "E-commerce took that job away. So the mall forces the real question: when a business loses the function it was built for, what value is left?",
     18, INK, after=14)
para(tf, "Two answers \u2014 and they map exactly onto good and evil:", 18, INK, bold=True, after=8)
para(tf, "\u25A0  Only ever a machine for selling  \u2192  it deserves to die.", 17, CORAL, bold=True, after=6)
para(tf, "\u25A0  Still gives what a screen can't  \u2192  it survives.", 17, GREEN, bold=True, after=0)
# right: two big stacked chips
cx = 8.0
shape(s, cx, 2.25, 4.4, 1.55, fill=CORAL, line=INK, lw=3)
tf = tb(s, cx+0.3, 2.45, 3.8, 1.2)
para(tf, "\u201cJUST SELLING\u201d", 20, PAPER, bold=True, first=True, after=4)
para(tf, "Value = the transaction.\nIf that's all, it deserves to die.", 15, PAPER, italic=True)
shape(s, cx, 4.15, 4.4, 1.55, fill=GREEN, line=INK, lw=3)
tf = tb(s, cx+0.3, 4.35, 3.8, 1.2)
para(tf, "\u201cBEYOND SELLING\u201d", 20, PAPER, bold=True, first=True, after=4)
para(tf, "Value = gathering, experience,\nbeing seen. It survives \u2014 reshaped.", 15, PAPER, italic=True)
footer(s, "02")
notes(s, "[0:20-1:10] Address the objection head-on. Walk down to: does a business exist only to extract, or to create what people need?")

# ============ SLIDE 3 — Yes, but transformed ============
s = sl(); bg(s)
kicker(s, "THE ANSWER", y=0.6)
bigtitle(s, "Yes \u2014 but survivors sell being together", y=1.02, size=32)
shape(s, 0.9, 1.85, 1.5, 0.09, fill=BLUE, line=None)
# left card (green): what a screen can't do
shape(s, 0.85, 2.2, 5.75, 3.95, fill=PAPER, line=GREEN, lw=4)
shape(s, 0.85, 2.2, 5.75, 0.16, fill=GREEN, line=None)
tf = tb(s, 1.15, 2.5, 5.15, 3.6)
para(tf, "WHAT A SCREEN CAN'T DO", 18, GREEN, bold=True, first=True, after=10)
para(tf, "\u25A0  Experience \u2014 a hot meal, a cinema, a soft-play maze", 16, INK, after=8)
para(tf, "\u25A0  Being seen \u2014 the \u2018third place\u2019 people still want", 16, INK, after=8)
para(tf, "\u25A0  Serendipity \u2014 the accidental discovery", 16, INK, after=12)
para(tf, "Who goes: people lonely for a place to be, not a thing to own.", 15, MUTE, italic=True)
# right card (coral): pessimist
shape(s, 6.75, 2.2, 5.75, 3.95, fill=PAPER, line=CORAL, lw=4)
shape(s, 6.75, 2.2, 5.75, 0.16, fill=CORAL, line=None)
tf = tb(s, 7.05, 2.5, 5.15, 3.6)
para(tf, "THE PESSIMIST'S HONEST CASE", 18, CORAL, bold=True, first=True, after=10)
para(tf, "\u25A0  Built on car culture, cheap land, idle middle class \u2014 all changing", 16, INK, after=8)
para(tf, "\u25A0  Ghost malls across the US; half-empty malls in China", 16, INK, after=8)
para(tf, "\u25A0  Convenience is addictive \u2014 malls get skipped, not killed", 16, INK, after=12)
para(tf, "The building becomes a stranded asset.", 15, MUTE, italic=True)
footer(s, "03")
notes(s, "[1:10-3:20] Argue both sides. E-commerce won on selection and price; the mall must compete on what a screen can't do. Then be fair: many malls die by a thousand 'why go out?'s.")

# ============ SLIDE 4 — Takeaway (dark) ============
s = sl(); bg(s, INK)
shape(s, 0, 0, SW, 0.22, fill=BLUE, line=None)
tf = tb(s, 0.85, 0.85, 6.5, 0.5); para(tf, "THE DEEPER POINT", 14, RGBColor(0x8F,0xB4,0xFF), bold=True, first=True)
tf = tb(s, 0.85, 1.35, 6.7, 2.4)
para(tf, "A business defined\nby its form can be\ndestroyed by a\ntechnology.",
     34, PAPER, bold=True, first=True, spacing=1.02, font=FONT_H)
tf = tb(s, 0.85, 4.0, 6.7, 1.4)
para(tf, "One defined by the job it does for people survives \u2014 it just changes shape.",
     20, RGBColor(0xD6,0xDA,0xE2), italic=True, first=True)
# right: signpost illustration
illo_signpost(s, 9.9, 1.7, scale=1.15)
# bottom ribbon
shape(s, 0.85, 5.65, 6.6, 1.0, fill=RGBColor(0x1F,0x22,0x2A), line=BLUE, lw=3)
tf = tb(s, 1.1, 5.75, 6.1, 0.8, anchor=MSO_ANCHOR.MIDDLE)
para(tf, "The mall won't die \u2014 it changes jobs: from a warehouse of goods to a stage for human life.",
     16, PAPER, bold=True, first=True)
footer(s, "04", dark=True)
notes(s, "[3:20-4:00] Land the takeaway: form vs function. Close on the one-liner.")

out = r"C:\Users\dlwlrma\OneDrive\Documents\deepseek-harness\default-workspace\Shopping_Malls_Short_Deck.pptx"
prs.save(out)
print("saved:", out, "| slides:", len(prs.slides))
