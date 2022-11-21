#
#       5
#        \
#         0  6
#       /   \|
#      4     1
#    / |     |
#   9  3 --- 2 -- 7
#      |
#      8

from itertools import permutations

limbs = [(5,0,1), (6,1,2), (7,2,3), (8,3,4), (9,4,0)]
#limbs = [(3,0,1), (4,1,2), (5,2,0)]

def get_valid_limb_fills(ring, n):
    remaining_nums = [i for i in range(1, len(ring)+1) if i not in ring]
    magic_sum = sum([ring[i] for i in limbs[0]])
    current_sum = sum([ring[i] for i in limbs[n]])
    indices_to_fill = [i for i in limbs[n] if ring[i] == 0]
    new_rings = []
    for perm in permutations(remaining_nums, len(indices_to_fill)):
        if current_sum + sum(perm) == magic_sum:
            new_ring = ring[:]
            for i, index in enumerate(indices_to_fill):
                new_ring[index] = perm[i]
            new_rings.append(new_ring)
    return new_rings

def describe_ring(ring):
    smallest_outer, smallest_limb_i = 10, 0
    for i,limb in enumerate(limbs):
        if ring[limb[0]] < smallest_outer:
            smallest_outer = ring[limb[0]]
            smallest_limb_i = i
    s = ''
    j = smallest_limb_i
    for _ in range(len(limbs)):
        for i in limbs[j]:
            s += str(ring[i])
        j += 1
        j %= len(limbs)
    return s

def solve():
    solns = set()
    for perm in permutations([1,2,3,4,5,6,7,8,9], 2):
        r0 = [0]*10
        r0[limbs[0][0]] = 10
        r0[limbs[0][1]] = perm[0]
        r0[limbs[0][2]] = perm[1]
        for r1 in get_valid_limb_fills(r0, 1):
            for r2 in get_valid_limb_fills(r1, 2):
                for r3 in get_valid_limb_fills(r2, 3):
                    for r4 in get_valid_limb_fills(r3, 4):
                        solns.add(describe_ring(r4))
    return int(sorted(solns)[-1])