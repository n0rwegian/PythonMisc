n, m = list(map(int, input().split()))

matrix = [[0 for j in range(m)] for i in range(n)]

cnt = 1
for j in range(m + n - 1):
    for i in range(min(j + 1, n)):
        if j - i < m:
            matrix[i][j - i] = cnt
            cnt += 1

[print(*i) for i in matrix]
