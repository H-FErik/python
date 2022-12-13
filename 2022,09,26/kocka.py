import random

kocka = [1,2,3,4,5,6]
dobas=0
hatos=0

while dobas != 1000000:
    dobas+=1
    print(random.choice(kocka))
    if kocka == 6:
        hatos+=1
    print(hatos)