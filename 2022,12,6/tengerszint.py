'''
Írjon programot tengerszint néven!
Kérjen be addig földrajzi hely nevét és tengerszint feletti magasságát, 
amíg üres karaktert nem üt a felhasználó!

Írjon függvényt!
a tengerszintek néven, amely alföldet,"dombságot,"középhegység" és "magashegység" különböztet meg!
200m alatt alföldet,
200m és 500m között dombságot
500m és 1500m között középhegység
1500m magashegység


# Fájl írása tenger.txt néven az amelyben az összes eredmény szerepel!

Beadandó

A program forráskódja .py kiterjesztéssel a Githubra!
A program forráskódja .txt kiterjesztéssel dkt-ra!

'''
def tengerszint2(tengersz):
    if tengersz < 200:
        return("Alfold")
    elif tengersz >200 and 500:
        return("Dombság")
    elif tengersz >500 and 1500:
        return("Hegység")
    else:
        return("Magashegység")
foldr=None
while foldr != " ":
    foldr = input("Kérem adja meg a földrajzi helyet: ")
    if foldr != "":
        tengersz = int(input("Kérem adja meg a tengerszintet: "))
    else:
        break

print(f"A tengerszint: {tengerszint2(tengersz)}, {foldr}-ban(-ben)")

