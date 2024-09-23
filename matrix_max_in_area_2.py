n = int(input())
matrix = [[int(j) for j in input().split()] for i in range(n)]

print(max(matrix[i][j] for i in range(n) for j in range(n) if i >= n - 1 - j))
