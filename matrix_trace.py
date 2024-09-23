n = int(input())
matrix = []

for _ in range(n):
    matrix.append([int(i) for i in input().split()])

print(sum(matrix[i][i] for i in range(n)))
