n, m = list(map(int, input().split()))

matrix = [[m * i + m - j if i % 2 else m * i + j + 1 for j in range(m)] for i in range(n)]

[print(*i) for i in matrix]
