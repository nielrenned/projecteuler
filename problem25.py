from utilities import fibonnaci
from math import log

def solve():
    k = 0
    while True:
        if len(str(fibonnaci(k))) >= 1000:
            return k+1
        k += 1