s = input().split()
ans = [[]]

for i in range(1, len(s) + 1):
    for j in range(len(s) - i + 1):
        ans.append(s[j:j + i])

print(ans)
