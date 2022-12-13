
név= input("Mi a gép neve? ")
mukodik = True if input ("Műkodik (i/n)? ") == 'i' else False
ar = int(input("Mi az ára? "))

if(név == 'ZX Spectrum' or név == 'c64') and mukodik and ar <=25000:
    print("Biznisz!!!! ")
else:
    print("Gagyi nyócbitesek.... Kinek kellenek? ")


