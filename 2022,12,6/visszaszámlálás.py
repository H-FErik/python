t= int(input("Hány órás visszaszámlálást tervezünk? "))
i=0
halasztva = 0
while i < t:
    print(f"Visszaállítás:{t-i}")
    kell_e = input("Fel kell függeszteni a visszaszámlálást (I/N)? ")
    if (kell_e == "i"):
        halasztva += 1
    i+=1
print(f"A rakéta a visszaszámlálást követően ennyi órával indul:{t+halasztva}")