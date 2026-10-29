# -*- coding: utf-8 -*-
"""生成《复旦一日游攻略（雨天版）》docx，用于导出 PDF"""
import os
from docx import Document
from docx.shared import Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.section import WD_SECTION
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

BLUE = RGBColor(0x0B, 0x4F, 0x8C)
RED = RGBColor(0x8C, 0x1D, 0x18)
INK = RGBColor(0x1B, 0x2A, 0x41)
GREY = RGBColor(0x66, 0x66, 0x66)

CN = '微软雅黑'


def set_run(run, size=10, bold=False, color=INK, font=CN):
    run.font.size = Pt(size)
    run.font.bold = bold
    run.font.color.rgb = color
    run.font.name = font
    rpr = run._element.get_or_add_rPr()
    rfonts = rpr.find(qn('w:rFonts'))
    if rfonts is None:
        rfonts = OxmlElement('w:rFonts')
        rpr.append(rfonts)
    for attr in ('w:ascii', 'w:hAnsi', 'w:eastAsia', 'w:cs'):
        rfonts.set(qn(attr), font)


def shade(cell, hexcolor):
    tcpr = cell._tc.get_or_add_tcPr()
    shd = OxmlElement('w:shd')
    shd.set(qn('w:val'), 'clear')
    shd.set(qn('w:color'), 'auto')
    shd.set(qn('w:fill'), hexcolor)
    tcpr.append(shd)


def cell_borders(cell, color='C9D4E2', sz=4):
    tcpr = cell._tc.get_or_add_tcPr()
    borders = OxmlElement('w:tcBorders')
    for edge in ('top', 'left', 'bottom', 'right'):
        el = OxmlElement('w:' + edge)
        el.set(qn('w:val'), 'single')
        el.set(qn('w:sz'), str(sz))
        el.set(qn('w:color'), color)
        borders.append(el)
    tcpr.append(borders)


def para(cell_or_doc, text='', size=9, bold=False, color=INK, align=None,
         space_before=0, space_after=0, first=False, line=None):
    if first and hasattr(cell_or_doc, 'paragraphs') and cell_or_doc.paragraphs:
        p = cell_or_doc.paragraphs[0]
    else:
        p = cell_or_doc.add_paragraph()
    run = p.add_run(text)
    set_run(run, size=size, bold=bold, color=color)
    pf = p.paragraph_format
    pf.space_before = Pt(space_before)
    pf.space_after = Pt(space_after)
    if line:
        pf.line_spacing = line
    if align is not None:
        p.alignment = align
    return p


def rich(cell, parts, size=9, space_after=0, first=False, align=None):
    """parts: [(text, bold, color)]"""
    p = cell.paragraphs[0] if (first and cell.paragraphs) else cell.add_paragraph()
    for text, bold, color in parts:
        set_run(p.add_run(text), size=size, bold=bold, color=color or INK)
    p.paragraph_format.space_after = Pt(space_after)
    p.paragraph_format.space_before = Pt(0)
    if align is not None:
        p.alignment = align
    return p


def h1(doc, text, sub=None):
    p = doc.add_paragraph()
    set_run(p.add_run(text), size=20, bold=True, color=BLUE)
    p.paragraph_format.space_after = Pt(2)
    if sub:
        p2 = doc.add_paragraph()
        set_run(p2.add_run(sub), size=9, color=GREY)
        p2.paragraph_format.space_after = Pt(10)


def h2(doc, text):
    p = doc.add_paragraph()
    set_run(p.add_run(text), size=12.5, bold=True, color=BLUE)
    p.paragraph_format.space_before = Pt(11)
    p.paragraph_format.space_after = Pt(4)
    # bottom border for the heading
    ppr = p._element.get_or_add_pPr()
    pbdr = OxmlElement('w:pBdr')
    bottom = OxmlElement('w:bottom')
    bottom.set(qn('w:val'), 'single')
    bottom.set(qn('w:sz'), '6')
    bottom.set(qn('w:space'), '2')
    bottom.set(qn('w:color'), 'C9D4E2')
    pbdr.append(bottom)
    ppr.append(pbdr)


def body(doc, text, size=10, color=INK, space_after=2, bold=False):
    p = doc.add_paragraph()
    set_run(p.add_run(text), size=size, color=color, bold=bold)
    p.paragraph_format.space_after = Pt(space_after)
    p.paragraph_format.line_spacing = 1.25
    return p


def bullet(doc, text, size=9.5):
    p = doc.add_paragraph()
    set_run(p.add_run('•  '), size=size, color=BLUE, bold=True)
    set_run(p.add_run(text), size=size, color=INK)
    pf = p.paragraph_format
    pf.left_indent = Cm(0.5)
    pf.first_line_indent = Cm(-0.35)
    pf.space_after = Pt(2)
    pf.line_spacing = 1.2
    return p


def make_table(doc, rows, widths_cm, header=None, size=8.8, header_size=9):
    ncols = len(widths_cm)
    total = len(rows) + (1 if header else 0)
    t = doc.add_table(rows=total, cols=ncols)
    t.alignment = WD_TABLE_ALIGNMENT.LEFT
    t.autofit = False
    idx = 0
    if header:
        for j, htext in enumerate(header):
            c = t.cell(0, j)
            shade(c, '0B4F8C')
            cell_borders(c, '0B4F8C')
            para(c, htext, size=header_size, bold=True, color=RGBColor(0xFF, 0xFF, 0xFF), first=True)
        idx = 1
    for i, row in enumerate(rows):
        for j, val in enumerate(row):
            c = t.cell(i + idx, j)
            cell_borders(c)
            shade(c, 'F7F9FC' if (i % 2 == 1) else 'FFFFFF')
            if isinstance(val, list):
                for k, (text, bold, color) in enumerate(val):
                    rich(c, [(text, bold, color)], size=size, first=(k == 0))
            else:
                para(c, val, size=size, first=True)
    for row in t.rows:
        for j, cell in enumerate(row.cells):
            cell.width = Cm(widths_cm[j])
    # keep whole rows together
    for row in t.rows:
        trpr = row._tr.get_or_add_trPr()
        cant = OxmlElement('w:cantSplit')
        trpr.append(cant)
    return t


def callout(doc, text_parts, bg='FFF4E5', bar='C67C00'):
    t = doc.add_table(rows=1, cols=1)
    t.autofit = False
    c = t.cell(0, 0)
    shade(c, bg)
    tcpr = c._tc.get_or_add_tcPr()
    borders = OxmlElement('w:tcBorders')
    for edge, sz, color in (('top', 4, bg), ('bottom', 4, bg), ('right', 4, bg),
                            ('left', 24, bar)):
        el = OxmlElement('w:' + edge)
        el.set(qn('w:val'), 'single')
        el.set(qn('w:sz'), str(sz))
        el.set(qn('w:color'), color)
        borders.append(el)
    tcpr.append(borders)
    c.width = Cm(17.0)
    rich(c, text_parts, size=9, first=True)
    return t


# ---------------- build ----------------
doc = Document()
sec = doc.sections[0]
sec.page_width = Cm(21.0)
sec.page_height = Cm(29.7)
sec.left_margin = Cm(2.0)
sec.right_margin = Cm(2.0)
sec.top_margin = Cm(1.9)
sec.bottom_margin = Cm(1.7)

style = doc.styles['Normal']
style.font.name = CN
style.font.size = Pt(10)
style.element.rPr.rFonts.set(qn('w:eastAsia'), CN)

# footer
footer_p = sec.footer.paragraphs[0]
set_run(footer_p.add_run('复旦大学一日游览攻略 · 雨天版　|　建议出行日期：2026 年 11 月 1 日（周日）'),
        size=8, color=GREY)
footer_p.alignment = WD_ALIGN_PARAGRAPH.CENTER

# ---- title ----
h1(doc, '复旦大学一日游览攻略',
   '邯郸校区 + 江湾校区 · 雨天专属动线 · 午餐在邯郸 · 晚餐在大学路')

info = doc.add_table(rows=1, cols=3)
info.autofit = False
cells_info = [
    ('出行日期', '2026 年 11 月 1 日（周日）'),
    ('主干线路', '10 号线 · 18 号线 + 步行'),
    ('预算参考', '门票 0 元 · 餐饮 100–200 元'),
]
for j, (k, v) in enumerate(cells_info):
    c = info.cell(0, j)
    c.width = Cm(5.66)
    shade(c, 'F7F9FC')
    cell_borders(c, 'C9D4E2', 6)
    para(c, k, size=8.5, bold=True, color=BLUE, first=True)
    para(c, v, size=9.5)

h2(doc, '核心思路')
body(doc, '雨天把「室内馆」当主菜，把「户外地标」当点缀。邯郸校区的复旦源六馆、江湾校区的李兆基图书馆都有大量室内与连廊空间，'
          '足以撑起一整天；两个校区之间用地铁 10 号线打通，避免长距离步行与换乘淋雨。')

h2(doc, '一、出发前必做（三件事）')
make_table(doc, [
    ['① 邯郸校区进校登记', '微信关注「复旦信息办」公众号，提前 1 天在线登记并选「上午」，当天刷身份证进校'
                          '（邯郸校区本部，含北苑学生生活园区）。江湾校区等其他区域可直接刷身份证进校。', '不登记进不了本部'],
    ['② 复旦源六馆预约', '微信小程序「复旦源」，提前 7 天可约，时段为 09:00–12:00 / 12:00–14:30 / 14:30–17:00。'
                        '社会公众凭身份证预约，按预约时段核验入馆。', '名额有限，尽早约上午场'],
    ['③ 装备', '雨衣优于雨伞（风大易翻）；防滑好走的鞋（江湾草坪雨天泥泞）；手机防水袋。', '雨天校园共享单车很少'],
], widths_cm=[3.4, 9.9, 3.7], header=['事项', '怎么做', '备注'])
doc.add_paragraph().paragraph_format.space_after = Pt(2)
callout(doc, [('开放时间：', True, RED),
              ('六馆周二至周日（周一闭馆）9:00–17:00；博物馆 16:00 后、艺术馆与科技成果馆 16:30 后停止入馆。'
               '特藏档案馆无需预约，入校即可观展；校友馆仅对校友开放。', False, INK)], bg='FDEEEE', bar='8C1D18')

h2(doc, '二、全天时间轴（雨天主方案）')
make_table(doc, [
    ['08:50–09:10', '10 号线江湾体育场站 7/8 号口 → 东一门', '出站步行约 10 分钟，沿途有商铺可避雨', '低'],
    ['09:10–09:40', '光华楼（东一门内）', '复旦最具标志性的建筑；可尝试上高层观景（以现场开放为准）', '中'],
    ['09:40–10:20', '任重书院中庭 → 相辉堂前草坪', '百年礼堂与大草坪，雨中取景有倒影', '中'],
    ['10:20–12:00', '复旦源 · 一源六馆', '校史馆（2150㎡ 沉浸式）· 博物馆 · 艺术馆 · 科技成果馆 · 特藏档案馆', '低'],
    ['12:00–13:10', '南区食堂 / 南苑食堂（午餐）', '访客可微信/支付宝支付；避开 11:15–12:30 高峰，故先逛馆后吃饭', '低'],
    ['13:10–13:40', '正门（邯郸路 220 号）→ 燕园 → 中轴线', '百年奠基石、校钟、理科图书馆、文科楼', '中'],
    ['13:40–14:10', '正门 → 18 号线 复旦大学站', '沿邯郸路向东约 400 米即 2 号口', '低'],
    ['14:10–14:30', '18 号线 复旦大学 → 长江南路', '约 10 分钟，出站打车 5 分钟到江湾 6 号门', '低'],
    ['14:30–16:30', '江湾校区', '李兆基图书馆（日湖湖景自习室）· 月湖黑天鹅 · 江湾大草原 · 法学院欧式建筑群', '中'],
    ['16:30–17:00', '10 号线 新江湾城 → 江湾体育场', '3 号门步行 5 分钟到 6/7 号口，10 分钟回五角场', '低'],
    ['17:30–19:00', '大学路（晚餐）', '复旦学子的后街：咖啡馆、小酒馆、书店、异国料理，人均 60–150 元', '低'],
    ['19:00–20:00', '大学路 → 五角场', '天幕彩蛋、合生汇、万达，雨天逛商场；可顺路逛书店', '低'],
    ['20:00 后', '10 号线江湾体育场站 返程', '10 号线可达南京东路、虹桥枢纽方向', '—'],
], widths_cm=[2.6, 5.0, 8.2, 1.2], header=['时间', '地点', '内容与提示', '淋雨'], size=8.4)
para(doc, '淋雨栏表示雨天暴露程度：中 = 短时户外、需打伞；低 = 室内或有连廊。', size=8, color=GREY,
     space_before=4, space_after=2)

h2(doc, '三、两条备选线（按雨势自由切换）')
body(doc, 'A．大雨锁死版（几乎不出楼）', bold=True)
body(doc, '光华楼 → 校史馆 → 博物馆 → 艺术馆 → 科技成果馆 → 南区食堂午餐 → 18 号线 → 江湾李兆基图书馆 + 湖畔连廊 → '
          '10 号线回五角场 → 大学路 → 合生汇。砍掉：江湾大草原、燕园、正门中轴线。')
body(doc, 'B．雨小转晴版（加户外）', bold=True)
body(doc, '在 A 的基础上：正门留 20 分钟拍照 → 江湾大草原走一圈（走木栈道，避开积水）→ 大学路咖啡馆等雨停。')
callout(doc, [('调整原则：', True, RGBColor(0xC6, 0x7C, 0x00)),
              ('中午 11:15–12:30 食堂只对校内师生开放，务必错峰；博物馆 16:00、艺术馆与科技成果馆 16:30 停止入馆，别拖到下午再去。',
               False, INK)])

h2(doc, '四、交通一览')
body(doc, '4.1　校门与地铁对应', bold=True, color=BLUE)
make_table(doc, [
    ['正门（邯郸路 220 号）', '18 号线 复旦大学站 2 号口', '出站左转向东约 400 米（正门是路上第二个门）',
     '中轴线：理科图书馆、二/三教、化学楼、物理楼、立人生物楼'],
    ['东南三门（国权路门）', '18 号线 复旦大学站 2 号口', '步行约 3 分钟', '燕园、吕志和楼、相辉堂、复旦源六馆'],
    ['东一门（国定路门）', '10 号线 江湾体育场站 7/8 号口', '步行约 10 分钟', '光华楼、旦苑餐厅、大学路、五角场'],
    ['江湾 2 号门', '10 号线 国帆路站 3 号口', '出站即到', '江湾校区主入口'],
    ['江湾 3 号门', '10 号线 新江湾城站 6/7 号口', '步行约 5 分钟', '江湾校区东侧'],
    ['江湾 6 号门', '3 / 18 号线 长江南路站', '骑行 5–10 分钟（雨天打车）', '江湾校区西侧'],
], widths_cm=[3.6, 4.0, 4.0, 5.4], header=['校门', '最近地铁', '出站到门', '门内通向'], size=8.4)

body(doc, '')
body(doc, '4.2　邯郸 ⇄ 江湾 三种走法', bold=True, color=BLUE)
make_table(doc, [
    ['① 地铁 10 号线（推荐）', '江湾体育场站 ⇄ 新江湾城站，约 10 分钟一站，出站步行 5–10 分钟。全程地下，雨天最稳。'],
    ['② 地铁 18 号线 + 3 号线', '复旦大学站 → 长江南路站（约 10 分钟，同站换乘 3 号线）→ 江湾 6 号门打车 5 分钟。适合从正门、东南三门出发。'],
    ['③ 校车（访客基本坐不了）', '有邯郸—江湾线，但乘车必须凭校园一卡通等有效证件；邯郸上车点在日月西路近理科图书馆。'],
], widths_cm=[4.6, 12.4], header=['方式', '说明'], size=8.6)

body(doc, '')
body(doc, '4.3　城市交通', bold=True, color=BLUE)
bullet(doc, '火车站：上海站 / 虹桥站均可经 10 号线（虹桥 → 10 号线直达江湾体育场站）；打车约 30–50 分钟。')
bullet(doc, '机场：浦东机场换乘 1 次可抵 18 号线复旦大学站；虹桥机场 10 号线直达江湾体育场站。')
bullet(doc, '公交：复旦正门「复旦大学站」有 10 余条线路，942 路直达上海站，夜间有 329 路。')

h2(doc, '五、吃饭细节')
make_table(doc, [
    ['午餐（邯郸）', '首选南区食堂 / 南苑食堂——这是校外访客可用的两个食堂（网上常说的旦苑餐厅并不对访客开放）。'
                    '微信/支付宝扫码，按规定收取搭伙费，谢绝向师生借卡。午餐 10:30–13:30 供餐，但 11:15–12:30 只对师生开放，'
                    '建议 12:00 后进食堂。'],
    ['晚餐（大学路）', '咖啡馆、日料、韩式烤肉、新疆菜、意大利菜、小酒馆一条街，普遍人均 60–150 元。'
                      '周日 18:00–19:00 是高峰，17:30 前到店最稳；街区多为外摆位，雨天坐室内。'],
], widths_cm=[3.4, 13.6], size=8.8)

h2(doc, '六、地标打卡清单')
marks = [
    '光华楼（东一门内，复旦名片）', '相辉堂 + 相辉堂前大草坪', '老校门（复旦源区域，1920 年代校门）',
    '校史馆（百廿复旦，沉浸式数字展）', '博物馆 / 艺术馆 / 科技成果馆 / 特藏档案馆', '燕园（百年奠基石、校钟）',
    '正门（邯郸路 220 号）', '理科图书馆 + 中轴线', '旦苑餐厅（仅路过打卡）',
    '江湾李兆基图书馆（日湖湖景自习室）', '江湾大草原 + 月湖黑天鹅', '江湾法学院等欧式建筑群',
    '大学路 + 五角场天幕',
]
rows_marks = []
for i in range(0, len(marks), 2):
    a = marks[i]
    b = marks[i + 1] if i + 1 < len(marks) else ''
    rows_marks.append(['□  ' + a, ('□  ' + b) if b else ''])
mt = make_table(doc, rows_marks, widths_cm=[8.5, 8.5], size=9)
for row in mt.rows:
    for cell in row.cells:
        shade(cell, 'F7F9FC')

h2(doc, '七、雨天应急与文明参观')
bullet(doc, '校园内不进入教学、科研、办公区与学生宿舍，不长时间占用座位，未经批准不在校内直播拍摄。')
bullet(doc, '雨大时不要在光华楼高层平台久留，注意湿滑；江湾大草坪有积水，走木栈道。')
bullet(doc, '随身查看「复旦源」小程序，确认场馆余票与临时闭馆通知。')
bullet(doc, '若进校登记名额紧张，可从南三门 / 老校门入校参观复旦源（凭预约 + 身份证）。')
bullet(doc, '校园服务热线 021-65640000（交通、食堂、失物招领均可咨询）；校园地图 map.fudan.edu.cn。')

h2(doc, '八、一页速查')
quick = ('10 号线 江湾体育场站(7/8 口) → 东一门 → 光华楼 → 相辉堂 → 复旦源六馆（室内为主，9:00–12:00 时段）'
         ' → 12:00 后 南区 / 南苑食堂午餐 → 正门 + 燕园 + 中轴线 → 18 号线 复旦大学站 → 长江南路 → 江湾 6 号门'
         ' → 李兆基图书馆 + 月湖 + 大草原 → 10 号线 新江湾城 → 江湾体育场 → 大学路晚餐 → 五角场 → 返程')
qt = doc.add_table(rows=1, cols=1)
qt.autofit = False
qc = qt.cell(0, 0)
qc.width = Cm(17.0)
shade(qc, 'EAF1F8')
cell_borders(qc, '0B4F8C', 12)
rich(qc, [(quick, True, RGBColor(0x12, 0x37, 0x5C))], size=9.5, first=True)

h2(doc, '信息来源（复旦大学官方渠道）')
srcs = [
    '复旦大学官网《打卡复旦四大校区，你一定需要这份交通指南》 fudan.edu.cn/2025/0630/c24a146130/page.htm',
    '复旦大学官网《建成「一源六馆」新格局，「复旦源」文化育人功能区启幕》 fudan.edu.cn/2025/0519/c24a145424/page.htm',
    '复旦大学《关于新学期优化校园开放措施的通告》 news.fudan.edu.cn/2024/0831/c45a142031/page.htm',
    '总务处《关于食堂餐饮》常见问答 xyfw.fudan.edu.cn/39407/list.htm',
    '总务处《关于通讯交通》常见问答（校车） xyfw.fudan.edu.cn/39409/list.htm',
    '校友服务平台《复旦校友 / 社会访客进校申请及停车指南》 alu.fudan.edu.cn/alumniService/',
    '说明：以上为编辑整理，预约规则、食堂开放窗口、校车时刻均可能临时调整，请以出行前官方最新通知为准。',
]
for s in srcs:
    para(doc, '· ' + s, size=8, color=GREY, space_after=1)

out = os.path.join(os.path.dirname(os.path.abspath(__file__)), '复旦一日游攻略_雨天版.docx')
doc.save(out)
print('OK', out, os.path.getsize(out))
