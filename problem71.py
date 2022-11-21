from utilities import gcd

def solve():
    proper_fractions = set()
    best_n, best_ratio = 0, 0
    for d in range(2, 1000000+1):
        if d == 7:
            continue
        #if d % 100000 == 0:
        #    print(d)
        n = (d*3)//7
        if gcd(n,d) == 1 and float(n)/d > best_ratio:
            #print(n, d, float(n)/d)
            best_n = n
            best_ratio = float(n)/d
    return best_n