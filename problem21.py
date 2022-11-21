from utilities import prime_seive, divisors

primes = prime_seive(101)

def d(n):
    return sum(divisors(n,primes))-n

def solve():
    total = 0
    for a in range(2,10000):
        b = d(a)
        if d(b) == a and b != a:
            total += a
    return total