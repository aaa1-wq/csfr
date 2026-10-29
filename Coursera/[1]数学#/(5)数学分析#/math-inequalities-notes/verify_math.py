# -*- coding: utf-8 -*-
"""对笔记中所有关键不等式做随机数值抽查，确保符号与方向正确。"""
import math
import random

random.seed(0)
ok = 0
bad = []


def chk(name, cond):
    global ok
    if cond:
        ok += 1
    else:
        bad.append(name)


for _ in range(3000):
    a = random.uniform(0.01, 12)
    b = random.uniform(0.01, 12)

    # 1. 四均值链 H <= G <= A
    A = (a + b) / 2
    G = math.sqrt(a * b)
    H = 2 * a * b / (a + b)
    chk("H<=G", H <= G + 1e-12)
    chk("G<=A", G <= A + 1e-12)

    # 2. ln x <= x-1
    chk("ln x<=x-1", math.log(a) <= a - 1 + 1e-12)
    # 3. e^x >= 1+x
    x = random.uniform(-8, 8)
    chk("e^x>=1+x", math.exp(x) >= 1 + x - 1e-12)
    # 4. x/(1+x) <= ln(1+x) <= x
    chk("x/(1+x)<=ln(1+x)", a / (1 + a) <= math.log(1 + a) + 1e-12)
    chk("ln(1+x)<=x", math.log(1 + a) <= a + 1e-12)
    # 5. |sin x| <= |x|
    t = random.uniform(-10, 10)
    chk("|sin x|<=|x|", abs(math.sin(t)) <= abs(t) + 1e-12)
    # 6. sin x < x < tan x on (0, pi/2)
    s = random.uniform(0.001, math.pi / 2 - 0.001)
    chk("sin<x", math.sin(s) < s)
    chk("x<tan", s < math.tan(s))
    # 7. cos x >= 1-x^2/2 on [-pi/2, pi/2]
    c = random.uniform(-math.pi / 2, math.pi / 2)
    chk("cos>=1-x^2/2", math.cos(c) >= 1 - c * c / 2 - 1e-12)
    # 8. cos x <= 1-x^2/2+x^4/24 on [-1,1]
    c1 = random.uniform(-1, 1)
    chk("cos<=1-x^2/2+x^4/24",
        math.cos(c1) <= 1 - c1 ** 2 / 2 + c1 ** 4 / 24 + 1e-12)

    # 9. Bernoulli (1+x)^n >= 1+nx
    bern = random.uniform(-0.999, 5)
    for n in (2, 3, 7, 20):
        chk("bernoulli", (1 + bern) ** n >= 1 + n * bern - 1e-9)

    # 10. Young: ab <= a^p/p + b^q/q
    p = random.uniform(1.1, 6)
    q = p / (p - 1)
    chk("young", a * b <= a ** p / p + b ** q / q + 1e-9)

    # 11. Cauchy-Schwarz
    n = 5
    u = [random.uniform(-5, 5) for _ in range(n)]
    v = [random.uniform(-5, 5) for _ in range(n)]
    lhs = sum(x * y for x, y in zip(u, v)) ** 2
    rhs = sum(x * x for x in u) * sum(y * y for y in v)
    chk("cauchy", lhs <= rhs + 1e-9)

    # 12. Titu
    aa = [random.uniform(0.1, 5) for _ in range(n)]
    bb = [random.uniform(0.1, 5) for _ in range(n)]
    chk("titu", sum(x * x / y for x, y in zip(bb, aa)) >=
        sum(bb) ** 2 / sum(aa) - 1e-9)

    # 13. AM-GM n 元
    vals = [random.uniform(0.05, 20) for _ in range(n)]
    chk("amgm-n", math.prod(vals) ** (1 / n) <= sum(vals) / n + 1e-9)

    # 14. Hermite-Hadamard (e^x, 凸)
    lo, hi = sorted([random.uniform(-3, 3), random.uniform(-3, 3)])
    if hi - lo > 1e-3:
        mid = (lo + hi) / 2
        integ = (math.exp(hi) - math.exp(lo)) / (hi - lo)
        chk("HH-left", math.exp(mid) <= integ + 1e-9)
        chk("HH-right", integ <= (math.exp(lo) + math.exp(hi)) / 2 + 1e-9)

    # 15. 排序不等式
    a2 = sorted([random.uniform(-5, 5) for _ in range(n)])
    b2 = sorted([random.uniform(-5, 5) for _ in range(n)])
    same = sum(x * y for x, y in zip(a2, b2))
    rev = sum(x * y for x, y in zip(a2, reversed(b2)))
    perm = a2[:]
    random.shuffle(b2)
    chk("rearrange", rev <= sum(x * y for x, y in zip(a2, b2)) + 1e-9)
    chk("rearrange2", same >= rev - 1e-9)

# 16. 裂项：sum_{k=1}^n 1/k^2 <= 2 - 1/n
for n in (1, 2, 5, 50, 500):
    S = sum(1 / k ** 2 for k in range(1, n + 1))
    chk("裂项上界", S <= 2 - 1 / n + 1e-12)

# 17. H_n 与 ln n
for n in (1, 10, 100, 10000):
    Hn = sum(1 / k for k in range(1, n + 1))
    chk("Hn>=ln(n+1)", Hn >= math.log(n + 1) - 1e-12)
    chk("Hn<=1+ln n", Hn <= 1 + math.log(n) + 1e-12)

# 18. 例题：x_n = 1 + 1/n
for n in (1, 7, 99):
    xn = math.prod(1 + 1 / k for k in range(1, n + 1)) / n
    chk("x_n=1+1/n", abs(xn - (1 + 1 / n)) < 1e-9)

# 19. 例题：n - S_n -> ln2/2
big = 200000
S = sum(k * math.log1p(1 / k) for k in range(big + 1, 2 * big + 1))
chk("n-Sn -> ln2/2", abs((big - S) - math.log(2) / 2) < 1e-4)

# 20. Chebyshev 反例
A_ = [1, 3]
B_ = [3, 1]
chk("chebyshev反例", sum(x * y for x, y in zip(A_, B_)) <
    sum(A_) * sum(B_) / len(A_))

# 21. 递推 a_{n+1}=sqrt(2+a_n) -> 2
an = math.sqrt(2)
seq_ok = True
for _ in range(200):
    an2 = math.sqrt(2 + an)
    if an2 < an - 1e-15:
        seq_ok = False
    an = an2
chk("递推单调", seq_ok)
chk("递推极限", abs(an - 2) < 1e-9)

# 22. (1+1/n)^n < 3
for n in (2, 3, 10, 100):
    chk("e界", (1 + 1 / n) ** n < 3)

# 23. n 次根号 n -> 1，且 h_n <= sqrt(2/(n-1))
for n in (2, 10, 1000):
    h = n ** (1 / n) - 1
    chk("h_n界", h <= math.sqrt(2 / (n - 1)) + 1e-12)

print(f"通过检查: {ok}")
if bad:
    from collections import Counter
    print("失败项:", Counter(bad))
else:
    print("全部通过 ✔")
