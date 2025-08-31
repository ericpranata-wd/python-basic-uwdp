# contoh soal 1
ls3=int(input('Masukan angka untuk start list 3 : '))
lst1=[1]
lst2=[0]
lst3=[ls3]
panjang=int(input('Masukan panjang deret            : '))
for i in range (panjang-1):
    lsti=lst1[i]*2
    lst1.append(lsti)
    if (i+1)%3==0:
        lsti=lst2[i]-1
    else:    
        lsti=lst2[i]+1
    lst2.append(lsti)
    lsti=lst3[i]-1
    lst3.append(lsti)
print()
# print('='*3+2)
print(f'1.  {lst1}')
print(f'2.  {lst2}')
print(f'2.  {lst3}')

ada 5 menu
setiap menu dikasi harga
dapat diulang terus
jika pengguna memasukan menu ke 0 program memberi rincian harga 

# burger  15k
# ayam    18k
# teh es  7k
# nasi    5k
# ikan    15k