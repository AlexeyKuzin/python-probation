#-*- coding utf-8 -*-

genome = input()
s = genome.lower()
cont1 = s.count("g".lower())
cont2 = s.count("c".lower())
cont = cont1 + cont2
res = cont/len(s) * 100
print(res)

