with open("pulsar.txt", "r") as f_in:
    data = f_in.read().splitlines()
    for i in range(len(data)):
        data[i] = ("".join(data[i].split(" ")))

with open("pulsar_formatted.txt", "w") as f_out:
    f_out.write('\n'.join(line for line in data))
