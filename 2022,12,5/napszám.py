def hetnapja(honap, nap):
    napnev=["Vasárnap","Hetfo","Kedd","szerda","Csutortok","Pentek","Szombat"]
    napszam=[0,30,59,90,120,151,181,212,243,273,304,335]
    napsorszam=(napszam[honap+1]+nap) %7
    hetnapja= napnev[napsorszam]
    return napnev[napsorszam]

print(hetnapja(1,8))
