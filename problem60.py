from utilities import prime_seive, is_prime
from itertools import combinations

def get_concats(x, y):
    s1 = str(x)
    s2 = str(y)
    i1 = int(s1 + s2)
    i2 = int(s2 + s1)
    return (i1, i2)

def check_list(l):
    for x in l:
        for y in l:
            if x == y:
                continue
            i1, i2 = get_concats(x,y)
            if not is_prime(i1) or not is_prime(i2):
                return False
    return True

def solve():
    primes = prime_seive(10000)
    l = len(primes)
    #print("primes gen'd")
    for i1 in range(l):
        p1 = primes[i1]
        if p1 == 2 or p1 == 5:
            continue
        for i2 in range(i1 + 1, l):
            p2 = primes[i2]
            n1, n2 = get_concats(p1, p2)
            if not is_prime(n1) or not is_prime(n2):
                #print('with {} skipping {}'.format(p1, p2))
                continue
            for i3 in range(i2 + 1, l):
                p3 = primes[i3]
                if not check_list((p1, p2, p3)):
                    #print('with {},{} skipping {}'.format(p1, p2, p3))
                    continue
                for i4 in range(i3 + 1, l):
                    p4 = primes[i4]
                    if not check_list((p1, p2, p3, p4)):
                        continue
                    for i5 in range(i4 + 1, l):
                        p5 = primes[i5]
                        if check_list((p1, p2, p3, p4, p5)):
                            return (p1 + p2 + p3 + p4 + p5)