def solve():
    n = 10
    while True:
        compare_against = sorted(str(n))
        if sorted(str(2*n)) == compare_against and \
           sorted(str(3*n)) == compare_against and \
           sorted(str(4*n)) == compare_against and \
           sorted(str(5*n)) == compare_against and \
           sorted(str(6*n)) == compare_against:
           return n
        n += 1