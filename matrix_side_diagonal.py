n = int(input())

matrix = [[[0, 2, 1][(i == n - 1 - j) + (i >= n - 1 - j)] for j in range(n)] for i in range(n)]

[print(*i) for i in matrix]
