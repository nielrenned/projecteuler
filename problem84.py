from random import randint, shuffle
from collections import defaultdict

def solve():
    n = 2500000
    doubles_streak = 0
    current_square = 0
    counts = defaultdict(int)
    chance = list(range(1, 17))
    community_chest = list(range(1, 17))
    shuffle(chance)
    shuffle(community_chest)
    chance_index = 0
    community_chest_index = 0
    for _ in range(n):
        d1, d2 = randint(1,4), randint(1,4)
        if d1 == d2:
            doubles_streak += 1
            if doubles_streak == 3:
                current_square = 10 # JAIL
                doubles_streak = 0
                counts[current_square] += 1
                continue
        else:
            doubles_streak = 0
        
        current_square += d1 + d2
        current_square %= 40
        if current_square in [7, 22, 36]: # chance
            result = chance[chance_index]
            chance_index += 1
            chance_index %= 16
            if result == 1:
                current_square = 0 # GO
            elif result == 2:
                current_square = 10 # JAIL
            elif result == 3:
                current_square = 11 # C1
            elif result == 4:
                current_square = 24 # E3
            elif result == 5:
                current_square = 39 # H2
            elif result == 6:
                current_square = 5  # R1
            elif result == 7 or result == 8:
                if current_square < 5 or current_square >= 35:
                    current_square = 5  # R1
                elif current_square < 15:
                    current_square = 15 # R2
                elif current_square < 25:
                    current_square = 25 # R3
                else:
                    current_square = 35 # R4
            elif result == 9:
                if current_square < 12 or current_square >= 28:
                    current_square = 12 # U1
                else:
                    current_square = 28 # U2
            elif result == 10:
                current_square -= 3
                current_square %= 40
        
        if current_square in [2, 17, 33]: # community chest
            result = community_chest[community_chest_index]
            community_chest_index += 1
            community_chest_index %= 16
            if result == 1:
                current_square = 0 # GO
            elif result == 2:
                current_square = 10 # JAIL
        
        if current_square == 30: # GO TO JAIL
            current_square = 10 # JAIL
        
        counts[current_square] += 1
    results = []
    for i in range(40):
        results.append((counts[i]/n, i))
    results = sorted(results)
    #print(results)
    s = '{:02}{:02}{:02}'.format(results[-1][1], results[-2][1], results[-3][1])
    return int(s)