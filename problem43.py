from itertools import permutations

def solve():
    total = 0
    for t in permutations('123456789'):
        s = ''
        for d in t:
            s += d
        for i in range(1,10):
            k = s[:i] + '0' + s[i:]
            if int(k[1:4]) % 2  == 0 and \
               int(k[2:5]) % 3  == 0 and \
               int(k[3:6]) % 5  == 0 and \
               int(k[4:7]) % 7  == 0 and \
               int(k[5:8]) % 11 == 0 and \
               int(k[6:9]) % 13 == 0 and \
               int(k[7:10]) % 17 == 0:
               total += int(k)
    return total