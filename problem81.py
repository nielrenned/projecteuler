test_matrix = [[131, 673, 234, 103,  18],
               [201,  96, 342, 965, 150],
               [630, 803, 746, 422, 111],
               [537, 699, 497, 121, 956],
               [805, 732, 524,  37, 331]]

def solve():
    with open('inputs/p081_matrix.txt') as f:
        rows = f.read().split('\n')[:-1]
    M = [list(map(int, row.split(','))) for row in rows]
    N = len(M)
    for d in range(2*N-2, -1, -1):
        r, c = 0, 0
        if d <= N-1:
            c = d
        else:
            r = d - (N-1)
            c = N-1
        while r < N and c >= 0:
            if c == r == N-1:
                pass
            elif c == N-1:
                M[r][c] += M[r+1][c]
            elif r == N-1:
                M[r][c] += M[r][c+1]
            else:
                M[r][c] += min(M[r][c+1], M[r+1][c])
            c -= 1
            r += 1
    return M[0][0]