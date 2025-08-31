import os
import random

# header
def header():
    print('|===================|')
    print('|                   |')
    print('|   BERMAIN TOGEL   |')
    print('|                   |')
    print('|===================|')
header()

# pemilihan angka random
lst=[1]
for i in range (2,11):
    lst=lst+[i]
angka=random.choice(lst)
print (f'angka orang dalam {angka}')

# looping untuk tebak!=angka
tebak=None
while tebak!=angka:
    tebak= int (input('Masukan angka : '))

    # jika tebakan benar
    if tebak==angka:
        print()
        print('|===================|')
        print('|                   |')
        print('|   Tebakan benar   |')
        print('|                   |')
        print('|===================|')
        print()
        x=input('apakah anda ingin lanjut? (1=ya / 0=tidak) : ')

        # jika ingin mengulang
        if x=='1':
            os.system("cls")
            header()
            angka=random.choice(lst)
            print (f'angka orang dalam {angka}')
            tebak=None

        # jika tidak ingin mengulang
        else:
            ()

    # 
    elif tebak<angka:
        print()
        print('|==========================================|')
        print('|   Tebakan kurang dari angka sebenarnya   |')
        print('|==========================================|')
        print()
    elif tebak>angka:
        print()
        print('|==========================================|')
        print('|    Tebakan lebih dari angka sebenarnya   |')
        print('|==========================================|')
        print()