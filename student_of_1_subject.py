(lambda x, z: ([x.remove(y) if y in x else x.add(y) for y in z] and None) or print(len(x) if x else 'NO'))(set(), [input() for _ in range(int(input()) + int(input()))])

#(lambda x, z: [x.add(y) if y in x else x.remove(y) for y in z])(set(), [input() for _ in range(int(input()) + int(input()))])

#(lambda y: print(y, len(y) if y else 'NO'))(([lambda x: [x.add(y), x.remove(y)][y in x] for y in [input() for _ in range(int(input()) + int(input()))]])(set()))
