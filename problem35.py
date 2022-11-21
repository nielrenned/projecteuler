from utilities import prime_seive

N = 1000000
primes = prime_seive(N)
primes_set = set(primes)

def rotate_string(s):
    if len(s) == 1:
        return s
    s = s[1:] + s[0]
    return s

def get_all_rotations(s):
    l = []
    for i in range(len(str(s))):
        l.append(s)
        s = rotate_string(s)
    return l

def solve():
    count = 0
    for i in range(2, N):
        for n in get_all_rotations(str(i)):
            if int(n) not in primes_set:
                break
        else:
            count += 1
    return count