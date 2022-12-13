celsius=int(input("Kérem adja meg hogy menny fok van (C°"))
kelvin=celsius+276.15
print(kelvin)

if celsius < 21 and celsius > 16:
    print("A hőmérséklet jó")
elif celsius > 22:
    print("A hőmérséklet magas")
elif celsius <16 :
    
    print("A hőmérséklet alacsony")