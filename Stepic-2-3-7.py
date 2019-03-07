#-*- coding utf-8 -*-

a = int(input())
b = int(input())
s = 0
count = 0
while (a % 3) != 0:
    a += 1
for i in range(a, b+1, 3):
    s += i
    count +=1
c = s / count
print(c)
