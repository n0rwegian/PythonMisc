n = int(input())
matrix = []

for _ in range(n):
    matrix.append([int(i) for i in input().split()])

print(max(matrix[i][j] for j in range(n) for i in range(n) \
          if (i >= j and i <= n - j - 1) or (i <= j and i >= n - j - 1)))
