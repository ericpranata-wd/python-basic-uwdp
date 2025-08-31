print('|=======================|')
print('|   penjumlahan deret   |')
print('|=======================|')

n=int(input('masukan nilai n : '))
n3=n
n2=n-1
for i in range (1,n):
    n=n+(n2)
    n2=n2-1
# for i in range (n,0,-1):
#     n=n//n
print (f'penjumlahan deret dari n={n3} adalah {n}')
print (f'')
input ('tekan enter untuk exit   ')