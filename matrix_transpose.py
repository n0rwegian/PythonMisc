n = int(input())
matrix = [[int(j) for j in input().split()] for i in range(n)]

for i in range(n):
    for j in range(i, n):
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

[print(*i) for i in matrix]
