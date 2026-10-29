# -*- coding: utf-8 -*-
"""数学分析期中(2021, 王彦/吴语?) 数值答案的高精度复核。
只用标准库 decimal（高精度）与 fractions，不依赖 sympy。
"""
from decimal import Decimal as D
from fractions import Fraction as F
import itertools

print("=" * 60)
print("Q3(2)  lim (1/(n+sqrt1) + ... + 1/(n+sqrt n))")
print("=" * 60)
for n in [10, 100, 1000, 10000, 100000]:
    s = sum(1.0 / (n + i ** 0.5) for i in range(1, n + 1))
    print("  n=%7d  sum=%.10f" % (n, s))

print()
print("=" * 60)
print("Q3(4)  lim_{x->+inf} x^{3/2}(sqrt(x+1)+sqrt(x-1)-2sqrt x)")
print("=" * 60)


def f(x):
    return x ** 1.5 * (x ** 0.5 * ((1 + 1 / x) ** 0.5 + (1 - 1 / x) ** 0.5) - 2 * x ** 0.5)


for x in [10, 1e2, 1e3, 1e4, 1e6, 1e8]:
    print("  x=%10.0e  f=%.10f" % (x, f(x)))
print("  理论值 -1/8 =", -1 / 8)

print()
print("=" * 60)
print("Q3(3)  lim_{x->0} (x+e^x)^{1/x}")
print("=" * 60)
import math
for x in [0.1, 0.01, 0.001, 0.0001, -0.1, -0.01, -0.001]:
    v = x + math.exp(x)
    print("  x=%8.4f  base=%.10f  1/x=%.1f  value=%s" % (x, v, 1 / x, "N/A(base<0)" if v <= 0 else "%.6f" % (v ** (1 / x))))

print()
print("=" * 60)
print("Q3(5)  2y sin x + x ln y = 0, 求 d2y/dx2")
print("=" * 60)
# implicit derivative: 2 y cos x + 2 y' sin x + ln y + x y'/y = 0
#   => y'(2 sin x + x/y) = -(2 y cos x + ln y)
#   => y' = -(2 y cos x + ln y) / (2 sin x + x/y)
# 数值检验：取 (x0,y0) 满足方程，比较差分商

def Y(x, y0):
    return y0


def deriv_check(x0, y0v):
    # y0 应满足 2 y sin x0 + x0 ln y0 = 0 -> 对给定 x0 用求根
    lo, hi = D("1e-6"), D(50)
    def g(y):
        return 2 * y * D(str(math.sin(x0))) + D(str(x0)) * D(math.log(y))
    for _ in range(200):
        mid = (lo + hi) / 2
        if g(mid) < 0:
            lo = mid
        else:
            hi = mid
    y0 = (lo + hi) / 2
    return y0


for x0 in [0.7, 1.2]:
    y0 = deriv_check(x0, None)
    print("  x0=%.2f  y0=%.10f  2y sinx+x lny=%.2e" % (x0, float(y0), float(2 * y0 * D(str(math.sin(x0))) + D(str(x0)) * D(math.log(y0)))))

print()
print("=" * 60)
print("Q3(6)  x=sin(at), y=cos(bt):  d2y/dx2 数值检验")
print("=" * 60)


def param_d2(a, b, t, h=1e-5):
    def X(t):
        return math.sin(a * t)

    def Yv(t):
        return math.cos(b * t)
    x0, xp, xm = X(t), X(t + h), X(t - h)
    y0, yp, ym = Yv(t), Yv(t + h), Yv(t - h)
    # 用参数化的二阶导数公式
    xprime = (xp - xm) / (2 * h)
    yprime = (yp - ym) / (2 * h)
    xbis = (xp - 2 * x0 + xm) / (h * h)
    ybis = (yp - 2 * y0 + ym) / (h * h)
    return (ybis * xprime - yprime * xbis) / xprime ** 3


a, b = 2.0, 3.0
t0 = 0.4
num = param_d2(a, b, t0)
ana = -(b * b / (a * a)) * math.cos(b * t0) / math.sin(a * t0 + math.pi / 2) / (math.sin(a * t0) ** 2)
# 直接解析式：y''_xx = -b^2 sin(bt)/(a^2 cos^3(at))
ana2 = -(b ** 2) * math.sin(b * t0) / ((a ** 2) * math.cos(a * t0) ** 3)
print("  数值 %.8f   解析 %.8f" % (num, ana2))
