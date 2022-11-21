from utilities import totient, prime_seive

def solve():
    primes = prime_seive(1000)
    count = 0
    for d in range(2, 1000000 + 1):
        count += totient(d, primes)
    return count