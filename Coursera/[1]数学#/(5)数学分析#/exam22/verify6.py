# -*- coding: utf-8 -*-
"""Q3 numbers via integer arithmetic only."""

# basis B1 = {1, 1+x, (1+x)^2};  coordinates in E = {1, x, x^2} are the columns of C
C = [[1, 1, 1],
     [0, 1, 2],
     [0, 0, 1]]

# determinant of upper-triangular C = product of the diagonal
detC = C[0][0] * C[1][1] * C[2][2]
print("det C =", detC, "(=1, so B1 is a basis of P^2)")

# inverse of an upper-triangular matrix: solve C y = e_i by back substitution
def solve_upper(C, rhs):
    n = len(C)
    y = [0] * n
    for i in range(n - 1, -1, -1):
        s = rhs[i]
        for j in range(i + 1, n):
            s -= C[i][j] * y[j]
        y[i] = s // C[i][i] if s % C[i][i] == 0 else s / C[i][i]
    return y

cols = []
for i in range(3):
    e = [1 if j == i else 0 for j in range(3)]
    cols.append(solve_upper(C, e))
Cinv = [[cols[j][i] for j in range(3)] for i in range(3)]
print("C^-1 =", Cinv)

# verify C * Cinv = I with exact integers
prod = [[sum(C[i][k] * Cinv[k][j] for k in range(3)) for j in range(3)] for i in range(3)]
print("C . C^-1 =", prod, " -> identity:", prod == [[1, 0, 0], [0, 1, 0], [0, 0, 1]])

# coefficients of p = 2 + 4x + 6x^2 in B1:  a + b(1+x) + c(1+2x+x^2)
# c = 6 ; b = 4 - 2c ; a = 2 - b - c
c3 = 6
c2 = 4 - 2 * c3
c1 = 2 - c2 - c3
print("k = (k1, k2, k3) =", (c1, c2, c3))
print("re-expand: 1:", c1 + c2 + c3, " x:", c2 + 2 * c3, " x^2:", c3)

# also via Cinv applied to (2,4,6)
v = [2, 4, 6]
res = [sum(Cinv[i][j] * v[j] for j in range(3)) for i in range(3)]
print("Cinv * (2,4,6) =", res)
