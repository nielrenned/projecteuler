### I'm sad I'm just using Decimal here, because I remember coding up a cooler way to do this
import decimal
from decimal import Decimal
from utilities import is_square

def solve():
    decimal.getcontext().prec = 110
    total = 0
    for n in range(1, 100):
        if is_square(n):
            continue
        root = Decimal(n).sqrt()
        total += sum(map(int, str(root)[0] + str(root)[2:101]))
    return total