import random

people = []
for _ in range(int(input())):
    people.append(input())

random.shuffle(people)
for i in range(-1, len(people) - 1):
    print(people[i],'-', people[i + 1])
