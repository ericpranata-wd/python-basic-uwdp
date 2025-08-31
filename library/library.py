# library merupakan koleksi/kumpulan program 
# yang menunjang script dasar

# syntax
# import<nama library>

# biasanya library selalu diletakan di bagian teratas coding.

# contoh library python yg sifatnya default
# 1. (os) ganti directory, hapus tampilan, cek operation system.
# 2. (Tabulate) membuat table
# 3. (timer) Mengatus jeda program/paralel computing
# 4. (random) menghasilkan bilangan acak

import os
def header():
    print('|=============================|')
    print('|                             |')
    print('|   Penghitung luas persegi   |')
    print('|                             |')
    print('|=============================|')
lanjut=1
while lanjut == 1:
    s=float(input('Masukan panjang sisi persegi : '))
    luas=s*2
    print(f'Luas persegi anda adalah {luas}')
    lanjut = int (input('Apakah anda ingin mencari luas persegi lagi? (1 = ya / 0 = tidak) : '))
    if lanjut==0:
        print('|==============================================|')
        print('|                                              |')
        print('|  Terimakasih untuk menggunakan program saya  |')
        print('|            Made by : Eric Pranata            |')
        print('|                                              |')
        print('|==============================================|')
    else: 
        os.system("cls")
        header()