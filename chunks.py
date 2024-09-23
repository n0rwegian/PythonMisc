ans = []
s = input().split()
n = int(input())

i = 0
while i < len(s):
    ans.append(s[i:i + n])
    i += n

print(ans)
