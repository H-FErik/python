

liter=0
max=3,5

#viz=input("Kérem adja meg mennyi dl vizet ivott! ")
#print("Ennyi literből",liter,"Ennyit ittál meg:",viz)

while liter != max:
    deci = int(input("Hány dl vizet ittál "))
    liter += deci/10
    print("Eddig ennyi liter vizet ittál meg",liter)

    if deci ==0:
        print("0-át nem lehet megadni!!!")
        break

    if liter == 2.5:
        print("Elérted a 2,5 litert, szép munka")


if liter == max:
    print("Viszlát, holnap T.")
