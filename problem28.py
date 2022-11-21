def solve():
    total = 1
    for k in range(3, 1001 + 1, 2):
        total += k*k
        total += k*k - (k-1)
        total += k*k - 2*(k-1)
        total += k*k - 3*(k-1)
    return total