import math
import random

#m=int("Adja meg a henger magasságát")
#r=int("Adja meg a henger magasságát")

m=random.randint(2,10)
r=random.randint(2,10)

Ta =math.pow(r,2)*math.pi
Tp=2*math.pi*r*m 
terfogat=Ta*m
felszin=2*Ta*Tp

print(f"{terfogat:10.2}","cm^3")
print(f"{terfogat:10.2}","cm^2")





# Henger felszíne és térfogata

Te=int(input("Kérem adja meg a henger terültét"))
Tp=int(input("Kérem adja meg a másik henger terültét"))
f=2* Te+Tp
print("A henger felszíne ",f )

Pi=3.14
r=int(input("Adja meg a henger sugarát! "))
m=int(input("Kérem adja meg a henger magasságát! "))
v=Pi * r * r * m
print("A henger térfogata",v)
