a=[]
b=[]
hasil=0
l=int(input('Masukan dimensi vektor : '))
print()
print()
print('Untuk vektor a')
print()
print()
for i in range(1,l+1):
    a1=int(input(f'Masukan angka di a{i} : '))
    a.append(a1)
print()
print()
print('Untuk vektor b')
print()
print()
for i in range(1,l+1):
    b1=int(input(f'Masukan angka di b{i} : '))
    b.append(b1)
for i in range (l):
    baris1=a[i]*b[i]
    hasil=hasil+baris1
print(hasil)