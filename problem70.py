from utilities import prime_seive, totient, is_permutation

def solve():
    primes = prime_seive(int(10**(3.5))+1)
    best_n, best_ratio = 1, 100000000
    for n in range(2, 10000000):
        phi = totient(n, primes)
        if is_permutation(n, phi) and float(n)/phi < best_ratio:
            best_n = n
            best_ratio = float(n)/phi
    return best_n