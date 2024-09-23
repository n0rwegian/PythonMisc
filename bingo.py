from random import randint


used = set()
n = 5
matrix = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    j = 0
    while j < n:
        x = randint(1, 75)
        if x in used:
            continue
        matrix[i][j] = x
        used.add(x)
        j += 1
matrix[2][2] = 0

[print(*(str(k).ljust(3) for k in matrix[i])) for i in range(n)]

'''
numbers = sample(list(range(1, 76)), 25)
bingo = [numbers[i:i + 5] for i in range(0, 21, 5)]
bingo[2][2] = 0
'''