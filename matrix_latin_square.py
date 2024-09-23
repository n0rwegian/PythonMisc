n = int(input())
matrix = [[int(j) for j in input().split()] for i in range(n)]
s = set(range(1, n + 1))

if any(set(i) != s for i in matrix) or any(set(matrix[i][j] for i in range(n)) != s for j in range(n)):
    print('NO')
else:
    print('YES')
