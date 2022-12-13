koltes=int(input("mennyit költött kedden?"))
koltes2=int(input("Mennyit költött szerdán?"))

if koltes<koltes2:   
    print(f"kedden ",koltes2,"Ft-t Költött")
elif koltes2<koltes:
    print(f"Szerdán ",koltes,"Ft-t Költött")
     
else:
    print("Ugyanannyit költött")