from utilities import is_palindrome

def is_lychrel(n):
    for i in range(50):
        reversed_n = int(str(n)[::-1])
        n = n + reversed_n
        if is_palindrome(n):
            return False
    return True

def solve():
    count = 0
    for i in range(1, 10000):
        if is_lychrel(i):
            count += 1
    return count