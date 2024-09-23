import random as rnd
matrix = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12],
          [13, 14, 15, 16]]

n, m = len(matrix), len(matrix[0])
flat_list = list(matrix[i][j] for i in range(n) for j in range(m))
rnd.shuffle(flat_list)

for i in range(n):
    for j in range(m):
        matrix[i][j] = flat_list[i * m + j]
