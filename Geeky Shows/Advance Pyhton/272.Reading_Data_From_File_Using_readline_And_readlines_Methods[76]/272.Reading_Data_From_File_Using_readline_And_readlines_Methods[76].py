f=open('temp.txt')
data1=f.readline()
data2=f.readline(2)
print(data1,end='')
print(data2)
f.close()
print('--End--')
f=open('temp.txt')
data3=f.readlines()
print(data3)
for i in data3:
    print(i,end='')
f.close()
print('\n--End--')
f=open('temp.txt')
data4=f.readlines(1)
print(data4)
for i in data4:
    print(i,end='')
f.close()
print('--End--')