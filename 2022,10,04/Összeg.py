
#Keresés tétel!

'''''
t=[3,8,2,4,5,1,6]
t1=["d","f","g","h","j","u"]
#Egy sorozathoz egy értéket

osszeg=0
szorzat=1
kokat='' 
for num in t:
    osszeg=osszeg+num
    szorzat = szorzat * num
print("Szorzat: ",szorzat)
print("Összeg: ",osszeg)

t=[3,8,2,4,5,1,6]
megszamol = len(t)
count = 0
for num in t:
    if num >5:
        count=count+1
print("5-nél nagyobb: ",count)

#eldontes tetel
t=[3,8,2,4,5,1,6]
n = len(t)
ker = 5
i=0
while i<n and t[i] != ker:
    i = i+1

if i<n:
    print("Van ilyen: ",ker)

else:
    print("Nincs ilyen elem: ",ker)


t=[3,8,2,4,5,1,6]
n=len(t)
ker=5

i=0
while t[i] != ker:
    i =i+1

print("Hányadik helyen van: ",i+1)
'''

lista=[2,5,4,6,7,2,3,4]

#Összeg
oszeg=0
for num in lista:
    oszeg=oszeg+num
print(oszeg)

#megszámlálás

tobb=0
for num in lista:
    if lista[num] > 3:
        tobb +1
print(tobb)



