from utilities import is_permutation

def solve():
    k = 8
    while True:
        cubes = [n**3 for n in range(int(10**((k-1)/3))+1, int(10**(k/3))+1)]
        for i in range(len(cubes)):
            n = cubes[i]
            count = 1
            for j in range(i, len(cubes)):
                if i == j:
                    continue
                if is_permutation(n, cubes[j]):
                    count += 1
            if count == 5:
                return n
        k += 1