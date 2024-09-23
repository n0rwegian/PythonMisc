import random

n = 10**6       # количество испытаний
in_figure = 0

for _ in range(n):
    x, y = random.uniform(-1, 1), random.uniform(-1, 1)
    if (x ** 2 + y ** 2 <= 1):
        in_figure += 1
print((in_figure / n) * 4)
