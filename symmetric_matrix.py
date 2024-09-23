n = int(input())
matrix = []

for i in range(n):
    matrix.append([int(j) for j in input().split()])

flag = 0
for i in range(n):
    if flag:
        break
    for j in range(n):
        if matrix[i][j] != matrix[j][i]:
            flag = 1
            break
print('NO' if flag else 'YES')
