num_days = [31,28,31,30,31,30,31,31,30,31,30,31]

def solve():
    year = 1901
    day = 2
    count = 0
    while year < 2001:
        is_leap_year = False
        if year % 4 == 0:
            if year % 100 != 0:
                is_leap_year = True
            if year % 100 == 0 and year % 400 == 0:
                is_leap_year = True
        for i in range(12):
            day += num_days[i]
            if i == 1 and is_leap_year:
                day += 1
            day %= 7
            if day == 0:
                count += 1
        year += 1
    return count