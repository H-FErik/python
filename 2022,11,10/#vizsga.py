#vizsga

#ahogy én gondolnám

nev = input('Add meg a vizsgázó nevét! ')
pont=int(input("Adja meg a pontszámot: "))

if pont>=48:
    print(nev,"Vizsga sikeres!")
elif pont < 48:
    print('vizsgája sikeretlen.')


#fügyvény

def dontes(pont):
    if pont<48:
        return False
    else:
        return True

nev=None
while  nev != '':
    nev= input("Adja meg a nevét")
    pont=int(input("Adja meg a pontszámát: "))
    if dontes(pont):
        print(f'{nev}, vizsgája sikeres.')
    else:
        print(f'{nev}, vizsgája sikeretlen.')
    

