given = ''
with open('p067_triangle.txt') as f:
    given = f.read()

triangle = [list(map(int, line.split(' '))) for line in given.split('\n')]

def solve():
    for r in range(len(triangle)-1, 0, -1):
        for c in range(len(triangle[r])-1):
            triangle[r-1][c] += int(max(triangle[r][c], triangle[r][c+1]))
    return triangle[0][0]