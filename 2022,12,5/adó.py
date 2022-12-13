def red(t,w,l ):
    if l<=25 or w<=15:
        t = 0.8 *t
    return t

t = int(input("Kérem a kedvezmény nélküli adót: "))
l = int(input("Kérem a telek hosszát: "))
w = int(input("Kérem a telek szélességét: "))
print("A kedvezményes adó:", red(t,w,l))