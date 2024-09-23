n = 8
c = input()
y = ord(c[0]) - ord('a')
x = n - int(c[1])
matrix = [['.' for _ in range(n)] for _ in range(n)]

for i in range(n):
    matrix[i][y] = '*'
    matrix[x][i] = '*'
    if x - i >= 0 and y - i >= 0:
        matrix[x - i][y - i] = '*'
    if x - i >= 0 and y + i < n:
        matrix[x - i][y + i] = '*'
    if x + i < n and y - i >= 0:
        matrix[x + i][y - i] = '*'
    if x + i < n and y + i < n:
        matrix[x + i][y + i] = '*'

matrix[x][y] = 'Q'

[print(*i) for i in matrix]
