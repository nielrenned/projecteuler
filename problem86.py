import math
from utilities import gcd


def solve():
    M = 100
    unique_side_lengths = set()
    for m in range(1, int((math.sqrt(4*M +1)+1)/2)+1):
        for n in range(1, m):
            if gcd(m, n) != 1:
                continue
            a0 = m*m - n*n
            b0 = 2*m*n
            c0 = m*m + n*n
            k = 1
            while k*a0 <= M and k*b0 <= M:
                a = k*a0
                b = k*b0
                s1 = a
                for s2 in range(1, b):
                    s3 = b - s2
                    if s1 <= M and s2 <= M and s3 <= M:
                        unique_side_lengths.add(frozenset((s1, s2, s3)))
                k += 1
        
    return len(unique_side_lengths)