import random

length = int(input())    # длина пароля
for _ in range(length):
    print(chr([random.randint(65,90), random.randint(97,122)][random.randint(0,1)]), end='')