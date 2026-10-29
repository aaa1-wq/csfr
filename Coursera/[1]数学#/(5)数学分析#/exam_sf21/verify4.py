# -*- coding: utf-8 -*-
"""最终复核：极值/极限/导数，全部用高精度 Decimal 或多种独立算法交叉验证。"""
import math
from decimal import Decimal, getcontext, localcontext
from fractions import Fraction as F

getcontext().prec = 60

print("=" * 66)
print("Q3(4)  lim x^{3/2}( sqrt(x+1)+sqrt(x-1)-2 sqrt x ),  x->+inf")
print("=" * 66)
rows = []
for k in [2, 4, 6, 8, 10]:
    with localcontext() as ctx:
        ctx.prec = 80
        X = Decimal(10) ** k
        s = (X + 1).sqrt() + (X - 1).sqrt() - 2 * X.sqrt()
        res = s * X * X.sqrt()
        rows.append((k, +res))
for k, r in rows:
    print("   x=1e%-2d   value = %s" % (k, str(r)[:30]))
print("   -> 极限 = -1/4 =", -0.25)

print()
print("=" * 66)
print("Q3(3)  lim_{x->0} (x + e^x)^{1/x}")
print("=" * 66)
with localcontext() as ctx:
    ctx.prec = 40
    for k in [1, 2, 3, 4]:
        x = Decimal(10) ** (-k)
        base = x + x.exp()
        val = (base.ln() / x).exp()
        xn = -Decimal(10) ** (-k)
        basen = xn + xn.exp()
        valn = (basen.ln() / xn).exp()
        print("   x=%8s   L=%s | x=%9s  L=%s" % (x, str(+val)[:12], xn, str(+valn)[:12]))
print("   e^2 =", str(Decimal(2).exp())[:12])

print()
print("=" * 66)
print("Q3(2)  lim (1/(n+sqrt k) 求和 k=1..n)")
print("=" * 66)
for n in [10, 100, 1000, 10000, 100000]:
    s = math.fsum(1.0 / (n + math.sqrt(k)) for k in range(1, n + 1))
    print("   n=%6d  S_n=%.10f   (n 越小越靠近 1)" % (n, s))

print()
print("=" * 66)
print("Q3(6)  x=sin(at), y=cos(bt) 二阶导：参数式 vs 直接差分")
print("=" * 66)
a, b, t0 = 2.0, 3.0, 0.4
xp = a * math.cos(a * t0)
xpp = -a * a * math.sin(a * t0)
yp = -b * math.sin(b * t0)
ypp = -b * b * math.cos(b * t0)
param = (xp * ypp - yp * xpp) / xp ** 3


def y_of_x(xv):
    return math.cos(b * math.asin(xv) / a)


x0 = math.sin(a * t0)
diff = (y_of_x(x0 + 1e-4) - 2 * y_of_x(x0) + y_of_x(x0 - 1e-4)) / 1e-8
closed = -(b * b) * math.sin(b * t0) / (a * a * math.cos(a * t0) ** 3)
print("   参数式  = ", round(param, 9))
print("   差分    = ", round(diff, 9))
print("   闭式 -(b^2/a^2) sin(bt)/cos^3(at) = ", round(closed, 9))

print()
print("=" * 66)
print("Q3(5)  2y sin x + x ln y = 0 的二阶导（数值验证公式）")
print("=" * 66)


def y_solve(x):
    lo, hi = 1e-8, 100.0
    for _ in range(200):
        mid = (lo + hi) / 2
        if 2 * mid * math.sin(x) + x * math.log(mid) < 0:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def yprime(x):
    y = y_solve(x)
    return -(2 * math.sin(x) * y + x) / (2 * y)  # dx 形式，稍后统一


# 用隐函数 y' = -(2y cos x + ln y) / (2 sin x + x/y)
def yp_implicit(x):
    y = y_solve(x)
    return -(2 * y * math.cos(x) + math.log(y)) / (2 * math.sin(x) + x / y)


for x0 in [0.7, 1.2]:
    h = 1e-6
    num = (y_solve(x0 + h) - 2 * y_solve(x0) + y_solve(x0 - h)) / h ** 2
    # 解析：对 y' = -(2y cos x + ln y)/(2 sin x + x/y) 再求导
    y = y_solve(x0)
    N = 2 * y * math.cos(x0) + math.log(y)
    Dn = 2 * math.sin(x0) + x0 / y
    y1 = -N / Dn
    dN = 2 * y1 * math.cos(x0) - 2 * y * math.sin(x0) + y1 / y
    dD = 2 * math.cos(x0) + 1 / y - x0 * y1 / (y * y)
    y2 = -(dN * Dn - N * dD) / (Dn * Dn)
    print("   x=%.1f  数值二阶导 %.8f   解析 %.8f" % (x0, num, y2))

print()
print("=" * 66)
print("Q3(7)  y = x^2/(1+x) 的渐近线")
print("=" * 66)
for x in [100, 1e4, 1e6]:
    y = x * x / (1 + x)
    print("   x=%-8.0f  y=%.4f   y-(x-1)=%.6f" % (x, y, y - (x - 1)))
print("   x=-1 处：分母为零，y->+-inf，x=-1 是竖直渐近线")
