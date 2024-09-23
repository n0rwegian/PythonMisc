alphabet_rus = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'

inpt = 'яндекс'
string = list((inpt + ' запретил букву а').split())

for letter in alphabet_rus:
    if not any(letter in w for w in string):
        continue
    string[-1] = letter
    if sum((w != '') for w in string) == 1:
        break
    print(' '.join(w for w in string if w))

    for i in range(len(string) - 1):
        string[i] = ''.join(c for c in string[i] if c != letter)

