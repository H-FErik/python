'''''
print("eldöntés - True/false")
wr=open("H:\eldöntés.txt",'w')
t=[2,5,6,9,10,12,4]
wr.write('t=[2,5,6,9,10,12,4]')
n= len(t)
wr.write(f"{n}\n")
ker=5
wr.write(f"A keresett szám: {ker}")
i=0
while i<n and t[i] != ker:
    i = i+1
if i<n:
    print("Van ilyen ", ker)
    wr.write(f'van ilyen, {ker}\n')
else:
    print("Nincs ilyen ", ker)
    wr.write(f"nincs ilyen {ker}\n")
wr.close()

print("kiválasztás")

# kiválasztás, kiválogatás, szétválogatás

t=[2,5,6,9,10,12,4]
n=len(t)
ker=5
i=0 #hely
while t[i] != ker:
    i=i+1
print("ezen a helyen található ", i+1) #0-val kezdődik

print('lineáris keresés')
print('eldöntés (van-nincs), kiválasztás tétel (hely megadás')
#lista t= [2,5,6,9,10,12,4]
n=len(t)
print(n)
ker = 5
I=0
while i<n and t[i] != ker:
    i=i+1
    if (i<n):
        print(f'van {ker} elem a listában')
        print(f'helye {i+1}')
    else:
        print(f'nincs{ker}elem a listában')

maxElem=0
maxElem=t[0]
for elem in t:
    if elem > maxElem:
        maxElem=elem
print(maxElem)

minElem=t[0]
for elem in t:
    if elem < minElem:
        minElem=elem
print(minElem)

print(f"Egyszerű számtani átlag : {(minElem + maxElem)/2}")

#max
wr = open('max.txt','w')
t=[2,4,7,1,8,5,9]
wr.write(f't=[2,4,7,1,8,9]\n')
maxElem = t[0]
for elem in t :
    if elem > maxElem:
        maxElem = elem
print(f'{maxElem}\n')
wr.write(f'{maxElem}\n')
wr.close()

#min
minElem = t[0]
for elem in t:
    if elem > minElem:
        minElem = elem
print(f'{minElem}\n')
wr.close

t=[2,4,7,1,8,5,9]
#másolás
d = []
c = []
d = []
def dupla (num):
    return num*2

for elem in t:
    d.append(dupla(elem))
    if elem%22 == 0:
        c.append(elem)
    if elem < 5:
        d.append(elem)
    if elem%2 !=0:
        e.append(elem)
print(d)
print(c)

print('kiválogatás')
'''
#buborékrendezés
t=[2,4,7,1,8,5,9]
n =len(t)
for i in range(n-1,0,-1):
    for j in range(0,i):
        if(t[j]>t[j+1]):
            tmp = t[j+1]
            t[j+1] = t[j]
            t[j] = tmp
print(t)
