
def solve():
    highest, best_d = 0,0
    for d in range(2,1000):
        if d % 2 == 0 or d % 5 == 0:
            continue # no repeating part
        powers_of_ten = [1]
        k = 1
        t = 0
        while True:
            x = 10**k % d
            if x in powers_of_ten:
                t = k
                break
            powers_of_ten.append(x)
            k += 1
        if t > highest:
            highest = t
            best_d = d
    return best_d