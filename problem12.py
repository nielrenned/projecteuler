from utilities import prime_factorization, prime_seive, powerset, prod, sum_naturals
import math

def solve():
    primes = prime_seive(2**16) # Since we can usually use 32-bit #'s 2**16 is a fine upper bound
    k = 1
    while True:
        n = sum_naturals(k)
        factorization = prime_factorization(n, primes)
        divisors = set(map(prod, powerset(factorization)))
        if len(divisors) >= 500:
            return n
        k += 1