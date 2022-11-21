numbers = {1: "one", 
           2: "two", 
           3: "three", 
           4: "four", 
           5: "five", 
           6: "six", 
           7: "seven", 
           8: "eight", 
           9: "nine",
           10: "ten",
           11: "eleven",
           12: "twelve",
           13: "thirteen",
           14: "fourteen",
           15: "fifteen",
           16: "sixteen",
           17: "seventeen",
           18: "eighteen",
           19: "nineteen",
           20: "twenty",
           30: "thirty",
           40: "forty",
           50: "fifty",
           60: "sixty",
           70: "seventy",
           80: "eighty",
           90: "ninety",
           100: "hundred",
           1000: "thousand"}

def written_number(n):
    if n == 1000:
        return 'onethousand'
    s = ''
    hundreds = n//100
    if hundreds != 0:
        s += numbers[hundreds] + 'hundred'
    small_part = n%100
    if small_part == 0:
        return s
    elif hundreds != 0:
        s += 'and'
    if small_part < 20:
        s += numbers[small_part]
    else:
        tens = (n % 100)//10
        if tens != 0:
            s += numbers[tens*10]
        ones = n%10
        if ones != 0:
            s += numbers[ones]
    return s

def solve():
    total = 0
    for i in range(1, 1000 + 1):
        total += len(written_number(i))
    return total