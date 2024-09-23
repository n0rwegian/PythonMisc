timur = input()
ruslan = input()

if timur == ruslan:
    print('ничья')
else:
    results = {
        'камень': ['ножницы', 'ящерица'],
        'ножницы': ['бумага', 'ящерица'],
        'бумага': ['камень', 'Cпок'],
        'ящерица': ['Спок', 'бумага'],
        'Спок': ['камень', 'ножницы'],
    }
    if ruslan in results[timur]:
        print('Тимур')
    else:
        print('Руслан')
