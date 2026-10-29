# -*- coding: utf-8 -*-
"""复旦一日游攻略 PDF 生成脚本"""
import os
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (BaseDocTemplate, Frame, PageTemplate, Paragraph,
                                Spacer, Table, TableStyle, PageBreak)

W, H = A4
MX = 16 * mm
TOP = 18 * mm
BOT = 16 * mm
CW = W - 2 * MX

pdfmetrics.registerFont(TTFont('YH', r'C:\Windows\Fonts\msyh.ttc', subfontIndex=0))
pdfmetrics.registerFont(TTFont('YHB', r'C:\Windows\Fonts\msyhbd.ttc', subfontIndex=0))
pdfmetrics.registerFont(TTFont('Hei', r'C:\Windows\Fonts\simhei.ttf'))

INK = colors.HexColor('#1b2a41')
BLUE = colors.HexColor('#0b4f8c')
RED = colors.HexColor('#8c1d18')
GREY = colors.HexColor('#666666')
LIGHT = colors.HexColor('#eef2f7')
LINE = colors.HexColor('#c9d4e2')

LQ = '「'
RQ = '」'


def S(name, **kw):
    base = dict(fontName='YH', fontSize=9.3, leading=14.2, textColor=INK,
                wordWrap='CJK', spaceAfter=2)
    base.update(kw)
    return ParagraphStyle(name, **base)


st_h1 = S('h1', fontName='YHB', fontSize=20, leading=26, textColor=BLUE, spaceAfter=2)
st_sub = S('sub', fontSize=9, leading=13, textColor=GREY, spaceAfter=8)
st_h2 = S('h2', fontName='YHB', fontSize=12.5, leading=17, textColor=BLUE,
          spaceBefore=9, spaceAfter=5)
st_body = S('body')
st_small = S('small', fontSize=8.2, leading=11.6, textColor=GREY, spaceAfter=1.5)
st_note = S('note', fontSize=8.7, leading=12.8, textColor=colors.HexColor('#444444'),
            leftIndent=3, rightIndent=3)
st_cell = S('cell', fontSize=8.6, leading=12)
st_th = S('th', fontName='YHB', fontSize=8.8, leading=12, textColor=colors.white)
st_code = S('code', fontName='Hei', fontSize=8.4, leading=14, textColor=colors.HexColor('#12375c'))
st_tick = S('tick', fontSize=9, leading=13.8)


def P(t, s=st_body):
    return Paragraph(t, s)


def bullets(items):
    return [Paragraph('<font color="#0b4f8c">•</font> ' + t, st_body) for t in items]


def table(rows, widths, header=None, fs=8.6):
    data = []
    if header:
        data.append([Paragraph(h, st_th) for h in header])
    for r in rows:
        data.append([c if not isinstance(c, str) else Paragraph(c, st_cell) for c in r])
    t = Table(data, colWidths=widths, repeatRows=1 if header else 0, hAlign='LEFT')
    cmds = [
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('GRID', (0, 0), (-1, -1), 0.4, LINE),
        ('LEFTPADDING', (0, 0), (-1, -1), 5),
        ('RIGHTPADDING', (0, 0), (-1, -1), 5),
        ('TOPPADDING', (0, 0), (-1, -1), 3.2),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3.2),
    ]
    if header:
        cmds.append(('BACKGROUND', (0, 0), (-1, 0), BLUE))
        cmds.append(('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, LIGHT]))
    else:
        cmds.append(('ROWBACKGROUNDS', (0, 0), (-1, -1), [colors.white, LIGHT]))
    t.setStyle(TableStyle(cmds))
    return t


def callout(lines, bg='#fff4e5', bar='#c67c00'):
    body = [Paragraph('<font color="%s"><b>%s</b></font>%s' % (bar, a, b), st_note)
            for a, b in lines]
    t = Table([[Paragraph('<br/>'.join([]) or '', st_note)] if False else [body]],
              colWidths=[CW], hAlign='LEFT')
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor(bg)),
        ('LINEBEFORE', (0, 0), (0, -1), 3.2, colors.HexColor(bar)),
        ('LEFTPADDING', (0, 0), (-1, -1), 8),
        ('RIGHTPADDING', (0, 0), (-1, -1), 8),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
    ]))
    return t


class Doc(BaseDocTemplate):
    def __init__(self, path):
        super().__init__(path, pagesize=A4,
                         leftMargin=MX, rightMargin=MX, topMargin=TOP, bottomMargin=BOT,
                         title='复旦大学一日游览攻略（雨天版）',
                         author='DeepSeek Harness', subject='Fudan one-day itinerary')
        frame = Frame(MX, BOT, CW, H - TOP - BOT, id='f',
                      leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
        self.addPageTemplates([PageTemplate(id='main', frames=[frame], onPage=self.deco)])

    def deco(self, canv, doc):
        canv.saveState()
        canv.setStrokeColor(BLUE)
        canv.setLineWidth(2)
        canv.line(MX, H - TOP + 7 * mm, W - MX, H - TOP + 7 * mm)
        canv.setFont('YH', 7.6)
        canv.setFillColor(GREY)
        canv.drawString(MX, H - TOP + 9.2 * mm, '复旦大学一日游览攻略 · 雨天版')
        canv.drawRightString(W - MX, H - TOP + 9.2 * mm, '邯郸校区 → 江湾校区 → 大学路')
        canv.setStrokeColor(LINE)
        canv.setLineWidth(0.6)
        canv.line(MX, BOT - 6 * mm, W - MX, BOT - 6 * mm)
        canv.setFont('YH', 7.6)
        canv.drawString(MX, BOT - 10.5 * mm, '建议出行日期：2026 年 11 月 1 日（周日）')
        canv.drawRightString(W - MX, BOT - 10.5 * mm, '第 %d 页' % doc.page)
        canv.restoreState()


story = []

story.append(P('复旦大学一日游览攻略', st_h1))
story.append(P('邯郸校区 + 江湾校区 · 雨天专属动线 · 午餐在邯郸 · 晚餐在大学路', st_sub))

info = Table([[
    Paragraph('<b>出行日期</b><br/>2026 年 11 月 1 日（周日）', st_cell),
    Paragraph('<b>主干线路</b><br/>10 号线 · 18 号线 + 步行', st_cell),
    Paragraph('<b>预算参考</b><br/>门票 0 元 · 餐饮 100–200 元', st_cell),
]], colWidths=[CW / 3.0] * 3, hAlign='LEFT')
info.setStyle(TableStyle([
    ('BOX', (0, 0), (-1, -1), 0.8, LINE),
    ('INNERGRID', (0, 0), (-1, -1), 0.5, LINE),
    ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor('#f7f9fc')),
    ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ('TOPPADDING', (0, 0), (-1, -1), 7),
    ('BOTTOMPADDING', (0, 0), (-1, -1), 7),
    ('LEFTPADDING', (0, 0), (-1, -1), 8),
]))
story.append(info)
story.append(Spacer(1, 6))

story.append(P('核心思路', st_h2))
story.append(P('雨天把' + LQ + '室内馆' + RQ + '当主菜，把' + LQ + '户外地标' + RQ
               + '当点缀。邯郸校区的' + LQ + '复旦源' + RQ
               + '六馆、江湾校区的李兆基图书馆都有大量室内与连廊空间，足以撑起一整天；'
               '两个校区之间用地铁 10 号线打通，避免长距离步行与换乘淋雨。'))

story.append(P('一、出发前必做（三件事）', st_h2))
story.append(table([
    ['<b>① 邯郸校区进校登记</b>',
     '微信关注<b>复旦信息办</b>公众号，<b>提前 1 天</b>在线登记并选' + LQ + '上午' + RQ
     + '，当天刷身份证进校（邯郸校区本部，含北苑学生生活园区）。江湾校区等其他区域可直接刷身份证进校。',
     '不登记进不了本部'],
    ['<b>② 复旦源六馆预约</b>',
     '微信小程序<b>复旦源</b>，<b>提前 7 天</b>可约，时段为 09:00–12:00 / 12:00–14:30 / 14:30–17:00。'
     '社会公众凭身份证预约，按预约时段核验入馆。',
     '名额有限，尽早约上午场'],
    ['<b>③ 装备</b>',
     '雨衣优于雨伞（风大易翻）；防滑好走的鞋（江湾草坪雨天泥泞）；手机防水袋。',
     '雨天校园共享单车很少'],
], widths=[CW * 0.20, CW * 0.58, CW * 0.22], header=['事项', '怎么做', '备注'], fs=8.4))
story.append(Spacer(1, 6))
story.append(callout([
    ('', '六馆开放：周二至周日（<b>周一闭馆</b>），9:00–17:00；博物馆 16:00 后、艺术馆与科技成果馆 16:30 后停止入馆。'
          '特藏档案馆无需预约，入校即可观展；校友馆仅对校友开放。')
], bg='#fdeeee', bar='#8c1d18'))

story.append(P('二、全天时间轴（雨天主方案）', st_h2))
rows = [
    ['08:50–09:10', '10 号线<b>江湾体育场站</b>7/8 号口 → 东一门', '出站步行约 10 分钟，沿途有商铺可避雨', '低'],
    ['09:10–09:40', '<b>光华楼</b>（东一门内）', '复旦最具标志性的建筑；可尝试上高层观景（以现场开放为准）', '中'],
    ['09:40–10:20', '任重书院中庭 → <b>相辉堂</b>前草坪', '百年礼堂与大草坪，雨中有倒影', '中'],
    ['10:20–12:00', '<b>复旦源 · 一源六馆</b>', '校史馆（2150㎡ 沉浸式）· 博物馆 · 艺术馆 · 科技成果馆 · 特藏档案馆', '低'],
    ['12:00–13:10', '<b>南区食堂 / 南苑食堂</b>（午餐）', '访客可微信/支付宝支付；避开 11:15–12:30 高峰，故先逛馆后吃饭', '低'],
    ['13:10–13:40', '<b>正门</b>（邯郸路 220 号）→ <b>燕园</b> → 中轴线', '百年奠基石、校钟、理科图书馆、文科楼', '中'],
    ['13:40–14:10', '正门 → <b>18 号线 复旦大学站</b>', '沿邯郸路向东约 400 米即 2 号口', '低'],
    ['14:10–14:30', '18 号线 复旦大学 → <b>长江南路</b>', '约 10 分钟，出站打车 5 分钟到江湾 <b>6 号门</b>', '低'],
    ['14:30–16:30', '<b>江湾校区</b>', '<b>李兆基图书馆</b>（日湖湖景自习室）· <b>月湖</b>黑天鹅 · 江湾大草原 · 法学院欧式建筑群', '中'],
    ['16:30–17:00', '10 号线 新江湾城 → 江湾体育场', '3 号门步行 5 分钟到新江湾城站 6/7 号口，10 分钟回五角场', '低'],
    ['17:30–19:00', '<b>大学路</b>（晚餐）', '复旦学子的后街：咖啡馆、小酒馆、书店、异国料理，人均 60–150 元', '低'],
    ['19:00–20:00', '大学路 → <b>五角场</b>', '天幕彩蛋、合生汇、万达，雨天逛商场；可顺路逛书店', '低'],
    ['20:00 后', '10 号线<b>江湾体育场站</b> 返程', '10 号线可达南京东路、虹桥枢纽方向', '—'],
]
story.append(table(rows, widths=[CW * 0.155, CW * 0.295, CW * 0.475, CW * 0.075],
                   header=['时间', '地点', '内容与提示', '淋雨'], fs=8.3))
story.append(Spacer(1, 5))
story.append(P('淋雨栏表示雨天暴露程度：中 = 短时户外、需打伞；低 = 室内或有连廊。', st_small))

story.append(PageBreak())

story.append(P('三、两条备选线（按雨势自由切换）', st_h2))
story.append(P('<b>A．大雨锁死版（几乎不出楼）</b>'))
story.append(P('光华楼 → 校史馆 → 博物馆 → 艺术馆 → 科技成果馆 → 南区食堂午餐 → 18 号线 → '
               '江湾李兆基图书馆 + 湖畔连廊 → 10 号线回五角场 → 大学路 → 合生汇。<br/>'
               '砍掉：江湾大草原、燕园、正门中轴线。'))
story.append(Spacer(1, 3))
story.append(P('<b>B．雨小转晴版（加户外）</b>'))
story.append(P('在 A 的基础上：正门留 20 分钟拍照 → 江湾大草原走一圈（走木栈道，避开积水）→ 大学路咖啡馆等雨停。'))
story.append(Spacer(1, 4))
story.append(callout([
    ('调整原则：', '中午 11:15–12:30 食堂只对校内师生开放，务必错峰；博物馆 16:00、'
                   '艺术馆与科技成果馆 16:30 停止入馆，别拖到下午再去。'),
]))

story.append(P('四、交通一览', st_h2))
story.append(P('<b>4.1　校门与地铁对应</b>'))
story.append(table([
    ['正门（邯郸路 220 号）', '18 号线 复旦大学站 2 号口', '出站左转向东约 400 米（正门是路上第二个门）',
     '中轴线：理科图书馆、二/三教、化学楼、物理楼、立人生物楼'],
    ['东南三门（国权路门）', '18 号线 复旦大学站 2 号口', '步行约 3 分钟', '燕园、吕志和楼、相辉堂、复旦源六馆'],
    ['东一门（国定路门）', '10 号线 江湾体育场站 7/8 号口', '步行约 10 分钟', '光华楼、旦苑餐厅、大学路、五角场'],
    ['江湾 2 号门', '10 号线 国帆路站 3 号口', '出站即到', '江湾校区主入口'],
    ['江湾 3 号门', '10 号线 新江湾城站 6/7 号口', '步行约 5 分钟', '江湾校区东侧'],
    ['江湾 6 号门', '3 / 18 号线 长江南路站', '骑行 5–10 分钟（雨天打车）', '江湾校区西侧'],
], widths=[CW * 0.21, CW * 0.235, CW * 0.235, CW * 0.32],
   header=['校门', '最近地铁', '出站到门', '门内通向'], fs=8.2))
story.append(Spacer(1, 6))

story.append(P('<b>4.2　邯郸 ⇄ 江湾 三种走法</b>'))
tm = Table([
    [Paragraph('<b>① 地铁 10 号线（推荐）</b><br/>江湾体育场站 ⇄ 新江湾城站，约 10 分钟一站，'
               '出站步行 5–10 分钟。全程地下，雨天最稳。', st_cell)],
    [Paragraph('<b>② 地铁 18 号线 + 3 号线</b><br/>复旦大学站 → 长江南路站（约 10 分钟，同站换乘 3 号线）'
               '→ 江湾 6 号门打车 5 分钟。适合从正门、东南三门出发。', st_cell)],
    [Paragraph('<b>③ 校车（访客基本坐不了）</b><br/>有邯郸—江湾线，但乘车<b>必须凭校园一卡通等有效证件</b>；'
               '邯郸上车点在日月西路近理科图书馆。', st_cell)],
], colWidths=[CW], hAlign='LEFT')
tm.setStyle(TableStyle([
    ('GRID', (0, 0), (-1, -1), 0.4, LINE),
    ('ROWBACKGROUNDS', (0, 0), (-1, -1), [colors.white, LIGHT]),
    ('LEFTPADDING', (0, 0), (-1, -1), 7),
    ('TOPPADDING', (0, 0), (-1, -1), 5),
    ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
]))
story.append(tm)
story.append(Spacer(1, 6))

story.append(P('<b>4.3　城市交通</b>'))
story.extend(bullets([
    '<b>火车站</b>：上海站 / 虹桥站均可经 10 号线（虹桥 → 10 号线直达江湾体育场站）；打车约 30–50 分钟。',
    '<b>机场</b>：浦东机场换乘 1 次可抵 18 号线复旦大学站；虹桥机场 10 号线直达江湾体育场站。',
    '<b>公交</b>：复旦正门复旦大学站有 10 余条线路，942 路直达上海站，夜间有 329 路。',
]))

story.append(P('五、吃饭细节', st_h2))
story.append(table([
    ['<b>午餐</b><br/>邯郸校区',
     '首选<b>南区食堂 / 南苑食堂</b>——这是校外访客可用的两个食堂（网上常说的旦苑餐厅并不对访客开放）。'
     '微信/支付宝扫码，按规定收取搭伙费，<b>谢绝向师生借卡</b>。午餐 10:30–13:30 供餐，'
     '但 11:15–12:30 只对师生开放，建议 12:00 后进食堂。'],
    ['<b>晚餐</b><br/>大学路',
     '咖啡馆、日料、韩式烤肉、新疆菜、意大利菜、小酒馆一条街，普遍人均 60–150 元。'
     '周日 18:00–19:00 是高峰，<b>17:30 前到店</b>最稳；街区多为外摆位，雨天坐室内。'],
], widths=[CW * 0.18, CW * 0.82], fs=8.5))

story.append(P('六、地标打卡清单', st_h2))
marks = [
    '光华楼（东一门内，复旦名片）', '相辉堂 + 相辉堂前大草坪', '老校门（复旦源区域，1920 年代校门）',
    '校史馆（百廿复旦，沉浸式数字展）', '博物馆 / 艺术馆 / 科技成果馆 / 特藏档案馆', '燕园（百年奠基石、校钟）',
    '正门（邯郸路 220 号）', '理科图书馆 + 中轴线（物理楼、化学楼、文科楼）', '旦苑餐厅（仅路过打卡）',
    '江湾李兆基图书馆（日湖湖景自习室）', '江湾大草原 + 月湖黑天鹅', '江湾法学院等欧式建筑群',
    '大学路 + 五角场天幕',
]
half = (len(marks) + 1) // 2
colA = [Paragraph('□　' + x, st_tick) for x in marks[:half]]
colB = [Paragraph('□　' + x, st_tick) for x in marks[half:]]
if len(colB) < len(colA):
    colB.append(Paragraph('', st_tick))
lt = Table([[colA, colB]], colWidths=[CW / 2.0, CW / 2.0], hAlign='LEFT')
lt.setStyle(TableStyle([
    ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ('BOX', (0, 0), (-1, -1), 0.6, LINE),
    ('INNERGRID', (0, 0), (-1, -1), 0.4, LINE),
    ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor('#f7f9fc')),
    ('LEFTPADDING', (0, 0), (-1, -1), 8),
    ('TOPPADDING', (0, 0), (-1, -1), 6),
    ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
]))
story.append(lt)

story.append(P('七、雨天应急与文明参观', st_h2))
story.extend(bullets([
    '校园内<b>不进入教学、科研、办公区与学生宿舍</b>，不长时间占用座位，未经批准不在校内直播拍摄。',
    '雨大时不要在光华楼高层平台久留，注意湿滑；江湾大草坪有积水，走木栈道。',
    '随身查看复旦源小程序，确认场馆<b>余票与临时闭馆</b>通知。',
    '若进校登记名额紧张，可从<b>南三门 / 老校门</b>入校参观复旦源（凭预约 + 身份证）。',
    '校园服务热线 <b>021-65640000</b>（交通、食堂、失物招领均可咨询）；校园地图 map.fudan.edu.cn。',
]))

story.append(P('八、一页速查', st_h2))
code = Table([[P('10 号线 江湾体育场站(7/8 口) → 东一门 → 光华楼 → 相辉堂<br/>'
                 '→ 复旦源六馆（室内为主，9:00–12:00 时段）<br/>'
                 '→ 12:00 后 南区 / 南苑食堂午餐<br/>'
                 '→ 正门 + 燕园 + 中轴线 → 18 号线 复旦大学站<br/>'
                 '→ 长江南路 → 江湾 6 号门 → 李兆基图书馆 + 月湖 + 大草原<br/>'
                 '→ 10 号线 新江湾城 → 江湾体育场 → 大学路晚餐 → 五角场 → 返程', st_code)]],
             colWidths=[CW], hAlign='LEFT')
code.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor('#eaf1f8')),
    ('BOX', (0, 0), (-1, -1), 1.0, BLUE),
    ('LEFTPADDING', (0, 0), (-1, -1), 10),
    ('RIGHTPADDING', (0, 0), (-1, -1), 10),
    ('TOPPADDING', (0, 0), (-1, -1), 8),
    ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
]))
story.append(code)
story.append(Spacer(1, 8))

story.append(P('信息来源（复旦大学官方渠道）', st_small))
srcs = [
    '复旦大学官网《打卡复旦四大校区，你一定需要这份交通指南》 fudan.edu.cn/2025/0630/c24a146130/page.htm',
    '复旦大学官网《建成一源六馆新格局，复旦源文化育人功能区启幕》 fudan.edu.cn/2025/0519/c24a145424/page.htm',
    '复旦大学《关于新学期优化校园开放措施的通告》 news.fudan.edu.cn/2024/0831/c45a142031/page.htm',
    '总务处《关于食堂餐饮》常见问答 xyfw.fudan.edu.cn/39407/list.htm',
    '总务处《关于通讯交通》常见问答（校车） xyfw.fudan.edu.cn/39409/list.htm',
    '校友服务平台《复旦校友 / 社会访客进校申请及停车指南》 alu.fudan.edu.cn/alumniService/',
    '说明：以上为编辑整理，预约规则、食堂开放窗口、校车时刻均可能临时调整，请以出行前官方最新通知为准。',
]
for s in srcs:
    story.append(P('· ' + s, st_small))

out = os.path.join(os.path.dirname(os.path.abspath(__file__)), '复旦一日游攻略_雨天版.pdf')
Doc(out).build(story)
print('OK', out, os.path.getsize(out))
