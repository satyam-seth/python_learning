a=10
b=0 #Or b=5
try:
    c=a/b
    print(c)    #Or print(d)
except (NameError,ZeroDivisionError):
    print('Exception Handler')
print('Rest Of The Code')