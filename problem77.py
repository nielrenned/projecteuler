from utilities import prime_partitions, prime_seive

def solve():
    primes = prime_seive(10000)
    primes_set = set(primes)
    for n in range(4, 10000):
        p = prime_partitions(n, primes)
        if p > 5000:
            return n