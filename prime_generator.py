from itertools import takewhile


def primes():
    i = 2
    while True:
        if all(i % j for j in range(2, i)):
            yield i
        i += 1

print(list(takewhile(lambda x : x <= 31, primes())))