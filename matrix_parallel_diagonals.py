n = int(input())
matrix = [[abs(j - i) for j in range(n)] for i in range(n)]

[print(*i) for i in matrix]
