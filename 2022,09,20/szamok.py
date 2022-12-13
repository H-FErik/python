
from re import I


import random

a=5
b=random.randint(5,25)
c=input("Adjon meg egy harmadik számot")

print("a= ", a)
print("b= ", b)
print("c= ", c)

print("A három szám összege", a+b+c)
print("A shárom szám szorzata", a*b*c)

szorzat = a*b*c

if szorzat >500:
    print("A számok szorzata nagyobb mint 500")
else:
    print("A számok szorzata kisebbek mint 500")

if (c%2):
    print("A c szám páratlan ")




