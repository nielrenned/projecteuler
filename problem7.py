from utilities import prime_seive

def solve():
    primes = prime_seive(1000000)
    return primes[10000]