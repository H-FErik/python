from random import random



import random

dobas = random.randint(1,2)
if dobas ==1 :
    print("fej")
else:
    print("Irás")

dobas = random.choice(["Írás","Fej"])
print(dobas)
