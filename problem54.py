values = {'2': 2, 
          '3': 3, 
          '4': 4, 
          '5': 5, 
          '6': 6, 
          '7': 7, 
          '8': 8, 
          '9': 9, 
          'T': 10, 
          'J': 11, 
          'Q': 12, 
          'K': 13, 
          'A': 14}

suits = {'S': 1, 'C': 2, 'H': 3, 'D': 4}

def count_values(hand):
    vals = {}
    for value, suit in hand:
        if value in vals:
            vals[value] += 1
        else:
            vals[value] = 1
    return vals

def is_pair(hand):
    vals = count_values(hand)
    for value in vals:
        if vals[value] == 2:
            return True, value
    return False, 0

def is_two_pair(hand):
    vals = count_values(hand)
    count = 0
    pair_values = []
    for value in vals:
        if vals[value] == 2:
            count += 1
            pair_values.append(value)
    if count == 2:
        return True, tuple(sorted(pair_values))
    return False, 0

def is_three_of_a_kind(hand):
    vals = count_values(hand)
    for value in vals:
        if vals[value] == 3:
            return True, value
    return False, 0

def is_straight(hand):
    n = hand[0][0]
    if hand[1][0] == n+1 and \
       hand[2][0] == n+2 and \
       hand[3][0] == n+3 and \
       hand[4][0] == n+4:
       return True, n
    return False, 0

def is_flush(hand):
    suit = hand[0][1]   
    if hand[1][1] == suit and \
       hand[2][1] == suit and \
       hand[3][1] == suit and \
       hand[4][1] == suit:
       return True, 0
    return False, 0

def is_full_house(hand):
    vals = count_values(hand)
    keys = list(vals.keys())
    if len(keys) != 2:
        return False, 0
    if vals[keys[0]] == 2 and vals[keys[1]] == 3:
        return True, (keys[1], keys[0])
    if vals[keys[0]] == 3 and vals[keys[1]] == 2:
        return True, (keys[0], keys[1])
    return False, 0

def is_four_of_a_kind(hand):
    vals = count_values(hand)
    for value in vals:
        if vals[value] == 4:
            return True, value
    return False, 0

def is_straight_flush(hand):
    if is_straight(hand)[0] and is_flush(hand)[0]:
        return is_straight(hand)
    return False, 0

def is_royal_flush(hand):
    if is_straight_flush(hand) and hand[0][0] == 10:
        return True, 0
    return False, 0

scores = (lambda x: (True, 0), 
          is_pair, 
          is_two_pair, 
          is_three_of_a_kind, 
          is_straight, 
          is_flush, 
          is_full_house, 
          is_four_of_a_kind, 
          is_straight_flush, 
          is_royal_flush)

def score_hand(hand):
    rank = 0
    for i in range(len(scores)):
        test = scores[i]
        is_rank, score = test(hand)
        if is_rank:
            rank = (i, score)
    return rank + tuple(map(lambda x: x[0], hand[::-1]))

def check_winner(hand1, hand2):
    if score_hand(hand1) > score_hand(hand2):
        return 1
    return 2

def solve():
    with open('inputs/p054_poker.txt') as f:
        lines = f.read().split('\n')
    split_lines = map(lambda s: s.split(' '), lines)
    hands = []
    for line in split_lines:
        hand = list(map(lambda s: (values[s[0]], suits[s[1]]), line))
        hands.append((sorted(hand[:5]), sorted(hand[5:])))
    count = 0
    for i in range(len(hands)):
        h1, h2 = hands[i]
        #print(lines[i], score_hand(h1), score_hand(h2))
        if check_winner(h1, h2) == 1:
            count += 1
    return count

'''Test Hands:
5H 5C 6S 7S KD 2C 3S 8S 8D TD
5D 8C 9S JS AC 2C 5C 7D 8S QH
2D 9C AS AH AC 3D 6D 7D TD QD
4D 6S 9H QH QC 3D 6D 7H QD QS
2H 2D 4C 4D 4S 3C 3D 3S 9S 9D'''