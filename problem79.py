from itertools import permutations

def solve():
    with open('inputs/p079_keylog.txt') as f:
        lines = sorted(set(f.read().split('\n')[:-1]))
    digits = set()
    for line in lines:
        digits.update(map(int, line))
    for perm in permutations(digits):
        for line in lines:
            if not (perm.index(int(line[0])) < perm.index(int(line[1])) < perm.index(int(line[2]))):
                break
        else:
            retval = 0
            for k in perm:
                retval *= 10
                retval += k
            return retval