with open('nums.txt', 'r') as f:
    data = f.read()

    total = 0
    word = []
    for char in data:
        if char.isdigit():
            word.append(char)
        else:
            if word:
                total += int(''.join(word))
                word = []

    print(total)

'''
with open('numbers.txt', encoding='utf-8') as file:
    row = ''.join(c if c.isdigit() else ' ' for c in file.read())
    print(sum(map(int, row.split())))
'''

'''
import re
print(sum(map(int, re.findall(r'\d+', open('numbers.txt').read()))))
'''