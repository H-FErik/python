
'''
a = 3
b = 5
'''
a=int(input('Kérek egy számot')) 
b=int(input('Kérek egy másik számot'))
c = a+b

a=input('Kérek egy számot')
b=input('Kérek egy másik számot')
c = a+b

print(a)
print(b)
print(a+b)
print(c)

print(f'Az {a} és {b} összege {c}-vel egyenlő')

if a>b:
    print(f'a nagyobb mint b')
    print(f'{a} nagyobb mint {b}')
elif b>a:
    print(f'b nagyobb mint a')
    print(f'{b} nagyobb mint {a}')
else:
    print(f'A két szám egyenlő')

if a%2 == 0:
    print('páros')

else:
    print('páratlan')