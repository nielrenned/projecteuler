
def solve():
    names = ''
    with open('p022_names.txt') as f:
        names = list(map(lambda x: x[1:-1], f.read().split(',')))
    names = sorted(names)
    total = 0
    for i in range(len(names)):
        name = names[i]
        index = i+1
        value = sum(map(lambda c: ord(c) - 64, name))
        score = index * value
        total += score
    return total
