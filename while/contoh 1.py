angka =5
tebak=None
while tebak != angka:
    tebak = int (input ('Masukan tebakan : '))
    if tebak != angka:
        print('tebakan anda salah')
    else:
        print('tebakan anda benar')