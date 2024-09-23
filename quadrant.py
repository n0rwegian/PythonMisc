

n = 10
quadrants = [0 for _ in range(4)]
for i in range(n):
    x, y = [int(i) for i in input().split()]
    if not x or not y:
        continue
    quadrants[(x < 0) + (y < 0) + (x > 0 and y < 0) * 2] += 1

print(quadrants)
[print(['Первая', 'Вторая', 'Третья', 'Четвертая'][s], 'четверть:', quadrants[s]) for s in range(4)]


(lambda i: [print(i[k + 1], i[k], end=' ') if k < len(i) - 1 else print(i[k]) for k in range(0,len(i),2)])([j for j in input().split()])

(lambda i: [print(i[k + 1], i[k],end=' ') if k < len(i) - 1 else print(i[k]) for k in range(0,len(i),2)])(list(input().split()))