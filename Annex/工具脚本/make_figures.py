# -*- coding: utf-8 -*-
"""Generate the figures used in the study-handbook PDF."""
import os
from PIL import Image, ImageDraw, ImageFont

OUT = "assets"
os.makedirs(OUT, exist_ok=True)

BLACK = "C:/Windows/Fonts/simhei.ttf"      # bold sans
REG = "C:/Windows/Fonts/msyh.ttc"          # regular sans
SERIF = "C:/Windows/Fonts/simsun.ttc"

S = 2  # supersample factor


def font(path, size):
    return ImageFont.truetype(path, size * S)


def text_w(d, s, f):
    box = d.textbbox((0, 0), s, font=f)
    return box[2] - box[0], box[3] - box[1]


def wrap(d, s, f, maxw):
    lines, cur = [], ""
    for ch in s:
        if ch == "\n":
            lines.append(cur)
            cur = ""
            continue
        if text_w(d, cur + ch, f)[0] <= maxw:
            cur += ch
        else:
            lines.append(cur)
            cur = ch
    if cur:
        lines.append(cur)
    return lines


def new_canvas(w, h, bg="white"):
    img = Image.new("RGB", (w * S, h * S), bg)
    return img, ImageDraw.Draw(img)


def finish(img, name):
    img = img.resize((img.width // S, img.height // S), Image.LANCZOS)
    path = os.path.join(OUT, name)
    img.save(path, "PNG")
    print("saved", path, img.size)


def draw_multiline(d, xy, text, f, fill, maxw, spacing=1.45, align="left"):
    x, y = xy
    lh = int(f.size * spacing / S) * S
    for ln in wrap(d, text, f, maxw):
        w = text_w(d, ln, f)[0]
        dx = 0 if align == "left" else (maxw - w) // 2
        d.text((x + dx, y), ln, font=f, fill=fill)
        y += lh
    return y


# ---------------------------------------------------------------- figure: stair
def fig_staircase():
    W, H = 1040, 575
    img, d = new_canvas(W, H)
    L, R, T, B = 130, 910, 110, 360
    d.line((L, B * S, R * S, B * S), fill="#555555", width=2 * S)
    d.line((L * S, B * S, L * S, T * S), fill="#555555", width=2 * S)
    d.text((30 * S, (T - 30) * S), "海拔（米）", font=font(REG, 15), fill="#333333")

    steps = [
        (0.00, 0.32, 4000, "第一级阶梯", "青藏高原（4000米以上）", "#efe4d2"),
        (0.34, 0.64, 1500, "第二级阶梯", "内蒙古高原、黄土高原、云贵高原（1000—2000米）", "#f6efdd"),
        (0.66, 0.96, 300, "第三级阶梯", "东北平原、华北平原、长江中下游平原（500米以下）", "#eef6e6"),
    ]
    f_cap = font(BLACK, 14)
    for k, (x0, x1, h, cap, names, fill) in enumerate(steps):
        px0, px1 = L + (R - L) * x0, L + (R - L) * x1
        py = B - h / 4200 * (B - T)
        d.rectangle((px0 * S, py * S, px1 * S, B * S), fill=fill, outline="#7a7a7a", width=S)
        d.line((px0 * S, py * S, px1 * S, py * S), fill="#7a7a7a", width=2 * S)
        w, _ = text_w(d, cap, f_cap)
        d.text(((px0 + px1) / 2 - w / 2, (py + 10) * S), cap, font=f_cap, fill="#111111")
        # mark on the y axis
        d.line((L * S - 8 * S, py * S, L * S, py * S), fill="#555555", width=2 * S)
        lab = f"{h}"
        w, _ = text_w(d, lab, font(REG, 12))
        d.text((L * S - 16 * S - w, (py - 9) * S), lab, font=font(REG, 12), fill="#555555")

    # name legend under the axis
    f_txt = font(REG, 13)
    y = B + 22
    for x, tag, names, color in [(L, "①", "青藏高原（4000米以上）", "#b98b5e"),
                                 (L, "②", "内蒙古高原、黄土高原、云贵高原（1000—2000米）", "#c8a94f"),
                                 (L, "③", "东北平原、华北平原、长江中下游平原（500米以下）", "#6aa84f")]:
        d.rectangle((x * S, (y + 3) * S, (x + 14) * S, (y + 17) * S), fill=color)
        d.text(((x + 22) * S, y * S), f"{tag}{names}", font=f_txt, fill="#333333")
        y += 24
    d.text((L * S, (y + 6) * S), "（第一级阶梯以高原为主；第二级阶梯高原与盆地相间；"
                                 "第三级阶梯以平原和丘陵为主）", font=font(REG, 13), fill="#666666")

    d.line((R * S - 6 * S, (B + 122) * S, L * S + 6 * S, (B + 122) * S), fill="#2b6cb0", width=2 * S)
    d.polygon([(L * S + 2 * S, (B + 122) * S), (L * S + 16 * S, (B + 115) * S),
               (L * S + 16 * S, (B + 129) * S)], fill="#2b6cb0")
    d.text(((L + 24) * S, (B + 132) * S), "河流整体自西向东入海；海洋暖湿气流自东向西推进",
           font=font(REG, 14), fill="#2b6cb0")

    d.rectangle(((R + 8) * S, T * S, (R + 40) * S, B * S), fill="#cfe4f5", outline="#7fb2dd", width=S)
    d.text(((R + 46) * S, ((T + B) / 2 - 10) * S), "海洋", font=font(BLACK, 15), fill="#2b6cb0")
    d.text((L * S, 14 * S), "图1  中国地势三级阶梯示意图（按教材表述绘制，高度比例仅为示意）",
           font=font(BLACK, 17), fill="#111111")
    finish(img, "fig_staircase.png")


# ------------------------------------------------------------- figure: China map
def fig_map():
    src = Image.open(os.path.join(OUT, "china_map.jpeg")).convert("RGB")
    map_only = src.crop((0, 0, src.width, 700))          # keep the two insets intact
    scale = 1180 / map_only.width
    map_only = map_only.resize((1180, int(map_only.height * scale)), Image.LANCZOS)
    PW = 1320
    IMG_W, IMG_H = map_only.size

    img = Image.new("RGB", ((PW + 300) * S, (IMG_H + 60) * S), "white")
    img.paste(map_only.resize((IMG_W * S, IMG_H * S), Image.LANCZOS), (0, 0))
    d = ImageDraw.Draw(img)

    # schematic locators: (x, y, kind) loosely placed on their real position on this map
    marks = [
        (250, 300, "青藏高原"),
        (560, 175, "内蒙古高原"),
        (640, 330, "黄土高原"),
        (640, 560, "云贵高原"),
        (960, 145, "东北平原"),
        (905, 300, "华北平原"),
        (950, 430, "长江中下游平原"),
    ]
    f_lbl = font(BLACK, 15)
    for x, y, name in marks:
        X, Y = x * S, y * S
        d.ellipse((X - 6 * S, Y - 6 * S, X + 6 * S, Y + 6 * S), outline="#c0392b", width=2 * S)
        w, h = text_w(d, name, f_lbl)
        d.rectangle((X + 9 * S, Y - h - 8 * S, X + 9 * S + w + 10 * S, Y + 8 * S), fill="#ffffff")
        d.rectangle((X + 9 * S, Y - h - 8 * S, X + 9 * S + w + 10 * S, Y + 8 * S), outline="#c0392b", width=S)
        d.text((X + 14 * S, Y - h - 5 * S), name, font=f_lbl, fill="#7b241c")

    # Yellow River: source on the Qinghai plateau -> "几" shaped loop in Inner Mongolia
    # -> south along the Shaanxi/Shanxi border -> east into the Bohai Sea
    yellow = [(300, 330), (400, 300), (520, 205), (620, 175), (640, 300), (620, 345), (680, 395), (760, 385)]
    d.line([(x * S, y * S) for x, y in yellow], fill="#1f6feb", width=4 * S, joint="curve")
    d.polygon([(768 * S, 381 * S), (748 * S, 372 * S), (752 * S, 392 * S)], fill="#1f6feb")
    w, _ = text_w(d, "黄河", font(BLACK, 17))
    d.rectangle((700 * S, 108 * S, 700 * S + w + 12 * S, 140 * S), fill="white")
    d.text((706 * S, 112 * S), "黄河", font=font(BLACK, 17), fill="#1f6feb")

    # Yangtze: source on the Qinghai-Tibet plateau -> Yunnan -> Sichuan basin
    # -> middle and lower reaches -> East China Sea near Shanghai
    yangtze = [(310, 370), (360, 430), (450, 480), (560, 500), (700, 510), (840, 500), (905, 485)]
    d.line([(x * S, y * S) for x, y in yangtze], fill="#0b7285", width=4 * S, joint="curve")
    d.polygon([(913 * S, 481 * S), (893 * S, 472 * S), (897 * S, 492 * S)], fill="#0b7285")
    d.rectangle((600 * S, 516 * S, 600 * S + w + 12 * S, 548 * S), fill="white")
    d.text((606 * S, 520 * S), "长江", font=font(BLACK, 17), fill="#0b7285")

    # side legend panel
    px = IMG_W * S + 20 * S
    d.text((px, 20 * S), "四大高原（红圈）", font=font(BLACK, 16), fill="#111111")
    yy = 50 * S
    for t in ["青藏高原——世界屋脊，我国最高的高原",
              "内蒙古高原——地面平坦，草原广布",
              "黄土高原——黄土深厚，水土流失明显",
              "云贵高原——地表崎岖，喀斯特地貌发育"]:
        yy = draw_multiline(d, (px, yy), t, font(REG, 14), "#333333", 270 * S) + 10 * S
    yy += 10 * S
    d.text((px, yy), "三大平原（红圈）", font=font(BLACK, 16), fill="#111111")
    yy += 30 * S
    for t in ["东北平原——我国面积最大的平原",
              "华北平原——又称黄淮海平原，地势低平",
              "长江中下游平原——河湖密布，鱼米之乡"]:
        yy = draw_multiline(d, (px, yy), t, font(REG, 14), "#333333", 270 * S) + 10 * S
    yy += 10 * S
    d.text((px, yy), "长江、黄河（蓝/青色箭头）", font=font(BLACK, 16), fill="#111111")
    yy += 30 * S
    for t in ["黄河：呈“几”字形，自西向东注入渤海",
              "长江：自西向东注入东海，我国第一长河",
              "两河均发源于青藏高原，上游落差大、水能丰富"]:
        yy = draw_multiline(d, (px, yy), t, font(REG, 14), "#333333", 270 * S) + 10 * S
    yy += 6 * S
    draw_multiline(d, (px, yy), "注：本图为示意标注，河流走向与高原、平原范围已简化，"
                                "精确界线请以教材原图和课堂讲解为准。审图号见原图 GS(2016)1609号。",
                   font(REG, 12), "#8a5a00", 270 * S)
    finish(img, "fig_map_annotated.png")


# ------------------------------------------------------- figure: rivers bar chart
def fig_rivers():
    W, H = 880, 340
    img, d = new_canvas(W, H)
    d.text((30 * S, 16 * S), "图3  长江与黄河的长度对比（公里）", font=font(BLACK, 17), fill="#111111")
    L, T = 150, 70
    BW, BH, GAP = 560, 46, 46
    data = [("长江", 6300, "#0b7285"), ("黄河", 5464, "#1f6feb")]
    mx = 7000
    for i, (name, val, color) in enumerate(data):
        y = T + i * (BH + GAP)
        d.text((30 * S, (y + 8) * S), name, font=font(BLACK, 16), fill="#111111")
        w = int(BW * val / mx)
        d.rectangle((L * S, y * S, (L + w) * S, (y + BH) * S), fill=color)
        d.text(((L + w + 10) * S, (y + 10) * S), f"{val:,}", font=font(BLACK, 15), fill="#111111")
    d.text((600 * S, 14 * S), "长度（公里）", font=font(REG, 14), fill="#333333")
    d.text((30 * S, 250 * S), "黄河的突出特点不是长度，而是含沙量：多年平均输沙量约16亿吨，"
                              "为世界之最；近几十年因黄土高原水土保持、退耕还林还草等措施，输沙量已明显减少。",
           font=font(REG, 13), fill="#444444")
    finish(img, "fig_rivers.png")


# ------------------------------------------------- figure: why muddy (黄河)
def fig_muddy():
    W, H = 1000, 470
    img, d = new_canvas(W, H)
    d.text((30 * S, 16 * S), "图4  “跳进黄河也洗不清”的成因链", font=font(BLACK, 17), fill="#111111")

    boxes = [
        (30, 90, "黄土土质疏松\n垂直节理发育"),
        (270, 90, "夏季暴雨集中\n地表冲刷强烈"),
        (510, 90, "黄土高原植被破坏\n水土流失严重"),
        (750, 90, "泥沙汇入黄河\n河水常年浑浊"),
    ]
    for x, y, t in boxes:
        d.rectangle((x * S, y * S, (x + 200) * S, (y + 110) * S), fill="#fdf6ec", outline="#c08b45", width=2 * S)
        yy = (y + 18) * S
        for ln in t.split("\n"):
            w, h = text_w(d, ln, font(BLACK, 15))
            d.text((x * S + (200 * S - w) / 2, yy), ln, font=font(BLACK, 15), fill="#7b4b12")
            yy += 30 * S
    for x in (230, 470, 710):
        d.line(((x + 4) * S, 145 * S, (x + 36) * S, 145 * S), fill="#c08b45", width=3 * S)
        d.polygon([((x + 40) * S, 145 * S), ((x + 28) * S, 139 * S), ((x + 28) * S, 151 * S)], fill="#c08b45")

    d.rectangle((30 * S, 240 * S, 950 * S, 330 * S), fill="#eaf2fb", outline="#1f6feb", width=2 * S)
    draw_multiline(d, (50 * S, 258 * S),
                   "结果：河水含沙量极高（多年平均输沙量约16亿吨），水体浑浊、颜色发黄。"
                   "“洗不清”本是一句夸张的俗语，用水的浑浊比喻事情说不明白、脱不了干系；"
                   "它同时准确反映了黄河含沙量大这一自然现象。",
                   font(REG, 14), "#123a6b", 880 * S)
    draw_multiline(d, (30 * S, 350 * S),
                   "补充：黄河下游流经华北平原，河道变宽、流速变慢，泥沙大量沉积，"
                   "河床逐年抬高，形成著名的“地上河”，这也是黄河需要持续治理的原因。",
                   font(REG, 14), "#444444", 920 * S)
    finish(img, "fig_muddy.png")


# ------------------------------------------- figure: everyday environmental acts
def fig_green_acts():
    W, H = 1000, 560
    img, d = new_canvas(W, H)
    d.text((30 * S, 16 * S), "图5  与市民生活息息相关的环保措施（举例）", font=font(BLACK, 17), fill="#111111")

    items = [
        ("垃圾分类", "46个重点城市先行先试；上海市生活垃圾管理条例自2019年7月1日起施行，"
                     "居民按可回收物、有害垃圾、湿垃圾（厨余）、干垃圾（其他）分类投放。", "#2f855a"),
        ("限塑令", "2008年6月1日起，全国范围内禁止生产、销售、使用厚度小于0.025毫米的"
                   "超薄塑料购物袋，并实行塑料购物袋有偿使用制度。", "#2b6cb0"),
        ("机动车排放标准", "全国自2023年7月1日起实施国六b排放标准，"
                           "新车污染物排放限值进一步收紧。", "#805ad5"),
        ("清洁取暖与能源替代", "北方地区推进“煤改气”“煤改电”，用天然气、电力替代散煤取暖，"
                               "减少冬季雾霾，也改善室内空气质量。", "#c05621"),
        ("河长制、湖长制", "每条河、每个湖都有明确的责任人（河长、湖长），"
                           "负责水污染防治、水环境治理和水生态修复。", "#0b7285"),
        ("新能源汽车", "购买新能源汽车免征或减免车辆购置税、可上绿色牌照、"
                       "部分城市不限行，充电桩进入居民小区和公共停车场。", "#b7791f"),
    ]
    y = 60
    for name, desc, color in items:
        d.rectangle((30 * S, y * S, (30 + 150) * S, (y + 66) * S), fill=color)
        w, h = text_w(d, name, font(BLACK, 16))
        d.text((30 * S + (150 * S - w) / 2, y * S + (66 * S - h) / 2 - 4 * S), name,
               font=font(BLACK, 16), fill="white")
        draw_multiline(d, ((30 + 165) * S, (y + 4) * S), desc, font(REG, 14), "#333333", 775 * S, spacing=1.5)
        y += 80
    finish(img, "fig_green_acts.png")


# --------------------------------------------------- figure: state organ tree
def fig_state_organs():
    W, H = 1080, 560
    img, d = new_canvas(W, H)
    d.text((30 * S, 16 * S), "图6  中国国家机构简图（宪法框架下的主要机关）", font=font(BLACK, 17), fill="#111111")

    def box(x, y, w, h, title, sub, fill, edge):
        d.rectangle((x * S, y * S, (x + w) * S, (y + h) * S), fill=fill, outline=edge, width=2 * S)
        f1 = font(BLACK, 15)
        tw, th = text_w(d, title, f1)
        d.text((x * S + (w * S - tw) / 2, (y + 12) * S), title, font=f1, fill="#111111")
        draw_multiline(d, ((x + 8) * S, (y + 40) * S), sub, font(REG, 12), "#444444", (w - 16) * S, align="center")

    box(380, 60, 320, 78, "全国人民代表大会", "最高国家权力机关；常设机关为全国人大常委会", "#e8f0fe", "#1f6feb")

    box(60, 240, 240, 96, "国家主席", "国家元首，由全国人大选举产生", "#fdf6ec", "#c08b45")
    box(340, 240, 200, 96, "国务院", "中央人民政府，最高国家行政机关", "#eaf7ee", "#2f855a")
    box(580, 240, 200, 96, "国家监察委员会", "最高监察机关", "#f4ecfb", "#805ad5")
    box(820, 240, 210, 96, "最高人民法院\n最高人民检察院", "最高审判机关／最高法律监督机关", "#fdecec", "#c0392b")

    for cx in (180, 440, 680, 925):
        d.line((540 * S, 140 * S, 540 * S, 190 * S), fill="#888888", width=2 * S)
        d.line((540 * S, 190 * S, cx * S, 190 * S), fill="#888888", width=2 * S)
        d.line((cx * S, 190 * S, cx * S, 240 * S), fill="#888888", width=2 * S)

    d.rectangle((60 * S, 400 * S, 1030 * S, 490 * S), fill="#f7f7f7", outline="#999999", width=S)
    draw_multiline(d, (80 * S, 414 * S),
                   "中国人民政治协商会议（政协）不是国家权力机关，而是中国人民爱国统一战线的组织、"
                   "中国共产党领导的多党合作和政治协商的重要机构，主要职能是政治协商、民主监督、参政议政。",
                   font(REG, 14), "#333333", 930 * S)
    draw_multiline(d, (80 * S, 508 * S),
                   "根本政治制度：人民代表大会制度。基本政治制度：中国共产党领导的多党合作和政治协商制度、"
                   "民族区域自治制度、基层群众自治制度。",
                   font(REG, 14), "#123a6b", 930 * S)
    finish(img, "fig_state_organs.png")


# ------------------------------------------------------ figure: high-speed rail
def fig_hsr():
    W, H = 900, 400
    img, d = new_canvas(W, H)
    d.text((30 * S, 16 * S), "图7  中国高铁营业里程的增长（万公里，约数）", font=font(BLACK, 17), fill="#111111")
    L, B, T = 110, 310, 80
    R = 850
    d.line((L * S, B * S, R * S, B * S), fill="#555555", width=2 * S)
    d.line((L * S, T * S, L * S, B * S), fill="#555555", width=2 * S)
    data = [("2008", 0.0), ("2012", 0.9), ("2016", 2.2), ("2020", 3.8), ("2025", 4.8)]
    mx = 5.4
    n = len(data)
    slot = (R - L) / n
    bw = slot * 0.46
    f_x = font(BLACK, 13)
    f_v = font(BLACK, 14)
    for i, (yr, v) in enumerate(data):
        x = L + slot * i + (slot - bw) / 2
        h = (v / mx) * (B - T)
        d.rectangle((x * S, (B - h) * S, (x + bw) * S, B * S), fill="#1f6feb")
        label = f"{v:g}"
        w, _ = text_w(d, label, f_v)
        d.text(((x + bw / 2) * S - w / 2, (B - h - 26) * S), label, font=f_v, fill="#111111")
        w, _ = text_w(d, yr, f_x)
        d.text(((x + bw / 2) * S - w / 2, (B + 10) * S), yr, font=f_x, fill="#333333")
    for gv in (1, 2, 3, 4, 5):
        y = B - (gv / mx) * (B - T)
        d.line((L * S, y * S, R * S, y * S), fill="#dddddd", width=S)
        d.text(((L - 34) * S, y * S - 8 * S), str(gv), font=font(REG, 12), fill="#666666")
    draw_multiline(d, (30 * S, 350 * S),
                   "数据为公开报道的约数（含高铁与部分城际铁路统计口径差异），仅用于说明“从无到有”的增长趋势。",
                   font(REG, 12), "#8a5a00", 840 * S)
    finish(img, "fig_hsr.png")


if __name__ == "__main__":
    fig_staircase()
    fig_map()
    fig_rivers()
    fig_muddy()
    fig_green_acts()
    fig_state_organs()
    fig_hsr()
