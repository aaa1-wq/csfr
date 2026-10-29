# -*- coding: utf-8 -*-
"""Build a 40-minute discussion-leader deck for Theme 5: Business.
Two-track spine: Business as glorious / human progress  vs.  Business as evil / havoc.
Maps the five questions on slide 2 of the source deck onto that spine.
"""
from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

# ---------- palette ----------
INK      = RGBColor(0x1A, 0x1A, 0x1A)
DARK     = RGBColor(0x2B, 0x2B, 0x2B)
GREY     = RGBColor(0x6E, 0x6E, 0x6E)
RED      = RGBColor(0xCF, 0x2B, 0x2B)   # "evil" accent (matches source FF0000 family)
GREEN    = RGBColor(0x1F, 0x8A, 0x5A)   # "good" accent
WHITE    = RGBColor(0xFF, 0xFF, 0xFF)
LIGHT    = RGBColor(0xF4, 0xF1, 0xEC)
PANEL_D  = RGBColor(0x22, 0x22, 0x22)

FONT = "Calibri"

prs = Presentation()
prs.slide_width  = Inches(13.333)
prs.slide_height = Inches(7.5)
SW, SH = 13.333, 7.5
BLANK = prs.slide_layouts[6]


def add_slide():
    return prs.slides.add_slide(BLANK)


def rect(slide, x, y, w, h, fill=None, line=None, lw=1.0, shape=MSO_SHAPE.RECTANGLE):
    sp = slide.shapes.add_shape(shape, Inches(x), Inches(y), Inches(w), Inches(h))
    if fill is None:
        sp.fill.background()
    else:
        sp.fill.solid(); sp.fill.fore_color.rgb = fill
    if line is None:
        sp.line.fill.background()
    else:
        sp.line.color.rgb = line; sp.line.width = Pt(lw)
    sp.shadow.inherit = False
    return sp


def txbox(slide, x, y, w, h, anchor=MSO_ANCHOR.TOP):
    tb = slide.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    tf = tb.text_frame
    tf.word_wrap = True
    tf.vertical_anchor = anchor
    tf.margin_left = tf.margin_right = Inches(0.05)
    tf.margin_top = tf.margin_bottom = Inches(0.03)
    return tb, tf


def para(tf, text, size=18, color=INK, bold=False, first=False, align=PP_ALIGN.LEFT,
         space_before=0, space_after=4, italic=False, font=FONT, bullet=None, level=0):
    p = tf.paragraphs[0] if first else tf.add_paragraph()
    p.alignment = align
    p.space_before = Pt(space_before)
    p.space_after = Pt(space_after)
    p.level = level
    if bullet:
        text = f"{bullet}  {text}"
    run = p.add_run(); run.text = text
    f = run.font
    f.size = Pt(size); f.bold = bold; f.italic = italic
    f.color.rgb = color; f.name = font
    return p


def rich(tf, segments, size=18, first=False, align=PP_ALIGN.LEFT, space_before=0,
         space_after=4, bullet=None):
    """segments: list of (text, {bold,color,italic,size})"""
    p = tf.paragraphs[0] if first else tf.add_paragraph()
    p.alignment = align
    p.space_before = Pt(space_before); p.space_after = Pt(space_after)
    if bullet:
        r0 = p.add_run(); r0.text = f"{bullet}  "
        r0.font.size = Pt(size); r0.font.color.rgb = GREY; r0.font.name = FONT; r0.font.bold = True
    for text, st in segments:
        r = p.add_run(); r.text = text
        f = r.font
        f.size = Pt(st.get("size", size)); f.name = FONT
        f.bold = st.get("bold", False); f.italic = st.get("italic", False)
        f.color.rgb = st.get("color", INK)
    return p


def notes(slide, text):
    slide.notes_slide.notes_text_frame.text = text


def kicker(slide, text, color=RED, x=0.75, y=0.55):
    tb, tf = txbox(slide, x, y, 11, 0.4)
    para(tf, text.upper(), size=13, color=color, bold=True, first=True)
    return tb


def title(slide, text, size=32, color=INK, x=0.75, y=0.92, w=11.8, h=1.0):
    tb, tf = txbox(slide, x, y, w, h)
    para(tf, text, size=size, color=color, bold=True, first=True)
    return tb


def accent_rule(slide, x=0.78, y=None, color=RED, w=1.6):
    if y is None:
        y = 1.95
    rect(slide, x, y, w, 0.06, fill=color)


def footer(slide, left, num):
    tb, tf = txbox(slide, 0.5, SH - 0.5, 9, 0.35)
    para(tf, left, size=10, color=GREY, first=True)
    tb2, tf2 = txbox(slide, SW - 1.2, SH - 0.5, 0.9, 0.35)
    para(tf2, num, size=10, color=GREY, first=True, align=PP_ALIGN.RIGHT)


page = 0
def num():
    global page
    page += 1
    return f"{page:02d}"

# ============================================================ 1. TITLE
s = add_slide()
rect(s, 0, 0, SW, SH, fill=PANEL_D)
rect(s, 0, 0, 0.28, SH, fill=RED)
tb, tf = txbox(s, 1.1, 2.35, 11, 1.3)
para(tf, "THEME 5", size=22, color=RED, bold=True, first=True)
tb, tf = txbox(s, 1.1, 3.05, 11.2, 1.6)
para(tf, "Business: Glorious or Evil?", size=52, color=WHITE, bold=True, first=True)
tb, tf = txbox(s, 1.12, 4.55, 11, 1.0)
para(tf, "Two sides of the same engine — and the choices that decide which one wins",
     size=22, color=RGBColor(0xD6, 0xD0, 0xC6), first=True, italic=True)
tb, tf = txbox(s, 1.12, 5.75, 11, 0.5)
para(tf, "A 40-minute guided discussion  ·  Cases from film & real life", size=14,
     color=GREY, first=True)
notes(s, "[0:00–1:30] Hook. 'Every business is an engine. An engine can drive an ambulance or a tank — "
         "the machine is the same; the intent is not.' Today we test both readings. Five questions, one spine: "
         "is business more good than bad, and what does that mean for how I choose an employer, and one day run a company?")

# ============================================================ 2. ROADMAP
s = add_slide()
kicker(s, "The road for the next 40 minutes")
title(s, "Five questions, one spine")
accent_rule(s)
rows = [
    ("01", "Good & evil, side by side", "Two faces of one industry — movies + real life", "6 min"),
    ("02", "Can business be more good than bad?", "The case for yes — and the pushback", "8 min"),
    ("03", "Will you weigh CSR / ESG in a job?", "Your future employer under a moral lens", "8 min"),
    ("04", "If you lead one day: profit or purpose?", "The trade-off you'll actually face", "8 min"),
    ("05", "Will there be shopping malls?", "Business as a form of human life", "6 min"),
]
y = 2.25
for n, t, sub, dur in rows:
    tb, tf = txbox(s, 0.8, y, 0.85, 0.7)
    para(tf, n, size=26, color=RED, bold=True, first=True)
    tb, tf = txbox(s, 1.75, y - 0.02, 8.6, 0.75)
    para(tf, t, size=19, color=INK, bold=True, first=True, space_after=1)
    para(tf, sub, size=13, color=GREY)
    tb, tf = txbox(s, 10.6, y, 1.9, 0.6)
    para(tf, dur, size=14, color=DARK, bold=True, first=True, align=PP_ALIGN.RIGHT)
    y += 0.92
footer(s, "Theme 5: Business", num())
notes(s, "[1:30–3:00] Preview. Note the arc: we open with the shock of contrast, then move from the world "
         "to the self — from 'is business good?' to 'what will YOU do about it?' Close on the mall question, "
         "which sounds trivial but quietly asks whether the whole institution survives.")

# ============================================================ 3. SECTION DIVIDER — Part 1
def divider(n, title_text, sub, note_text):
    s = add_slide()
    rect(s, 0, 0, SW, SH, fill=LIGHT)
    rect(s, 0, 0, SW, 0.22, fill=RED)
    tb, tf = txbox(s, 1.0, 2.55, 11, 1.2)
    para(tf, n, size=90, color=RGBColor(0xDD, 0xD6, 0xCB), bold=True, first=True)
    tb, tf = txbox(s, 1.0, 3.75, 11, 1.0)
    para(tf, title_text, size=40, color=INK, bold=True, first=True)
    tb, tf = txbox(s, 1.02, 4.75, 10.5, 0.9)
    para(tf, sub, size=18, color=GREY, first=True, italic=True)
    notes(s, note_text)
    return s

s = divider("PART 1", "Glorious or Evil?",
            "Same industry, two headlines. Hold both in your hands at once.",
            "[3:00–4:00] Transition. Deliberately keep the two examples in the SAME industry so the contrast "
            "is a genuine comparison, not apples-to-oranges. Ask the room: 'Which one is the real business?'")
num()

# ============================================================ 4. Two-track contrast — PHARMA
s = add_slide()
kicker(s, "Q1 · One industry, two truths")
title(s, "Same industry. Two headlines.", size=30)
accent_rule(s)
# left card good
def card(x, header, header_color, bullets, foot):
    rect(s, x, 2.35, 5.7, 4.15, fill=WHITE, line=RGBColor(0xE2, 0xDD, 0xD4), lw=1)
    rect(s, x, 2.35, 5.7, 0.75, fill=header_color)
    tb, tf = txbox(s, x + 0.25, 2.43, 5.2, 0.6)
    tf.vertical_anchor = MSO_ANCHOR.MIDDLE
    para(tf, header, size=17, color=WHITE, bold=True, first=True)
    tb, tf = txbox(s, x + 0.28, 3.25, 5.15, 2.9)
    for i, b in enumerate(bullets):
        rich(tf, b, size=13.5, first=(i == 0), space_after=7, bullet="—")
    tb, tf = txbox(s, x + 0.28, 5.95, 5.15, 0.45)
    para(tf, foot, size=11, color=GREY, first=True, italic=True)

card(0.78, "THE GLORY  ·  Pharma that saved millions",
     GREEN,
     [[("mRNA vaccines", {"bold": True}), (" compressed a decade of R&D into ~1 year during COVID-19; billions of doses shipped.", {})],
      [("Eradication of disease:", {"bold": True}), (" smallpox, near-eradication of polio — private R&D at planetary scale.", {})],
      [("Profit as fuel:", {"bold": True}), (" returns funded the next generation of cures.", {})]],
     "Business as humanity's best-funded problem-solver.")
card(6.85, "THE WRECKAGE  ·  Pharma that fueled an epidemic",
     RED,
     [[("Purdue's OxyContin:", {"bold": True}), (" marketed a heroin-class drug as safe; ~645,000 US overdose deaths 1999–2021.", {})],
      [("EpiPen:", {"bold": True}), (" price up 600%+ with no real competition — $1 of drug, $735 a pack.", {})],
      [("The playbook:", {"bold": True}), (" capture the regulator, patent a lifeline, price the vulnerable.", {})]],
     "Business as a machine for converting pain into profit.")
footer(s, "Q1 · examples from film & real life (Painkiller 2023; EpiPen / Mylan)", num())
notes(s, "[4:00–7:00] Same industry = pharma. Left: the glory (vaccines, disease eradication). Right: the "
         "wreckage (Purdue/OxyContin from 'Painkiller', the Mylan EpiPen price spike). Point: it is not "
         "one industry's 'nature' — it is a sequence of decisions. Film clip option: Painkiller Ep.02 09:52–13:52 "
         "(sales rep kicked out of a clinic).")

# ============================================================ 5. Movie mirror — Modern Times vs Silicon Valley
s = add_slide()
kicker(s, "Q1 · The stories we tell ourselves")
title(s, "How film frames the machine", size=30)
accent_rule(s)
rect(s, 0.78, 2.35, 5.7, 4.0, fill=LIGHT)
tb, tf = txbox(s, 1.0, 2.55, 5.25, 3.7)
para(tf, "Modern Times (1936)", size=18, color=INK, bold=True, first=True, space_after=6)
para(tf, "Chaplin as a cog in the production line.", size=13.5, color=GREY, italic=True, space_after=10)
para(tf, "Business is evil.", size=14.5, color=RED, bold=True, space_after=2)
para(tf, "Businessmen have no heart.", size=14.5, color=RED, bold=True, space_after=2)
para(tf, "Workers are machines.", size=14.5, color=RED, bold=True, space_after=10)
para(tf, "The fear: efficiency swallows the human.", size=13, color=GREY, italic=True)
rect(s, 6.85, 2.35, 5.7, 4.0, fill=LIGHT)
tb, tf = txbox(s, 7.07, 2.55, 5.25, 3.7)
para(tf, "Silicon Valley (S3E3)", size=18, color=INK, bold=True, first=True, space_after=6)
para(tf, "A tiny startup pressured to 'go enterprise'.", size=13.5, color=GREY, italic=True, space_after=10)
para(tf, "The founder builds something they love.", size=14.5, color=GREEN, bold=True, space_after=2)
para(tf, "The CEO turns it into a boxed product.", size=14.5, color=GREEN, bold=True, space_after=2)
para(tf, "Growth vs. soul, on one whiteboard.", size=14.5, color=GREEN, bold=True, space_after=10)
para(tf, "The hope: the small can still choose.", size=13, color=GREY, italic=True)
footer(s, "Q1 · film as a mirror", num())
notes(s, "[7:00–9:00] Contrast the two films. Modern Times = the classic fear of industry as a meat-grinder. "
         "Silicon Valley = the modern version: not evil bosses, but incentives that quietly turn craft into product. "
         "Ask: which is scarier — a villain, or a good person doing a questionable thing because the numbers say so?")

# ============================================================ 6. Big is evil, small is beautiful — cycle
s = add_slide()
kicker(s, "Q1 · the cycle")
title(s, "Big is evil, small is beautiful — until it isn't", size=28)
accent_rule(s)
# three-node cycle
nodes = [
    (1.6, "THE REBEL", "A newcomer attacks the giant.\nApple's 1984 ad: 'Big Brother' IBM.", GREEN),
    (5.35, "THE GIANT", "The rebel becomes the giant.\nApple is now the 'white terror'.", DARK),
    (9.1, "THE NEW REBEL", "The next newcomer attacks Apple.\nMotorola 2011 Super Bowl: the cycle restarts.", RED),
]
for x, h, body, col in nodes:
    rect(s, x, 2.45, 3.35, 2.75, fill=WHITE, line=RGBColor(0xDD, 0xD8, 0xCF), lw=1)
    rect(s, x, 2.45, 3.35, 0.14, fill=col)
    tb, tf = txbox(s, x + 0.22, 2.72, 2.95, 0.5)
    para(tf, h, size=15, color=col, bold=True, first=True)
    tb, tf = txbox(s, x + 0.22, 3.25, 2.95, 1.8)
    for i, line in enumerate(body.split("\n")):
        para(tf, line, size=13, color=DARK, first=(i == 0), space_after=4)
tb, tf = txbox(s, 0.78, 5.55, 11.8, 1.1)
para(tf, "Orwell's 1984 warned of Big Brother. Every revolution breeds its own Big Brother — "
         "so the question is never 'small or big', it is 'what keeps power accountable?'",
     size=15, color=INK, first=True, italic=True)
footer(s, "Q1 · sources: Orwell's 1984; Apple 1984 & Motorola 2011 Super Bowl ads", num())
notes(s, "[9:00–11:00] The 'small is beautiful' romance is a cycle, not a permanent truth. Apple was the rebel "
         "in 1984 and the Big Brother in Motorola's 2011 ad. Moral: good vs evil is a POSITION on a cycle, "
         "not a property of a company. This sets up Q2: can a business be NET more good than bad?")

# ============================================================ 7. DIVIDER — Part 2
s = divider("PART 2", "Can business be more good than bad?",
            "If yes — how? If no — why not?",
            "[11:00–11:30] Transition into the central normative question.")
num()

# ============================================================ 8. The question, sharpened
s = add_slide()
kicker(s, "Q2")
title(s, "The real question isn't 'good or evil'", size=28)
accent_rule(s)
tb, tf = txbox(s, 0.9, 2.3, 11.5, 1.4)
rich(tf, [("It's whether, ", {"size": 30}),
          ("on net", {"size": 30, "bold": True, "color": RED}),
          (", the value business creates outweighs the harm it externalizes.", {"size": 30})],
     first=True)
cols = [
    ("The case for YES", GREEN, [
        "Value creation is real: goods, jobs, innovation, tax base.",
        "Harm is often a side-effect that regulation can price.",
        "Institutions can be redesigned → business can be steered.",
    ]),
    ("The case for NO", RED, [
        "The profit motive structurally externalizes harm.",
        "'Good' conduct is often PR — greenwashing, ESG-washing.",
        "Bad actors outlast regulation; the market rewards the worst.",
    ]),
    ("The synthesis", DARK, [
        "Not 'good vs evil' but 'good vs badly governed'.",
        "The variable is accountability: rules, transparency, competition.",
        "So: business is a multiplier — good or evil depends on what it multiplies.",
    ]),
]
x = 0.78
for h, col, items in cols:
    rect(s, x, 3.55, 3.85, 3.1, fill=WHITE, line=RGBColor(0xE2, 0xDD, 0xD4), lw=1)
    rect(s, x, 3.55, 3.85, 0.1, fill=col)
    tb, tf = txbox(s, x + 0.2, 3.78, 3.45, 0.4)
    para(tf, h, size=15, color=col, bold=True, first=True)
    tb, tf = txbox(s, x + 0.2, 4.25, 3.5, 2.3)
    for i, it in enumerate(items):
        para(tf, it, size=12.5, color=DARK, first=(i == 0), space_after=6, bullet="•")
    x += 4.0
footer(s, "Q2", num())
notes(s, "[11:30–14:00] Lay out both horns, then move to synthesis. The key move is reframing from a moral "
         "question to an institutional one: 'what it multiplies'. Invite the room to pick a side before you "
         "show the synthesis — then ask what evidence would change their mind.")

# ============================================================ 9. The levers — accountability
s = add_slide()
kicker(s, "Q2 · if yes, HOW")
title(s, "Four levers that decide the sign of the multiplier", size=27)
accent_rule(s)
levers = [
    ("COMPETITION", "Monopoly (CNKI, Monsanto) removes the check that keeps prices and conduct honest.", "20:00"),
    ("TRANSPARENCY", "Sunlight as disinfectant — but 'Facebook has your data' shows how weak it can be.", "14:00"),
    ("REGULATION", "Price a harm and the math changes; unpriced harm is a subsidy to bad behavior.", "20:00"),
    ("NORMS & PEOPLE", "The choices of individual leaders still move the needle — see Q4.", "14:00"),
]
x = 0.78
for h, body, _ in levers:
    rect(s, x, 2.4, 2.85, 3.55, fill=LIGHT)
    rect(s, x, 2.4, 2.85, 0.1, fill=GREEN)
    tb, tf = txbox(s, x + 0.2, 2.65, 2.5, 0.5)
    para(tf, h, size=13.5, color=INK, bold=True, first=True)
    tb, tf = txbox(s, x + 0.2, 3.15, 2.5, 2.6)
    para(tf, body, size=12.5, color=DARK, first=True)
    x += 3.03
tb, tf = txbox(s, 0.78, 6.15, 11.8, 0.7)
para(tf, "The point: 'more good than bad' isn't a personality trait of a company — it's an outcome of the "
         "pressure system around it.", size=13.5, color=GREY, italic=True, first=True)
footer(s, "Q2 · real cases: CNKI monopoly, Monsanto seed lock-in, Facebook/Cambridge Analytica", num())
notes(s, "[14:00–17:00] Four levers. Give one real case each: CNKI (monopoly price-raising, theses locked in), "
         "Monsanto (patented seeds, 90% market), Facebook/Cambridge Analytica (50M users' data to steer opinion). "
         "Punchline: anonymity of the boardroom doesn't matter — the pressure system does.")

# ============================================================ 10. DIVIDER — Part 3
s = divider("PART 3", "Will you weigh CSR / ESG in a job?",
            "The moral lens meets the job offer.",
            "[17:00–17:30] Transition from the world to the self — the first question that directly implicates the students.")
num()

# ============================================================ 11. Employer choice data
s = add_slide()
kicker(s, "Q3 · the evidence")
title(s, "Does purpose actually move your job choice?", size=27)
accent_rule(s)
# left: attractive employers table
tb, tf = txbox(s, 0.8, 2.2, 5.6, 0.5)
para(tf, "Most Attractive Employers in China 2026", size=15, color=INK, bold=True, first=True)
para(tf, "Engineering students (Universum)", size=11, color=GREY)
emps = ["Huawei", "Tencent", "Xiaomi", "ByteDance", "Alibaba", "Apple", "BYD", "JD.com", "Baidu", "State Grid"]
y = 3.0
for i, e in enumerate(emps):
    col = 0.8 if i < 5 else 3.6
    row = y + (i % 5) * 0.52
    tb, tf = txbox(s, col, row, 2.7, 0.45)
    rich(tf, [(f"{i+1}. ", {"bold": True, "color": RED, "size": 13}), (e, {"size": 13, "bold": True})], first=True)
# right: survey stat block
rect(s, 6.55, 2.2, 5.95, 1.35, fill=LIGHT)
tb, tf = txbox(s, 6.8, 2.32, 5.5, 1.15)
rich(tf, [("~9 in 10", {"size": 30, "bold": True, "color": GREEN}),
          (" Gen Z say a company's purpose affects how long they'll stay.", {"size": 14})], first=True)
para(tf, "Deloitte Global 2025 Gen Z & Millennial Survey", size=10.5, color=GREY, italic=True)
rect(s, 6.55, 3.75, 5.95, 2.95, fill=WHITE, line=RGBColor(0xE2, 0xDD, 0xD4), lw=1)
tb, tf = txbox(s, 6.8, 3.9, 5.5, 2.7)
para(tf, "But watch the gap:", size=14, color=INK, bold=True, first=True, space_after=6)
para(tf, "Stated values ≠ revealed preferences (we say CSR matters, then chase the highest offer).", size=12.5, space_after=5, bullet="•")
para(tf, "The most 'attractive' employers are often the most contested (data, gig work, market power).", size=12.5, space_after=5, bullet="•")
para(tf, "Question: is 'attractive' the same as 'good'?", size=12.5, color=RED, bold=True, bullet="•")
footer(s, "Q3 · source: Universum China 2026; Deloitte Gen Z & Millennial Survey 2025", num())
notes(s, "[17:30–20:00] Present the data. Note the tension: the most attractive employers are frequently the "
         "most contested. Ask the room to be honest: 'when your two offers differ by 30% salary but 30% on ethics, "
         "which do you take?' This is the lived version of Q2.")

# ============================================================ 12. Would you leave?
s = add_slide()
kicker(s, "Q3 · the harder half")
title(s, "Would you actually leave?", size=30)
accent_rule(s)
tb, tf = txbox(s, 0.9, 2.3, 11.5, 0.9)
para(tf, "A company is 'socially irresponsible' the week after you sign. Do you walk?", size=20, color=INK, italic=True, first=True)
blocks = [
    ("Reasons to stay", GREEN, ["Voice beats exit: reform from inside.", "You need the job; principle has a price too.", "The 'irresponsible' firm may still do net good."]),
    ("Reasons to leave", RED, ["Complicity has a cost — the OxyContin rep could have refused.", "Your labor IS the product; you fund the harm.", "Sunk cost is not a moral argument."]),
    ("The honest middle", DARK, ["Draw your line BEFORE the offer, not after.", "Leave the room, not always the company: raise it first.", "Ask: what would I want on my conscience in 10 years?"]),
]
x = 0.78
for h, col, items in blocks:
    rect(s, x, 3.35, 3.85, 3.05, fill=LIGHT)
    rect(s, x, 3.35, 3.85, 0.1, fill=col)
    tb, tf = txbox(s, x + 0.2, 3.55, 3.45, 0.4)
    para(tf, h, size=15, color=col, bold=True, first=True)
    tb, tf = txbox(s, x + 0.2, 4.0, 3.5, 2.3)
    for i, it in enumerate(items):
        para(tf, it, size=12.5, color=DARK, first=(i == 0), space_after=6, bullet="•")
    x += 4.0
footer(s, "Q3", num())
notes(s, "[20:00–23:00] This is the crux of Q3. Force the honesty: would you leave? The 'honest middle' "
         "is the most useful — set your line in advance. Note that the Painkiller sales reps WERE the mechanism "
         "of harm; individual choice is not a fiction.")

# ============================================================ 13. DIVIDER — Part 4
s = divider("PART 4", "If you lead one day: profit or purpose?",
            "The trade-off from the other side of the desk.",
            "[23:00–23:30] Transition to the leadership seat.")
num()

# ============================================================ 14. Profit vs purpose
s = add_slide()
kicker(s, "Q4 · the leader's seat")
title(s, "You are the CEO. Profit — or something else?", size=27)
accent_rule(s)
# shareholder vs stakeholder
rect(s, 0.78, 2.35, 5.6, 1.9, fill=WHITE, line=RGBColor(0xE2, 0xDD, 0xD4), lw=1)
tb, tf = txbox(s, 1.0, 2.5, 5.2, 1.65)
para(tf, "The shareholder view", size=15, color=DARK, bold=True, first=True, space_after=4)
para(tf, "\"Maximize profit within the rules.\" Friedman's claim: the only social responsibility "
         "of business is to increase its profits — and to be honest about it.", size=12.5, color=INK)
rect(s, 6.75, 2.35, 5.75, 1.9, fill=WHITE, line=RGBColor(0xE2, 0xDD, 0xD4), lw=1)
tb, tf = txbox(s, 6.97, 2.5, 5.35, 1.65)
para(tf, "The stakeholder view", size=15, color=DARK, bold=True, first=True, space_after=4)
para(tf, "The firm owes something to workers, customers, communities, and the future — "
         "not only to shareholders. Profit is a means, not the end.", size=12.5, color=INK)
# the real dilemma line
rect(s, 0.78, 4.55, 11.72, 1.15, fill=LIGHT)
tb, tf = txbox(s, 1.05, 4.68, 11.2, 0.95)
rich(tf, [("The trade-off is real, but usually not a straight line. ", {"bold": True, "size": 15}),
          ("Firms that gut safety, labor, or the environment usually destroy value later — see Purdue, "
           "which ended in bankruptcy and a $7.4B judgment.", {"size": 14})], first=True)
tb, tf = txbox(s, 0.9, 5.9, 11.5, 0.9)
para(tf, "Turn to your friend: If you run this company, do you take the profitable-but-harmful contract? "
         "Why — and how does your classmate answer differently?", size=14.5, color=RED, bold=True, first=True)
footer(s, "Q4 · Friedman vs stakeholder theory; Purdue Pharma (Painkiller)", num())
notes(s, "[23:30–27:00] Put Friedman on the table honestly, then the stakeholder reply. The key nuance: "
         "the trade-off is usually NOT a straight line at a single instant — bad profit is often deferred cost. "
         "Then run the 'ask your friend' prompt for 2 minutes of pair discussion.")

# ============================================================ 15. The long game — good is good business?
s = add_slide()
kicker(s, "Q4 · the long game")
title(s, "When 'good' becomes the profitable move", size=28)
accent_rule(s)
rows = [
    (GREEN, "Trust is an asset.", "Brands that keep promises can charge a premium and retain talent — hard to fake, hard to copy."),
    (GREEN, "Cheap harm is short-lived harm.", "Purdue's 'savings' on safety became a $7.4B bill. Externalized cost comes home."),
    (RED, "But timing matters.", "Short-horizon leaders can profit from harm for years before consequences arrive — the incentive to do wrong is real."),
    (RED, "So governance closes the gap.", "Make the future cost visible now: liability, disclosure, and competition (back to Q2)."),
]
y = 2.35
for col, h, body in rows:
    rect(s, 0.78, y, 0.12, 0.9, fill=col)
    tb, tf = txbox(s, 1.1, y - 0.03, 4.0, 0.9)
    para(tf, h, size=15, color=col, bold=True, first=True)
    tb, tf = txbox(s, 5.1, y - 0.03, 7.3, 0.95)
    para(tf, body, size=13, color=DARK, first=True)
    y += 1.02
footer(s, "Q4 · resolves Q2: accountability closes the timing gap", num())
notes(s, "[27:00–29:00] Resolve the tension: good conduct IS profitable — over the long run, and only if "
         "the timing gap is closed by governance. This loops back to Q2's 'pressure system'. Profit and purpose "
         "converge when you stop letting firms borrow from the future.")

# ============================================================ 16. DIVIDER — Part 5
s = divider("PART 5", "Will there be shopping malls in the future?",
            "The odd question that asks whether the institution survives.",
            "[29:00–29:30] Transition to the closing question. It sounds light but it's profound.")
num()

# ============================================================ 17. Malls
s = add_slide()
kicker(s, "Q5 · the closing riddle")
title(s, "Will there be shopping malls in the future?", size=27)
accent_rule(s)
# two scenarios
rect(s, 0.78, 2.35, 5.6, 3.65, fill=LIGHT)
rect(s, 0.78, 2.35, 5.6, 0.1, fill=GREEN)
tb, tf = txbox(s, 1.0, 2.55, 5.2, 3.35)
para(tf, "YES — but transformed", size=16, color=GREEN, bold=True, first=True, space_after=6)
para(tf, "Not for buying things — e-commerce ate that.", size=12.5, space_after=5, bullet="•")
para(tf, "For experience: food, play, services, community, 'third places'.", size=12.5, space_after=5, bullet="•")
para(tf, "The mall becomes a stage for human presence, not a warehouse of goods.", size=12.5, space_after=5, bullet="•")
para(tf, "Who goes: people lonely for a place to be, not a thing to own.", size=12.5, bullet="•")
rect(s, 6.75, 2.35, 5.75, 3.65, fill=LIGHT)
rect(s, 6.75, 2.35, 5.75, 0.1, fill=RED)
tb, tf = txbox(s, 6.97, 2.55, 5.35, 3.35)
para(tf, "NO — the institution dies", size=16, color=RED, bold=True, first=True, space_after=6)
para(tf, "Delivery + AR retail + social commerce dissolve the need.", size=12.5, space_after=5, bullet="•")
para(tf, "The mall was a child of car culture and cheap land — both changing.", size=12.5, space_after=5, bullet="•")
para(tf, "Ghost malls already dot the US and China — the trend is visible.", size=12.5, space_after=5, bullet="•")
para(tf, "The function disperses; the building is a stranded asset.", size=12.5, bullet="•")
tb, tf = txbox(s, 0.9, 6.2, 11.5, 0.7)
para(tf, "Whichever you choose, you're really answering: is business a place we go, or a function that finds us?",
     size=14, color=INK, italic=True, first=True)
footer(s, "Q5 · tie back: business as a form of human life", num())
notes(s, "[29:30–33:00] Run this as a live vote: yes/no. Then explore WHY. The deep point: the mall question "
         "is a proxy for 'does business still need a physical/communal form, or does it become invisible ambient "
         "infrastructure?' Connect to Q1: is business a stage for human life, or a function that processes us?")

# ============================================================ 18. Synthesis
s = add_slide()
rect(s, 0, 0, SW, SH, fill=PANEL_D)
rect(s, 0, 0, 0.28, SH, fill=RED)
kicker(s, "Synthesis", color=RED, x=1.1, y=0.75)
tb, tf = txbox(s, 1.1, 1.15, 11, 0.9)
para(tf, "What we actually decided today", size=32, color=WHITE, bold=True, first=True)
pts = [
    ("01", "Business is a multiplier, not a moral agent.", "It amplifies whatever it is pointed at. The pointing is human."),
    ("02", "Good vs evil is a position on a cycle.", "Today's rebel is tomorrow's Big Brother — vigilance, not romance."),
    ("03", "Accountability, not virtue, decides the sign.", "Competition, transparency, regulation, norms (Q2)."),
    ("04", "Your choices are the last lever.", "The job you take and the contract you refuse are real votes (Q3, Q4)."),
]
y = 2.35
for n, h, b in pts:
    tb, tf = txbox(s, 1.1, y, 0.9, 0.9)
    para(tf, n, size=24, color=RED, bold=True, first=True)
    tb, tf = txbox(s, 2.0, y - 0.05, 10.4, 0.95)
    para(tf, h, size=18, color=WHITE, bold=True, first=True, space_after=2)
    para(tf, b, size=13, color=RGBColor(0xC9, 0xC3, 0xB8))
    y += 1.12
notes(s, "[33:00–36:00] Land the four takeaways. Emphasize #4: the abstract debate resolves into personal "
         "decisions. This is the bridge to the closing.")

# ============================================================ 19. Closing / discussion
s = add_slide()
kicker(s, "Over to you")
title(s, "Three questions to leave with", size=31)
accent_rule(s)
qs = [
    ("Pick ONE firm you admire. Argue the opposite case honestly.", "What harm does its business model externalize?"),
    ("Draw your line now.", "What would make you leave a job you love?"),
    ("The mall, but bigger:", "If business disappeared tomorrow, what part of human life would you miss most?"),
]
y = 2.35
for i, (q, sub) in enumerate(qs):
    rect(s, 0.78, y, 11.72, 1.15, fill=LIGHT)
    tb, tf = txbox(s, 1.0, y + 0.08, 0.8, 0.9)
    para(tf, f"Q{i+1}", size=20, color=RED, bold=True, first=True)
    tb, tf = txbox(s, 1.95, y + 0.1, 10.3, 0.95)
    para(tf, q, size=15, color=INK, bold=True, first=True, space_after=2)
    para(tf, sub, size=12, color=GREY)
    y += 1.28
tb, tf = txbox(s, 0.9, 6.35, 11.5, 0.6)
para(tf, "Thank you — discussion now open.", size=16, color=RED, bold=True, first=True, align=PP_ALIGN.CENTER)
footer(s, "Theme 5: Business  ·  end", num())
notes(s, "[36:00–40:00] Open discussion. Q1 forces steel-manning the opposite view. Q2 forces a personal "
         "commitment. Q3 is the emotional close — 'what would you miss' reframes business as part of human life. "
         "Buffer: if short on time, drop Q3 and end on Q2.")

prs.save(r"C:\Users\dlwlrma\OneDrive\Documents\deepseek-harness\default-workspace\Theme5_Business_Discussion_40min.pptx")
print("saved, slides =", len(prs.slides.__iter__.__self__._sldIdLst))
