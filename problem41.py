from utilities import is_prime
from itertools import permutations

def solve():
    highest = 0
    for n in range(2, 7 + 1):
        for t in permutations(range(1, n+1)):
            k = 0
            for d in t:
                k *= 10
                k += int(d)
            if is_prime(k) and k > highest:
                highest = k
    return highest