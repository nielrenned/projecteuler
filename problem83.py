test_matrix = [[131, 673, 234, 103,  18],
               [201,  96, 342, 965, 150],
               [630, 803, 746, 422, 111],
               [537, 699, 497, 121, 956],
               [805, 732, 524,  37, 331]]

from utilities import DirectedGraph, dijkstra
            
def solve():
    with open('p083_matrix.txt') as f:
        rows = f.read().split('\n')[:-1]
    M = [list(map(int, row.split(','))) for row in rows]
    #M = test_matrix
    N = len(M)
    vertices = [(r,c) for r in range(N) for c in range(N)]
    edges = set()
    weights = {}
    for r,c in vertices:
        if c > 0:
            e = ((r,c), (r, c-1))
            edges.add(e)
            weights[e] = M[r][c-1]
        if c < N-1:
            e = ((r,c), (r, c+1))
            edges.add(e)
            weights[e] = M[r][c+1]
        if r < N-1:
            e = ((r,c), (r+1, c))
            edges.add(e)
            weights[e] = M[r+1][c]
        if r > 0:
            e = ((r,c), (r-1, c))
            edges.add(e)
            weights[e] = M[r-1][c]
    G = DirectedGraph(vertices, edges, weights)
    dist, _ = dijkstra(G, (0,0))
    return dist[(N-1, N-1)] + M[0][0]