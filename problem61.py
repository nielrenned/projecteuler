from utilities import triangle, is_square, is_pentagonal, is_hexagonal, is_heptagonal, is_octagonal
from itertools import permutations

def find_nums(n, func):
    first_digits = n%100
    if first_digits < 10:
        return []
    nums = []
    for m in range(first_digits*100, (first_digits+1)*100):
        if func(m):
            nums.append(m)
    return nums

def solve():
    nums = []
    n = 1
    k = triangle(n)
    while k < 10000:
        if k >= 1000:
            nums.append(k)
        n += 1
        k = triangle(n)
    for perm in permutations([is_square, is_pentagonal, is_hexagonal, is_heptagonal, is_octagonal]):
        for m in nums:
            f1, f2, f3, f4, f5 = perm
            for n1 in find_nums(m, f1):
                for n2 in find_nums(n1, f2):
                    for n3 in find_nums(n2, f3):
                        for n4 in find_nums(n3, f4):
                            for n5 in find_nums(n4, f5):
                                if n5%100 == m//100:
                                    return sum((m, n1, n2, n3, n4, n5))