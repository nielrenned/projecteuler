from utilities import gcd, is_square
from math import sqrt

ONE_BIL = 1000000000

def is_int(n):
    return round(n) == n

'''
a = m*m - n*n
b = 2*m*n
c = m*m + n*n
'''

# Isosceles triangles with integer area are exactly those whose inner two triangles integer right triangles.
# So we need to search the space of pythagorean triples for triples satisfying c = 2b +- 1 or c = 2a +- 1
# and then our triangles will be (c,c,2b) or (c,c,2a).
# 
# 
#

def solve():
    triangles = []
    for m in range(2, int(sqrt(ONE_BIL/5))+1):
        if is_square((m*m+1)/3):
            n = round(sqrt((m*m+1)/3))
            a = m*m - n*n
            c = m*m + n*n
            triangles.append((c,c,2*a))
        if is_square((m*m-1)/3):
            n = round(sqrt((m*m-1)/3))
            a = m*m - n*n
            c = m*m + n*n
            triangles.append((c,c,2*a))
        if is_square(12*m*m+1) and is_int((4*m - sqrt(12*m*m+1))/2):
            n = round((4*m - sqrt(12*m*m+1))/2)
            b = 2*m*n
            c = m*m + n*n
            triangles.append((c,c,2*b))
        if is_square(12*m*m-1) and is_int((4*m - sqrt(12*m*m-1))/2):
            n = round((4*m - sqrt(12*m*m+1))/2)
            b = 2*m*n
            c = m*m + n*n
            triangles.append((c,c,2*b))
    return sum(filter(lambda x: x <= ONE_BIL, map(sum, triangles)))