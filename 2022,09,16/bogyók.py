
név = input("Mi az ő neve? ")
bogyók = int(input("Hány bsogyója van "))

if bogyók < 10:
    minősítés = "zsenge"
elif bogyók > 20:
    minősítés = "nagy koponya"
else:
    minősítés = "gyüjtögető"

print(f"{név} egy {minősítés}.")