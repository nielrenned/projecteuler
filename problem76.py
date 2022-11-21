from utilities import partitions

def solve():
    # partitions also count 100 == 100, but that's not a sum
    return partitions(100)-1