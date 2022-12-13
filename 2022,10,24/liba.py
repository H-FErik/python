from pickle import APPEND


liba=[2,4,7,9,8,5,4,3] 
összeg=0
n=len(liba)
for i in range(0,len(liba)):
    összeg=összeg+liba[i]
print(összeg)
print(n)
átlag=sum(liba)/n
print("A libák kg átlaga",átlag,"kg")
újliba=[4,7,8,6,5,3]
liba.append(újliba)
print(liba)

print('Egy sorozathoz egy sorozatot rendel')
print('Másol')

liba2=[2,3,4,5,6,7,7]
liba3=["fekete liba,tarka liba"]


róka = 0
for i in range(0,len(liba)):
    if liba(i)>=5:
        róka += 1
print(róka)


