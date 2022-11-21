from utilities import prime_seive, prime_factorization, prod, powerset
from itertools import combinations
from math import sqrt

def non_trivial_factorizations(n, primes=None):
    if n in non_trivial_factorizations.computed:
        return non_trivial_factorizations.computed[n]
    pf = prime_factorization(n, primes)
    if len(pf) == 1:
        return set()
    if len(pf) == 2:
        return set([(n/pf[0], n/pf[1])])
    low_divs = filter(lambda x: x <= sqrt(n), map(prod, powerset(pf)))
    facts = set()
    for d in low_divs:
        if d == 1:
            continue
        facts.add((d, n/d))
        for f in non_trivial_factorizations(n/d, primes):
            facts.add(tuple(sorted((d, ) + f)))
    non_trivial_factorizations.computed[n] = facts
    return facts

non_trivial_factorizations.computed = {}

def find_min_product_sum(k, primes=None):
    n = k # The minimal prod-sum numbers is always > k (idk why), 
    #       and even more interesting, appears to be very close to k (again, idk why)
    while True:
        for f in non_trivial_factorizations(n, primes):
            if n - sum(f) + len(f) == k:
                return n
        n += 1

def solve():
    primes = prime_seive(10000)
    min_nums = set()
    max_n = 0
    for k in range(2, 12000+1):
        if k % 100 == 0:
            print(k)
        n = find_min_product_sum(k, primes)
        if n < k:
            print(k, n)
        min_nums.add(n)
    return sum(min_nums)
                    