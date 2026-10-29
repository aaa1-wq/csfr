# -*- coding: utf-8 -*-
"""逐步核对 Q3(6)：参数曲线二阶导的两种算法是否一致（用不同 h 做收敛检验）"""
import math

a, b, t0 = 2.0, 3.0, 0.4


def X(t):
    return math.sin(a * t)


def Y(t):
    return math.cos(b * t)


# 法一：参数式 (x'y'' - y'x'')/(x')^3
xp = a * math.cos(a * t0)
xpp = -(a * a) * math.sin(a * t0)
yp = -b * math.sin(b * t0)
ypp = -(b * b) * math.cos(b * t0)
val_param = (xp * ypp - yp * xpp) / xp ** 3
print("参数式: (x'y''-y'x'')/x'^3 =", round(val_param, 8))

# 法二：换成 y=y(x) 后直接二阶差分（多个 h 看是否收敛到法一）
def y_of_x(xv):
    tt = math.asin(xv) / a
    return Y(tt)


x0 = X(t0)
print("x0 =", x0)
for eps in [1e-2, 1e-3, 1e-4]:
    d2 = (y_of_x(x0 + eps) - 2 * y_of_x(x0) + y_of_x(x0 - eps)) / eps ** 2
    print("  h=%g  二阶差分 = %.8f" % (eps, d2))

# 法三：直接对参数式求数值导数（用于校验 xp, xpp, yp, ypp）
h = 1e-6
xpp_num = (X(t0 + h) - 2 * X(t0) + X(t0 - h)) / h ** 2
ypp_num = (Y(t0 + h) - 2 * Y(t0) + Y(t0 - h)) / h ** 2
print("xpp 解析 %.8f 数值 %.8f" % (xpp, xpp_num))
print("ypp 解析 %.8f 数值 %.8f" % (ypp, ypp_num))
