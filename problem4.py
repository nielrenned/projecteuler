from utilities import is_palindrome

def solve():
    highest = 0
    for a in range(100,1000):
        for b in range(100,1000):
            p = a*b
            if is_palindrome(p) and p > highest:
                highest = p
    return highest