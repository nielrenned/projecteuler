from utilities import num_combinations

def solve():
    count = 0
    for n in range(1, 100 + 1):
        for r in range(n + 1):
            if num_combinations(n,r) > 1000000:
                count += 1
    return count