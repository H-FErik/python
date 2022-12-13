fovarosok = []
fovarosok = ["Bécs","Bern","Párizs","London","Budapest","Varsó","Prága","róma","Madrid","Helsinki"]
fváros = None
while fváros !="":
    print('fváros jelenleg:',','.join(fovarosok))
    fvaros = input('Kérek egy fvarost ')
    if fvaros != '':
        fovarosok.append(fvaros)

#n - random.randint(1)len(fovarosok)-

for index,fovaros in enumerate(fovarosok):
    print(index,fovarosok)

while len(fovarosok)>0:
    print("fővárosaink: ", ",".join(fovarosok))
    melyik=input("Melyik főváros a legszebb, válaszd ki! ")
    if melyik in fovarosok:
        fovarosok.remove(melyik)
    else:
        print("Ilyen város nincs a listában! ")
