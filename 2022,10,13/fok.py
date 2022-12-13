

#from operator import ne

"""
fok= float(input("Adja meg a hőfokát! "))

if fok < 36:
    print("Nincs láza.")

elif fok >= 36.1 and fok <=37.5:
    print("Hőemelkedése van. ")
else:
    print("Láza van")
"""

lista=[]
fokok=[]
eredmeny=[]



for i in range(3):
    nev=input("Kérem adja meg a nevét! ")
    fok= float(input("Adja meg a hőfokát! "))
    lista.append(nev)
    fokok.append(fok)
    if fok < 36:
        print("Nincs láza.")
        eredmeny.append[eredmeny]
    elif fok >= 36.1 and fok <=37.5:
        print("Hőemelkedése van. ")
    else:
        print("Láza van")
print(eredmeny)

print(lista)
print(fokok)
print(f"Első ember neve {lista[0]}és az első ember hőmérsékléete {fokok[0]}")
print(f"Második ember neve{lista[2]}és a második ember hőmérsékléete {fokok[1]}")
print(f"Harmadik ember neve{lista[2]}és a harmadik ember hőmérsékléete {fokok[2]}")