# contoh fibonaci 
n=[0,1]
lenght=int(input('Masukan panjang deret : '))
for i in range (2,lenght):
    ni=n[i-1]+n[i-2]
    n.append(ni)
print(n)