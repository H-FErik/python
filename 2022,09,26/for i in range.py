'''
for i in range (1,101):
    print(i)

for i in range (100):
    print(i)

for i in range (1,100,2):
    print(i)

for i in range (1,100,1):
    print(i)
    
for i in range(100,1,2):
    print(i)
    '''
'''
szoveg="alma:korte:barack"
tomb = szoveg.split(":")
print(tomb)

szoveg="alma:korte:barack"
elso,masodik,harmadik=szoveg.split(":")
print(elso,masodik,harmadik)

szoveg="alma:korte:barack"
elso,masodik,harmadik=szoveg.split(":")
print(elso,masodik,harmadik)

sor = "vi farkas más"
if "farkas" in sor:
    print("ok")
    '''

ip=input("Ip cím: ")
ipDigitsStr=ip.replace(',','')
print(ipDigitsStr)