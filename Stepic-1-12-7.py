#-*- coding utf-8 -*-
n = int(input())
a1 = n // 100000
a2 = n // 10000 - (a1 * 10)
a3 = n // 1000 - (a1 * 100 + a2 * 10)
sum1 = a1 + a2 + a3
n = n - (a1 * 100000 + a2 * 10000 + a3 * 1000)
b1 = n // 100
b2 = n // 10 - (b1 * 10)
b3 = n - (b1 * 100 + b2 * 10)
sum2 = b1 + b2 + b3
if sum1 == sum2:
    print("Счастливый")
else:
    print("Обычный")