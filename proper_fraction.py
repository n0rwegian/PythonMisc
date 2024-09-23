from fractions import Fraction as F

f1, f2 = [input() for _ in range(2)]

print(f'{f1} + {f2} = {F(f1) + F(f2)}')
print(f'{f1} - {f2} = {F(f1) - F(f2)}')
print(f'{f1} * {f2} = {F(f1) * F(f2)}')
print(f'{f1} / {f2} = {F(f1) / F(f2)}')
