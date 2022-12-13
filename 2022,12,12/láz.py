def láz(hom):
    if hom>37.5:
        return 'lázas'
    else:
        return 'nem lázas'

nev = None

while nev != ' ':
    nev = input ('Kérem adja meg a nevét!')
    if nev:
        hom = float(input ('Kérem adja meg a hőmérsékletét!'))
        if laz(hom):
            print(f"{nev} lázas ") 
        else:
            print(f"{nev} nem lázas")    