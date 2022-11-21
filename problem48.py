def solve():
    s = 0
    for i in range(1,1000+1):
        s += i**i
    return s % 10000000000