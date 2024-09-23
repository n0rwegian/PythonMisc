n = int(input())

matrix = [[[0, 1][(i == j) or (i == n - 1 - j)] for j in range(n)] for i in range(n)]

[print(*i) for i in matrix]
