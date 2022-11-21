from utilities import gcd

def solve():
    prod_n = 1
    prod_d = 1
    for n in range(10,100):
        for d in range(10,100):
            for i in range(10):
                c = str(i)
                if c in str(n) and c in str(d):
                    if str(n).index(c) == str(d).index(c): #trivial example
                        continue
                    new_n = int(str(n).replace(c, '', 1))
                    new_d = int(str(d).replace(c, '', 1))
                    if new_n * d == n * new_d and n/d < 1:
                        print(n, d)
                        prod_n *= n
                        prod_d *= d
    prod_d /= gcd(prod_n, prod_d)
    return prod_d