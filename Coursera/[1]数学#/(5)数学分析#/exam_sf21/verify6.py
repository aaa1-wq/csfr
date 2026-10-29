# -*- coding: utf-8 -*-
"""Q4(2) 常数 1/8 的精确性：用 exp 修正函数验证等号可取到。"""
import math

# 取 [0,1]，f(x) = x - e^x? 不行（端点不为 0）。
# 用标准"等号函数"：f(x) = (x-a)(b-x)/2 * M 的二次函数给出 |f| 峰值 = M(b-a)^2/8
# 验证二次函数达到界，且二阶导恰为 M
a, b, M = 0.0, 1.0, 2.0
f = lambda x: (M / 2) * (x - a) * (b - x)
print("f(a), f(b) =", f(a), f(b))
h = 1e-6
x0 = 0.37
d2 = (f(x0 + h) - 2 * f(x0) + f(x0 - h)) / h ** 2
print("f'' =", round(d2, 6), " = -M =", -M)
mx = max(abs(f(a + i * (b - a) / 2000)) for i in range(2001))
print("max|f| =", round(mx, 10), " (1/8)(b-a)^2 M =", (1 / 8) * (b - a) ** 2 * M)

# 尝试更"挑"的函数：f(x)=sin(pi x) 在 [0,1]，M=pi^2，比较 |f|max 与界
f2 = lambda x: math.sin(math.pi * x)
m2 = (1 / 8) * 1 ** 2 * math.pi ** 2
print()
print("f(x)=sin(pi x): max|f| =", 1.0, " 界 =", round(m2, 6), " -> 界成立且不紧")
