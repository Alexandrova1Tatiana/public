e = int(input("Введите трехзначное число"))
r = e//100
t = e%100
y = t//10
u = t%10
o= u*100+y*10+r
print("Ответ",e-o)