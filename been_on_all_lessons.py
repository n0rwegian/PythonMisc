print(*sorted(set.intersection(*({input() for _ in range(int(input()))} for _ in range(int(input()))))), sep='\n')


# (lambda n, s: ([s.intersection_update({input() for _ in range(int(input()))}) for _ in range(n - 1)] and None) or print(*sorted(s), sep='\n'))(int(input()), {input() for _ in range(int(input()))})





'''n = int(input())
s = {input() for _ in range(int(input()))}
for i in range(n - 1):
    s.intersection_update({input() for _ in range(int(input()))})
print(*sorted(s), sep='\n')'''



#(lambda n, s: print(len((s & {input() for _ in range(int(input()))} for _ in range(n - 1)))))(int(input()), {input() for _ in range(int(input()))})