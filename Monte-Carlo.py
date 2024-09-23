import random

n = 10**6       # количество испытаний
in_figure = 0

for _ in range(n):
    x, y = random.uniform(-2, 2), random.uniform(-2, 2)
    if (x ** 3 + y ** 4 + 2 >= 0) and 3 * x + y ** 2 <= 2:
        in_figure += 1
print((in_figure / n) * 16)