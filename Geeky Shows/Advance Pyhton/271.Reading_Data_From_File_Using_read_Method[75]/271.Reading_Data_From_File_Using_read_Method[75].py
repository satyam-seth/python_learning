f=open('temp.txt')
data1=f.read(2)
data2=f.read(2)
data3=f.read()
data4=f.read()
print(data1)
print(data2)
print(data3)
print(data4)
f.close()
print('Completed!!..')