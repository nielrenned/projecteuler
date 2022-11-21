from utilities import prime_seive

def get_truncations(s):
    l = [s]
    for i in range(1,len(s)):
        l.append(s[i:])
        l.append(s[:-i])
    return l

def solve():
    total = 0
    primes = prime_seive(1000000)
    primes_set = set(primes)
    for p in primes:
        if p < 10:
            continue
        for n in get_truncations(str(p)):
            if int(n) not in primes_set:
                break
        else:
            total += p
    return total