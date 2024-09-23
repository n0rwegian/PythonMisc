n = int(input())
matrix = [['.*'[(i == j) or (i == n - 1 - j) or (i == n // 2) or (j == n // 2)] for j in range(n)] for i in range(n)]

[print(*i) for i in matrix]
