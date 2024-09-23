n = int(input())
matrix = []

for _ in range(n):
    matrix.append([int(i) for i in input().split()])

for i in range(n):
    print(len([matrix[i][j] for j in range(n) if matrix[i][j] > sum(k for k in matrix[i]) / n]))
