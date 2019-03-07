#-*- coding utf-8 -*-

a = int(input())
b = int(input())
c = int(input())
d = int(input())

print(" ", end="\t")
for i in range (c, d+1):
    print(i, end="\t")
print()
for i in range(a, b+1):
    print(i, end="\t")
    for j in range(c, d+1):
        a = i * j
        print(a, end="\t")
    print()


