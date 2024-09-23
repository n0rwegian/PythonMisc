from fractions import Fraction as F

n = int(input())
ans = set()

for numerator in range(1, n):
    for denominator in range(n, numerator, -1):
        ans.add(F(numerator, denominator))

print(*sorted(ans), sep='\n')
