from utilities import is_prime

def solve():
    k = 3
    total = 0
    while True:
        p1 = k*k - (k-1)
        p2 = k*k - 2*(k-1)
        p3 = k*k - 3*(k-1)
        if is_prime(p1):
            total += 1
        if is_prime(p2):
            total += 1
        if is_prime(p3):
            total += 1
        if float(total) / (2*k-1) < 0.1:
            break
        k += 2
    return k