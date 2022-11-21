from utilities import gcd
from collections import defaultdict
import math

def solve():
    triples = set()
    for m in range(2, 1100):
        for n in range(1, m):
            if gcd(m,n) != 1:
                continue
            a = m*m - n*n
            b = 2*m*n
            c = m*m + n*n
            triples.add(tuple(sorted((a,b,c))))
            k = 2
            while sum((k*a, k*b, k*c)) <= 1500000:
                triples.add(tuple(sorted((k*a, k*b, k*c))))
                k += 1
    num_solns = defaultdict(int)
    for t in triples:
        s = sum(t)
        num_solns[s] += 1
    count = 0
    for L in num_solns:
        if L <= 1500000 and num_solns[L] == 1:
            count += 1
    return count