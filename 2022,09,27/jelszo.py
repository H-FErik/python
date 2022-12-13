
from operator import truediv


bejutott = False

while not bejutott:
    felhasználónév = input("Kérem adja meg a felhasználónevét")
    jelszo = input("Kérem adja meg a jelszavát")
    if felhasználónév == "bori99" and jelszo=='kismehe<3':
        bejutott = true
        print("A beléőés megengedve")
        
    else:
        print("Belépés megtagadva")