
wr=open("H:\osz.txt","w")

wr.write("öszi szünet\n")
wr.write("2022,november,7. napon Hétfő van.\n")
x=0
for i in range (1,101):
    x+=1
    wr.write(str(x))
wr.close



