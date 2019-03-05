#-*- coding utf-8 -*-

n = int(input())
a = ""
if n == 1 or ((n % 10) == 1 and ((n % 100) != 11)):
    a = ""
elif (2 <= n <= 4) or (1 < (n % 10) < 5 and ((n % 100) < 11 or (n % 100 ) > 20)):
    a = "a"
else:
    a = "ов"
print(str(n) + " программист" + a)
