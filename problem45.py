from utilities import solve_quadratic, triangle, is_pentagonal, is_hexagonal

def solve():
    n = 286
    while True:
        T_n = triangle(n)
        if is_pentagonal(T_n) and is_hexagonal(T_n):
            return T_n
        n += 1