def dot_prod(v1, v2):
    if len(v1) != len(v2):
        raise Exception('Attempted dot product of different len vectors.')
    return sum([v1[i]*v2[i] for i in range(len(v1))])

def solve():
    N = 50
    count = 0
    for x1 in range(N+1):
        for y1 in range(N+1):
            P = (x1, y1)
            if P == (0, 0):
                continue
            for x2 in range(N+1):
                for y2 in range(N+1):
                    Q = (x2, y2)
                    if Q == (0, 0) or P == Q:
                        continue
                    PQ = (x2 - x1, y2 - y1)
                    if dot_prod(P, Q) == 0 or dot_prod(P, PQ) == 0 or dot_prod(Q, PQ) == 0:
                        count += 1
    return count//2