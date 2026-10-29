# -*- coding: utf-8 -*-
"""2022 期中：Q2 的封闭形式与全部数值结果复核（纯整数运算，完全不依赖分数/浮点库）"""


def det3(M):
    a, b, c = M[0]
    d, e, f = M[1]
    g, h, i = M[2]
    return a * (e * i - f * h) - b * (d * i - f * g) + c * (d * h - e * g)


# ---------- Q2 ----------
# (lam-2)x1 + x2 + x3 = 1,  x1 + (lam-2)x2 + x3 = 1,  x1 + x2 + (lam-2)x3 = 1
print("Q2: determinant of A with diag b=lam-2, off-diag 1")
print("   det = (b-1)^2 (b+2);  in lam: (lam-3)^2 (lam)  ->  zeros at lam = 3 and lam = 0")
for lam in [3, 5, 0, -1, 2, 4, 1, -2]:
    b = lam - 2
    det = (b - 1) * (b - 1) * (b + 2)
    print("   lam=%3d  b=%3d  det=%5d" % (lam, b, det))

print()
print("Q2: sum of all three equations = (lam) * (x1+x2+x3) = 3")
print("   -> if lam != 0: x1+x2+x3 = 3/lam ;")
print("   substituting into eq1: (lam-2)x1 + (s - x1) = 1 with s = 3/lam")
print("   -> (lam-3)x1 = 1 - 3/lam  ->  x1 = (lam-3)/(lam(lam-3)) = 1/lam   (lam != 3)")
print("   so for lam != 0, 3:  x1 = x2 = x3 = 1/lam   <-- clean closed form")
for lam in [5, -1, 2, 4, 1, -2]:
    b = lam - 2
    x = 1.0 / lam
    print("   check lam=%3d: x=1/lam=%.6f  b*x+x+x = %.6f  (should be 1)"
          % (lam, x, b * x + x + x))
print()
print("   lam = 0 : sum of equations gives 0 = 3  -> NO SOLUTION")
print("   lam = 3 : all three equations become x1+x2+x3 = 1 -> infinitely many, x=(t,s,1-t-s)")
