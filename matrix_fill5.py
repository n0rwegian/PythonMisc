n, m = list(map(int, input().split()))

matrix = [[(j + i) % m + 1 for j in range(m)] for i in range(n)]

[print(*i) for i in matrix]
