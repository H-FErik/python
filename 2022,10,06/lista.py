

from pickle import APPEND
from this import s


ps = [10,20,30,40]
qs = ["alma","eper","barack"]
print(ps)
print(qs)

# beágyazott
zs = ["Hello",2.0,5,[10,20]]
print(zs)
print(zs[3])

szotar = ["alma","sajt","kutya"]
szamok = [17,123]
ures_lista = []
print(szotar,szamok,ures_lista)

#elemek elérés

szamok = [17,123]

#elemek helye
print(szamok[0])
for i in enumerate(szamok):
    print(i)

#mit csinálunk?
for (i,ert) in enumerate(szamok):
    szamok[i] = ert**2
    print(szamok[i])

for (i,v) in enumerate(["banán","alma","körte","cirtom"]):
    print(i,v)

#lista metódus
s_lista = []
s_lista. append(6)
s_lista. append(20)
s_lista. append(4)
s_lista. append(16)
print(s_lista)

#Szúrjunk be a 10-t az 1-es pozícióra

s_lista.insert(1,10)
print(s_lista)

s_lista.insert(0,16)
print(s_lista)

#Hány 12-es érték szerepel a listában?

print(s_lista.count(16))

#Hány 16-es érték szerepel a listában?

print(s_lista.count(16))

#Szúrjunk be a teljes listát a sajat_listaba
s_lista.extend([5,9,5,11])
print(s_lista)

#Keressük meg az első 9-es érték indexet

print(s_lista.index(9))

#Fordítsuk meg a listát!
s_lista.reverse()
print(s_lista)

#Rendezzük a listát!

s_lista.sort()
print(s_lista)

#Távolítsuk el az első 12-es értéket a listából!

s_lista.remove(16)
print(s_lista)

#Rendezzük egy szöveges adatokat tartalmazó listát!

szoveg_lista = ["barack","alma","mandarin"]
szoveg_lista.sort()
print(szoveg_lista)
szoveg_lista2=["én","te","Ő","mi","ti","ők"]
szoveg_lista2.sort()
print(szoveg_lista2)