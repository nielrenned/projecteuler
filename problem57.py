from fractions import Fraction as F
import sys

def root2frac(n, first=True):
    if n == 0:
        return 0
    elif first == True:
        return F(1) + F(1, 2 + root2frac(n-1, False))
    else:
        return F(1, 2 + root2frac(n-1, False))

def solve():
    sys.setrecursionlimit(2000)
    count = 0
    for i in range(1,1000 + 1):
        f = root2frac(i)
        n = f.numerator
        d = f.denominator
        if len(str(n)) > len(str(d)):
            count += 1
    return count