# -*- coding: utf-8 -*-
"""高精度复核：用 Decimal(math.sin) 太弱，这里改用整数/有理+级数或直接高精度差分。
重点：
  Q3(4) 的常数到底是多少（-1/8 还是 -1/4）
  Q3(6) 的二阶导公式
"""
from decimal import Decimal, getcontext
import math

getcontext().prec = 50


def sqrt_d(x):
    return x.sqrt()


print("=" * 62)
print("Q3(4)  x^{3/2}(sqrt(x+1)+sqrt(x-1)-2 sqrt x)  —— 用 Decimal 高精度")
print("=" * 62)
for k in [2, 3, 4, 5, 6, 7, 8, 10, 12]:
    x = 10 ** k
    X = Decimal(x)
    val = sqrt_d(X + 1) + sqrt_d(X - 1) - 2 * sqrt_d(X)
    # 乘以 x^{3/2}
    res = val * X * sqrt_d(X)
    print("  x=1e%-2d   res = %s" % (k, str(+res)[:24]))
print()
print("  解析：令 t=1/x，sqrt(x+-1)=sqrt(x)(1+t)^{1/2}")
print("  (1+t)^{1/2}+(1-t)^{1/2}-2 = (1/2)(1/4)t^2*2 + O(t^4) = -t^2/4 + O(t^4)")
print("  x^{3/2} * (-t^2/4) * sqrt(x)  ->  x^2 * (1/x^2) * (-1/4) = -1/4")

print()
print("=" * 62)
print("Q3(6)  x=sin(at), y=cos(bt), 求 d2y/dx2  （取 a=2,b=3,t=0.4）")
print("=" * 62)
a, b, t0 = 2.0, 3.0, 0.4
# 用极高精度差分做对照（中心差分用 5 点公式以减小误差）
h = 1e-4


def X(t):
    return math.sin(a * t)


def Y(t):
    return math.cos(b * t)


# 参数曲线二阶导: (x'y'' - y'x'')/x'^3
ypp_x = -(b * b) * math.sin(b * t0) / (a * a * math.cos(a * t0) ** 3)
print("  解析式  -(b^2/a^2) sin(bt)/cos^3(at) =", round(ypp_x, 8))

# 直接对 y(x) 做差分：先取 x(t)，再在同一 x 附近取样
def y_of_x(xv):
    tt = math.asin(xv) / a
    return math.cos(b * tt)


eps = 1e-5
x0 = math.sin(a * t0)
d2 = (y_of_x(x0 + eps) - 2 * y_of_x(x0) + y_of_x(x0 - eps)) / eps ** 2
print("  数值差分 y''(x) ≈", round(d2, 8))
