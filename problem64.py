from utilities import is_square, solve_quadratic, continued_frac_root
from math import sqrt

def solve():
    count = 0
    for n in range(2, 10000+1):
        if is_square(n):
            continue
        f = continued_frac_root(n)
        #print(n, f)
        if len(f[1]) % 2 == 1:
            count += 1
    return count