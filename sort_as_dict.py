athletes = [('Дима', 10, 130, 35), ('Тимур', 11, 135, 39), ('Руслан', 9, 140, 33), ('Рустам', 10, 128, 30), ('Амир', 16, 170, 70), ('Рома', 16, 188, 100), ('Матвей', 17, 168, 68), ('Петя', 15, 190, 90)]

(lambda x: [print(*i) for i in sorted(athletes, key=lambda y: y[x - 1])])(int(input()))

'''
def gen_comparator(field=1):
    def comp(seq):
        return seq[field - 1]
    return comp

cmp = gen_comparator(int(input()))
athletes.sort(key=cmp)
for a in athletes:
    print(*a)
'''