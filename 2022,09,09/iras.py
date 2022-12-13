
'''
Német = 19
Brit = 10
Cseh = 21
Lengyel = 23
Magyar =27

nettó_ár= float(input('Hogyér\' adnak egy mütyürkét '))
print(f'A mütyürke brutto árai:')
print(f'{nettó_ár*(1+Német/100):^10.2f} picula Németországban.')
print(f'{nettó_ár*(1+Brit/100):^10.2f} picula Nagy-Britanniában.')
print(f'{nettó_ár*(1+Cseh/100):^10.2f} picula Csehországban.')
print(f'{nettó_ár*(1+Lengyel/100):^10.2f} picula Lengyelországban.')
print(f'{nettó_ár*(1+Magyar/100):^10.2f} picula Magyarországban.')
'''
'''
Op = 1539
Fp = 2750

hofok=int(input("Kérem adjon meg egy hőfokot! "))

if hofok < Op:
    print("Szilárd")
elif hofok > Fp:
    print("Folyékony")
else:
    print("Gáz")
    '''