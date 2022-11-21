from utilities import continued_frac_root, is_square
from fractions import Fraction as F

def continued_frac_conv(frac, n, k=0):
    c = frac[1][k%len(frac[1])]
    if n == 0:
        if k == 0:
            return frac[0]
        else:
            return 0
    if k == 0:
        return F(frac[0]) + F(1, c + continued_frac_conv(frac, n-1, k+1))
    else:
        return F(1, c + continued_frac_conv(frac, n-1, k+1))

def solve_pells_eq(D):
    frac = continued_frac_root(D)
    n = 1
    while True:
        f = continued_frac_conv(frac, n)
        h, k = f.numerator, f.denominator
        if h*h - D*k*k == 1:
            return (h, k)
        n += 1

def solve():
    highest_x, best_d = 0,0
    for d in range(2, 1000 + 1):
        if is_square(d):
            continue
        x, _ = solve_pells_eq(d)
        if x > highest_x:
            highest_x, best_d = x, d
    return best_d