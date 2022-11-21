from utilities import prime_seive

N = 1000000

def solve():
    primes = prime_seive(N)
    primes_set = set(primes)
    longest, p = 0,0
    for i in range(len(primes)-1):
        l = 2
        s = primes[i] + primes[i+1]
        while i+l < len(primes) and s < N:
            if s in primes_set and l > longest:
                longest = l
                p = s
            s += primes[i+l]
            l += 1
    return p