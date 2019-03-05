# -*- coding utf-8 -*-

a = int(input())
b = int(input())
c = int(input())
max_ = 0; min_ = 0; mid_ = 0
if a >= b and a >= c:
    if b >= c:
        max_ = a; min_ = c; mid_ = b
    else:
        max_ = a; min_ = b; mid_ = c
elif b > a and b >= c:
    if a >= c:
        max_ = b; min_ = c; mid_ = a
    else:
        max_ = b; min_ = a; mid_ = c
elif c > a and c > b:
    if a >= b:
        max_ = c; min_ = b; mid_ = a
    else:
        max_ = c; min_ = a; mid_ = b
print(max_)
print(min_)
print(mid_)
