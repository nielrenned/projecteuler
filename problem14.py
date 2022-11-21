from utilities import collatz

def solve():
    steps = {1: 0}
    highest, index = 0, 0
    for i in range(1, 1000000):
        n = i
        count = 0
        while n != 1:
            n = collatz(n)
            count += 1
            if n in steps:
                count += steps[n]
                steps[i] = count
                break
        if count > highest:
            highest, index = count, i
    return index