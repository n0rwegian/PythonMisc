from functools import reduce


from functools import reduce

def evaluate(coefficients: list[int], x: int) -> int:
    return reduce(lambda a, b: a + b, map(lambda m, n: m * x ** n, coefficients, range(len(coefficients))[::-1]))


print(evaluate([int(i) for i in input().split()], int(input())))


def evaluate1(coefficients: list[int], x: int) -> int:
    return reduce(lambda m, n: n[0] * x ** n[1] + m, zip(coefficients, range(len(coefficients) - 1, -1, -1)), 0)

print(evaluate([int(i) for i in input().split()], int(input())))



'''
def evaluate(coefficients: str, x: str) -> int:
    y = [int(i) for i in coefficients.split()]
    return sum(y[j] * int(x) ** (len(y) - 1 - j) for j in range(len(y)))

print(evaluate(input(), input()))
'''

# разложение по схеме Горнера
# evaluate = lambda coefficients, x: reduce(lambda s, a: s * x + a, coefficients, 0)

'''
def evaluate(l, x):
    ch = list(map(lambda y, z: y * x**z, l, list(range(len(l)-1, -1, -1))))
    return sum(ch)
'''