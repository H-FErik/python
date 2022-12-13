#fakitermelés


'''
ABC falva erdőmérnőke programmal szeretné meghatározni az októberi fakitermelés tervét favágó 
csapata számára. Írjon programot, amellyel az erdőmérnök a következő problémákat tudja megoldani!

Hozza létre a megfelelő adatszerkezetetm amellyel a feladat megoldható. 
'''

import random

#1 A kitermelés 50 és 100 m3 között lehetséges naponta októberben!
fa=[]

for i in range(31):
    fa.append(random.randint(50,100))
print(fa)

#2 A legnagyobb fakitermelés mennyiségét a tervszerint 
max=fa[0]
for num in fa:
    if num < max:
        max=num
print(f"A legnagyobb fakitermelés mennyiségét a tervszerint: {max} ")

#3 A legkisebb fakitermelés mennyiségét a tervszerint

min=0
for num in fa:
    if num < min:
        min=num
print(f"A legnagyobb fakitermelés mennyiségét a tervszerint: {min} ")

#4 Hány alkalommal volt a fakitermelés mennyiségé 82 m3 felett?

count = 0
for i in fa:
    if i > 82:
        count+=1
print(f'{count} alkalommal volt 82 felett a fakitermelés mennyisége')

#5 mekkora volt a fakitermelés mennyisége októberi 20.-án?
mennyiség = len(fa)
ker = 20
print(f'{ker}fa volt kitermelve októberi 20.-án')

#6 mekkora volt a fakitermelés átlag mennyisége?
összeg = 0
összeg1=0
for szam in fa:
    összeg +=szam
    összeg1+=1
print(összeg)
print(összeg1)


print(f'Átlag= {összeg/összeg1}')

wr=open ('fakitermelés.txt','w')
wr.write(f'lista:,{fa}\n')
wr.write(f"A legnagyobb fakitermelés mennyiségét a tervszerint: {max} \n")
wr.write(f"A legnagyobb fakitermelés mennyiségét a tervszerint: {min} \n")
wr.write(f'{count} alkalommal volt 82 felett a fakitermelés mennyisége \n')
wr.write(f'{ker}fa volt kitermelve októberi 20.-án \n')
wr.write(f'Átlag= {összeg/összeg1} \n')

wr.close()





