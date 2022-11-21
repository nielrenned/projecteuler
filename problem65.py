from fractions import Fraction as F

def convergent_e(n, k=0):
    c = 1
    if k % 3 == 1:
        c = 2*(k+2)//3
    if n == 0:
        if k == 0:
            return 2
        else:
            return 0
    if k == 0:
        return F(2) + F(1, c + convergent_e(n-1, k+1))
    else:
        return F(1, c + convergent_e(n-1, k+1))

def solve():
    f = convergent_e(99)
    return sum(map(int, str(f.numerator)))