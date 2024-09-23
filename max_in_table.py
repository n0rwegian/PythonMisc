n = int(input())
m = int(input())
matrix = []

for i in range(n):
    matrix.append([int(j) for j in input().split()])

max_val = matrix[0][0]
max_elem = (0, 0)

for i in range(n):
    for j in range(m):
        if matrix[i][j] > max_val:
            max_val = matrix[i][j]
            max_elem = (i, j)

print(*max_elem)
