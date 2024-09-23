n = int(input())
matrix = []

for i in range(n):
    matrix.append([int(j) for j in input().split()])

flag = 0
for i in range(n):
    matrix[i][i], matrix[n - 1 - i][i] = matrix[n - 1 - i][i], matrix[i][i]

[print(*i) for i in matrix]
