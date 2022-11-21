def next(n):
    return sum([int(i)*int(i) for i in str(n)])

TEN_MIL = 10000000

def solve():
    count = 0
    for n in range(1, TEN_MIL):
        if n%100000 == 0:
            print(n)
        while n != 1 and n != 89:
            n = next(n)
        if n == 89:
            count += 1
    return count