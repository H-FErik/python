#halmazok

homersekletek = []

pentek = [11, 19, 17]
szombat = [13, 22, 20]
vasarnap = [15, 30, 25]
hetfo = [7, 16, 15]

#halmazba hozzáadás

homersekletek.append(pentek)
homersekletek.append(szombat)
homersekletek.append(vasarnap)
homersekletek.append(hetfo)  

print=homersekletek

#lista első indexű elemének a kiírása
print(homersekletek[0])

#lista első indexéből a második elem
print(homersekletek[0][1])

#Az összes adat kiírása
for nap in homersekletek:
	      for meres in nap:
		        print(meres)

#Érték módosítása
homersekletek[0][1] = 22

#Érték beszúrása
homersekletek[0].insert(0, 0)

#sor beszúrása
homersekletek.insert(1, [0, 0, 0])

#Érték törlése, a pop() metódus visszatérési értéke a törölt érték
del homersekletek[0][0]
homersekletek[0].pop(0)

#Sor törlése
del homersekletek[1]
homersekletek.pop(1)

