test_matrix = [[131, 673, 234, 103,  18],
               [201,  96, 342, 965, 150],
               [630, 803, 746, 422, 111],
               [537, 699, 497, 121, 956],
               [805, 732, 524,  37, 331]]

from utilities import DirectedGraph, dijkstra
            
def solve():
    with open('p082_matrix.txt') as f:
        rows = f.read().split('\n')[:-1]
    M = [list(map(int, row.split(','))) for row in rows]
    #M = test_matrix
    N = len(M)
    vertices = [(r,c) for r in range(N) for c in range(N)]
    edges = set()
    weights = {}
    for r,c in vertices:
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
    min_dist = sum(M[0])
    for i in range(N):
        print(i)
        initial_cost = M[i][0]
        dist, _ = dijkstra(G, (i,0))
        for j in range(N):
            d = initial_cost + dist[(j, N-1)]
            if d < min_dist:
                min_dist = d
    return min_dist