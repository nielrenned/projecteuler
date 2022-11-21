def solve():
    words = None
    with open('p042_words.txt') as f:
        words = list(map(lambda x: x[1:-1], f.read().split(',')))
    triangle_nums = set()
    n = 1
    while n*(n+1)/2 <= 286:
        triangle_nums.add(n*(n+1)/2)
        n += 1
    
    count = 0
    for word in words:
        value = 0
        for c in word:
            value += ord(c) - 64
        if value in triangle_nums:
            count += 1
    return count