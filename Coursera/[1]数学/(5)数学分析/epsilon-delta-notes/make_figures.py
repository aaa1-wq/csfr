# -*- coding: utf-8 -*-
"""生成「ε-δ / ε-N 语言」笔记所需的数轴示意图。全部输出矢量 PDF。"""
import os
import sys
import math

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".pylibs")))

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyArrowPatch, Rectangle, Ellipse
from matplotlib.lines import Line2D

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "figures")
os.makedirs(OUT, exist_ok=True)

plt.rcParams.update({
    "font.family": "serif",
    "font.serif": ["SimSun", "Noto Serif SC", "DejaVu Serif"],
    "mathtext.fontset": "cm",
    "axes.unicode_minus": False,
    "font.size": 11,
    "savefig.bbox": "tight",
    "savefig.pad_inches": 0.10,
})

MAIN = "#1f4e79"
UP = "#c0392b"
DOWN = "#1e8449"
ORANGE = "#e67e22"
PURPLE = "#6c3483"
GREY = "#7f8c8d"


def save(fig, name):
    path = os.path.join(OUT, name)
    fig.savefig(path)
    plt.close(fig)
    print("saved", name)


def number_axis(ax, x0, x1, y=0.0, ticks=(), labels=None, color="k",
                tick_len=0.055, lw=1.3, arrow=True, fs=11.5):
    """画一条数轴 + 刻度。"""
    if arrow:
        ax.annotate("", xy=(x1, y), xytext=(x0, y),
                    arrowprops=dict(arrowstyle="-|>", color=color, lw=lw,
                                    shrinkA=0, shrinkB=0, mutation_scale=13))
    else:
        ax.plot([x0, x1], [y, y], color=color, lw=lw)
    for t in ticks:
        ax.plot([t, t], [y - tick_len, y + tick_len], color=color, lw=1.0)
    if labels:
        for t, lab in zip(ticks, labels):
            ax.text(t, y - tick_len - 0.075, lab, ha="center", va="top",
                    fontsize=fs)


# ============================================================================
# 图 1：ε-N 定义 —— 数列的点列落在 ε 带内
# ============================================================================
def fig_epsilon_N():
    fig, ax = plt.subplots(figsize=(8.6, 3.5))
    N = 11
    a = 1 + 1 / np.arange(1, 31) * np.cos(np.arange(1, 31) * 2.3) * 1.6
    # 让前几项杂乱、后段收敛到 1
    a = 1 + (0.9 * np.cos(np.arange(1, 31) * 1.7)) / np.arange(1, 31) ** 0.45
    a[:4] = [2.35, 0.35, 1.95, 0.62]

    eps = 0.28
    ax.axhspan(1 - eps, 1 + eps, color=DOWN, alpha=0.16, zorder=0)
    ax.axhline(1, color=ORANGE, lw=1.5, ls="-.", zorder=1)
    ax.axhline(1 + eps, color=DOWN, lw=1.1, ls="--", zorder=1)
    ax.axhline(1 - eps, color=DOWN, lw=1.1, ls="--", zorder=1)
    ax.axvline(N, color=UP, lw=1.6, zorder=1)

    n = np.arange(1, 31)
    inside = n >= N
    ax.plot(n[~inside], a[~inside], "x", color=UP, ms=8, mew=2.0,
            label=r"$n<N$：允许落在带外", zorder=4)
    ax.plot(n[inside], a[inside], "o", color=MAIN, ms=6.5,
            label=r"$n\geq N$：必须落在带内", zorder=5)

    # 右侧标签（放到绘图区外，避免被裁切）
    xr = 31.5
    bb = dict(fc="white", ec="none", alpha=0.92, pad=1.5)
    ax.text(xr, 1.0, r"$A$", color=ORANGE, va="center", ha="left", fontsize=13,
            bbox=bb)
    ax.text(xr, 1 + eps, r"$A+\varepsilon$", color=DOWN, va="center",
            ha="left", fontsize=11, bbox=bb)
    ax.text(xr, 1 - eps, r"$A-\varepsilon$", color=DOWN, va="center",
            ha="left", fontsize=11, bbox=bb)
    # N 的标注放到轴线上方，避免与散点重叠
    ax.text(N - 0.45, 2.45, r"$N$", color=UP, ha="right", va="center",
            fontsize=13)
    ax.plot([N, N], [2.32, 2.42], color=UP, lw=1.0)
    ax.text((N + 30) / 2, 1 + eps + 0.17,
            r"$\forall n\geq N:\ \vert a_n-A\vert<\varepsilon$",
            color=DOWN, ha="center", fontsize=11)

    ax.set_xlim(0, 35.6)
    ax.set_ylim(-0.62, 2.75)
    ax.set_xticks([])
    ax.set_yticks([])
    for s in ax.spines.values():
        s.set_visible(False)
    ax.legend(fontsize=9.5, loc="lower left", framealpha=0.95, ncol=2)
    ax.set_xlabel(r"$n$", fontsize=12)
    ax.set_ylabel(r"$a_n$", fontsize=12)
    save(fig, "fig1_epsilon_N.pdf")


# ============================================================================
# 图 2：ε-δ 定义 —— 两条数轴的“矩形控制”
# ============================================================================
def fig_epsilon_delta():
    fig, ax = plt.subplots(figsize=(9.0, 4.8))
    x0, delta, eps = 2.4, 0.58, 0.44
    L = 1.45          # 极限值 A
    y0 = 2.42         # f(x0)
    x_r, y_t = 6.2, 4.1

    ax.annotate("", xy=(x_r + 0.15, 0), xytext=(0.05, 0),
                arrowprops=dict(arrowstyle="-|>", color="k", lw=1.4,
                                mutation_scale=13))
    ax.annotate("", xy=(0, y_t + 0.12), xytext=(0, 0.05),
                arrowprops=dict(arrowstyle="-|>", color="k", lw=1.4,
                                mutation_scale=13))

    # 曲线：在 x0±δ 内保持在 A±ε 内，外侧迅速跑出带外
    def f(t):
        u = (t - x0) / delta
        return L + 0.24 + 0.34 * np.tanh(1.8 * u) ** 3 * (1 + 0.30 * np.cos(2.0 * t))

    xs = np.linspace(0.18, x_r, 600)
    ax.plot(xs, f(xs), color=MAIN, lw=2.2, zorder=6)

    # ε 横带
    ax.add_patch(Rectangle((-1.15, L - eps), x_r + 1.30, 2 * eps, color=ORANGE,
                           alpha=0.15, zorder=0))
    ax.axhline(L, color=ORANGE, lw=1.4, ls="-.", zorder=1)
    ax.axhline(L + eps, color=ORANGE, lw=1.0, ls="--", zorder=1)
    ax.axhline(L - eps, color=ORANGE, lw=1.0, ls="--", zorder=1)

    # δ 竖带
    ax.add_patch(Rectangle((x0 - delta, 0), 2 * delta, y_t, color=DOWN,
                           alpha=0.17, zorder=0))
    ax.axvline(x0, color=DOWN, lw=1.4, ls="-.", zorder=1)
    ax.axvline(x0 - delta, color=DOWN, lw=1.0, ls="--", zorder=1)
    ax.axvline(x0 + delta, color=DOWN, lw=1.0, ls="--", zorder=1)

    # 交点与辅助虚线
    ax.plot([x0], [y0], "o", color="k", ms=6.5, zorder=8)
    ax.plot([x0], [L], "o", color=ORANGE, ms=5.5, zorder=8)
    ax.plot([x0, 0], [y0, y0], color=GREY, lw=0.9, ls=":", zorder=2)
    ax.plot([x0, 0], [L, L], color=GREY, lw=0.9, ls=":", zorder=2)

    # ---- y 轴标签：放到橙色带左侧（带外）、加不透明白底并提高层级 ----
    lx = -0.88
    bbx = dict(fc="white", ec="none", alpha=1.0, pad=2.0)
    ax.text(lx, L + eps, r"$A+\varepsilon$", color=ORANGE, ha="left",
            va="center", fontsize=11.5, bbox=bbx, zorder=20)
    ax.text(lx, L, r"$A$", color=ORANGE, ha="left", va="center",
            fontsize=13, bbox=bbx, zorder=20)
    ax.text(lx, L - eps, r"$A-\varepsilon$", color=ORANGE, ha="left",
            va="center", fontsize=11.5, bbox=bbx, zorder=20)
    ax.text(lx, y0, r"$f(x_0)$", color=MAIN, ha="left", va="center",
            fontsize=11.5, bbox=bbx, zorder=20)

    # ---- x 轴标签 ----
    ax.text(x0, -0.30, r"$x_0$", color=DOWN, ha="center", va="top",
            fontsize=13.5)
    ax.text(x0 - delta, -0.30, r"$x_0-\delta$", color=DOWN, ha="center",
            va="top", fontsize=11.5)
    ax.text(x0 + delta, -0.30, r"$x_0+\delta$", color=DOWN, ha="center",
            va="top", fontsize=11.5)

    # ---- 说明 ----
    ax.text((x0 + x_r) / 2 + 0.2, y_t - 0.30,
            r"给定橙色 $\varepsilon$ 带 $\Rightarrow$ 可找到绿色 $\delta$ 带",
            fontsize=10.5, ha="center",
            bbox=dict(fc="white", ec=GREY, alpha=0.92, pad=4))
    ax.text((x0 + x_r) / 2 + 0.2, y_t - 0.78,
            r"使绿带内曲线（灰蓝）不外露于橙带",
            fontsize=10.5, ha="center",
            bbox=dict(fc="white", ec=GREY, alpha=0.92, pad=4))

    ax.set_xlim(-2.30, x_r + 0.35)
    ax.set_ylim(-0.68, y_t + 0.45)
    ax.axis("off")
    save(fig, "fig2_epsilon_delta.pdf")


# ============================================================================
# 图 3：量词顺序 —— “δ 可以依赖 ε”的扇形示意
# ============================================================================
def fig_quantifier():
    fig, ax = plt.subplots(figsize=(8.4, 4.0))
    eps_list = [(0.55, ORANGE), (0.34, PURPLE), (0.18, DOWN)]
    base = 1.4
    x0 = 1.0

    ax.annotate("", xy=(6.4, 0), xytext=(0.3, 0),
                arrowprops=dict(arrowstyle="-|>", color="k", lw=1.3,
                                mutation_scale=12))
    ax.annotate("", xy=(0.3, 4.0), xytext=(0.3, 0.05),
                arrowprops=dict(arrowstyle="-|>", color="k", lw=1.3,
                                mutation_scale=12))

    xs = np.linspace(0.6, 6.1, 400)
    g = lambda t: base + 0.75 * np.sin(0.85 * t) + 0.10 * t
    ax.plot(xs, g(xs), color=MAIN, lw=2.0, zorder=6)
    ax.axhline(base, color="k", lw=0.9, ls="-.", zorder=1)

    for eps, col in eps_list:
        ax.axhline(base + eps, color=col, lw=1.0, ls=":", zorder=2)
        ax.axhline(base - eps, color=col, lw=1.0, ls=":", zorder=2)
        # 求需要的 δ（数值搜索临界点）
        target = base + eps
        lo, hi = x0 + 1e-6, 6.05
        # 找右侧第一个越过 target 的位置
        cand = None
        for t in np.linspace(x0 + 0.002, 6.05, 4000):
            if abs(g(t) - base) >= eps:
                cand = t
                break
        d = (cand - x0) if cand else 5.0
        ax.add_patch(Rectangle((x0 - d, 0), 2 * d, 3.9, color=col, alpha=0.09,
                               zorder=0))
        ax.plot([x0 - d, x0 - d], [0, 3.9], color=col, lw=1.0, ls="--",
                alpha=0.7)
        ax.plot([x0 + d, x0 + d], [0, 3.9], color=col, lw=1.0, ls="--",
                alpha=0.7)
        ax.text(x0 + d, -0.20, r"$\delta$", color=col, ha="center",
                fontsize=10.5)
        ax.text(-0.05, base + eps, r"$\varepsilon$", color=col, ha="right",
                va="center", fontsize=10.5)

    ax.annotate("", xy=(x0, 3.72), xytext=(x0 - 0.55 + 1.15, 3.72),
                arrowprops=dict(arrowstyle="<->", color=GREY, lw=1.1))
    ax.text(x0 + 0.1, 3.86, r"$\varepsilon$ 越小 $\Rightarrow\ \delta$ 越小",
            fontsize=10.5, ha="center",
            bbox=dict(fc="white", ec="none", alpha=0.9))

    ax.set_xlim(-0.5, 6.7)
    ax.set_ylim(-0.45, 4.15)
    ax.axis("off")
    save(fig, "fig3_quantifier.pdf")


# ============================================================================
# 图 4：连续 vs 一致连续 —— δ 是否与 x0 无关
# ============================================================================
def fig_uniform():
    fig, axes = plt.subplots(1, 2, figsize=(11.2, 4.4))

    # (a) 连续但不一致连续：f(x)=1/x 在 (0,1]
    ax = axes[0]
    xs = np.linspace(0.085, 1.0, 600)
    ax.plot(xs, 1 / xs, color=MAIN, lw=2.1, zorder=5)

    eps = 0.55
    # δ 的“刻度尺”画在 y=0.35 处（水平双箭头），直观比较长度
    ybar = 0.38
    for x0, col in [(0.85, DOWN), (0.42, PURPLE), (0.15, UP)]:
        y = 1 / x0
        xr = 1 / (y + eps)                    # 1/x = y+eps
        d = x0 - xr                            # 需要的 δ
        ax.plot([xr, xr], [0, y + eps], color=col, lw=1.0, ls=":", zorder=3)
        ax.plot([x0, x0], [0, y], color=col, lw=1.0, ls=":", zorder=3)
        ax.annotate("", xy=(x0, ybar), xytext=(xr, ybar),
                    arrowprops=dict(arrowstyle="<->", color=col, lw=1.6,
                                    shrinkA=1, shrinkB=1), zorder=8)
        ax.plot([x0], [y], "o", color=col, ms=6, zorder=7)
        if col == UP:
            ax.text(0.60, 6.45,
                    r"三条箭头用同一个 $\varepsilon=%.2f$" % eps,
                    color=UP, ha="center", fontsize=9.5,
                    bbox=dict(fc="white", ec="none", alpha=0.9, pad=2))
        ax.text((xr + x0) / 2, ybar + 0.30, r"$\delta=%.3f$" % d, color=col,
                ha="center", fontsize=9.5,
                bbox=dict(fc="white", ec="none", alpha=0.9, pad=1.2))

    ax.text(0.52, 8.55,
            r"$\varepsilon$ 固定时，$x_0\to0^{+}$ 使所需 $\delta\to0$",
            fontsize=9.8, ha="center", color=UP,
            bbox=dict(fc="white", ec="none", alpha=0.9, pad=2))
    ax.set_xlim(0, 1.08)
    ax.set_ylim(0, 9.3)
    ax.set_xlabel(r"$x$")
    ax.set_ylabel(r"$y$")
    ax.grid(True, ls=":", color="0.85")
    ax.spines["right"].set_visible(False)
    ax.spines["top"].set_visible(False)
    ax.set_title(r"(a) $f(x)=\dfrac{1}{x}$ 在 $(0,1]$：连续，但不一致连续" "\n"
                 r"（三段蓝色双箭头是同一个 $\varepsilon$ 下所需的 $\delta$）",
                 fontsize=10)

    # (b) 一致连续：f(x)=sqrt(x) 在 [0,1]
    ax = axes[1]
    xs = np.linspace(0, 1.0, 600)
    ax.plot(xs, np.sqrt(xs), color=MAIN, lw=2.1, zorder=5)
    eps = 0.20
    ybar = 0.055
    for x0, col in [(0.88, DOWN), (0.48, PURPLE), (0.09, UP)]:
        y = math.sqrt(x0)
        lo = (y - eps) ** 2 if y - eps > 0 else 0.0
        hi = (y + eps) ** 2
        d = min(x0 - lo, hi - x0)
        ax.plot([x0 - d, x0 - d], [0, y + eps], color=col, lw=1.0, ls=":",
                zorder=3)
        ax.plot([x0 + d, x0 + d], [0, y + eps], color=col, lw=1.0, ls=":",
                zorder=3)
        ax.annotate("", xy=(x0 + d, ybar), xytext=(x0 - d, ybar),
                    arrowprops=dict(arrowstyle="<->", color=col, lw=1.6,
                                    shrinkA=1, shrinkB=1), zorder=8)
        ax.plot([x0], [y], "o", color=col, ms=6, zorder=7)
        ax.text(x0, ybar + 0.075, r"$\delta=%.3f$" % d, color=col,
                ha="center", fontsize=9.5,
                bbox=dict(fc="white", ec="none", alpha=0.9, pad=1.2))

    ax.text(0.52, 1.055,
            r"同一个 $\varepsilon$ 下，$\delta$ 处处可用同一个值",
            fontsize=9.8, ha="center", color=DOWN,
            bbox=dict(fc="white", ec="none", alpha=0.9, pad=2))
    ax.set_xlim(-0.02, 1.08)
    ax.set_ylim(0, 1.16)
    ax.set_xlabel(r"$x$")
    ax.set_ylabel(r"$y$")
    ax.grid(True, ls=":", color="0.85")
    ax.spines["right"].set_visible(False)
    ax.spines["top"].set_visible(False)
    ax.set_title(r"(b) $f(x)=\sqrt{x}$ 在 $[0,1]$：一致连续" "\n"
                 r"$\delta$ 只依赖 $\varepsilon$，与 $x_0$ 的位置无关",
                 fontsize=10)
    fig.tight_layout()
    save(fig, "fig4_uniform.pdf")


# ============================================================================
# 图 5：一致连续的否定 —— 存在 ε0，任何 δ 都失效
# ============================================================================
def fig_uniform_neg():
    fig, ax = plt.subplots(figsize=(8.8, 4.2))
    xs = np.linspace(0.0, 1.0, 900)
    ys = np.sin(np.pi / xs ** 2)
    mask = xs > 0.02
    ax.plot(xs[mask], ys[mask], color=MAIN, lw=1.5)

    # 展示：任意小 δ 区间里都能找到一对点，函数值差 >= eps0
    labels = [r"(i) $\delta=0.04$", r"(ii) $\delta=0.02$", r"(iii) $\delta=0.01$"]
    ly = [1.52, 1.28, 1.04]            # 图例三行的纵坐标
    lx = 0.86                          # 图例文字左端
    for i, x in enumerate([0.30, 0.16, 0.085]):
        seg = np.linspace(max(x - 0.025, 1e-6), x + 0.025, 6000)
        yv = np.sin(np.pi / seg ** 2)
        k1 = np.argmax(yv)
        k2 = np.argmin(yv)
        p1, p2 = seg[k1], seg[k2]
        col = [DOWN, PURPLE, ORANGE][i]
        ax.plot([p1, p1], [0, yv[k1]], color=col, lw=1.1, ls="--", zorder=4)
        ax.plot([p2, p2], [0, yv[k2]], color=col, lw=1.1, ls="--", zorder=4)
        ax.plot([p1, p2], [yv[k1], yv[k2]], "o", color=col, ms=6.5, zorder=7)
        # 直线引线：从两点连线的中点指到图例行
        ax.annotate("", xy=((p1 + p2) / 2, (yv[k1] + yv[k2]) / 2 + 0.05),
                    xytext=(lx - 0.02, ly[i]),
                    arrowprops=dict(arrowstyle="-", color=col, lw=0.9,
                                    alpha=0.6), zorder=5)
        ax.text(lx, ly[i], labels[i], color=col, ha="left", va="center",
                fontsize=9.8)

    ax.text(0.02, 1.80,
            r"取 $\varepsilon_0=1$：任何 $\delta>0$ 的区间内都能找到一对点 "
            r"$p,q$ 使 $\vert f(p)-f(q)\vert\geq\varepsilon_0$",
            fontsize=9.8, color=UP, ha="left",
            bbox=dict(fc="white", ec="none", alpha=0.92, pad=2))

    ax.set_xlim(0, 1.26)
    ax.set_ylim(-1.30, 1.98)
    ax.set_xlabel(r"$x$")
    ax.set_ylabel(r"$y$")
    ax.grid(True, ls=":", color="0.85")
    ax.spines["right"].set_visible(False)
    ax.spines["top"].set_visible(False)
    ax.set_title(r"一致连续的否定：$f(x)=\sin(\pi/x^2)$ 在 $(0,1]$ 上连续但非一致连续"
                 "\n" r"越靠近 $0$ 振荡越快 —— 任何 $\delta$ 都无法“锁住”函数值的变化幅度",
                 fontsize=10.5)
    save(fig, "fig5_uniform_neg.pdf")


# ============================================================================
# 图 6：极限存在的否定 —— 量词否定的图像
# ============================================================================
def fig_neg_limit():
    fig, axes = plt.subplots(1, 2, figsize=(11.0, 3.9))

    # (a) 极限不存在：振荡
    ax = axes[0]
    n = np.arange(1, 26)
    a = np.where(n % 2 == 1, 1.0, -1.0) + 1 / n
    ax.axhspan(-1 - 0.15, -1 + 0.15, color=UP, alpha=0.12)
    ax.axhspan(1 - 0.15, 1 + 0.15, color=DOWN, alpha=0.12)
    ax.plot(n, a, "o", color=MAIN, ms=5.5)
    ax.axhline(1, color=DOWN, lw=1.0, ls="--")
    ax.axhline(-1, color=UP, lw=1.0, ls="--")
    ax.set_title(r"(a) $a_n=(-1)^n+\frac{1}{n}$：极限不存在" "\n"
                 r"取 $\varepsilon_0=1$，任何 $N$ 之后都有两种值无法同时落入一条 $\varepsilon_0$ 带",
                 fontsize=9.6)
    ax.set_xlabel(r"$n$")
    ax.set_ylabel(r"$a_n$")
    ax.set_ylim(-1.6, 1.6)
    ax.grid(True, ls=":", color="0.85")
    ax.spines["right"].set_visible(False)
    ax.spines["top"].set_visible(False)

    # (b) 函数极限不存在：sin(1/x)
    ax = axes[1]
    xs = np.linspace(0.012, 0.5, 6000)
    ax.plot(xs, np.sin(1 / xs), color=MAIN, lw=0.9)
    ax.axhspan(1 - 0.3, 1 + 0.3, color=DOWN, alpha=0.12)
    ax.axhspan(-1 - 0.3, -1 + 0.3, color=UP, alpha=0.12)
    ax.axhline(1, color=DOWN, lw=1.0, ls="--")
    ax.axhline(-1, color=UP, lw=1.0, ls="--")
    ax.axvline(0, color="k", lw=1.0)
    ax.set_xlim(0, 0.5)
    ax.set_ylim(-1.5, 1.5)
    ax.set_xlabel(r"$x$")
    ax.set_ylabel(r"$y$")
    ax.set_title(r"(b) $f(x)=\sin\frac{1}{x}$ 在 $x\to0$ 时极限不存在" "\n"
                 r"取 $\varepsilon_0=\frac{1}{2}$：任何 $\delta>0$ 内都能找到函数值差 $>\varepsilon_0$ 的两点",
                 fontsize=9.6)
    ax.grid(True, ls=":", color="0.85")
    ax.spines["right"].set_visible(False)
    ax.spines["top"].set_visible(False)
    fig.tight_layout()
    save(fig, "fig6_neg_limit.pdf")


# ============================================================================
# 图 7：Heine 定理（数列刻画）—— 连续性与序列判据
# ============================================================================
def fig_heine():
    fig, ax = plt.subplots(figsize=(8.4, 4.0))
    xs = np.linspace(0.4, 4.6, 500)
    f = lambda t: 0.8 + 0.6 * np.sin(0.9 * t) + 0.22 * t
    ax.plot(xs, f(xs), color=MAIN, lw=2.1, zorder=5)
    x0 = 2.2
    y0 = f(x0)
    ax.plot([x0], [y0], "o", color="k", ms=7, zorder=8)

    # 收敛到 x0 的点列
    n = np.arange(1, 9)
    xn = x0 + 2.1 * (-1) ** n / (n ** 0.7)
    ax.plot(xn, f(xn), "o", color=UP, ms=6, zorder=7,
            label=r"$x_n\to x_0$")
    for i in range(len(n)):
        ax.plot([xn[i], xn[i]], [0, f(xn[i])], color=UP, lw=0.7, ls=":",
                alpha=0.55, zorder=1)
    for i in range(len(n) - 1):
        ax.annotate("", xy=(xn[i + 1], f(xn[i + 1])),
                    xytext=(xn[i], f(xn[i])),
                    arrowprops=dict(arrowstyle="->", color=UP, lw=0.8,
                                    alpha=0.5, shrinkA=2, shrinkB=2))

    ax.axhline(y0, color=ORANGE, lw=1.2, ls="-.", zorder=2)
    ax.plot([x0, x0], [0, y0], color=GREY, lw=0.9, ls=":")
    ax.plot([0.4, x0], [y0, y0], color=GREY, lw=0.9, ls=":")
    ax.text(x0, -0.30, r"$x_0$", ha="center", fontsize=12.5)
    ax.text(0.42, y0, r"$f(x_0)$", va="center", ha="left", color=ORANGE,
            fontsize=11.5)
    ax.text(3.5, 0.30, r"$f(x_n)\to f(x_0)$", color=UP, fontsize=11.5,
            bbox=dict(fc="white", ec="none", alpha=0.85))

    ax.set_xlim(0.4, 4.75)
    ax.set_ylim(-0.45, 3.3)
    ax.grid(True, ls=":", color="0.85")
    ax.spines["right"].set_visible(False)
    ax.spines["top"].set_visible(False)
    ax.set_xlabel(r"$x$")
    ax.set_ylabel(r"$y$")
    ax.legend(fontsize=10, loc="upper left")
    ax.set_title(r"Heine 定理：$f$ 在 $x_0$ 连续 $\Longleftrightarrow$ 对每个 $x_n\to x_0$ 都有 $f(x_n)\to f(x_0)$",
                 fontsize=10.5)
    save(fig, "fig7_heine.pdf")


# ============================================================================
# 图 8：三种语言的统一 —— ε-N / ε-δ / ε-M 对照
# ============================================================================
def fig_three_langs():
    # 竖排三栏（3 行 1 列），保证在 A4 正文宽度下公式清晰可读
    fig, axes = plt.subplots(3, 1, figsize=(7.2, 6.6))

    def draw(ax, x0, x1, lo, hi, ticks, labels, fs_tick, band, title,
             top_label, formula, extra=None):
        number_axis(ax, x0, x1, y=0, ticks=ticks, labels=[], color="k",
                    lw=1.2)
        ax.add_patch(Rectangle((band[0], -0.17), band[1] - band[0], 0.34,
                               color=DOWN, alpha=0.22))
        # 端点竖线
        ax.plot([band[0]], [0], "|", color=UP, ms=13, mew=2.2)
        ax.plot([band[1]], [0], "|", color=UP, ms=13, mew=2.2)
        if extra:
            extra(ax)
        ax.text((band[0] + band[1]) / 2, 0.26, top_label, ha="center",
                color=DOWN, fontsize=10.5)
        ax.text((x0 + x1) / 2, -0.62, formula, ha="center", va="center",
                fontsize=9.2)
        ax.set_xlim(x0 - 0.3, x1 + 0.3)
        ax.set_ylim(-0.92, 0.50)
        ax.axis("off")
        ax.set_title(title, fontsize=10.5, pad=3)

    # ---------------- (a) ε-N ----------------
    ax = axes[0]
    def _tick_a(ax):
        for t in np.arange(1.0, 10.0, 0.8):
            ax.plot([t], [0], "|", color=MAIN, ms=10, mew=1.8)
        ax.text(2.4, -0.24, r"$N$", color=UP, ha="center", va="top",
                fontsize=12)
    number_axis(ax, 0, 10.4, y=0, color="k", lw=1.3)
    ax.add_patch(Rectangle((2.4, -0.17), 8.0, 0.34, color=DOWN, alpha=0.22))
    for t in np.arange(1.0, 10.0, 0.8):
        ax.plot([t], [0], "|", color=MAIN, ms=10, mew=1.8)
    ax.plot([2.4], [0], "|", color=UP, ms=13, mew=2.2)
    ax.text(2.4, -0.24, r"$N$", color=UP, ha="center", va="top", fontsize=12.5)
    ax.text(6.6, 0.27, r"尾部 $n>N$", ha="center", color=DOWN, fontsize=10.5)
    ax.text(5.2, -0.66,
            r"$\forall\varepsilon>0,\ \ \exists N\in\mathbb{N},\ \ "
            r"n>N\ \Rightarrow\ \vert a_n-A\vert<\varepsilon$",
            ha="center", va="center", fontsize=9.6)
    ax.set_xlim(-0.3, 10.7)
    ax.set_ylim(-0.95, 0.50)
    ax.axis("off")
    ax.set_title(r"(a) 数列：$\varepsilon$-$N$ 语言", fontsize=10.5,
                 pad=2)

    # ---------------- (b) ε-δ ----------------
    ax = axes[1]
    number_axis(ax, 0, 10.4, y=0, color="k", lw=1.3)
    ax.add_patch(Rectangle((3.2, -0.17), 3.6, 0.34, color=DOWN, alpha=0.22))
    ax.plot([3.2], [0], "|", color=UP, ms=13, mew=2.2)
    ax.plot([6.8], [0], "|", color=UP, ms=13, mew=2.2)
    ax.plot([5.0], [0], "o", color="white", mec=MAIN, ms=11, mew=2.2, zorder=6)
    ax.text(3.2, -0.24, r"$x_0-\delta$", ha="center", va="top", fontsize=10)
    ax.text(6.8, -0.24, r"$x_0+\delta$", ha="center", va="top", fontsize=10)
    ax.text(5.0, -0.46, r"$x_0$（去心）", ha="center", va="top", fontsize=10.5)
    ax.text(5.0, 0.27, "去心 δ 邻域", ha="center", color=DOWN, fontsize=10.5)
    ax.text(5.2, -0.72,
            r"$\forall\varepsilon>0,\ \ \exists\delta>0,\ \ "
            r"0<\vert x-x_0\vert<\delta\ \Rightarrow\ \vert f(x)-A\vert<\varepsilon$",
            ha="center", va="center", fontsize=9.6)
    ax.set_xlim(-0.3, 10.7)
    ax.set_ylim(-1.00, 0.50)
    ax.axis("off")
    ax.set_title(r"(b) 函数：$\varepsilon$-$\delta$ 语言", fontsize=10.5,
                 pad=2)

    # ---------------- (c) ε-M ----------------
    ax = axes[2]
    number_axis(ax, 0, 10.4, y=0, color="k", lw=1.3)
    ax.add_patch(Rectangle((6.2, -0.17), 4.2, 0.34, color=DOWN, alpha=0.22))
    ax.plot([6.2], [0], "|", color=UP, ms=13, mew=2.2)
    ax.text(6.2, -0.24, r"$M$", color=UP, ha="center", va="top", fontsize=12.5)
    ax.text(8.4, 0.27, r"$\vert x\vert>M$", ha="center", color=DOWN,
            fontsize=11)
    ax.text(5.2, -0.66,
            r"$\forall\varepsilon>0,\ \ \exists M>0,\ \ "
            r"\vert x\vert>M\ \Rightarrow\ \vert f(x)-A\vert<\varepsilon$",
            ha="center", va="center", fontsize=9.6)
    ax.set_xlim(-0.3, 10.7)
    ax.set_ylim(-0.95, 0.50)
    ax.axis("off")
    ax.set_title(r"(c) 无穷远：$\varepsilon$-$M$ 语言", fontsize=10.5,
                 pad=2)

    fig.tight_layout(h_pad=0.9)
    save(fig, "fig8_three_langs.pdf")


# ============================================================================
# 图 9：Cauchy 收敛准则 —— 双指标控制
# ============================================================================
def fig_cauchy():
    fig, ax = plt.subplots(figsize=(8.6, 3.6))
    n = np.arange(1, 27)
    a = 2 + np.cumsum(0.6 * np.cos(n * 1.3) / n ** 1.15)
    eps = 0.34
    ax.plot(n, a, "-o", color=MAIN, ms=4.5, lw=1.2)
    N = 13
    ax.axvline(N, color=UP, lw=1.5)
    ax.text(N, a.min() - 0.28, r"$N$", color=UP, ha="center", fontsize=12.5)

    # 在 N 之后任取两点，用带显示它们的差小于 eps
    sel = [15, 19, 22, 25]
    lo = min(a[np.searchsorted(n, s)] for s in sel)
    hi = max(a[np.searchsorted(n, s)] for s in sel)
    ax.axhspan(lo - (eps - (hi - lo)) / 2, lo - (eps - (hi - lo)) / 2 + eps,
               xmin=(N - 0.5) / 26.5, color=DOWN, alpha=0.15, zorder=0)
    ax.axhline(lo - (eps - (hi - lo)) / 2, color=DOWN, lw=1.0, ls="--")
    ax.axhline(lo - (eps - (hi - lo)) / 2 + eps, color=DOWN, lw=1.0, ls="--")

    for s in sel:
        idx = np.searchsorted(n, s)
        ax.plot([s], [a[idx]], "o", color=UP, ms=7, zorder=6)
    ax.annotate("", xy=(sel[1], a[np.searchsorted(n, sel[1])]),
                xytext=(sel[0], a[np.searchsorted(n, sel[0])]),
                arrowprops=dict(arrowstyle="<->", color=ORANGE, lw=1.5,
                                shrinkA=4, shrinkB=4))
    ax.text((sel[0] + sel[1]) / 2, a[np.searchsorted(n, sel[0])] + 0.30,
            r"$\vert a_m-a_n\vert<\varepsilon$", color=ORANGE, fontsize=11,
            ha="center")

    ax.set_xlim(0, 27)
    ax.set_ylim(a.min() - 0.55, a.max() + 0.75)
    ax.set_xlabel(r"$n$")
    ax.set_ylabel(r"$a_n$")
    ax.grid(True, ls=":", color="0.85")
    ax.spines["right"].set_visible(False)
    ax.spines["top"].set_visible(False)
    ax.set_title(r"Cauchy 准则：$m,n>N$ 时 $\vert a_m-a_n\vert<\varepsilon$"
                 "\n" r"只比较项与项，无需事先知道极限 $A$",
                 fontsize=10.5)
    save(fig, "fig9_cauchy.pdf")


if __name__ == "__main__":
    fig_epsilon_N()
    fig_epsilon_delta()
    fig_uniform()
    fig_uniform_neg()
    fig_neg_limit()
    fig_heine()
    fig_three_langs()
    fig_cauchy()
    print("all figures done")
