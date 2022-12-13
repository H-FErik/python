'''''
for i in range (1,100):
    print("Szamok",i)

for f in range (2,100,2):
    print("Szamok parosaval.")
    print(f)

for f in range (100,-1,-1):
    print(f)

for f in range (100,-1,-2):
    print(f)

lista = ["1","2","3"]
for szam in lista:
    print(szam)


gyumolcsok = ["Banán","Alma","Körte"]
for gyumolcs in gyumolcsok:
    print(gyumolcsok)
if gyumolcsok == "Banán":
    print("Van babán")
else:
    print("Nincs banán")


összeg = 0
for i in range(1,101):
    összeg=összeg+i
    print(összeg)

összeg=0
while összeg != 5050:
    összeg+1
print(összeg)
'''

szoveg=input("Kérem adja meg a nevét ")
print(szoveg)
szoveghossz=len(szoveg)
print(szoveghossz)
print(szoveg[:2])
print(szoveg[-2])

print(szoveg.find('e'))

for i in szoveg:
    print(szoveg)
print((szoveg.upper))




