from itertools import combinations

squares = [[0, 1], [0, 4], [0, 9], [1, 6], [2, 5], [3, 6], [4, 9], [6, 4], [8, 1]]

def can_represent_squares(l1, l2):
    d1 = set(l1)
    d2 = set(l2)
    if 6 in d1:
        d1.add(9)
    if 9 in d1:
        d1.add(6)
    if 6 in d2:
        d2.add(9)
    if 9 in d2:
        d2.add(6)
    for c1, c2 in squares:
        if not ((c1 in d1 and c2 in d2) or (c1 in d2 and c2 in d1)):
            return False
    return True

def solve():
    digits = [0,1,2,3,4,5,6,7,8,9]
    total = 0
    for d1 in combinations(digits, 6):
        for d2 in combinations(digits, 6):
            if can_represent_squares(d1, d2):
                total += 1
    return total/2 # We count each pair of combinations twice (d1, d2) and (d2, d1)