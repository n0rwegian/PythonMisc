n = int(input())
k = int(input())

people_in_circle = [i for i in range(1, n + 1)]
m, j = n, 0
indx = 0
while m > 1:
    if people_in_circle[indx]:
        j += 1
        if j == k:
            people_in_circle[indx] = 0
            m -= 1
            j = 0
    indx += 1
    if indx >= n:
        indx = indx % n

print(*[i for i in people_in_circle if i])

''' better
res = 0
for i in range(1, n+1):
    res = (res + k) % i
print(res + 1)
'''