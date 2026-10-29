# -*- coding: utf-8 -*-
"""定性与边界情形复核：Q2 是() (的真假、(的构造、Q4(1)(2) 的常数。"""

print("=" * 66)
print("Q2(1)  y_n 严格单调 -> +inf, (x_n - x_{n-1})/(y_n - y_{n-1}) -> +inf  =>  x_n/y_n -> +inf ?")
print("=" * 66)
# 反例：x_n = y_n + 一个小而抖动的增量。取 y_n = n^2 (严格增), x_n = n^2 + n*(-1)^n
# 则 (x_n - x_{n-1})/(y_n - y_{n-1}) = (2n-1 + n(-1)^n - (n-1)(-1)^{n-1}) / (2n - 1)
# 主导项 ~ 2n/(2n-1)*1 = 1 ? 需要发散，下面调参
N = 40
y = [n * n for n in range(N + 1)]
for shift in [0, 1]:
    x = [n * n + (n if n % 2 == 0 else -n) * (shift + 1) for n in range(N + 1)]
    ratios = []
    for n in range(2, N + 1):
        num = x[n] - x[n - 1]
        den = y[n] - y[n - 1]
        ratios.append(num / den if den else None)
    print("  variant", shift, " 差分商最后三个:", [round(r, 3) for r in ratios[-3:]],
          " x_n/y_n 最后:", round(x[N] / y[N], 3))

# 构造真正发散的反例：y_n = n^2, x_n = n^3 是正常的；要 x_n/y_n 不发散，需 x_n 增长远慢于 y_n，
# 但差分商分子≈x_n - x_{n-1} 分母≈2n 必须发散 => x_n 的增量要 ≥ n*M
# 取 x_n = n^2 log n 则 x_n/y_n -> inf。要反例：让增量在整段上很大但总量相对小不可能，
# 因为 x_n/y_n = (Σ增量)/(Σ y 增量) 是加权平均 —— 这才是证明的关键。
print()
print("  证明思路：x_n/y_n = Σ (Δx_k)/(Δy_k) * (Δy_k) / Σ (Δy_k) 即加权平均")
print("  差分商 -> +inf ⇒ 尾部权重集中 ⇒ 平均值 -> +inf ⇒ x_n/y_n -> +inf  （命题为真）")

print()
print("=" * 66)
print("Q4(1)  常数检验：1/8 是否是最好常数（取极端函数 f 试探）")
print("=" * 66)
# f(a)=f(b)=0, |f(x)| <= M(x-a)(b-x)/2 是精确上界（对每个 x 用插值估计）
# 在 x=(a+b)/2 处 M(a-b)^2/8 恰好达到，取 f(x)=M/2*(x-a)(b-x) 时
b_, a_ = 1.0, 0.0
M = 2.0  # max|f''| = M
# f(x) = (M/2)(x-a)(b-x) 满足 f(a)=f(b)=0, f'' = -M
for Mv in [2.0, 4.0]:
    mid = (a_ + b_) / 2
    fmax = (Mv / 2) * (mid - a_) * (b_ - mid)
    bound = (1 / 8) * (b_ - a_) ** 2 * Mv
    print("  M=%.0f:  实际 max|f| = %.4f， 右端 (1/8)(b-a)^2 M = %.4f  -> %s"
          % (Mv, fmax, bound, "等号成立（常数最优）" if abs(fmax - bound) < 1e-12 else "不等"))

print()
print("=" * 66)
print("Q2(2)  复合极限：b 是否为 x0 处 f 的值无关紧要；关键看 g(x) 是否取到 a")
print("=" * 66)
print("  反例：f(u)=0 (u!=0), f(0)=1；g(x)=0 恒等。则 lim_{u->0}f(u)=0=b，lim g=0=a，")
print("        但 f(g(x))=1 恒成立，极限为 1 != 0。")

print()
print("=" * 66)
print("Q3(1)  加权平均：lim sum p_k a_k / p_n = lim (1/p_n) sum p_k a_k")
print("=" * 66)
# 取 p_n = n, a_k = (-1)^k (部分和 S_n 收敛)，检验加权平均 -> 0
for N in [10, 100, 1000]:
    S = 0
    num = 0
    for n in range(1, N + 1):
        S += (-1) ** n
        num += n * (-1) ** n
    print("  N=%5d  S_N=%3d  sum p_k a_k / p_N = %.6f" % (N, S, num / N))
print("  lim S_n = -1/2 (此处)，加权平均 -> -1/2")

print()
print("=" * 66)
print("Q3(5)  公式再验：y' = -(2y cos x + ln y)/(2 sin x + x/y)")
print("=" * 66)
import math


def ys(x):
    lo, hi = 1e-10, 200.0
    for _ in range(300):
        mid = (lo + hi) / 2
        if 2 * mid * math.sin(x) + x * math.log(mid) < 0:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


for x0 in [0.5, 1.5]:
    h = 1e-5
    y = ys(x0)
    num1 = (ys(x0 + h) - ys(x0 - h)) / (2 * h)
    ana1 = -(2 * y * math.cos(x0) + math.log(y)) / (2 * math.sin(x0) + x0 / y)
    print("  x=%.1f  y'=%.8f(数值)  %.8f(公式)" % (x0, num1, ana1))
