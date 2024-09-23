n = int(input())
students = set()
correct_counter = 0
eps = 1e-06

for _ in range(n):
    student, is_correct = [i.strip() for i in input().split(':')]
    if is_correct == 'Correct':
        students.add(student)
        correct_counter += 1

if len(students) :
    print(f'Верно решили {len(students)} учащихся')
    print(f'Из всех попыток {int(correct_counter * 100 / n + 0.5)}% верных')
else:
    print("Вы можете стать первым, кто решит эту задачу")

'''
def int_r(num):
    num = int(num + (0.5 if num > 0 else -0.5))
    return num
'''