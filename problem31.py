def solve():
    total = 0
    for a in range(0, 200 + 1, 100):
        for b in range(0, 201 - a, 50):
            for c in range(0, 201 - (a+b), 20):
                for d in range(0, 201 - (a+b+c), 10):
                    for e in range(0, 201 - (a+b+c+d), 5):
                        for f in range(0, 201 - (a+b+c+d+e), 2):
                            total += 1
    return total + 1