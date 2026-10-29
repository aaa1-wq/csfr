# -*- coding: utf-8 -*-
"""修正版：修掉上标字形缺失（eˣ 的 ˣ 在 SimSun/SimHei 里没有）、标签压线、图6 刻度重复。"""
import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from PIL import Image, ImageDraw, ImageFont  # noqa: E402
from textdraw import TextDraw  # noqa: E402

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "out")
os.makedirs(OUT, exist_ok=True)

W, H = 1500, 950
SS = 2

ACC = (27, 79, 138)
ACC2 = (150, 80, 24)
RED = (190, 52, 40)
GREEN = (32, 118, 68)
PURPLE = (112, 72, 152)
GREY = (95, 100, 108)
LGREY = (198, 204, 212)
GRID = (232, 236, 242)
INK = (25, 25, 25)

FONT_DIR = os.path.join(os.environ.get("WINDIR", r"C:\Windows"), "Fonts")


def F(face, size):
    cands = {"hei": ["simhei.ttf"], "song": ["simsun.ttc"], "serif": ["times.ttf", "georgia.ttf"]}[face]
    for fn in cands:
        p = os.path.join(FONT_DIR, fn)
        if os.path.exists(p):
            try:
                return ImageFont.truetype(p, int(size * SS))
            except Exception:
                continue
    return ImageFont.load_default()


class Canvas:
    def __init__(self, xmin, xmax, ymin, ymax, pad=(135, 150, 75, 95)):
        self.img = Image.new("RGB", (W * SS, H * SS), "white")
        self.d = TextDraw(ImageDraw.Draw(self.img))
        self.xmin, self.xmax, self.ymin, self.ymax = xmin, xmax, ymin, ymax
        pl, pt, pr, pb = [v * SS for v in pad]
        self.pl, self.pt = pl, pt
        self.sx = (W * SS - pl - pr) / (xmax - xmin)
        self.sy = (H * SS - pt - pb) / (ymax - ymin)
        self.ax = pl + (xmax - xmin) * self.sx
        self.ay = pt + (ymax - ymin) * self.sy

    def P(self, x, y):
        return (self.pl + (x - self.xmin) * self.sx, self.pt + (self.ymax - y) * self.sy)

    def axes(self, xlabel="x", ylabel="y", xzero_label=True):
        for gx in range(int(math.floor(self.xmin)), int(math.ceil(self.xmax)) + 1):
            X, _ = self.P(gx, 0)
            if self.pl <= X <= self.ax:
                self.d.d.line([(X, self.pt), (X, self.ay)], fill=GRID, width=2 * SS)
        for gy in range(int(math.floor(self.ymin)), int(math.ceil(self.ymax)) + 1):
            _, Y = self.P(0, gy)
            if self.pt <= Y <= self.ay:
                self.d.d.line([(self.pl, Y), (self.ax, Y)], fill=GRID, width=2 * SS)
        x0, y0 = self.P(0, 0)
        self.d.d.line([(self.pl, y0), (self.ax, y0)], fill=(55, 55, 55), width=3 * SS)
        self.d.d.line([(x0, self.ay), (x0, self.pt)], fill=(55, 55, 55), width=3 * SS)
        self.d.d.polygon([(self.ax, y0), (self.ax - 16 * SS, y0 - 7 * SS),
                          (self.ax - 16 * SS, y0 + 7 * SS)], fill=(55, 55, 55))
        f = F("serif", 26)
        self.label_px(self.ax + 6 * SS, y0, "x", f, INK, "lm")
        self.label_px(x0 + 10 * SS, self.pt, "y", f, INK, "lm")
        for gx in range(int(math.floor(self.xmin)) + 1, int(math.ceil(self.xmax))):
            if gx == 0:
                continue
            X, _ = self.P(gx, 0)
            if self.pl + 25 * SS < X < self.ax - 25 * SS:
                self.label_px(X, y0 + 6 * SS, str(gx), F("serif", 20), GREY, "mt")

    def label_px(self, X, Y, s, f, color, anchor="lm"):
        bbox = self.d.d.textbbox((0, 0), s, font=f)
        w, h = bbox[2] - bbox[0], bbox[3] - bbox[1]
        ax, ay = anchor[0], anchor[1]
        x = X if ax == "l" else (X - w / 2 if ax == "c" else X - w)
        if ay == "m":
            y = Y - h / 2 - bbox[1]
        elif ay == "t":
            y = Y - bbox[1]
        else:
            y = Y - bbox[3]
        self.d.text((x, y), s, font=f, fill=color)
        return w, h

    def curve(self, fn, a, b, color=ACC, width=4, n=1000):
        pts = []
        for i in range(n + 1):
            x = a + (b - a) * i / n
            try:
                y = fn(x)
            except Exception:
                continue
            if not math.isfinite(y):
                continue
            pts.append(self.P(x, y))
        self.d.d.line(pts, fill=color, width=int(width * SS), joint="curve")

    def dot(self, x, y, color=RED, r=8):
        X, Y = self.P(x, y)
        self.d.d.ellipse([X - r * SS - 3, Y - r * SS - 3, X + r * SS + 3, Y + r * SS + 3], fill="white")
        self.d.d.ellipse([X - r * SS, Y - r * SS, X + r * SS, Y + r * SS], fill=color)

    def seg(self, p1, p2, color, width=3, dash=None):
        A, B = self.P(*p1), self.P(*p2)
        if dash is None:
            self.d.d.line([A, B], fill=color, width=int(width * SS))
            return
        (x1, y1), (x2, y2) = A, B
        L = math.hypot(x2 - x1, y2 - y1)
        if L == 0:
            return
        dx, dy = (x2 - x1) / L, (y2 - y1) / L
        t, on = 0.0, True
        while t < L:
            step = (dash[0] if on else dash[1]) * SS
            t2 = min(t + step, L)
            if on:
                self.d.d.line([(x1 + dx * t, y1 + dy * t), (x1 + dx * t2, y1 + dy * t2)],
                              fill=color, width=int(width * SS))
            t = t2
            on = not on

    def tag(self, x, y, s, color, size=22, face="song", anchor="lt"):
        self.label_px(*self.P(x, y), s, F(face, size), color, anchor)

    def save(self, name):
        self.img.resize((W, H), Image.LANCZOS).save(os.path.join(OUT, name), "PNG")
        print("saved", name)


def header(c, title, sub):
    c.label_px(W * SS / 2, 34 * SS, title, F("hei", 32), INK, "cm")
    c.label_px(W * SS / 2, 92 * SS, sub, F("song", 21), GREY, "cm")


# ============================ 图1
c = Canvas(-2.6, 3.1, -1.5, 8.8)
header(c, "图 1  下凸的定义：弦在曲线上方",
       "f(x) = x²；取 x1 = -2、x2 = 2.4、t = 0.35，则 tx1+(1-t)x2 = 0.86")
c.axes()
c.curve(lambda x: x * x, -2.6, 3.1, ACC, 4.2)
x1, x2, t = -2.0, 2.4, 0.35
xt = t * x1 + (1 - t) * x2
yc, yh = xt * xt, t * x1 * x1 + (1 - t) * x2 * x2
c.seg((x1, x1 * x1), (x2, x2 * x2), ACC2, 3.2, dash=(11, 7))
c.dot(x1, x1 * x1, ACC2)
c.dot(x2, x2 * x2, ACC2)
c.dot(xt, yc, ACC)
c.dot(xt, yh, RED)
c.seg((xt, yc), (xt, yh), RED, 2.6, dash=(7, 5))
c.tag(x1 - 0.12, x1 * x1 - 0.55, "A", ACC2, 26, "hei", "rt")
c.tag(x2 + 0.16, x2 * x2 + 0.55, "B", ACC2, 26, "hei", "lt")
c.tag(xt + 0.9, yh + 0.85, "弦上的点 tf(x1)+(1-t)f(x2)", RED, 21, "song", "lt")
c.tag(xt + 0.2, yc + 0.12, "曲线上的点 f(tx1+(1-t)x2)", ACC, 21, "song", "lt")
c.label_px(150 * SS, 890 * SS, "红色竖段 = 弦高 - 曲线高 >= 0，这就是“弦在曲线上方”。",
           F("song", 21), GREY, "lt")
c.save("fig1_chord.png")

# ============================ 图2
c = Canvas(-2.5, 2.5, -4.8, 4.8)
header(c, "图 2  下凸（凸）与上凸（凹）",
       "左边 f(x) = x²：弦在曲线上方；右边 g(x) = -x²：弦在曲线下方")
c.axes()
c.curve(lambda x: x * x, -2.05, -0.02, ACC, 4.2)
c.curve(lambda x: -x * x, 0.02, 2.05, RED, 4.2)
c.seg((-1.55, 2.4), (-0.45, 0.2), ACC2, 3)
c.dot(-1.55, 2.4, ACC2)
c.dot(-0.45, 0.2, ACC2)
c.seg((0.45, -0.2), (1.55, -2.4), ACC2, 3)
c.dot(0.45, -0.2, ACC2)
c.dot(1.55, -2.4, ACC2)
c.tag(-1.25, -1.05, "下凸（凸函数）", ACC, 25, "hei", "cm")
c.tag(-1.25, -1.85, "f'' >= 0：割线在曲线上方", GREY, 20, "song", "cm")
c.tag(1.25, 1.10, "上凸（凹函数）", RED, 25, "hei", "cm")
c.tag(1.25, 1.90, "g'' <= 0：割线在曲线下方", GREY, 20, "song", "cm")
c.save("fig2_convex_concave.png")

# ============================ 图3
c = Canvas(-2.5, 3.6, -2.4, 10.0)
header(c, "图 3  可导时的等价刻画：曲线在每点切线的上方",
       "f(x) = x² 在 x0 = 0.8 处的切线 y = 1.6x - 0.64，整条曲线都不低于它")
c.axes()
c.curve(lambda x: x * x, -2.5, 3.6, ACC, 4.2)
x0 = 0.8
c.seg((-1.4, 1.6 * -1.4 - 0.64), (3.2, 1.6 * 3.2 - 0.64), RED, 3)
c.dot(x0, x0 * x0, RED)
c.tag(1.05, 1.35, "切点 x0 = 0.8", RED, 21, "song", "lt")
c.tag(2.85, 4.0, "切线", RED, 25, "hei", "cm")
c.tag(-2.45, 8.7, "f(y) >= f(x) + f'(x)(y - x)", ACC, 24, "serif", "lt")
c.tag(-2.45, 7.6, "（对区间内所有 x, y 成立）", GREY, 20, "song", "lt")
c.save("fig3_tangent.png")

# ============================ 图4
c = Canvas(-2.7, 2.7, -1.3, 7.8)
header(c, "图 4  中点形式：f((x1+x2)/2) <= (f(x1)+f(x2))/2",
       "取 x1 = -2、x2 = 1.6，中点 -0.2：曲线高 0.04 <= 弦的中点高 3.28")
c.axes()
c.curve(lambda x: x * x, -2.7, 2.7, ACC, 4.2)
x1, x2 = -2.0, 1.6
xm = (x1 + x2) / 2
c.seg((x1, x1 * x1), (x2, x2 * x2), ACC2, 3.2)
c.dot(x1, x1 * x1, ACC2)
c.dot(x2, x2 * x2, ACC2)
c.dot(xm, (x1 * x1 + x2 * x2) / 2, RED)
c.dot(xm, xm * xm, ACC)
c.seg((xm, 0), (xm, (x1 * x1 + x2 * x2) / 2), LGREY, 2, dash=(6, 5))
c.tag(-0.35, 4.45, "弦中点高 (f(x1)+f(x2))/2", RED, 20, "song", "rt")
c.tag(xm + 0.55, xm * xm + 0.35, "曲线上的中点", ACC, 20, "song", "lt")
c.save("fig4_midpoint.png")

# ============================ 图5
c = Canvas(-2.7, 3.9, -3.4, 5.6)
header(c, "图 5  常见的凸 / 凹函数",
       "x²、exp(x)、|x| 都是下凸；ln x、sqrt(x)、-x² 都是上凸（看二阶导符号最快）")
c.axes()
c.curve(lambda x: x * x, -2.1, 2.1, ACC, 4)
c.curve(lambda x: math.exp(x), -2.6, 1.75, GREEN, 4)
c.curve(lambda x: math.log(x), 0.28, 3.6, RED, 4)
c.curve(lambda x: abs(x), -2.3, 0.0, PURPLE, 4)
c.tag(-2.55, 4.75, "y = x²", ACC, 23, "serif", "lt")
c.tag(0.50, 2.95, "y = exp(x)", GREEN, 23, "serif", "lt")
c.tag(2.35, 1.30, "y = ln x", RED, 23, "serif", "lt")
c.tag(-2.55, 2.15, "y = |x|", PURPLE, 23, "serif", "lt")
c.save("fig5_examples.png")

# ============================ 图6
c = Canvas(-0.14, 1.18, -0.095, 0.35, pad=(150, 150, 110, 100))
header(c, "图 6  第 4 题的常数 1/8 从哪来：t(1-t) 在 t = 1/2 取最大值 1/4",
       "把每一点的 (x-a)(b-x) 放大为 (b-a)²/4，于是 |f(x)| <= (M/2)(b-a)²/4 = (1/8)(b-a)²M")
c.axes()
c.curve(lambda t: t * (1 - t), 0, 1, ACC, 4.2)
c.dot(0.5, 0.25, RED)
c.tag(0.5, 0.285, "最大值 1/4", RED, 22, "song", "cm")
c.tag(-0.04, -0.035, "0", GREY, 20, "serif", "rt")
c.tag(1.02, -0.035, "1", GREY, 20, "serif", "lt")
c.tag(0.5, 0.275, "", GREY, 20)
c.label_px(*c.P(0.5, -0.075), "t = (x-a)/(b-a)  在 t = 1/2 取最大",
           F("song", 20), GREY, "cm")
c.save("fig6_oneeighth.png")

print("ALL DONE")
