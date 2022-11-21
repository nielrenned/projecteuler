from utilities import prime_factorization, prime_seive

def solve():
    primes = prime_seive(10000)
    n = 647
    while True:
        if len(set(prime_factorization(n)))   == 4 and \
           len(set(prime_factorization(n+1))) == 4 and \
           len(set(prime_factorization(n+2))) == 4 and \
           len(set(prime_factorization(n+3))) == 4:
           return n
        n += 1