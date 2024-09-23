d = {}
for _ in range(int(input())):
    num = int(input())
    d[num] = d.get(num, 0) + 1
n = int(input())
if n == 0:
    print('ДА' if 0 in d else 'НЕТ')
else:
    print(['НЕТ', 'ДА'][any(((n // i) in d) and ((n // i) * i == n) and (n // i != i or d[n // i] > 1) for i in d if i)])
