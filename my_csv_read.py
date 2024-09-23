def read_csv():
    with open('data.csv', 'r') as f:
        data = f.readlines()
    return [dict(zip(data[0].strip().split(','), data[i].strip().split(','))) for i in range(1, len(data))]


print(read_csv())
