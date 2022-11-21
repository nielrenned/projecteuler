fac_digits = {'1': 1, '0': 1, '3': 6, '2': 2, '5': 120, '4': 24, '7': 5040, '6': 720, '9': 362880, '8': 40320}

def factorial_digit_sum(n):
    return sum(map(lambda x: fac_digits[x], str(n)))

def get_chain_len(n):
    prev_numbers = set()
    while n not in prev_numbers:
        prev_numbers.add(n)
        n = factorial_digit_sum(n)
    return len(prev_numbers)

def solve():
    count = 0
    for n in range(2, 1000000):
        if get_chain_len(n) == 60:
            count += 1
    return count