n = int(input())
m = int(input())
matrix = []

for i in range(n):
    matrix.append([int(j) for j in input().split()])

a, b = list(map(int, input().split()))

for i in range(n):
    matrix[i][a], matrix[i][b] = matrix[i][b], matrix[i][a]

for i in range(n):
    print(*matrix[i])
