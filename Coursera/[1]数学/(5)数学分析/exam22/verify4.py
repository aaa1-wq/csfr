# -*- coding: utf-8 -*-
"""Final verification: determinants by explicit cofactor expansion, solving by integer-preserving elimination."""
import itertools


def det3(M):
    a, b, c = M[0]
    d, e, f = M[1]
    g, h, i = M[2]
    return a * (e * i - f * h) - b * (d * i - f * g) + c * (d * h - e * g)


print("=" * 72)
print("Q2  (lam-2)x1 + x2 + x3 = x1 + (lam-2)x2 + x3 = x1 + x2 + (lam-2)x3 = 1")
print("=" * 72)
for lf in [3, 5, 0, -1, 2, 4]:
    lam = lf
    b = lam - 2
    A = [[b, 1, 1], [1, b, 1], [1, 1, b]]
    detA = det3(A)
    # Cramer determinant for x1 (replace col 1 by (1,1,1))
    D1 = det3([[1, 1, 1], [1, b, 1], [1, 1, b]])
    D2 = det3([[b, 1, 1], [1, 1, 1], [1, 1, b]])
    D3 = det3([[b, 1, 1], [1, b, 1], [1, 1, 1]])
    print("lam", lam, " det =", detA, " D1,D2,D3 =", D1, D2, D3,
          " x =", (D1 / detA if detA else None), (D2 / detA if detA else None), (D3 / detA if detA else None))

print()
print("closed form check: x_i = 1/(lam^2+lam-2), T = (lam+2)(lam-1)")
for lam in [3, 5, 0, -1, 2, 4, -3]:
    T1 = lam * lam + lam - 2
    T2 = (lam + 2) * (lam - 1)
    c = 1 / T1
    b = lam - 2
    res = b * c + c + c
    print("lam", lam, "T", T1, T2, "c", round(c, 6), " (b+2)c =", round((b + 2) * c, 6),
          "residual", round(res, 6))

print()
print("=" * 72)
print("Q4  A=[[1,0,-1],[0,0,0],[0,0,0]] ; point (1,-1,1)")
print("=" * 72)
A = [[1, 0, -1], [0, 0, 0], [0, 0, 0]]
p = [1, -1, 1]
Ap = [sum(A[i][j] * p[j] for j in range(3)) for i in range(3)]
print("A p =", Ap, "=> the point is already in N(A); distance = 0")
n = [1, 0, -1]
print("N(A) = {x : x1 - x3 = 0} = plane with normal", n, "; n.p =", sum(n[i] * p[i] for i in range(3)))

print()
print("=" * 72)
print("Q3  independence of {1, 1+x, (1+x)^2}: det of coordinate matrix")
print("=" * 72)
C = [[1, 1, 1], [0, 1, 2], [0, 0, 1]]
print("det =", det3(C), " (nonzero -> independent, and 3 vectors in dim-3 space -> basis)")
print("inverse of C (cofactor / adjugate):")
# adjugate for upper triangular
import copy
M = copy.deepcopy(C)
n = 3
aug = [row + [1 if i == j else 0 for j in range(3)] for i, row in enumerate(M)]
# Gauss-Jordan with plain ints/floats
for c in range(3):
    piv = aug[c][c]
    aug[c] = [v / piv for v in aug[c]]
    for r in range(3):
        if r != c and aug[r][c] != 0:
            f = aug[r][c]
            aug[r] = [a - f * bb for a, bb in zip(aug[r], aug[c])]
inv = [row[3:] for row in aug]
print("C^-1 =", [[round(v, 6) for v in row] for row in inv])
print("C . C^-1 =", [[round(sum(C[i][k] * inv[k][j] for k in range(3)), 6) for j in range(3)] for i in range(3)])

print()
print("coefficients of 2+4x+6x^2 in {1, 1+x, (1+x)^2}:")
# a*1 + b*(1+x) + c*(1+2x+x^2) = 2 + 4x + 6x^2
# constant: a+b+c=2 ; x: b+2c=4 ; x^2: c=6
K3 = 6
K2 = 4 - 2 * K3
K1 = 2 - K2 - K3
print("  k1, k2, k3 =", K1, K2, K3)
print("  expand: const", K1 + K2 + K3, " x", K2 + 2 * K3, " x^2", K3)

print()
print("=" * 72)
print("Q5  N(A^T), N(B^T), A=[[1,0],[0,0]], B=[[0,1],[0,0]]")
print("=" * 72)
print("A^T = [[1,0],[0,0]] -> x1 = 0 -> N = {(0,t)}")
print("B^T = [[0,0],[1,0]] -> x1 = 0 -> N = {(0,t)}")
print("sum = {(0,t)}, dim = 1")

print()
print("=" * 72)
print("Q7  rank(A^T A) = rank(A A^T): integers, explicit rank via minors")
print("=" * 72)


def rank_int(M):
    """rank over Q by fraction-free Gaussian elimination."""
    from fractions import Fraction as F
    R = [[F(v) for v in row] for row in M]
    rows, cols = len(R), len(R[0])
    r = 0
    for c in range(cols):
        piv = next((i for i in range(r, rows) if R[i][c] != 0), None)
        if piv is None:
            continue
        R[r], R[piv] = R[piv], R[r]
        for i in range(rows):
            if i != r and R[i][c] != 0:
                f = R[i][c] / R[r][c]
                R[i] = [a - f * b for a, b in zip(R[i], R[r])]
        r += 1
    return r


def mm(X, Y):
    return [[sum(X[i][k] * Y[k][j] for k in range(len(Y))) for j in range(len(Y[0]))] for i in range(len(X))]


def tr(X):
    return [list(r) for r in zip(*X)]


for X in ([[1, 0, -1], [0, 0, 0], [0, 0, 0]],
          [[1, 0, 0], [0, 1, 0], [0, 0, 1]],
          [[1, 0, 1], [0, 1, 2], [0, 0, 0]],
          [[1, 2], [3, 4]],
          [[1, 2, 3], [2, 4, 6]],
          [[0, 0], [0, 0]]):
    XT = tr(X)
    print("A =", X, " rankA =", rank_int(X), " rank(AtA) =", rank_int(mm(XT, X)),
          " rank(AAt) =", rank_int(mm(X, XT)))
