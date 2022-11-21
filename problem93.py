from itertools import permutations, combinations_with_replacement

# Only works with single digits
def eval_rpn(s):
    stack = []
    for c in s:
        if c.isdigit():
            stack.append(int(c))
        else:
            x = stack.pop()
            y = stack.pop()
            if c == '+':
                stack.append(x+y)
            elif c == '-':
                stack.append(y-x)
            elif c == '*':
                stack.append(x*y)
            elif c == '/':
                if x == 0:
                    return -10000000
                stack.append(y/x)
    z = stack.pop()
    if z == int(z):
        return int(z)
    return z

'''
ddddooo
dddodoo
dddoodo
ddoddoo
ddododo
'''

valid_rpns = ['{0}{1}{2}{3}{4}{5}{6}', '{0}{1}{2}{3}{4}{6}{5}', '{0}{1}{2}{3}{5}{4}{6}', '{0}{1}{2}{3}{5}{6}{4}', '{0}{1}{2}{3}{6}{4}{5}', '{0}{1}{2}{3}{6}{5}{4}', '{0}{1}{2}{4}{3}{5}{6}', '{0}{1}{2}{4}{3}{6}{5}', '{0}{1}{2}{5}{3}{4}{6}', '{0}{1}{2}{5}{3}{6}{4}', '{0}{1}{2}{6}{3}{4}{5}', '{0}{1}{2}{6}{3}{5}{4}', '{0}{1}{2}{4}{5}{3}{6}', '{0}{1}{2}{4}{6}{3}{5}', '{0}{1}{2}{5}{4}{3}{6}', '{0}{1}{2}{5}{6}{3}{4}', '{0}{1}{2}{6}{4}{3}{5}', '{0}{1}{2}{6}{5}{3}{4}', '{0}{1}{4}{2}{3}{5}{6}', '{0}{1}{4}{2}{3}{6}{5}', '{0}{1}{5}{2}{3}{4}{6}', '{0}{1}{5}{2}{3}{6}{4}', '{0}{1}{6}{2}{3}{4}{5}', '{0}{1}{6}{2}{3}{5}{4}', '{0}{1}{4}{2}{5}{3}{6}', '{0}{1}{4}{2}{6}{3}{5}', '{0}{1}{5}{2}{4}{3}{6}', '{0}{1}{5}{2}{6}{3}{4}', '{0}{1}{6}{2}{4}{3}{5}', '{0}{1}{6}{2}{5}{3}{4}']

def check_digits(l):
    results = set()
    for op1, op2, op3 in combinations_with_replacement(['+', '-', '*', '/'], 3):
        for a,b,c,d in permutations(l):
            for rpn_format_str in valid_rpns:
                rpn = rpn_format_str.format(a,b,c,d,op1,op2,op3)
                results.add(eval_rpn(rpn))
    return results

def solve():
    best_streak = 0
    best_combo = []
    for a in range(1,7):
        for b in range(a+1, 8):
            for c in range(b+1, 9):
                for d in range(c+1, 10):
                    results = check_digits((a,b,c,d))
                    n = 1
                    while True:
                        if n not in results:
                            break
                        n += 1
                    if n > best_streak:
                        best_streak = n
                        best_combo = (a,b,c,d)
                        print(n, best_combo)
    a,b,c,d = best_combo
    return '{}{}{}{}'.format(a,b,c,d)