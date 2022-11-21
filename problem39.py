from utilities import gcd
from collections import defaultdict

def solve():
    triples = set()
    for m in range(2, 33):
        for n in range(1, m):
            if gcd(m,n) != 1:
                continue
            a = m*m - n*n
            b = 2*m*n
            c = m*m + n*n
            triples.add((a,b,c))
            k = 2
            while sum((k*a, k*b, k*c)) <= 1000:
                triples.add((k*a, k*b, k*c))
                k += 1
    num_solns = defaultdict(int)
    for t in triples:
        s = sum(t)
        num_solns[s] += 1
    highest, best_k = 0,0
    for k in num_solns:
        if num_solns[k] > highest:
            highest = num_solns[k]
            best_k = k
    return best_k