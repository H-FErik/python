'''''
def megfelel(magassag):
    if int(magassag)<170:
        return False
    else:
        return True

nev = None
while nev !='':
    nev = input ('Add meg a neved! ')
    if nev !='':
        m=input("Hány centi magas? ")
        if megfelel(m):
            print(nev,"megfelelő magasságú.")
        else:
            print(nev,"magassága nem megfelelő modellnek.")


nev=input("Kérem a vizsgázó nevét! ")
pont=int(input("Hány pontja lett? "))

if pont < 150:
    print(f"{nev}, nem szerezhet nyelvvizsgát")

elif pont > 150 and pont < 170:
    print(f"{nev}, Megkapja a nyevvizsgát")

elif pont > 170:
    print(f"{nev}, Megkapja az emeltfökú nyelvvizsgát.")

'''



