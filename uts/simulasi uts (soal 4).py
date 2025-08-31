print('Pilih gender\n0. Perempuan\n1. Laki-laki')
gender=input('Pilih salah satu angka diatas : ')
print('Pilih jabatan\n0. Staff biasa\n1. Manager\n2. Eksekutif manager')
jabatan=input('Pilih salah satu angka diatas : ')
cuti=5
peringatan='.'
match gender :
    case '0':
        cuti=cuti+5
        
    case _:
        ()

match jabatan:
    case '1':
        cuti=cuti+7
    case '2':
        cuti=cuti+14
    case _:
        cuti=cuti+5
print('Apakah anda sedang hamil\n0. tidak\n1. ya')
kondisi=input('Pilih salah satu angka diatas : ')
match kondisi:
    case '0':
        ()
    case '1':
        match gender:
            case '0':
                cuti=cuti+14
                
            case _:
                peringatan=',dan anda diperkenankan ke rumah sakit selama satu hari (bukan cuti)'
print(f'Anda diperkenankan {cuti} hari cuti{peringatan}')