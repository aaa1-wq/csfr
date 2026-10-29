# -*- coding: utf-8 -*-
"""
生成《数学分析中的不等式与放缩法》笔记所需的全部插图。
所有图都以 PDF 矢量格式输出，便于 LaTeX 直接引入。
"""
import os
import sys
import math

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".pylibs")))

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Polygon, FancyArrowPatch, Rectangle
from matplotlib.lines import Line2D

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "figures")
os.makedirs(OUT, exist_ok=True)

plt.rcParams.update({
    "font.family": "serif",
    "font.serif": ["SimSun", "Noto Serif SC", "DejaVu Serif"],
    "font.sans-serif": ["Microsoft YaHei", "SimHei"],
    "mathtext.fontset": "cm",
    "axes.unicode_minus": False,
    "font.size": 11,
    "axes.linewidth": 0.9,
    "savefig.bbox": "tight",
    "savefig.pad_inches": 0.08,
})

C_MAIN = "#1f4e79"
C_UP = "#c0392b"
C_DOWN = "#1e8449"
C_GREY = "#7f8c8d"
C_ORANGE = "#e67e22"
C_PURPLE = "#6c3483"


def save(fig, name):
    path = os.path.join(OUT, name)
    fig.savefig(path)
    plt.close(fig)
    print("saved", path)


def clean_axes(ax, xlabel="x", ylabel="y"):
    ax.spines["right"].set_visible(False)
    ax.spines["top"].set_visible(False)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.grid(True, ls=":", lw=0.6, color="0.75", alpha=0.8)
    return ax


# ----------------------------------------------------------------------------
# 图 1：均值不等式的几何证明（半径-半弦模型）
# ----------------------------------------------------------------------------
def fig_am_gm():
    """半圆模型：直径 AB 被 M 分成 a、b 两段，
    半径 MB = (a+b)/2 是算术平均，垂线 MP = sqrt(ab) 是几何平均。
    由直角三角形中直角边小于斜边得 sqrt(ab) <= (a+b)/2。
    """
    fig, ax = plt.subplots(figsize=(7.2, 4.6))
    b, a = 1.2, 4.6          # 左端点横坐标 b，右端点横坐标 a（先左后右）
    mid = (a + b) / 2.0
    R = (a - b) / 2.0
    h = math.sqrt(a * b)

    # 半圆
    th = np.linspace(0, np.pi, 500)
    ax.plot(mid + R * np.cos(th), R * np.sin(th), color=C_MAIN, lw=1.8,
            zorder=2)
    # 直径
    ax.plot([b, a], [0, 0], color="k", lw=1.4, zorder=3)
    # 弦 MB（半径，长度 = 算术平均）
    ax.plot([mid, b], [0, 0], color=C_UP, lw=2.6, zorder=4)
    # 垂线 MP（高度 = 几何平均）
    ax.plot([mid, mid], [0, h], color=C_DOWN, lw=2.6, zorder=4)
    # 虚线：PB 与 PA
    Pbx, Pby = mid, h
    ax.plot([Pbx, b], [Pby, 0], color=C_GREY, lw=1.0, ls=":", zorder=2)
    ax.plot([Pbx, a], [Pby, 0], color=C_GREY, lw=1.0, ls=":", zorder=2)
    # 直角标记
    ax.plot([mid, mid + 0.14], [0, 0], color="k", lw=0.9)
    ax.plot([mid + 0.14, mid + 0.14], [0, 0.14], color="k", lw=0.9)
    ax.plot([mid, mid], [0, 0.14], color="k", lw=0.9)
    # 端点
    for x, y, lab in [(b, 0, r"$B$"), (a, 0, r"$A$"), (mid, 0, r"$M$"),
                      (mid, h, r"$P$")]:
        ax.plot([x], [y], "o", color="k", ms=4.0, zorder=5)
        dx = {r"$B$": -0.16, r"$A$": 0.16}.get(lab, 0.0)
        dy = 0.22 if lab == r"$P$" else -0.24
        ax.text(x + dx, y + dy, lab, ha="center", va="center",
                fontsize=12.5, zorder=6)

    # 标注
    ax.text((b + mid) / 2, -0.52, r"$a$", ha="center", va="center",
            fontsize=12.5, color=C_UP)
    ax.text((mid + a) / 2, -0.52, r"$b$", ha="center", va="center",
            fontsize=12.5, color=C_MAIN)
    ax.text(mid - 0.10, h / 2, r"$h=\sqrt{ab}$", ha="right", va="center",
            fontsize=12.5, color=C_DOWN)
    ax.text((b + mid) / 2 + 0.05, 0.30, r"$R=\dfrac{a+b}{2}$", ha="center",
            va="bottom", fontsize=12.5, color=C_UP)

    # 长度对比：两条水平基准
    ax.set_xlim(b - 0.55, a + 0.55)
    ax.set_ylim(-0.85, R + 0.95)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_title("均值不等式的半圆模型\n"
                 r"$R=\dfrac{a+b}{2}\ \geq\ \sqrt{ab}=h$（直角边 $\leq$ 斜边）",
                 fontsize=11, pad=8)
    save(fig, "fig1_amgm.pdf")


# ----------------------------------------------------------------------------
# 图 2：算术—几何—调和平均的柱状比较
# ----------------------------------------------------------------------------
def fig_mean_chain():
    fig, ax = plt.subplots(figsize=(6.6, 3.8))
    a, b = 9.0, 1.0
    vals = [a, (a + b) / 2, np.sqrt(a * b), 2 * a * b / (a + b), b]
    labs = [r"$\max$", r"$A=\frac{a+b}{2}$", r"$G=\sqrt{ab}$",
            r"$H=\frac{2ab}{a+b}$", r"$\min$"]
    cols = ["#95a5a6", C_MAIN, C_DOWN, C_ORANGE, "#95a5a6"]
    bars = ax.bar(range(len(vals)), vals, color=cols, width=0.62,
                  edgecolor="k", linewidth=0.6, zorder=3)
    for x, v in zip(range(len(vals)), vals):
        ax.text(x, v + 0.18, f"{v:.2f}", ha="center", va="bottom",
                fontsize=10)
    ax.set_xticks(range(len(vals)))
    ax.set_xticklabels(labs, fontsize=10)
    ax.set_ylabel("数值")
    ax.set_ylim(0, a + 1.4)
    ax.grid(True, axis="y", ls=":", color="0.75", alpha=0.8)
    ax.spines["right"].set_visible(False)
    ax.spines["top"].set_visible(False)
    ax.set_title("四种平均数的序链  " + r"($a=9,\ b=1$)", fontsize=11)
    save(fig, "fig2_mean_chain.pdf")


# ----------------------------------------------------------------------------
# 图 3：伯努利不等式
# ----------------------------------------------------------------------------
def fig_bernoulli():
    fig, axes = plt.subplots(1, 3, figsize=(9.6, 3.7))
    xs = np.linspace(-0.97, 1.15, 600)
    settings = [(2, 0.40), (3, 0.32)]
    for ax, (n, alpha) in zip(axes[:2], settings):
        y1 = np.maximum(1 + xs, 0) ** n
        y0 = 1 + n * xs
        ax.plot(xs, y1, color=C_MAIN, lw=2.0, label=r"$(1+x)^n$")
        ax.plot(xs, y0, color=C_UP, lw=1.6, ls="--", label=r"$1+nx$")
        ax.fill_between(xs, y0, y1, where=(y1 >= y0), color=C_DOWN,
                        alpha=alpha, label=r"$(1+x)^n-(1+nx)\geq 0$")
        ax.axhline(0, color="k", lw=0.8)
        ax.axvline(0, color="k", lw=0.8)
        ax.plot([0], [1], "o", color="k", ms=3.5)
        ax.set_xlim(-1.05, 1.25)
        ax.set_ylim(-0.4, 4.2)
        clean_axes(ax)
        ax.set_title(r"$n=%d$" % n, fontsize=10.5)
        ax.legend(fontsize=8.2, loc="upper left", framealpha=0.92)

    # 第三幅：反向对照 —— 0 < n < 1 时不等号反向
    ax = axes[2]
    n = 0.5
    y1 = np.sqrt(np.maximum(1 + xs, 0))
    y0 = 1 + n * xs
    ax.plot(xs, y1, color=C_MAIN, lw=2.0, label=r"$(1+x)^{1/2}$")
    ax.plot(xs, y0, color=C_UP, lw=1.6, ls="--", label=r"$1+x/2$")
    ax.fill_between(xs, y1, y0, where=(y0 >= y1), color=C_ORANGE,
                    alpha=0.35, label=r"此时间号反向")
    ax.axhline(0, color="k", lw=0.8)
    ax.axvline(0, color="k", lw=0.8)
    ax.plot([0], [1], "o", color="k", ms=3.5)
    ax.set_xlim(-1.05, 1.25)
    ax.set_ylim(-0.4, 4.2)
    clean_axes(ax)
    ax.set_title(r"反例：$0<n=0.5<1$ 时 $(1+x)^n\leq 1+nx$", fontsize=9.5)
    ax.legend(fontsize=8.2, loc="upper left", framealpha=0.92)

    fig.suptitle(r"伯努利不等式 $(1+x)^n\geq 1+nx$  "
                 r"$(x>-1,\ n\in\mathbb{N},\ n\geq 2)$ 的阴影区域",
                 fontsize=11, y=1.03)
    fig.tight_layout()
    save(fig, "fig3_bernoulli.pdf")


# ----------------------------------------------------------------------------
# 图 4：切线 / 割线——对数不等式与 e^x 不等式
# ----------------------------------------------------------------------------
def fig_tangent():
    fig, axes = plt.subplots(1, 2, figsize=(8.4, 4.1))

    # (a) ln x
    ax = axes[0]
    xs = np.linspace(0.08, 5.0, 800)
    ax.plot(xs, np.log(xs), color=C_MAIN, lw=2.0, label=r"$y=\ln x$")
    ax.plot(xs, xs - 1, color=C_UP, lw=1.5, ls="--",
            label=r"切线 $y=x-1$（在 $x=1$ 处）")
    xs2 = np.linspace(0.02, 5.0, 800)
    ax.fill_between(xs, xs - 1, np.log(xs), color=C_DOWN, alpha=0.35,
                    label=r"$\ln x\leq x-1$")
    ax.axhline(0, color="k", lw=0.8)
    ax.axvline(0, color="k", lw=0.8)
    ax.plot([1], [0], "o", color=C_UP, ms=5)
    ax.set_xlim(0, 5)
    ax.set_ylim(-2.6, 2.2)
    clean_axes(ax)
    ax.legend(fontsize=9, loc="lower right")
    ax.set_title(r"(a) $\ln x\leq x-1$" "\n" r"$0<x<1$ 时放缩为负，$x>1$ 时放缩为正",
                 fontsize=9.8)

    # (b) e^x
    ax = axes[1]
    xs = np.linspace(-2.0, 1.9, 800)
    ax.plot(xs, np.exp(xs), color=C_MAIN, lw=2.0, label=r"$y=e^x$")
    ax.plot(xs, 1 + xs, color=C_UP, lw=1.5, ls="--",
            label=r"切线 $y=1+x$（在 $x=0$ 处）")
    ax.fill_between(xs, 1 + xs, np.exp(xs), color=C_DOWN, alpha=0.35,
                    label=r"$e^x\geq 1+x$")
    ax.axhline(0, color="k", lw=0.8)
    ax.axvline(0, color="k", lw=0.8)
    ax.plot([0], [1], "o", color=C_UP, ms=5)
    ax.set_xlim(-2.0, 1.9)
    ax.set_ylim(-0.9, 6.6)
    clean_axes(ax)
    ax.legend(fontsize=9, loc="upper left")
    ax.set_title(r"(b) $e^x\geq 1+x\quad(\forall x\in\mathbb{R})$", fontsize=10)
    fig.suptitle("“切线在曲线下方”型不等式：凸函数的支撑线", fontsize=11, y=1.03)
    fig.tight_layout()
    save(fig, "fig4_tangent.pdf")


# ----------------------------------------------------------------------------
# 图 5：|sin x| <= |x|、cos x <= 1 - x^2/2 + x^4/24
# ----------------------------------------------------------------------------
def fig_sin():
    fig, axes = plt.subplots(1, 2, figsize=(8.4, 4.0))
    xs = np.linspace(-2 * np.pi, 2 * np.pi, 1400)
    ax = axes[0]
    ax.plot(xs, np.sin(xs), color=C_MAIN, lw=1.8, label=r"$\sin x$")
    ax.plot(xs, xs, color=C_UP, lw=1.4, ls="--", label=r"$y=|x|$ 的两条边")
    ax.plot(xs, -xs, color=C_UP, lw=1.4, ls="--")
    # 用 |sin x| 与 |x| 的带形填充，逐分支处理符号翻转
    ax.fill_between(xs, np.abs(np.sin(xs)), np.abs(xs),
                    color=C_DOWN, alpha=0.30, label=r"$|\sin x|\leq|x|$")
    ax.axhline(0, color="k", lw=0.8)
    ax.axvline(0, color="k", lw=0.8)
    ax.set_xlim(-2 * np.pi, 2 * np.pi)
    ax.set_ylim(-2.6, 2.6)
    clean_axes(ax)
    ax.legend(fontsize=9, loc="lower right")
    ax.set_title(r"(a) $|\sin x|\leq|x|$ 的夹逼区域", fontsize=10)

    # Taylor 交替放缩
    ax = axes[1]
    xs = np.linspace(-np.pi, np.pi, 1200)
    ax.plot(xs, np.cos(xs), color="k", lw=2.4, label=r"$\cos x$")
    ts = [(1, "1", C_UP, "--", 2),
          (2, r"$1-\frac{x^2}{2!}$", C_DOWN, "-.", 3),
          (4, r"$1-\frac{x^2}{2!}+\frac{x^4}{4!}$", C_PURPLE, ":", 4),
          (6, r"$\sum_{k=0}^{3}\frac{(-1)^k x^{2k}}{(2k)!}$", C_ORANGE, "--", 2)]
    for order, lab, col, ls, off in ts:
        approx = np.zeros_like(xs)
        for k in range(order // 2 + 1):
            approx += (-1) ** k * xs ** (2 * k) / math.factorial(2 * k)
        ax.plot(xs, approx, color=col, lw=1.3, ls=ls, label=lab, zorder=off)
    ax.axhline(0, color="k", lw=0.8)
    ax.axvline(0, color="k", lw=0.8)
    ax.set_xlim(-np.pi, np.pi)
    ax.set_ylim(-1.4, 2.6)
    clean_axes(ax)
    ax.legend(fontsize=8.2, loc="upper center", ncol=1, framealpha=0.92)
    ax.set_title(r"(b) $\cos x$ 的 Taylor 部分和交替夹逼", fontsize=10)
    fig.suptitle("三角函数型基本不等式", fontsize=11, y=1.03)
    fig.tight_layout()
    save(fig, "fig5_sin.pdf")


# ----------------------------------------------------------------------------
# 图 6：几何平均-算术平均-积分平均（Hermite–Hadamard）
# ----------------------------------------------------------------------------
def fig_hermite():
    fig, ax = plt.subplots(figsize=(7.2, 4.2))
    f = lambda x: np.exp(x)
    xs = np.linspace(0, 1, 400)
    ax.plot(xs, f(xs), color=C_MAIN, lw=2.2, label=r"$f(x)=e^x$")
    # 内接梯形
    ax.fill([0, 0, 1, 1], [f(0), f(0), f(1), f(1)], color=C_UP, alpha=0.16,
            label=r"梯形面积 $=\frac{f(0)+f(1)}{2}$")
    ax.plot([0, 1], [f(0), f(1)], color=C_UP, lw=1.5, ls="--")
    # 实际积分
    ax.fill_between(xs, 0, f(xs), color=C_DOWN, alpha=0.30,
                    label=r"$\int_0^1 e^x\,dx$")
    # 中点切线
    ax.plot([0, 1], [np.exp(0.5), np.exp(0.5)], color=C_ORANGE, lw=1.5,
            ls="-.", label=r"中点切线 $y=f(\frac{a+b}{2})$")
    ax.axvline(0.5, color=C_GREY, lw=0.8, ls=":")
    ax.plot([0.5], [np.exp(0.5)], "o", color=C_ORANGE, ms=5)
    ax.plot([0, 1], [f(0), f(1)], "o", color=C_UP, ms=4)
    ax.set_xlim(-0.02, 1.05)
    ax.set_ylim(0.8, 2.9)
    clean_axes(ax)
    ax.legend(fontsize=9, loc="upper left")
    ax.set_title(r"$f\left(\frac{a+b}{2}\right)\leq\frac{1}{b-a}\int_a^b f\leq\frac{f(a)+f(b)}{2}$"
                 "(Hermite–Hadamard)", fontsize=11)
    save(fig, "fig6_hermite.pdf")


# ----------------------------------------------------------------------------
# 图 7：定积分大小的几何意义（放缩的“面积”直觉）
# ----------------------------------------------------------------------------
def fig_integral_area():
    fig, axes = plt.subplots(1, 2, figsize=(8.6, 4.1))
    xs = np.linspace(0, 1, 600)
    ax = axes[0]
    f = lambda x: 0.6 + 1.8 * x ** 2
    # 精确值：∫_0^1 (0.6 + 1.8x^2) dx = 0.6 + 0.6 = 1.2
    ax.fill_between(xs, 0, f(xs), color=C_MAIN, alpha=0.22,
                    label=r"$\int_0^1 f\,dx=0.6+0.6=1.2$")
    ax.plot(xs, f(xs), color=C_MAIN, lw=2.0, label=r"$f(x)=0.6+1.8x^2$")
    ax.add_patch(Rectangle((0, 0), 1, 0.6, fill=False, ec=C_DOWN, lw=1.7,
                           ls="--"))
    ax.add_patch(Rectangle((0, 0), 1, 2.4, fill=False, ec=C_UP, lw=1.7,
                           ls=":"))
    ax.annotate("", xy=(0.06, 0.0), xytext=(0.06, 0.6),
                arrowprops=dict(arrowstyle="<->", color=C_DOWN, lw=1.5,
                                shrinkA=0, shrinkB=0, mutation_scale=9))
    ax.annotate("", xy=(0.06, 0.0), xytext=(0.06, 2.4),
                arrowprops=dict(arrowstyle="<->", color=C_UP, lw=1.5,
                                shrinkA=0, shrinkB=0, mutation_scale=9))
    ax.text(0.10, 0.30, r"$m=0.6$", ha="left", va="center", color=C_DOWN,
            fontsize=10.5)
    ax.text(0.98, 2.40, r"$M=2.4$", ha="right", va="bottom", color=C_UP,
            fontsize=10.5,
            bbox=dict(fc="white", ec="none", alpha=0.85, pad=1.5))
    ax.text(0.50, 1.28, r"$0.6\leq\int_0^1 f\leq 2.4$", ha="center",
            va="bottom", fontsize=10, color=C_MAIN)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 2.85)
    clean_axes(ax)
    ax.legend(fontsize=8.8, loc="lower right", framealpha=0.93)
    ax.set_title(r"(a) $m(b-a)\leq\int_a^b f\leq M(b-a)$", fontsize=10.5)

    # 单调函数上下和
    ax = axes[1]
    n = 6
    xi = np.linspace(0, 1, n + 1)
    g = lambda x: 0.5 + 0.9 * np.sin(2.2 * x) + 0.5 * x
    xf = np.linspace(0, 1, 600)
    for i in range(n):
        ax.add_patch(Rectangle((xi[i], 0), xi[i + 1] - xi[i], g(xi[i]),
                               fc=C_DOWN, alpha=0.14, ec="none"))
        ax.add_patch(Rectangle((xi[i], 0), xi[i + 1] - xi[i], g(xi[i]),
                               fill=False, ec=C_DOWN, lw=1.1, ls="--"))
        ax.add_patch(Rectangle((xi[i], 0), xi[i + 1] - xi[i], g(xi[i + 1]),
                               fill=False, ec=C_UP, lw=1.1, ls=":"))
    ax.plot(xf, g(xf), color="k", lw=2.2, zorder=5)
    ax.legend(handles=[Line2D([], [], color=C_DOWN, ls="--", lw=1.2,
                              label=r"下和 $s_n$（左端点）"),
                       Line2D([], [], color=C_UP, ls=":", lw=1.2,
                              label=r"上和 $S_n$（右端点）")],
              fontsize=8.8, loc="upper left", framealpha=0.93)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 2.35)
    clean_axes(ax)
    ax.set_title(r"(b) 黎曼上下和：" + r" $s_n\leq\int_a^b g\leq S_n$ " + r" ($n=6$)",
                 fontsize=10.5)
    fig.suptitle("定积分的几何放缩：面积即不等式", fontsize=11, y=1.03)
    fig.tight_layout()
    save(fig, "fig7_integral.pdf")


# ----------------------------------------------------------------------------
# 图 8：放缩法“三明治”示意
# ----------------------------------------------------------------------------
def fig_sandwich():
    fig, ax = plt.subplots(figsize=(7.6, 4.2))
    xs = np.linspace(0.35, 4.2, 600)
    lower = 2 - 1.0 / xs
    upper = 2 + 1.0 / xs
    mid = 2 + 0.35 * np.sin(3 * xs) / xs
    ax.fill_between(xs, lower, upper, color=C_DOWN, alpha=0.16)
    ax.plot(xs, upper, color=C_UP, lw=1.6, ls="--", label=r"放大：$g(x)\leq U(x)$")
    ax.plot(xs, lower, color=C_DOWN, lw=1.6, ls="--", label=r"缩小：$L(x)\leq g(x)$")
    ax.plot(xs, mid, color=C_MAIN, lw=2.2, label=r"原式 $g(x)$")
    ax.axhline(2, color=C_ORANGE, lw=1.3, ls="-.", label=r"极限 $L=2$")
    ax.annotate("", xy=(3.9, 2.26), xytext=(3.9, 1.74),
                arrowprops=dict(arrowstyle="<->", color="k", lw=1.2))
    ax.text(3.95, 2.02, r"$U-L=\dfrac{2}{x}\to 0$",
            fontsize=10, va="center", ha="left",
            bbox=dict(fc="white", ec="none", alpha=0.85, pad=1.5))
    ax.set_xlim(0.35, 4.6)
    ax.set_ylim(0.6, 3.6)
    clean_axes(ax)
    ax.legend(fontsize=9, loc="upper right")
    ax.set_title("放缩法的“三明治”结构：上下界的差必须趋于 0", fontsize=11)
    save(fig, "fig8_sandwich.pdf")


# ----------------------------------------------------------------------------
# 图 9：数列极限中“部分放大”——n 项和
# ----------------------------------------------------------------------------
def fig_sum_bound():
    fig, axes = plt.subplots(1, 2, figsize=(8.6, 4.1))

    # (a) 逐项放缩：把分母“变小”从而把分数“变大”
    ax = axes[0]
    n = np.arange(1, 8)
    ax.bar(n - 0.17, 1 / (n ** 2 + n), width=0.32, color=C_MAIN, alpha=0.85,
           label=r"$\dfrac{1}{n^2+n}=\dfrac{1}{n}-\dfrac{1}{n+1}$")
    ax.bar(n + 0.17, 1 / n ** 2, width=0.32, color=C_UP, alpha=0.55,
           label=r"$\dfrac{1}{n^2}\geq\dfrac{1}{n^2+n}$")
    ax.set_xlabel("$n$")
    ax.set_ylabel("项值")
    ax.set_xticks(n)
    ax.legend(fontsize=8.8, loc="upper right", framealpha=0.93)
    ax.grid(True, axis="y", ls=":", color="0.75")
    ax.spines["right"].set_visible(False)
    ax.spines["top"].set_visible(False)
    ax.set_title("(a) 逐项放缩：分母放大则分数变小", fontsize=10.5)

    # (b) 裂项放缩：Σ 1/k^2 <= 1 + Σ_{k>=2} 1/(k(k-1)) = 2 - 1/n
    ax = axes[1]
    ns = np.arange(1, 41)
    s = np.cumsum(1 / ns ** 2)
    upper = 2 - 1 / ns            # 对 n>=1 成立的上界（n=1 时取等）
    ax.plot(ns, upper, color=C_DOWN, ls=":", lw=1.9,
            label=r"裂项上界 $2-\frac{1}{n}$")
    ax.plot(ns, s, "o-", ms=3.0, lw=1.3, color=C_MAIN,
            label=r"$S_n=\sum_{k=1}^{n}\frac{1}{k^{2}}$")
    ax.axhline(np.pi ** 2 / 6, color=C_UP, ls="--", lw=1.5,
               label=r"$\zeta(2)=\frac{\pi^{2}}{6}\approx1.6449$")
    ax.fill_between(ns, s, upper, color=C_DOWN, alpha=0.18)
    ax.set_xlabel("$n$")
    ax.set_ylabel("部分和")
    ax.set_ylim(1.0, 2.15)
    ax.grid(True, ls=":", color="0.75")
    ax.legend(fontsize=8.5, loc="lower right", framealpha=0.93)
    ax.spines["right"].set_visible(False)
    ax.spines["top"].set_visible(False)
    ax.set_title(r"(b) 裂项放缩：$\frac{1}{k^{2}}<\frac{1}{k(k-1)}$",
                 fontsize=10.5)
    fig.suptitle("数列求和中的放缩：把不可求的和换成可求的和", fontsize=11, y=1.03)
    fig.tight_layout()
    save(fig, "fig9_sum_bound.pdf")


# ----------------------------------------------------------------------------
# 图 10：Young 不等式（几何解释）
# ----------------------------------------------------------------------------
def fig_young():
    """Young 不等式 ab <= a^p/p + b^q/q 的面积解释。

    取 f(x)=x^{p-1}，则 f^{-1}(y)=y^{q-1}（1/p+1/q=1）。
    矩形 [0,a]x[0,b]（面积 ab）被曲线分割成两块：
        曲线下面积        \int_0^a f = a^p/p
        曲线左侧面积      \int_0^b f^{-1} = b^q/q
    二者之和覆盖矩形，故 ab <= a^p/p + b^q/q。
    当 b = a^{p-1} 即 b^{q} = a^{p} 时两块恰好拼成矩形，取等。
    """
    fig, axes = plt.subplots(1, 2, figsize=(8.6, 4.6))
    p = 2.6
    q = p / (p - 1)
    f = lambda t: t ** (p - 1)
    finv = lambda t: t ** (q - 1)
    xmax = 2.35
    ymax = 2.25

    def draw(ax, a, b, title):
        xs = np.linspace(0, xmax, 600)

        # 【区域1】曲线下方、x∈[0,a]：∫_0^a f = a^p/p
        xa = np.linspace(0, a, 400)
        ax.fill_between(xa, 0, f(xa), color=C_DOWN, alpha=0.55,
                        zorder=2, lw=0)
        # 【区域2】曲线左侧、y∈[0,b] 且 x∈[finv(y), a]：
        #          这是矩形 [0,a]x[0,b] 里扣除区域1 的剩余部分，
        #          其面积 = ab - a^p/p，也恰等于 max(0, b^q/q) 在 b>=a^{p-1} 时的…
        #          为避免图面歧义，这里直接画“矩形减去曲线下”的补集部分。
        yy = np.linspace(0, min(b, f(a)), 400)
        ax.fill_betweenx(yy, finv(yy), a, color=C_UP, alpha=0.40,
                         zorder=3, lw=0)
        # 若 b > f(a)，曲线右侧整条竖条也属于"曲线左侧"区域
        if b > f(a):
            y2 = np.linspace(f(a), b, 100)
            ax.fill_betweenx(y2, 0, a, color=C_UP, alpha=0.40, zorder=3, lw=0)

        # 矩形边框（面积 ab）
        ax.add_patch(Rectangle((0, 0), a, b, fill=False, ec="k", lw=1.6,
                               ls="--", zorder=8))
        ax.plot(xs, f(xs), color=C_MAIN, lw=2.4, zorder=9,
                label=r"$y=f(x)=x^{p-1}$")
        ax.plot([a, a], [0, b], color="k", lw=0.9, zorder=7)
        ax.plot([0, a], [b, b], color="k", lw=0.9, zorder=7)
        ax.plot([a], [b], "o", color="k", ms=5.5, zorder=10)

        # 刻度标注：用坐标轴刻度表示 a 与 b，避免与区域/图例重叠
        ax.set_xticks([0, a])
        ax.set_xticklabels(["0", r"$a$"], fontsize=11.5)
        ax.set_yticks([0, b])
        ax.set_yticklabels(["0", r"$b$"], fontsize=11.5)

        ax.set_xlim(0, xmax)
        ax.set_ylim(0, ymax)
        clean_axes(ax)
        # 面积数值标注，直接写在各自区域内
        ax.text(a * 0.42, f(a) * 0.28,
                r"$\dfrac{a^{p}}{p}=%.2f$" % (a ** p / p),
                ha="center", va="center", fontsize=9.5,
                bbox=dict(fc="white", ec="none", alpha=0.82, pad=2))
        ax.text(max(a * 0.55, finv(b) + 0.18) if b > f(a) else a * 0.62,
                min(b, ymax - 0.25) * 0.62,
                r"$\dfrac{b^{q}}{q}=%.2f$" % (b ** q / q),
                ha="center", va="center", fontsize=9.5,
                bbox=dict(fc="white", ec="none", alpha=0.82, pad=2))
        ax.set_title(title, fontsize=10)

    draw(axes[0], 0.80, 1.55,
         "(a) 一般情形（$b$ 与 $a^{p-1}$ 不相等）" "\n"
         r"两区域面积之和 $>$ 矩形面积，$ab<\dfrac{a^{p}}{p}+\dfrac{b^{q}}{q}$")
    # 取等：b = a^{p-1}，此时两区域恰好拼满矩形
    a0 = 1.02
    draw(axes[1], a0, f(a0),
         "(b) 取等情形（$b=a^{p-1}$）" "\n"
         r"两区域恰好拼满矩形，$ab=\dfrac{a^{p}}{p}+\dfrac{b^{q}}{q}$")

    fig.suptitle(r"Young 不等式 $ab\leq\dfrac{a^{p}}{p}+\dfrac{b^{q}}{q}$"
                 r"（$a,b\geq0$，$p,q>1$，$\frac{1}{p}+\frac{1}{q}=1$）的面积分解",
                 fontsize=11, y=1.02)
    fig.tight_layout()
    save(fig, "fig10_young.pdf")


# ----------------------------------------------------------------------------
# 图 11：Chebyshev 与排序不等式
# ----------------------------------------------------------------------------
def fig_chebyshev():
    fig, ax = plt.subplots(figsize=(6.8, 4.0))
    a = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
    b = np.array([0.9, 1.4, 2.6, 3.9, 4.6])
    ax.plot(a, b, "o", color=C_MAIN, ms=10, zorder=4,
            label=r"同序对 $(a_i,b_i)$")
    slope = np.polyfit(a, b, 1)[0]
    xs = np.array([0.8, 5.2])
    ax.plot(xs, np.polyval(np.polyfit(a, b, 1), xs), color=C_UP, lw=1.4,
            ls="--", label="同序：正相关")
    # 乱序：把 b 反向配对
    br = b[::-1]
    ax.plot(a, br, "s", color=C_ORANGE, ms=7, zorder=3,
            label=r"反序对 $(a_i,b_{n+1-i})$")
    ax.plot(xs, np.polyval(np.polyfit(a, br, 1), xs), color=C_DOWN,
            lw=1.4, ls=":", label="反序：负相关")
    for xi, yi in zip(a, b):
        ax.plot([xi, xi], [0, yi], color="0.85", lw=6, solid_capstyle="butt",
                zorder=1)
    ax.set_xlim(0.6, 5.4)
    ax.set_ylim(0, 5.6)
    clean_axes(ax)
    ax.legend(fontsize=9, loc="upper left")
    ax.set_title(r"排序不等式：" + r" 同序和 $\geq$ 乱序和 $\geq$ 反序和", fontsize=11)
    save(fig, "fig11_chebyshev.pdf")


# ----------------------------------------------------------------------------
# 图 12：夹逼定理（数列）与单调有界
# ----------------------------------------------------------------------------
def fig_squeeze_seq():
    fig, ax = plt.subplots(figsize=(7.4, 4.0))
    n = np.arange(1, 26)
    up = 1 + 1 / n
    lo = 1 - 1 / n
    mid = 1 + np.cos(n * 0.9) / (n ** 0.6)
    up[0] = 2.6
    lo[0] = -0.6
    ax.plot(n, up, "o--", color=C_UP, ms=3.2, lw=1.1,
            label=r"$u_n=1+\frac{1}{n}\to1$")
    ax.plot(n, lo, "s--", color=C_DOWN, ms=3.2, lw=1.1,
            label=r"$l_n=1-\frac{1}{n}\to1$")
    ax.plot(n, mid, "D", color=C_MAIN, ms=4.0, label=r"被夹逼的 $a_n$")
    ax.axhline(1.0, color=C_ORANGE, lw=1.2, ls="-.", label="极限 $=1$")
    ax.set_xlabel("$n$")
    ax.set_ylabel("值")
    ax.set_ylim(-1.2, 3.0)
    ax.grid(True, ls=":", color="0.75")
    ax.spines["right"].set_visible(False)
    ax.spines["top"].set_visible(False)
    ax.legend(fontsize=8.8, loc="upper right", ncol=2)
    ax.set_title("两边夹（夹逼）定理的几何图像", fontsize=11)
    save(fig, "fig12_squeeze_seq.pdf")


if __name__ == "__main__":
    fig_am_gm()
    fig_mean_chain()
    fig_bernoulli()
    fig_tangent()
    fig_sin()
    fig_hermite()
    fig_integral_area()
    fig_sandwich()
    fig_sum_bound()
    fig_young()
    fig_chebyshev()
    fig_squeeze_seq()
    print("all figures done")
