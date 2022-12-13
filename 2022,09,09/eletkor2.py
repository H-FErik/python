
auto=input("Kérem adja meg a kocsi nevét")
végsebesség = int(input("Mennyivel megy ez a "+ auto+"?"))
orszag=input("Hol készül a "+  auto + ' ?')

mondat1 = orszag + " vidékein készül a " + auto + ", ami" + str(végsebesség) + 'km/h'
print(mondat1)

mondat2 = "{o} vidékein készül a {v} km/h végsebességre képes."  .format (o=orszag,a=auto,v=végsebesség)
print(mondat2)

mondat3a = "{o} védéken készült a {a}, ami {v} km/h végsebességre képes." .format (o=orszag,a=auto,v=végsebesség)
print(mondat3a)

print(f'{orszag=}, {auto=}, {végsebesség=}')