from utilities import prime_seive

primes = set(prime_seive(10000))
bs = prime_seive(1000)

def test(a,b):
    n = 0
    while (n*n + a*n + b) in primes:
        n += 1
    return n

def solve():
    highest, best_a, best_b = 0,0,0
    for a in range(-1000, 1001):
        for b in bs:
            l = test(a,b)
            if l > highest:
                highest = l
                best_a, best_b = a,b
            l = test(a,-b)
            if l > highest:
                highest = l
                best_a, best_b = a,-b
    #print(highest, best_a, best_b)
    return best_a*best_b