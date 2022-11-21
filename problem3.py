from utilities import *
import math

#N = 13195
N = 600851475143

def solve():
    primes = prime_seive(int(math.sqrt(N))+1)
    highest = 0
    for p in primes:
        if N % p == 0 and p > highest:
            highest = p
    return highest