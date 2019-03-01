# -*- coding utf-8 -*-

a = int(input())
b = int(input())
d = 0
c = input()
if c == "+":
    d = a + b
elif c == "-":
    d = a - b
elif c == "/":
    if b == 0: d = "Деление на 0!"
    else: d = a / b
elif c == "mod":
    d = a % b
elif c == "pow":
    d = a**b
elif c == "div":
    d = a // b
print(d)
