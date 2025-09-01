# 1. Input angka yang dicari dari daerah lst
angka=int(input('Masukan angka yang ingin dicari dalam array : '))
lst=[1,3,5,7,9,11,13]
count=0
for i in (lst):
    if lst[i]==angka:
        print(f'Menemukan angka yang dicari pada index {count}')
        break
    count+=1