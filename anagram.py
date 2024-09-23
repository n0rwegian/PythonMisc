import random as rnd

word = input()
word = list(word)
rnd.shuffle(word)
print(''.join(word))

# print(*random.sample(word, len(word)), sep='')
