kata=input('Masukan sebuah kata : ')
count=0    
pengulangan=0
for i in (kata):
    count=count+1
count2=0
x=count
for i in range(count):
    for j in (kata):
        pengulangan+=1
        count2=count2+1
        if count2==count:
            print(j)
            count=count-1
            count2=0
            break
print('pengulangan =',pengulangan)