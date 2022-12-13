wr = open('10E2f.txt','w')
wr.write('Csordásné Kovács Judit')
wr.close

re = open ('10E2f.txt','r')
line = re.readline()
print(line)
re.close()

re = open ('10Ef.txt','r')
line =  re.readline()
while line !='':
    line = line.strip()
    print(line)
    line = re.readline()
re.close()
