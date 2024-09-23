dct = {}
for _ in range(int(input())):
    country, *cities = input().split()
    for city in cities:
        dct[city] = country
for _ in range(int(input())):
    print(dct[input()])