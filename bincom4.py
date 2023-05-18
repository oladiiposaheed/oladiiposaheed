import random
lst = []
for i in range(10):
    num = random.randint(1000, 9999)
    lst.append(num)
print(lst)
#print(random.randint(0, 1))
s = 0
for i in lst:
    s += i
print(s)