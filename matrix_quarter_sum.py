n = int(input())
matrix = []

for _ in range(n):
    matrix.append([int(i) for i in input().split()])

print(f'Верхняя четверть: {sum(matrix[i][j] for j in range(n) for i in range(n) if i < j and i < n - j - 1)}')
print(f'Правая четверть: {sum(matrix[i][j] for j in range(n) for i in range(n) if i < j and i > n - j - 1)}')
print(f'Нижняя четверть: {sum(matrix[i][j] for j in range(n) for i in range(n) if i > j and i > n - j - 1)}')
print(f'Левая четверть: {sum(matrix[i][j] for j in range(n) for i in range(n) if i > j and i < n - j - 1)}')


