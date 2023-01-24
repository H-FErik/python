def fugg(szám):
    if szám % 2 == 0:
        return "A ház a jobb oldalon áll"
    else:
        return "A ház az utca bal oldalán áll"

while True:
    utcanev = input("Adja meg az utca nevét")
    if utcanev == "":
        break
    házszám = int(input("Adja meg a ház számát"))
    print(fugg(házszám))
