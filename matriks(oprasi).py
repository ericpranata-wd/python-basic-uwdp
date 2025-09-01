print('1. pertambahan')
print('2. pengurangan')
print('3. perkalian')
pilih=(input('Masukan pilihan anda : '))

tinggi=int(input('Masukan panjang matriks : '))
panjang=int(input('Masukan tinggi matriks : '))
a=panjang
b=tinggi
matriks1=[]
matriks2=[]
hasil=[]
for i in range(panjang):
    temp=[]
    for j in range(tinggi):
        temp.append(int(input(f'Masukan angka di kordinat {i+1,j+1} : ')))
    matriks1.append(temp)
    print()
for i in range(panjang):
    print(matriks1[i])
print()
tinggi=int(input('Masukan panjang matriks : '))
panjang=int(input('Masukan tinggi matriks : '))
c=panjang
d=tinggi
for i in range(panjang):
    temp=[]
    for j in range(tinggi):
        temp.append(int(input(f'Masukan angka di kordinat {i+1,j+1} : ')))
    matriks2.append(temp)
    print()
for i in range(panjang):
    print(matriks2[i])
print()

ac=0
bd=0

if pilih=='3':
    # perkalian
    for i in range(panjang):
        temp=[]
        for j in range(tinggi):
            a=matriks1[j][i]*matriks2[i][j]
            temp.append(a)
        a=temp[0]+temp[1]+temp[2]
        hasil.append(a)
    
if a!=c:
    ac=a-c
    if ac<0:
        panjang=c
        ac=-ac
        # kurang panjang pada matriks 2
        temp=[]
        for i in range(a):
            temp.append(0)
        for i in range(ac):
            matriks1.append(temp)
    else:
        panjang=a
        temp=[]
        for i in range(c):
            temp.append(0)
        for i in range(ac):
            matriks2.append(temp)
        y=c
        # kurang panjang pada matriks 1
if b!=d:
    bd=b-d
    if bd<0:
        tinggi=d
        bd=-bd
        for j in range(panjang):
            for i in range(bd):
                matriks1[j].append(0)
            # kurang tinggi pada matriks 2
    else:
        tinggi=b
        for j in range(panjang):
            for i in range(bd):
                matriks2[j].append(0)
        # kurang tinggi pada matriks 1
if bd<ac:
    pan=bd
else:
    pan=ac
if pilih=='3':
    # perkalian
        for i in range(pan):
            temp=[]
            a=[]
            for l in range(pan):
                a.append(0)
            for j in range(pan):
                for k in range(pan):

                    a[k]=matriks1[i][j]*matriks2[j][k]+a[k]
            for p in range(pan):
                temp.append(a[p])
            hasil.append(temp)
for i in range(panjang):
    print(hasil[i])

else:    
    for i in range(panjang):
        temp=[]
        for j in range(tinggi):
            if pilih=='1':
                temp.append((matriks1[i][j])+(matriks2[i][j]))
            if pilih=='2':
                temp.append((matriks1[i][j])-(matriks2[i][j]))
        hasil.append(temp)
print()
for i in range(panjang):
    print(hasil[i])