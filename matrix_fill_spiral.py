n, m = list(map(int, input().split()))

matrix = [[-1] + [0 for j in range(m)] + [-1] for i in range(n)]
matrix.append([-1 for _ in range(m + 2)])

dx = (1, 0, -1, 0)
dy = (0, 1, 0, -1)
cur = 0

cnt = 1
i = 0
j = 1
while cnt <= n * m:
    matrix[i][j] = cnt
    cnt += 1
    if matrix[i + dy[cur]][j + dx[cur]]:
        cur = (cur + 1) % 4
    i += dy[cur]
    j += dx[cur]

[print(*i[1:-1]) for i in matrix[:-1]]
