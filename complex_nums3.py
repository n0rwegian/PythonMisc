n = int(input())
c1, c2 = [complex(input()) for _ in range(2)]

print(c1 ** n + c2 ** n + c1.conjugate() ** n + c2.conjugate() ** (n + 1))
