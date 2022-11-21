def solve():
    k = 1
    count = 0
    while len(str(9**k)) == k:
        for n in range(1, 10):
            if len(str(n**k)) == k:
                count += 1
        k += 1
    return count