from utilities import prime_seive
from itertools import combinations

def solve():
    primes = prime_seive(1000000)
    primes_set = set(primes)
    num_digits = 5
    while True:
        for r in range(num_digits-2):
            for indices in combinations(range(num_digits-1), r):
                d = num_digits - r
                for n in range(10**(d-1), 10**d):
                    if (n % 10) != 1 and (n % 10) != 3 and (n % 10) != 7 and (n % 10) != 9:
                        continue
                    i_n = 0
                    s_n = str(n)
                    s = ''
                    for i in range(num_digits):
                        if i in indices:
                            s += '_'
                        else:
                            s += s_n[i_n]
                            i_n += 1
                    count = 0
                    first_digit = None
                    if 0 in indices:
                        check_digits = ('1', '2', '3', '4', '5', '6', '7', '8', '9')
                    else:
                        check_digits = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
                    for k in check_digits:
                        p = int(s.replace('_', k))
                        if p in primes_set:
                            count += 1
                            if first_digit is None:
                                first_digit = k
                    if count == 8:
                        return int(s.replace('_', first_digit))
        num_digits += 1