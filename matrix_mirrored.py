n = int(input())
matrix = []

for i in range(n):
    matrix.append([int(j) for j in input().split()])

flag = 0
for i in range(n // 2):
    matrix[i], matrix[n - 1 - i] = matrix[n - i - 1], matrix[i]

[print(*i) for i in matrix]
