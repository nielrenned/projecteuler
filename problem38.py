def solve():
    highest = 0
    for n in range(1,10000):
        s = str(n)
        i = 2
        while len(s) < 9:
            s += str(i*n)
            i += 1
        if len(s) > 9:
            continue
        if sorted(s) == ['1', '2', '3', '4', '5', '6', '7', '8', '9'] and int(s) > highest:
            highest = int(s)
    return highest
            