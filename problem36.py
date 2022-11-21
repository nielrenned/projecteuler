from utilities import is_palindrome

def solve():
    total = 0
    for n in range(1,1000000):
        if is_palindrome(n) and is_palindrome("{0:b}".format(n)):
            total += n
    return total