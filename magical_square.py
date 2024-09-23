n = int(input())
matrix = []
elements = set()

flag = 0
for i in range(n):
    row = [int(j) for j in input().split()]
    matrix.append(row)
    if any(i in elements for i in row) or any(i < 1 for i in row):
        flag = 1
        print('NO')
        break
    else:
        elements.update(row)

if not flag:
    s = sum(matrix[0])
    if any(sum(i) != s for i in matrix) or any(sum(matrix[i][j] for i in range(n)) != s for j in range(n)) \
            or sum(matrix[i][i] for i in range(n)) != s or sum(matrix[i][n - 1 -i] for i in range(n)) != s:
        print('NO')
    else:
        print('YES')
