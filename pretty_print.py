def pretty_print(data, side='-', delimiter='|'):
    l = sum(map(len, map(str, data))) + 3 * len(data) - 1
    print('  ' + side * l + '  ')
    print('', *data, '', sep=' ' + delimiter + ' ')
    print('  ' + side * l + '  ')


pretty_print([1, 2, 10, 23, 123, 3000])
pretty_print(['abc', 'def', 'ghi', '12345'])
pretty_print(['abc', 'def', 'ghi'], side='*')
pretty_print(['abc', 'def', 'ghi'], delimiter='#')
pretty_print(['abc', 'def', 'ghi'], side='*', delimiter='#')