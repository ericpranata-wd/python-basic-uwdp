# header
print('   ===================')
print('  /   *               \\')
print(' /                  *  \\')
print('/                *      \\')
print('|>  Memasak kue vegan  <|')
print('\\                       /')
print(' \\   *                 /')
print('  \\             *     /')
print('   ====================')
print(' ')

# definisi variabel
bp=input('apakah anda menggunakan beaking powder (ada/tidak): ')
waktu=int(input('masukan lama pemanggangan(menit): '))

# penggunaan if tingkat 1
if bp.lower()==('ada'):
    # penggunaan if tingkat 2
    if waktu<15:
        print('Kue belum matang')
        print('==================================')
    else:
        # penggunaan if tingkat 3
        if waktu<30:
            print('Kue sudah matang')
            print('==================================')
        else:
            print('Kue anda gosong')
            print('==================================')
# kembali ke tingkat satu untuk kondisi bp tidak ada
else:
    print('Kue anda bantat')
    print('==================================')