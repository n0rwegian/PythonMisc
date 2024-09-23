n = (input())
matrix = [list('............') for _ in range(12)]

r = 8 - int(n[1]) + 2
c = ord(n[0]) - ord('a') + 2
matrix[r][c] = 'N'

dx = (-2, -2, -1, 1, 2,  2,  1, -1)
dy = (-1,  1,  2, 2, 1, -1, -2, -2)
for i in range(len(dx)):
    matrix[r + dx[i]][c + dy[i]] = '*'

[print(*i[2:10]) for i in matrix[2:10]]
