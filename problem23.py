from utilities import divisors, prime_seive, sum_naturals

primes = prime_seive(168)

def d(n):
    return sum(divisors(n, primes)) - n

def solve():
    abundant_numbers = []
    for n in range(2, 28123 + 1):
        if d(n) > n:
            abundant_numbers.append(n)
    total = sum_naturals(28123)
    can_be_written_as_sum = set()
    for a in abundant_numbers:
        for b in abundant_numbers:
            if a+b <= 28123:
                can_be_written_as_sum.add(a+b)
    return total - sum(can_be_written_as_sum)
    