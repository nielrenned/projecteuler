from itertools import chain, combinations
from collections import defaultdict
import math
import sys

def gcd(a,b):
    while b != 0:
        a,b = b,(a%b)
    return a

def prod(l):
    p = 1
    for x in l:
        p *= x
    return p

def fibonnaci(k):
    if k == 0 or k == 1:
        return 1
    if k == 2:
        return 2
    if k in fibonnaci.computed:
        return fibonnaci.computed[k]
    
    value = fibonnaci(k-1) + fibonnaci(k-2)
    fibonnaci.computed[k] = value
    return value

fibonnaci.computed = {}

def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

# Returns primes less than n
def prime_seive(n):
    if n <= 2:
        return []
    if n == 3:
        return [2]
    if n <= 5:
        return [2,3]
    l = [False, True]*(n//2) # l will be True at prime indices and False elsewhere
    l[1] = False
    l[2] = True
    if len(l) == n-1:
        l.append(False)
    primes = [2]
    for p in range(3,n):
        if l[p] == False: # Already known composite
            continue
        primes.append(p)
        k = 2
        while k*p < n:
            l[k*p] = False
            k += 1
    return primes

def is_prime(n):
    for k in range(2, int(math.sqrt(n)) + 1):
        if n % k == 0:
            return False
    return True

def is_palindrome(n):
    s = str(n)
    for i in range(len(s)):
        if s[i] != s[-(i+1)]:
            return False
    return True

def sum_naturals(n):
    if n <= 0:
        return 0
    return n*(n+1)//2

def sum_squares(n):
    if n <= 0:
        return 0
    return n*(n+1)*(2*n+1)//6

def prime_factorization(n, primes=None):
    computed = prime_factorization.computed
    if n in computed:
        return computed[n]
    if primes is None:
        primes = prime_seive(int(math.sqrt(n))+1)
    for p in primes:
        if p > math.sqrt(n):
            break
        if n % p == 0:
            factorization = [p] + prime_factorization(n/p, primes)
            computed[n] = factorization
            return factorization
    # If we get here, n is prime or 1
    computed[n] = [n]
    return [n]

prime_factorization.computed = {}

def divisors(n, primes=None):
    factorization = prime_factorization(n, primes)
    return set(map(prod, powerset(factorization)))

def collatz(n):
    if n % 2 == 0:
        return n/2
    else:
        return 3*n + 1

def factorial(n):
    if n == 0 or n == 1:
        return 1
    if n == 2:
        return 2
    return n*factorial(n-1)

def num_combinations(n, k):
    if k > n:
        return 0
    p = 1
    for i in range(n, n-k, -1):
        p *= i
    p /= factorial(k)
    return p

def triangle(n):
    return sum_naturals(n)

def square(n):
    return n*n

def pentagonal(n):
    return n*(3*n - 1)//2

def hexagonal(n):
    return n*(2*n-1)

def heptagonal(n):
    return n*(5*n-3)//2

def octagonal(n):
    return n*(3*n-2)

def solve_quadratic(a,b,c):
    return ((-b + math.sqrt(b*b-4*a*c))/(2*a), (-b - math.sqrt(b*b-4*a*c))/(2*a))

def is_square(k):
    n = round(math.sqrt(k))
    if n*n == k:
        return True
    return False

def is_pentagonal(k):
    s1, s2 = solve_quadratic(3, -1, -2*k)
    n1, n2 = int(round(s1)), int(round(s2))
    if (n1 > 0 and n1*(3*n1 - 1)//2 == k) or (n2 > 0 and n2*(3*n2 - 1)//2 == k):
        return True
    return False

def is_hexagonal(k):
    s1, s2 = solve_quadratic(2, -1, -k)
    n1, n2 = int(round(s1)), int(round(s2))
    if (n1 > 0 and n1*(2*n1 - 1) == k) or (n2 > 0 and n2*(2*n2 - 1) == k):
        return True
    return False

def is_heptagonal(k):
    s1, s2 = solve_quadratic(5, -3, -2*k)
    n1, n2 = int(round(s1)), int(round(s2))
    if (n1 > 0 and n1*(5*n1 - 3)//2 == k) or (n2 > 0 and n2*(5*n2 - 3)//2 == k):
        return True
    return False

def is_octagonal(k):
    s1, s2 = solve_quadratic(3, -2, -k)
    n1, n2 = int(round(s1)), int(round(s2))
    if (n1 > 0 and n1*(3*n1 - 2) == k) or (n2 > 0 and n2*(3*n2 - 2) == k):
        return True
    return False

def is_permutation(n1, n2):
    return sorted(str(n1)) == sorted(str(n2))

# https://perl.plover.com/yak/cftalk/INFO/gosper.txt
def continued_frac_root(n):
    if is_square(n):
        return (round(math.sqrt(n)), tuple())
    a = 0
    b = n
    c = 1
    k = int(math.sqrt(n))
    frac = []
    first_a, first_b, first_c = k*c-a, c, 2*k*a - k*k*c + b
    a, b, c = first_a, first_b, first_c
    while True:
        s1, s2 = solve_quadratic(c, -2*a, -b)
        k = int(max(s1, s2))
        frac.append(k)
        a, b, c = k*c-a, c, 2*k*a - k*k*c + b
        if a == first_a and b == first_b and c == first_c:
            break
    return (int(math.sqrt(n)), tuple(frac))

def totient(n, primes=None):
    if n == 1:
        return 1
    primes_dividing = set(prime_factorization(n, primes))
    prod = n
    for p in primes_dividing:
        prod *= (p-1)
        prod /= p
    return prod

def partitions_of_size(n, k):
    if n == 0 and k == 0:
        return 1
    if n <= 0 or k <= 0:
        return 0
    if k > n:
        return 0
    if (n, k) in partitions_of_size.computed:
        return partitions_of_size.computed[(n,k)]
    total = partitions_of_size(n-k, k) + partitions_of_size(n-1, k-1)
    partitions_of_size.computed[(n,k)] = total
    return total

partitions_of_size.computed = {}

'''def partitions(n):
    old_limit = sys.getrecursionlimit()
    sys.setrecursionlimit(n+100)
    total = 0
    for k in range(1, n+1):
        total += partitions_of_size(n, k)
    sys.setrecursionlimit(old_limit)
    return total'''

def partitions(n):
    if n == 0:
        return 1
    if n < 0:
        return 0
    if n in partitions.computed:
        return partitions.computed[n]
    total = 0
    lb = int(math.ceil(-(math.sqrt(24*n+1)+1.0)/6))
    ub = int(math.floor((math.sqrt(24*n+1)-1.0)/6))
    for k in range(lb, ub +1):
        if k == 0:
            continue
        coeff = 1
        if k % 2 == 0:
            coeff = -1
        total += coeff*partitions(n - k*(3*k+1)//2)
    partitions.computed[n] = total
    return total

partitions.computed = {}

def sum_of_prime_factors(n, primes=None):
    if n in sum_of_prime_factors.computed:
        return sum_of_prime_factors.computed[n]
    if primes is None:
        primes = prime_seive(n+1)
    total = 0
    for p in primes:
        if p > n:
            break
        if n % p == 0:
            total += p
    return total

sum_of_prime_factors.computed = {1: 0}

def prime_partitions(n, primes=None):
    if n == 1:
        return 0
    if n in prime_partitions.computed:
        return prime_partitions.computed[n]
    if primes is None:
        primes = prime_seive(n+1)
    total = sum_of_prime_factors(n, primes)
    for j in range(1, n):
        total += sum_of_prime_factors(j, primes)*prime_partitions(n-j, primes)
    total = total//n
    prime_partitions.computed[n] = total
    return total

prime_partitions.computed = {}

class DirectedGraph:
    # vertices is any iterable with hashable elements
    # edges is any iterable with elements of the form (A, B) 
    #   where A,B are in vertices and A-->B is an edge
    # weights is anything indexable with elements of edges, 
    #   where weight[edge] is a number that is the weight of that edge
    # If weights is None, all edges are given weight 1
    def __init__(self, vertices, edges, weights=None):
        self.vertices = set(vertices)
        self.edges = set(edges)
        self.weights = {}
        self.neighbors = defaultdict(set)
        for edge in self.edges:
            self.neighbors[edge[0]].add(edge[1])
            if weights is None:
                self.weights[edge] = 0
            else:
                self.weights[edge] = weights[edge]
    
    def get_neighbors(self, v):
        return self.neighbors[v]
    
    def get_weight(self, edge):
        return self.weights[edge]

def dijkstra(G, source):
    unvisited = set(G.vertices)
    dist = defaultdict(lambda: -1)
    dist[source] = 0
    prev = {}
    
    while len(unvisited) != 0:
        u = None
        least_dist = -1
        for v in unvisited:
            if dist[v] != -1 and (dist[v] < least_dist or least_dist == -1):
                u = v
                least_dist = dist[v]
        unvisited.remove(u)
        
        for v in unvisited.intersection(G.get_neighbors(u)):
            alt = dist[u] + G.get_weight((u, v))
            if alt < dist[v] or dist[v] == -1:
                dist[v] = alt
                prev[v] = u
    
    return dist, prev

'''def a_star(G, start, goal, heur):
    closed_set = set()
    open_set = set([start])
    came_from = {}
    
    g_score = defaultdict(lambda: INF)
    g_score[start] = 0
    
    f_score = defaultdict(lambda: INF)
    f_score[start] = heur(start, goal)
    
    while len(open_set) != 0:
        current = None
        min_score = INF
        for u in open_set:
            s = f_score[u] 
            if s < min_score:
                min_score = s
                current = u
        
        if current == goal:
            return g_score[current]
        
        open_set.remove(current)
        closed_set.add(current)
        
        for v in G.get_neighbors(current):
            if v in closed_set:
                continue
            
            tentative_g_score = g_score[current] + G.get_weight((current, v))
            if v not in open_set:
                open_set.add(v)
            elif tentative_g_score >= g_score[v]:
                continue
            
            came_from[v] = current
            g_score[v] = tentative_g_score
            f_score[v] = g_score[v] + heur(v, goal)'''
