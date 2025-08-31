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