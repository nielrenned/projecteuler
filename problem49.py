from utilities import prime_seive

def is_permutation(a, b):
    if sorted(str(a)) == sorted(str(b)):
        return True
    return False

def solve():
    primes = sorted(filter(lambda x: x >= 1000, prime_seive(10000)))
    for p1 in primes:
        for p2 in primes:
            if p2 <= p1 or not is_permutation(p1, p2):
                continue
            delta = p2 - p1
            if (p2 + delta) in primes and is_permutation(p1, p2+delta) and p1 != 1487:
                return int(str(p1) + str(p2) + str(p2 + delta))