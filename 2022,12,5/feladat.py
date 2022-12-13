def border():
    print()
    for i in range(80):
        print("-", sep="", end="")
    print("\n")

print("1.feladat")
border()

print("3.feladat")
border()

print("4.feladat")
border()

print("6.feladat")
border()


def border(n,s):
    print()
    for i in range(n):
        print(s, sep="", end="")
    print("\n")


border(80,"*")
print("1.feladat")
print('a) feladat')
border(10,'-')
print("b) feladat")
border(80,"*")
print("2.feladat")

a=None
def proc():
    global a
    a=5
    print(b)
    print(c)

b=0
c=3
proc()
print(a)

def proc(x):
    x+=1
    print(x)

proc(3)
a=10
proc(a)
print(a)

#tökéletes számok

def pn(num):
    end=int(num/2)
    s=1
    for i in range (2,end=""):
        if num % i ==0:
            s += i
    if s == num:
        print("Tökéletes szám")
    else:
        print("Nem tökéletes szám")
    
for i in range (2,1001):
    print(i,end="")
    pn(i)
ob = int(input("Kérem a vizsgálandó számot:"))
print(ob)

def red(t,w,l ):
    if l<=25 or w<=15:
        t = 0.8 *t
    return t

t = int(input("Kérem a kedvezmény nélküli adót: "))
l = int(input("Kérem a telek hosszát: "))
w = int(input("Kérem a telek szélességét: "))
print("A kedvezményes adó:", red(t,w,l))

