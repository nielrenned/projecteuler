def solve():
    upper_bound = 5*(9**5)
    total = 0
    for n in range(2, upper_bound + 1):
        sum_digits_fived = sum(map(lambda x: x**5, map(int, str(n))))
        if n == sum_digits_fived:
            total += n
            #print(n)
    return total