letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
upper_case = list(map(str.upper, letters))

def apply_key(key, data):
    i_k = 0
    i_d = 0
    text = ''
    while i_d < len(data):
        c = data[i_d] ^ ord(key[i_k])
        text += chr(c)
        i_d += 1
        i_k += 1
        i_k %= len(key)
    return text

def count_words(text, words):
    count = 0
    for word in words:
        if word in text:
            count += 1
        #count += text.count(word.upper())
    return count

def solve():
    with open('inputs/p059_cipher.txt') as f:
        data = list(map(int, f.read().split(',')))
    with open('inputs/p059_common_words.txt') as f:
        words = f.read().split('\n')
    words = words[:25]
    highest, best_key = 0,''
    for c1 in letters:
        for c2 in letters:
            for c3 in letters:
                key = c1 + c2 + c3
                text = apply_key(key, data)
                c = count_words(text, words)
                if c > highest:
                    highest = c
                    best_text = text
    return sum(map(ord, best_text))