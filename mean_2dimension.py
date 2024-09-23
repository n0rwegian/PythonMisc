list1 = [[1, 7, 8], [9, 7, 102], [102, 106, 105], [100, 99, 98, 103], [1, 2, 3]]
total = sum((sum(i for i in j) for j in list1))
counter = sum((sum(1 for i in j) for j in list1))
print(total / counter)

'''from statistics import mean
list1 = [[1, 7, 8], [9, 7, 102], [102, 106, 105], [100, 99, 98, 103], [1, 2, 3]]
print(mean(sum(list1, [])))'''