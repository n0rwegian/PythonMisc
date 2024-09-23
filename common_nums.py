# (lambda s1, s2: print(*sorted(s1 & s2, reverse=True, key=int) if s1 & s2 else ['BAD DAY']))(set(input().split()), set(input().split()))

print(*sorted(set(input().split()) & set(input().split()), reverse=True, key=int) or ['BAD DAY'])