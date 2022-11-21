from utilities import factorial

def solve():
    total = 0
    for n in range(10, 100000):
        if n == sum(map(factorial, map(int, str(n)))):
            total += n
    return total