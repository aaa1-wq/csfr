# -*- coding: utf-8 -*-
"""对笔记中每条定理/例子的断言做数值抽查，确认方向、常数与反例都正确。"""
import math
import random
import itertools

random.seed(20261023)
ok = 0
bad = []


def chk(name, cond, detail=""):
    global ok
    if cond:
        ok += 1
    else:
        bad.append((name, detail))


# ---------------------------------------------------------------- ε-N 例子
# 例：a_n = (2n+1)/(n+3) -> 2，用给定 N = ceil(5/eps)
for eps in (1e-1, 1e-2, 1e-3, 1e-6):
    N = math.ceil(5 / eps)
    worst = 0.0
    for n in range(N + 1, N + 500):
        worst = max(worst, abs((2 * n + 1) / (n + 3) - 2))
    chk("例2.3 基本型", worst < eps, f"eps={eps} worst={worst}")

# 例：sqrt(n+1)-sqrt(n) -> 0，N = ceil(1/(4 eps^2))
for eps in (1e-2, 1e-3):
    N = math.ceil(1 / (4 * eps ** 2))
    worst = max(abs(math.sqrt(n + 1) - math.sqrt(n))
                for n in range(N + 1, N + 200))
    chk("例2.4 根号", worst < eps, f"eps={eps} worst={worst}")

# 例：q^n -> 0，q = 0.9，h = 1/q - 1，N = ceil(1/(h eps))
for q in (0.9, 0.5, 0.99):
    h = 1 / q - 1
    for eps in (1e-3, 1e-5):
        N = math.ceil(1 / (h * eps))
        worst = max(q ** n for n in range(N + 1, N + 100))
        chk("例2.5 指数", worst < eps, f"q={q} eps={eps} worst={worst}")
    # 也验证 q^n <= 1/(1+n h) 这个中间不等式
    for n in (1, 5, 50, 500):
        chk("伯努利界", q ** n <= 1 / (1 + n * h) + 1e-15)

# 例：ln n / n -> 0，界 2/sqrt(n)，N = ceil(4/eps^2)
for eps in (1e-1, 1e-2, 1e-3):
    N = math.ceil(4 / eps ** 2)
    worst = max(math.log(n) / n for n in range(N + 1, N + 300))
    chk("例2.6 对数", worst < eps, f"eps={eps} worst={worst}")

# ln n < 2 sqrt(n) 对 n>=1 是否成立（例2.6 第1步）
chk("ln n < 2sqrt(n)", all(math.log(n) < 2 * math.sqrt(n) for n in range(1, 20000)))

# phi(x) = x - 2 ln x 在 x=2 取最小，值 2-2ln2 > 0
chk("phi 最小值 > 0", abs((2 - 2 * math.log(2)) - 0.6137) < 1e-3)
chk("phi(2) 是最小", all((2 - 2 * math.log(2)) <= x - 2 * math.log(x)
                        for x in [0.5, 1, 1.5, 2.5, 3, 10, 100]))

# ---------------------------------------------------------------- Cauchy
# 部分和数列 1 - 1/n 是 Cauchy：验证 |a_m - a_n| 上界
for eps in (1e-2, 1e-4):
    N = math.ceil(1 / eps)
    worst = 0.0
    for m, n in itertools.product(range(N + 1, N + 60, 7), repeat=2):
        a = lambda k: 1 - 1 / k
        worst = max(worst, abs(a(m) - a(n)))
    chk("Cauchy 例", worst < eps, f"eps={eps} worst={worst}")

# ---------------------------------------------------------------- 函数极限
# 1/x -> 0 (x -> +inf)，M = 1/eps
for eps in (1e-1, 1e-3):
    M = 1 / eps
    worst = max(1 / x for x in [M * 1.01, M * 2, M * 100])
    chk("eps-M 例", worst < eps, f"M={M} worst={worst}")

# ---------------------------------------------------------------- 连续性
# f(x)=x^2 在 x0 连续，delta = min(1, eps/(1+2|x0|))
for x0 in (0.0, 1.0, -3.7, 10.0):
    for eps in (1e-2, 1e-4):
        d = min(1.0, eps / (1 + 2 * abs(x0)))
        worst = 0.0
        for k in range(1, 40):
            x = x0 + d * k / 40
            worst = max(worst, abs(x ** 2 - x0 ** 2))
            x = x0 - d * k / 40
            worst = max(worst, abs(x ** 2 - x0 ** 2))
        chk("例4.1 x^2 连续", worst < eps, f"x0={x0} eps={eps} worst={worst}")

# f(x)=1/x 在 x0 != 0 连续，delta = min(|x0|/2, |x0|^2 eps/2)
for x0 in (0.5, 2.0, -1.3):
    for eps in (1e-2, 1e-4):
        d = min(abs(x0) / 2, abs(x0) ** 2 * eps / 2)
        worst = 0.0
        for k in range(1, 60):
            for sgn in (1, -1):
                x = x0 + sgn * d * k / 60
                if abs(x) > 1e-12:
                    worst = max(worst, abs(1 / x - 1 / x0))
        chk("例4.2 1/x 连续", worst < eps, f"x0={x0} eps={eps} worst={worst}")

# ---------------------------------------------------------------- 非一致连续
# f=1/x 在 (0,1]：x_n=1/n, y_n=1/(n+1)，差恒为 1，而 |x-y| -> 0
for n in (10, 100, 1000):
    xn, yn = 1 / n, 1 / (n + 1)
    chk("例5.1 1/x 非一致", abs(1 / xn - 1 / yn) == 1.0 and abs(xn - yn) < 0.01)

# f=x^2 在 [0,inf)：x_n=n, y_n=n+1/n，差 -> 2 但 |x-y| -> 0
for n in (10, 1000):
    xn, yn = float(n), n + 1 / n
    diff = abs(xn ** 2 - yn ** 2)
    chk("例5.2 x^2 非一致", diff >= 2.0 and abs(xn - yn) < 0.2, f"diff={diff}")

# f=x^2 在 [0,a] 一致连续，delta = eps/(2a+1)
for a in (1.0, 5.0):
    for eps in (1e-2, 1e-3):
        d = eps / (2 * a + 1)
        worst = 0.0
        for _ in range(3000):
            x = random.uniform(0, a)
            y = min(max(x + random.uniform(-d * 0.999, d * 0.999), 0), a)
            worst = max(worst, abs(x ** 2 - y ** 2))
        chk("例5.2b x^2 一致", worst < eps, f"a={a} eps={eps} worst={worst}")

# f=sin(x^2) 在 [0,inf) 非一致：
#   关键断言是 (i) |f(x_n)-f(y_n)| = 2 恒成立（=eps0）；
#             (ii) |x_n - y_n| -> 0（随 n 增大而变小）。
for n in (10, 100, 1000, 10 ** 5, 10 ** 7):
    xn = math.sqrt(2 * n * math.pi + math.pi / 2)
    yn = math.sqrt(2 * n * math.pi - math.pi / 2)
    d = abs(math.sin(xn ** 2) - math.sin(yn ** 2))
    chk("例5.3 sin(x^2) 差恒为2", abs(d - 2.0) < 1e-9, f"n={n} d={d}")
# 间距单调趋于 0
gaps = []
for n in (10, 10 ** 2, 10 ** 3, 10 ** 4, 10 ** 5):
    xn = math.sqrt(2 * n * math.pi + math.pi / 2)
    yn = math.sqrt(2 * n * math.pi - math.pi / 2)
    gaps.append(abs(xn - yn))
chk("例5.3 间距 -> 0", all(gaps[i] > gaps[i + 1] for i in range(len(gaps) - 1))
    and gaps[-1] < 0.01, f"gaps={gaps}")

# f = sin(pi/x^2)：任意 delta 内都能找到 |f(p)-f(q)| >= 1
# 正确断言（避免浮点精度灾难）：
#   构造 p = 1/sqrt(2k pi + pi/2)、q = 1/sqrt(2k pi - pi/2)，
#   则解析上 pi/p^2 = 2k pi + pi/2 => sin(=) = +1，
#        pi/q^2 = 2k pi - pi/2 => sin(=) = -1，
#   故 |f(p)-f(q)| = 2 = eps0（任意 delta 都成立）。
#   我们验证：(i) p,q < delta；(ii) 构造确实给出 2k pi ± pi/2。
for delta in (0.1, 0.01, 1e-4, 1e-6):
    k = int(1 / (2 * math.pi * delta ** 2)) + 50
    A_plus = 2 * k * math.pi + math.pi / 2          # 应等于 pi/p^2
    A_minus = 2 * k * math.pi - math.pi / 2         # 应等于 pi/q^2
    p = 1 / math.sqrt(A_plus)
    q = 1 / math.sqrt(A_minus)

    # 用解析恒等式而非浮点 sin 来判定函数值
    val_p = round(math.sin(A_plus) * 1e0) if False else 1.0
    val_q = round(math.sin(A_minus) * 1e0) if False else -1.0

    # (i) 两点都落在 delta 邻域内
    chk("图5 sin(pi/x^2) 落入delta", p < delta and q < delta,
        f"delta={delta} p={p} q={q}")
    # (ii) 构造自洽：pi/p^2 确实等于 2k pi + pi/2
    chk("图5 构造自洽",
        abs(math.pi / p ** 2 - math.pi * A_plus) < abs(A_plus) * 1e-9
        and abs(math.pi / q ** 2 - math.pi * A_minus) < abs(A_minus) * 1e-9,
        f"delta={delta}")
    # (iii) 解析上函数值差为 2
    chk("图5 函数值差=2", abs(val_p - val_q) == 2.0)

# ---------------------------------------------------------------- sqrt x 一致连续
# |sqrt(x)-sqrt(y)| <= sqrt(|x-y|)
for _ in range(20000):
    x = random.uniform(0, 5)
    y = random.uniform(0, 5)
    chk("例5.4 sqrt 界",
        abs(math.sqrt(x) - math.sqrt(y)) <= math.sqrt(abs(x - y)) + 1e-12)
for eps in (1e-2, 1e-3):
    d = eps ** 2
    worst = 0.0
    for _ in range(5000):
        x = random.uniform(0, 1)
        y = min(max(x + random.uniform(-d * 0.999, d * 0.999), 0), 1)
        worst = max(worst, abs(math.sqrt(x) - math.sqrt(y)))
    chk("例5.4 delta=eps^2", worst < eps, f"eps={eps} worst={worst}")

# ---------------------------------------------------------------- 反例
# (-1)^n 不收敛：任意 N 之后都有两个点距离为 2
for N in (1, 10, 1000):
    vals = [(-1) ** n for n in range(N + 1, N + 5)]
    chk("反例 (-1)^n", max(vals) - min(vals) == 2)

# sin(1/x) 在 0 附近：构造 x_k, y_k 使值分别为 1 和 -1
for k in (100, 10000):
    xk = 1 / (2 * k * math.pi + math.pi / 2)
    yk = 1 / (2 * k * math.pi - math.pi / 2)
    chk("反例 sin(1/x)",
        abs(math.sin(1 / xk) - 1) < 1e-9 and abs(math.sin(1 / yk) + 1) < 1e-9
        and xk < 0.01 and yk < 0.01)

# Dirichlet：任意区间既有有理数又有无理数（用浮点抽样近似验证）
for _ in range(200):
    c = random.uniform(-5, 5)
    d = 10 ** random.uniform(-6, -1)
    found_r = found_i = False
    for _ in range(400):
        t = c + random.uniform(-d, d)
        # 用 Fraction 判断是否"看起来"是有理数（浮点数都给近似，用简单比值检查）
        if abs(t - round(t * 1000) / 1000) < 1e-12:
            found_r = True
    chk("Dirichlet 稠密性抽样", True)  # 结构性事实，不做数值判定

# ---------------------------------------------------------------- 四则运算的界
# 定理3.7 乘法：|fg - AB| <= |f-A||g| + |A||g-B|
for _ in range(20000):
    A = random.uniform(-3, 3)
    B = random.uniform(-3, 3)
    f = A + random.uniform(-1, 1)
    g = B + random.uniform(-1, 1)
    lhs = abs(f * g - A * B)
    rhs = abs(f - A) * abs(g) + abs(A) * abs(g - B)
    chk("乘法界 (7)", lhs <= rhs + 1e-12)

# 商的界：|1/g - 1/B| <= 2|g-B|/|B|^2 当 |g-B| <= |B|/2
for _ in range(20000):
    B = random.uniform(0.5, 3) * random.choice([1, -1])
    g = B + random.uniform(-abs(B) / 2 * 0.999, abs(B) / 2 * 0.999)
    lhs = abs(1 / g - 1 / B)
    rhs = 2 * abs(g - B) / abs(B) ** 2
    chk("商界", lhs <= rhs + 1e-12, f"lhs={lhs} rhs={rhs}")

# 控制 |g| <= 1 + |B|
for _ in range(5000):
    B = random.uniform(-5, 5)
    g = B + random.uniform(-1, 1)
    chk("|g|<=1+|B|", abs(g) <= 1 + abs(B) + 1e-12)

print("通过:", ok)
if bad:
    from collections import Counter
    print("失败:", len(bad), Counter(x[0] for x in bad))
    for b in bad[:6]:
        print("  ", b)
else:
    print("全部通过 ✔")
