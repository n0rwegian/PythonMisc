ans = []

for c in input().split():
    if not ans:
        ans.append([c])
        continue
    if c == ans[-1][-1]:
        ans[-1].extend(c)
    else:
        ans.append([c])

print(ans)
