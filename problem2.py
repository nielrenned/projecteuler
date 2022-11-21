from utilities import *

def solve():
    k = 0
    f_k = fibonnaci(k)
    total = 0
    while f_k < 4000000:
        if f_k % 2 == 0:
            total += f_k
        k += 1
        f_k = fibonnaci(k)
    return total