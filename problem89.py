numerals = {' ': 0,
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000}

def parse_roman_numeral(s):
    streak = 1
    prev = ' '
    total = 0
    for c in s:
        if c == prev:
            streak += 1
            continue
        if prev == 'I':
            if c == 'V':
                total += 4 - 1
                continue
            elif c == 'X':
                total += 9 - 1
                continue
        elif prev == 'X':
            if c == 'L':
                total += 40 - 10
                continue
            elif c == 'C':
                total += 90 - 10
                continue
        elif prev == 'C':
            if c == 'D':
                total += 400 - 100
                continue
            if c == 'M':
                total += 900 - 100
                continue
        total += streak*numerals[prev]
        prev = c
        streak = 1
    total += streak*numerals[prev]
    return total

def write_roman_numeral(n):
    s = ''
    s += 'M'*(n//1000)
    hundreds = (n%1000)//100
    if hundreds == 9:
        s += 'CM'
    if 5 <= hundreds < 9:
        s += 'D'
        hundreds -= 5
    if hundreds == 4:
        s += 'CD'
    if 0 < hundreds < 4:
        s += 'C'*hundreds
    tens = (n%100)//10
    if tens == 9:
        s += 'XC'
    if 5 <= tens < 9:
        s += 'L'
        tens -= 5
    if tens == 4:
        s += 'XL'
    if 0 < tens < 4:
        s += 'X'*tens
    ones = (n%10)
    if ones == 9:
        s += 'IX'
    if 5 <= ones < 9:
        s += 'V'
        ones -= 5
    if ones == 4:
        s += 'IV'
    if 0 < ones < 4:
        s += 'I'*ones
    return s

def solve():
    #print(parse_roman_numeral('CCXCVIII'))
    #return
    with open('p089_roman.txt') as f:
        lines = f.read().split('\n')
    total = 0
    for line in lines:
        n = parse_roman_numeral(line)
        s = write_roman_numeral(n)
        if len(line) > len(s):
            print(n, line, s)
            total += len(line) - len(s)
    return total