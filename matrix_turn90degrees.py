n = int(input())
matrix = []
matrix1 = [[0 for j in range(n)] for i in range(n)]

for i in range(n):
    matrix.append([int(j) for j in input().split()])

flag = 0
for i in range(n):
    for j in range(n):
        matrix1[j][n - 1 - i] = matrix[i][j]

[print(*i) for i in matrix1]

'''
for row in zip(*matrix[::-1]):
    print(*row)
'''

'''
b = [[a[~i][j] for i in range(n)] for j in range(n)]

Допустим, надо взять i-й элемент с конца списка, считая от нуля.
Если бы от единицы, то по-питоновски это было бы просто a[-i], но нам нужно именно от нуля, 
чтобы зеркально элементу a[i]. Тогда придётся писать a[-i-1], но можно проще, a[~i], используя особенности 
хранения отрицательных целых чисел в дополнительном коде. По сути, это то же самое, что и a[-i-1], только запись
короче получается.
'''