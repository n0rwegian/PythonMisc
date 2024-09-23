n = int(input())
matrix = [[int(j) for j in input().split()] for i in range(n)]

if any(matrix[i][j] != matrix[n - 1 - j][n - 1 - i] for j in range(n - 1) for i in range(j + 1)):
    print('NO')
else:
    print('YES')
