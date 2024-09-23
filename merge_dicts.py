def merge(values):      # values - это список словарей
    dct = {}
    for value in values:
        for k, v in value.items():
            dct.setdefault(k, set()).add(v)
    return dct

result = merge([{'a': 1, 'b': 2}, {'b': 10, 'c': 100}, {'a': 1, 'b': 17, 'c': 50}, {'a': 5, 'd': 777}])
print(result)