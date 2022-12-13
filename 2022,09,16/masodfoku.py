
import math, cmath

a = input("Kérem az egyenlet főeggyütthatóhát")
a=float(a)
while a==0:
    print("Ez nem lesz másodfokú egyenlet?nem oldom meg.")
    a=input("Kérem a másik másodfokú egyenlet főeggyütthatóját:")
    a= float(a)

b= input("Kérem az elsőfokú tag eggyütthatóját:")
c=input("Kérem a konstans tagot: ")
b=float(b)
c=float(c)

d= b*b-4*a*c 
print("A diszkrimináns értéke", d)

if d>=0:
    print("Van valós megoldás.")
    x1=(-b-math.sqrt(d))/(2*a)
    x2=(-b+math.sqrt(d))/(2*a)
    print("Az egyik megoldás",x1)
    print('A másik megoldás',x2)