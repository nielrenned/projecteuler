def next_perm(perm):
    i = len(perm)-1
    while i > 0 and perm[i-1] >= perm[i]:
        i -= 1
    if (i <= 0):
        return sorted(perm)
        
    j = len(perm)-1
    while perm[j] <= perm[i-1]:
        j -= 1
    perm[i-1], perm[j] = perm[j], perm[i-1]
    perm = perm[:i] + sorted(perm[i:])
    return perm

def solve():
    perm = [0,1,2,3,4,5,6,7,8,9]
    index = 1
    while index < 1000000:
        perm = next_perm(perm)
        index += 1
    s = ''
    for i in range(len(perm)):
        s += str(perm[i])
    return int(s)