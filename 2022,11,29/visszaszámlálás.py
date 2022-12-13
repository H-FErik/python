vissza = input("Adja meg az időt: ")
print(f"Visszaszámlálás {vissza}")

függ = input(" Fel kell függeszteni a visszazsámlálás? (i/n): ")
while vissza != 1:
    print(függ)
    if függ != "n":
        print(vissza-1)
    