'''''
kacatok = ["csat","Gombolyag","vonatjegy"]
print (kacatok)
kacatok.append('kulcskarika')
kacatok.append("egérfogó")
print(kacatok)
kacatok_felsorolva = ",".join(kacatok)
print('A kacatjaim:', kacatok_felsorolva, ',', sep='')
'''
kacatok = []

kacat = "Bármi"
while kacat != "elfogyott":
    kacat = input("Kérem a kacatot! ")
    if kacat != "elfogyott":
        kacatok.append(kacat)

kacatok_felsorolva = ",".join(kacatok)
print("A kacatjaim ", kacatok_felsorolva, ",",sep='')