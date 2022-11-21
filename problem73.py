from utilities import gcd

def solve():
    count = 0
    for d in range(4, 12000 + 1):
        for n in range(d//3 + 1, d//2 + 1):
            if gcd(n, d) == 1:
                count += 1
    return count