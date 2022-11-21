import math
ONE_MIL = 1000000

partitions = [0]*ONE_MIL
partitions[0] = 1

def get_partitions(k):
    if k < 0:
        return 0
    if k >= ONE_MIL:
        return -1
    return partitions[k]

def solve():
    n = 1
    while n < ONE_MIL:
        total = 0
        lb = int(math.ceil(-(math.sqrt(24*n+1)+1.0)/6))
        ub = int(math.floor((math.sqrt(24*n+1)-1.0)/6))
        for k in range(lb, ub + 1):
            if k == 0:
                continue
            coeff = 1
            if k % 2 == 0:
                coeff = -1
            total += coeff*get_partitions(n - k*(3*k+1)//2) % ONE_MIL
            total %= ONE_MIL
        if total == 0:
            return n
        partitions[n] = total
        n += 1