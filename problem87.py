from utilities import prime_seive

MIL_50 = 50000000
MIL_50_2root = int(MIL_50**(1/2.0)) + 1
MIL_50_3root = int(MIL_50**(1/3.0)) + 1
MIL_50_4root = int(MIL_50**(1/4.0)) + 1

def solve():
    primes = prime_seive(10000)
    primes1 = list(filter(lambda x: x <= MIL_50_2root, primes))
    primes2 = list(filter(lambda x: x <= MIL_50_3root, primes))
    primes3 = list(filter(lambda x: x <= MIL_50_4root, primes))
    print(len(primes1), len(primes2), len(primes3))
    nums = set()
    for p1 in primes1:
        for p2 in primes2:
            for p3 in primes3:
                n = p1**2 + p2**3 + p3**4
                if n < MIL_50:
                    nums.add(n)
    return len(nums)