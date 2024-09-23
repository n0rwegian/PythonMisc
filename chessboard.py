n, m = list(map(int, input().split()))
matrix = [list('*.' * (m // 2) + '*' * (m % 2)) if i % 2 else list('.*' * (m// 2) + '.' * (m % 2)) for i in range(n)]

[print(*i) for i in matrix]

'''
board = [[".*"[(i + j) % 2] for j in range(m)] for i in range(n)]
'''