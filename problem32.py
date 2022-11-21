def solve():
    solns = set()
    for a in range(1,10000):
        for b in range(1,100):
            if sorted(str(a) + str(b) + str(a*b)) == ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
                solns.add(a*b)
    return sum(solns)