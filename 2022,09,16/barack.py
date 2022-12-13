
barack_ár = input("Mennyibe fáj a barack ")
barack_szám = int(input("Barack száma "))

körte_ár = input("Mennyibe fáj a körte ")
körte_szám = int(input("Körte száma "))

if barack_szám < körte_szám:
    print("Körtéből van több")
elif barack_szám > körte_szám:
    print("Barackból van több")
else:
    print("Hiba")

if barack_ár < körte_ár:
    print("Körtéből van több")
elif barack_ár > körte_ár:
    print("Barackból van több")
else:
    print("Hiba")
