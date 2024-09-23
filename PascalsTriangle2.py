def pascal(row: int) -> list:
    pt = [[1]]

    for i in range(1, row + 1):
        pt.append([1])
        pt[i].extend([pt[i - 1][j] + pt[i - 1][j + 1] for j in range(i - 1)])
        pt[i].append(1)

    return pt


[print(*i) for i in pascal(int(input()) - 1)]
