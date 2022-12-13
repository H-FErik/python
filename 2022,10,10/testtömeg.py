'''''

import math
nevek=["Péter","András"]
t=float(input("Kérem adja meg a tömegét! "))
m=float(input("Kérem adja meg a magasságát! "))
bmi=t/(m**2)*1000
#nem=input("Kérem adja meg a nemét! ")
nev=input("Kérem adja meg a vedét4 ")
nevek.append(nev)

print(t,"(kg)")
print(m,"(m)")
print(bmi)

if 20.5 < bmi < 26.5:
    print("Normális")
elif 26.6 < bmi <31.9:
    print("Nem normális")
elif 32.0 < bmi < 36.9:
    print("Elhízás")
elif 37 < bmi <41.9:
    print("2 fokú elhízás")
elif bmi > 42:
    print("Nagyon nem jó")

    

bmi=math(t/m**2)

print(bmi)

össz=t/m**2
print(össz)
'''
nevek=["Péter","András"]
#nev=input("Kérem adja meg a vedét4 ")
#nevek.append(nev)







