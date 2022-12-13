class Híres_katona:
    def __init__(self,nev,foglalkozás,nemzetiség):
        self.nev= nev
        self.foglalkozás = foglalkozás
        self.nemzetiség= nemzetiség
    def elotag(self):
        if nemzetiség == "n":
            return "Herr"
        else:
            return"Mister"
        
hires_katona = []
for _ in range (3):
    név=input ('Kérem adja meg a nevét!')
    foglalkozás = input ('Kérem adja meg a foglalkozását!')
    nemzetiség =input ('Kérem adja meg a nemzetiségét!')
    híres_katona1 = Híres_katona(név,foglalkozás,nemzetiség)
    híres_katona.append(híres_katona1)

for hkatona in híres_katona:
    print(f"{Híres_katona.elotag}{Híres_katona.név} egy híres {Híres_katona.foglalkozása}")