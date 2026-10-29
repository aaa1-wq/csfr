# -*- coding: utf-8 -*-
"""Author 19 editorial_bleed pages via STRICT template substitution, with:
- only declared typography sizes (body24, subtitle30, title46, annotation18)
- every text block wrapped to fit its slot/canvas width (multi-line tspans)
Preserves placeholder id/type/idx/bounds -> passes strict-adherence gate.
"""
import base64, os, html, re

PROJ = r"C:\Users\dlwlrma\OneDrive\Documents\deepseek-harness\default-workspace\projects\theme5_business_film_20261028"
IMG = os.path.join(PROJ, "images"); TPL = os.path.join(PROJ, "templates"); OUT = os.path.join(PROJ, "svg_output")
os.makedirs(OUT, exist_ok=True)

def b64(fn):
    with open(os.path.join(IMG, fn), "rb") as f:
        return "data:image/jpeg;base64," + base64.b64encode(f.read()).decode("ascii")
def esc(s): return html.escape(s, quote=False)
def load(n):
    with open(os.path.join(TPL, n), encoding="utf-8") as f: return f.read()

IMG_RE = re.compile(r'href="data:image/[^"]*"')
def set_img(svg, fn, n=1):
    ms = list(IMG_RE.finditer(svg))
    if len(ms) < n: return svg
    m = ms[n-1]
    return svg[:m.start()] + f'href="../images/{fn}"' + svg[m.end():]

# approximate char width factors (px per char per px font-size)
def wrap(text, max_width_px, size, font="body"):
    factor = 0.62 if font=="title" else 0.56
    per = factor*size
    maxchars = max(6, int(max_width_px/per))
    words = text.split()
    lines=[]; cur=""
    for w in words:
        t=(cur+" "+w).strip()
        if len(t)<=maxchars: cur=t
        else:
            if cur: lines.append(cur)
            cur=w
    if cur: lines.append(cur)
    return lines

def fit_carrier(svg, carrier_id, text, size, width_px, font="body", max_lines=None):
    """Replace carrier <text> content with wrapped tspans at given size; force size."""
    pat = re.compile(r'(<text[^>]*id="%s"[^>]*>)(.*?)(</text>)' % re.escape(carrier_id), re.S)
    m = pat.search(svg)
    if not m: 
        raise SystemExit("carrier not found: "+carrier_id)
    opentag = m.group(1)
    x = re.search(r'\bx="([\d.]+)"', opentag); x = x.group(1) if x else "80"
    y = re.search(r'\by="([\d.]+)"', opentag); y0 = float(y.group(1)) if y else 100.0
    # force font-size in opentag
    opentag2 = re.sub(r'font-size="[\d.]+"', f'font-size="{size}"', opentag)
    lines = wrap(text, width_px, size, font)
    if max_lines and len(lines)>max_lines:
        lines = lines[:max_lines]
        lines[-1] = lines[-1].rstrip(" ,.")+"\u2026"
    lh = int(size*1.28)
    body = '<tspan x="%s" dy="0">%s</tspan>' % (x, esc(lines[0]))
    for ln in lines[1:]:
        body += '<tspan x="%s" dy="%d">%s</tspan>' % (x, lh, esc(ln))
    return svg[:m.start()] + opentag2 + body + m.group(3) + svg[m.end():]

def credit(svg, txt):
    return svg.replace("</svg>",
      f'  <text x="1200" y="708" text-anchor="end" fill="#7A756C" font-family="Arial, sans-serif" font-size="18">{esc(txt)}</text>\n</svg>')

def finalize(name, svg):
    assert "{{" not in svg, "leftover token "+name
    with open(os.path.join(OUT, name+".svg"),"w",encoding="utf-8") as f: f.write(svg)

# declared sizes
BODY=24; SUBT=30; TITLE=46; ANN=18

# P01 cover (hero_full) title bounds 80 448 1120 96 sub 80 568 880 56
s=load("01_hero_full.svg"); s=set_img(s,"im_cover.jpg")
s=fit_carrier(s,"hero-full-title-carrier","Business: Glorious or Evil?",TITLE,1120,"title",1)
s=fit_carrier(s,"hero-full-subtitle-carrier","Two sides of the same engine \u2014 and the choices that decide which one wins",ANN,860,"body",2)
s=credit(s,"im_cover.jpg \u2014 Joe Haupt from USA / Wikimedia / CC BY-SA 2.0"); finalize("01_cover",s)

# P02 roadmap (full_statement) msg bounds 80 328 1120 200 ; support 80 556 880 56
s=load("09_full_statement.svg")
s=fit_carrier(s,"full-statement-message-carrier","Five questions, one spine",TITLE,1120,"title",2)
s=fit_carrier(s,"full-statement-support-carrier","01 Good & evil, side by side  \u00b7  02 More good than bad?  \u00b7  03 CSR / ESG in a job?  \u00b7  04 Profit or purpose?  \u00b7  05 Shopping malls?",ANN,840,"body",1)
finalize("02_roadmap",s)

# P03 Part1 (chapter_full) num bounds 80 232 320 72 ; title 80 332 1120 96 ; desc 80 452 880 56
s=load("05_chapter_full.svg"); s=set_img(s,"im_modern_times.jpg")
s=s.replace("{{CHAPTER_NUM}}", esc("PART 1")).replace('font-size="56"', 'font-size="46"').replace('x="80" y="292"', 'x="80" y="286"')
s=s.replace('font-size="56"', 'font-size="46"')
s=fit_carrier(s,"chapter-full-title-carrier","Glorious or Evil?",TITLE,1100,"title",1)
s=fit_carrier(s,"chapter-full-desc-carrier","Same industry, two headlines. Hold both in your hands at once.",ANN,860,"body",2)
s=credit(s,"im_modern_times.jpg \u2014 Public Domain / Wikimedia"); finalize("03_part1_divider",s)

# P04 pharma (split_bleed) title 720 216 480 88 ; body 720 336 480 240
s=load("03_split_bleed.svg"); s=set_img(s,"im_food_inc.jpg")
s=fit_carrier(s,"split-bleed-title-carrier","Same industry, two headlines",SUBT,470,"title",1)
s=fit_carrier(s,"split-bleed-body-carrier","THE GLORY: mRNA vaccines compressed a decade of R&D into a year; smallpox gone, polio nearly.  THE WRECKAGE: OxyContin marketed as safe, ~645,000 US deaths; EpiPen up 600% with no rival; capture the regulator, price the vulnerable.",ANN,462,"body",11)
finalize("04_pharma",s)

# P05 film mirror (triptych) title 80 64 1120 72 ; caps 32 560 363 128 / 459... / 886...
s=load("07_triptych.svg")
_imgs=["im_modern_times.jpg","im_silicon_valley.jpg","im_modern_times.jpg"]
for _nm in _imgs:
    s=IMG_RE.sub('href="../images/%s"'%_nm, s, count=1)
s=fit_carrier(s,"triptych-title-carrier","How film frames the machine",TITLE,1100,"title",1)
s=fit_carrier(s,"triptych-caption-one-carrier","Modern Times (1936): business is evil; workers are machines.",ANN,350,"body",3)
s=fit_carrier(s,"triptych-caption-two-carrier","Same engine, two stories: the fear, and the hope the small can still choose.",ANN,350,"body",3)
s=fit_carrier(s,"triptych-caption-three-carrier","Silicon Valley S3E3: the founder's craft vs the CEO's boxed product.",ANN,350,"body",3)
s=credit(s,"im_modern_times.jpg PD / im_silicon_valley.jpg \u2014 SanDiegoEntrepreneur / Wikimedia / CC BY-SA 4.0")
finalize("05_film_mirror",s)

# P06 cycle (full_statement)
s=load("09_full_statement.svg")
s=fit_carrier(s,"full-statement-message-carrier","Big is evil, small is beautiful \u2014 until it isn't",TITLE,1120,"title",2)
s=fit_carrier(s,"full-statement-support-carrier","THE REBEL attacks the giant (Apple 1984) \u00b7 THE GIANT becomes Big Brother \u00b7 THE NEW REBEL attacks it (Motorola 2011). Good vs evil is a position on a cycle.",ANN,840,"body",1)
finalize("06_cycle",s)

# P07 Part2
s=load("05_chapter_full.svg"); s=set_img(s,"im_food_inc.jpg")
s=s.replace("{{CHAPTER_NUM}}", esc("PART 2")).replace('font-size="56"', 'font-size="46"').replace('x="80" y="292"', 'x="80" y="286"')
s=s.replace('font-size="56"', 'font-size="46"')
s=fit_carrier(s,"chapter-full-title-carrier","More good than bad?",TITLE,1100,"title",1)
s=fit_carrier(s,"chapter-full-desc-carrier","If yes \u2014 how? If no \u2014 why not?",ANN,860,"body",1)
s=credit(s,"im_food_inc.jpg \u2014 Public Domain / Wikimedia"); finalize("07_part2_divider",s)

# P08 net good (split_bleed)
s=load("03_split_bleed.svg"); s=set_img(s,"im_modern_times.jpg")
s=fit_carrier(s,"split-bleed-title-carrier","Not 'good or evil' \u2014 net good?",SUBT,470,"title",1)
s=fit_carrier(s,"split-bleed-body-carrier","On NET: value vs externalized harm.  YES: value creation is real; harm can be priced.  NO: profit structurally externalizes harm; 'good' is often PR.  SYNTHESIS: 'good vs badly governed' \u2014 the variable is accountability.",ANN,462,"body",11)
finalize("08_net_good",s)

# P09 levers (full_statement)
s=load("09_full_statement.svg")
s=fit_carrier(s,"full-statement-message-carrier","Four levers that decide the sign of the multiplier",TITLE,1120,"title",2)
s=fit_carrier(s,"full-statement-support-carrier","COMPETITION \u00b7 TRANSPARENCY \u00b7 REGULATION \u00b7 NORMS & PEOPLE. 'More good than bad' is not a trait of a company \u2014 it is an outcome of the pressure system around it.",ANN,840,"body",1)
finalize("09_levers",s)

# P10 Part3
s=load("05_chapter_full.svg"); s=set_img(s,"im_facebook.jpg")
s=s.replace("{{CHAPTER_NUM}}", esc("PART 3")).replace('font-size="56"', 'font-size="46"').replace('x="80" y="292"', 'x="80" y="286"')
s=s.replace('font-size="56"', 'font-size="46"')
s=fit_carrier(s,"chapter-full-title-carrier","Will you weigh CSR / ESG in a job?",TITLE,1100,"title",1)
s=fit_carrier(s,"chapter-full-desc-carrier","The moral lens meets the job offer.",ANN,860,"body",1)
s=credit(s,"im_facebook.jpg \u2014 CC0 / Wikimedia"); finalize("10_part3_divider",s)

# P11 employer (split_bleed)
s=load("03_split_bleed.svg"); s=set_img(s,"im_silicon_valley.jpg")
s=fit_carrier(s,"split-bleed-title-carrier","Does purpose move you?",SUBT,470,"title",1)
s=fit_carrier(s,"split-bleed-body-carrier","Most attractive employers in China 2026 (engineering): Huawei, Tencent, Xiaomi, ByteDance, Alibaba, Apple, BYD, JD.com, Baidu, State Grid.  ~9 in 10 Gen Z say purpose affects how long they stay (Deloitte 2025).  The gap: the most 'attractive' employers are often the most contested.",ANN,462,"body",11)
s=credit(s,"im_silicon_valley.jpg \u2014 SanDiegoEntrepreneur / Wikimedia / CC BY-SA 4.0"); finalize("11_employer",s)

# P12 leave (full_statement)
s=load("09_full_statement.svg")
s=fit_carrier(s,"full-statement-message-carrier","Would you actually leave?",TITLE,1120,"title",1)
s=fit_carrier(s,"full-statement-support-carrier","STAY: voice beats exit; you need the job too.  LEAVE: your labor is the product; sunk cost is no moral argument.  MIDDLE: draw your line before the offer \u2014 what would you want on your conscience in ten years?",ANN,840,"body",1)
finalize("12_leave",s)

# P13 Part4
s=load("05_chapter_full.svg"); s=set_img(s,"im_painkiller.jpg")
s=s.replace("{{CHAPTER_NUM}}", esc("PART 4")).replace('font-size="56"', 'font-size="46"').replace('x="80" y="292"', 'x="80" y="286"')
s=s.replace('font-size="56"', 'font-size="46"')
s=fit_carrier(s,"chapter-full-title-carrier","Profit, or purpose?",TITLE,1100,"title",1)
s=fit_carrier(s,"chapter-full-desc-carrier","The trade-off from the other side of the desk.",ANN,860,"body",1)
s=credit(s,"im_painkiller.jpg \u2014 Jernej Furman from Slovenia / Wikimedia / CC BY 2.0"); finalize("13_part4_divider",s)

# P14 profit/purpose (split_bleed_reverse) title 80 216 480 88 ; body 80 336 480 240
s=load("04_split_bleed_reverse.svg"); s=set_img(s,"im_painkiller.jpg")
s=fit_carrier(s,"split-bleed-reverse-title-carrier","Profit \u2014 or something else?",SUBT,470,"title",1)
s=fit_carrier(s,"split-bleed-reverse-body-carrier","SHAREHOLDER: 'maximize profit within the rules' (Friedman).  STAKEHOLDER: the firm owes workers, customers, communities, the future; profit is a means.  NOT A STRAIGHT LINE: firms that gut safety or the environment destroy value later \u2014 Purdue: bankruptcy and a $7.4B judgment.",ANN,462,"body",11)
s=credit(s,"im_painkiller.jpg \u2014 Jernej Furman from Slovenia / Wikimedia / CC BY 2.0"); finalize("14_profit_purpose",s)

# P15 long game (full_statement)
s=load("09_full_statement.svg")
s=fit_carrier(s,"full-statement-message-carrier","When 'good' becomes the profitable move",TITLE,1120,"title",2)
s=fit_carrier(s,"full-statement-support-carrier","Trust is an asset. Cheap harm is short-lived (Purdue's 'savings' became a $7.4B bill). But timing matters \u2014 so governance closes the gap: make future cost visible now.",ANN,840,"body",1)
finalize("15_long_game",s)

# P16 Part5
s=load("05_chapter_full.svg"); s=set_img(s,"im_mall.jpg")
s=s.replace("{{CHAPTER_NUM}}", esc("PART 5")).replace('font-size="56"', 'font-size="46"').replace('x="80" y="292"', 'x="80" y="286"')
s=s.replace('font-size="56"', 'font-size="46"')
s=fit_carrier(s,"chapter-full-title-carrier","Will there be shopping malls?",TITLE,1100,"title",1)
s=fit_carrier(s,"chapter-full-desc-carrier","The odd question that asks whether the institution survives.",ANN,860,"body",2)
s=credit(s,"im_mall.jpg \u2014 Retail Thriller / Wikimedia / CC BY-SA 4.0"); finalize("16_part5_divider",s)

# P17 malls (split_bleed)
s=load("03_split_bleed.svg"); s=set_img(s,"im_mall.jpg")
s=fit_carrier(s,"split-bleed-title-carrier","Will there be shopping malls?",SUBT,470,"title",1)
s=fit_carrier(s,"split-bleed-body-carrier","YES: not for buying things (e-commerce ate that) but for experience \u2014 food, play, community.  NO: delivery + AR + social commerce dissolve the need; ghost malls already dot the US and China.  Either way: is business a place we go, or a function that finds us?",ANN,462,"body",11)
s=credit(s,"im_mall.jpg \u2014 Retail Thriller / Wikimedia / CC BY-SA 4.0"); finalize("17_malls",s)

# P18 synthesis (full_statement)
s=load("09_full_statement.svg")
s=fit_carrier(s,"full-statement-message-carrier","What we actually decided today",TITLE,1120,"title",1)
s=fit_carrier(s,"full-statement-support-carrier","01 Business is a multiplier, not a moral agent.  02 Good vs evil is a position on a cycle.  03 Accountability, not virtue, decides the sign.  04 Your choices are the last lever.",ANN,840,"body",1)
finalize("18_synthesis",s)

# P19 closing (closing_full) msg 80 468 1120 88 ; contact 80 580 880 48
s=load("10_closing_full.svg"); s=set_img(s,"im_closing.jpg")
s=fit_carrier(s,"closing-full-message-carrier","Three questions to leave with",TITLE,1100,"title",1)
s=fit_carrier(s,"closing-full-contact-carrier","Argue the opposite case / Draw your line before the offer / What would you miss most?  Thank you.",ANN,860,"body",1)
s=credit(s,"im_closing.jpg \u2014 Public Domain / Wikimedia"); finalize("19_closing",s)

print("Authored:", sorted(os.listdir(OUT)))

