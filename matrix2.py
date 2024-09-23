n = int(input())
m = int(input())
matrix = []

for _ in range(n):
    matrix.append([input() for _ in range(m)])

[print(*i) for i in matrix]
print()
for c in range(m):
    for r in range(n):
        print(matrix[r][c], end=' ')
    print()
