def build_query_string(params):
    return '&'.join(str(k) + '=' + str(v) for k, v in sorted(params.items()))


print(build_query_string({'name': 'timur', 'age': 28}))