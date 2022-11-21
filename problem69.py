from utilities import prime_seive, totient

def solve():
    primes = prime_seive(1000)
    best_n, best_ratio = 0, 0
    for n in range(2, 1000000+1):
        phi = totient(n, primes)
        ratio = float(n)/phi
        if ratio > best_ratio:
            best_n = n
            best_ratio = ratio
    return best_n