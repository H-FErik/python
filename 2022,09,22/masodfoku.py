import math
import random

a=5
b=random.randint(1,25)
c=int(input("Kérek egy számot! "))

print("Az a számjegy",a)
print("Az b számjegy",b)
print("Az c számjegy",c)



#a=float(a)

d=b*b-4*a*c
print("Az eredmény",b)
print("A megoldás","d=",b,"*","(b-4=)",b-4,"*",a,"*",c)

if a <= 9:
    print("A megadott szám egyjegyű szám")
else:
    print("A megadott szám kétjegyű")

if b <= 9:
    print("egyjegyű szám")
else:
    print("Ez egy kétjegyű szám")