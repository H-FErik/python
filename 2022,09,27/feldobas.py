
fővárosok = ["Párizs","Bécs","Róma","Prága"]

for index in range(len(fővárosok)):
    print(index,fővárosok[index])

import random

feldobások = []
for _ in range (10):
    feldobás= random.choice(["f","í"])
    feldobások.append(feldobás)

print("A feldobások:",", ".join(feldobások))
fej_utan_fej = 0
for index, feldobas in enumerate(feldobások):
    if index > 0 and \
        feldobas == 'f' and feldobások[index-1] == 'f':
            fej_utan_fej += 1

print("Ennyiszer volt fej utan fej: ", fej_utan_fej)

''''
szamlalo = 0
osszeg = 0
while szamlalo < 100:
    szamlalo +=1 
    osszeg = osszeg + szamlalo
print("Összesen: ", osszeg)
'''

for i in range (1,101):
    osszeg = osszeg +1
    szamlalo = szamlalo+1
print(osszeg)
