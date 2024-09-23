s = list(input().split())
n = int(input())
ans = []

for i in range(n):
    ans.append([c for c in s[i::n]])

print(ans)
