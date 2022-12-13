'''''
def alahuzas():
    for _ in range(10):
        print('.',end ='')
    print()


print('ez egy fontos figyelmeztetés')
alahuzas()
print("minden sora nagyon fontos!")
alahuzas()
print('Komolyan!')
alahuzas()

def pluszkettő(szám):
    print(szám+2)

print('5+2= ',end='')
pluszkettő(5)
def pluszkettő(szám):
    return(szám+2)
print('5+2= ',pluszkettő(5))
'''

#szélsőérték (max,min)
t=[2,5,6,9,10,12,4]
maxElem=t[0]
for elem in t:
    if elem > maxElem:
        maxElem=elem
print(mexElem)

minElem=t[0]
for elem in t:
    if elem < minElem:
        minElem=elem
print(minElem)

