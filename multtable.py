n = int(input())
m = int(input())
matrix = []

for i in range(n):
    matrix.append([i * j for j in range(m)])

for i in range(n):
    for j in range(m):
        print(str(matrix[i][j]).ljust(3), end=' ')
    print()
