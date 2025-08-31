print('=======================================================')
print('|>>>            kalkulator bangun datar            <<<|')
print('=======================================================')
print(' ')
print('=======================================================')
print('|ketentuan:                                           |')
print('|masukan angka berikut untuk bangun                   |')
print('|1. Persegi                                           |')
print('|2. Persegi panjang                                   |')
print('|3. Jajar genjang                                     |')
print('|4. Layang-layang                                     |')
print('|5. Lingkaran                                         |')
print('|6. Trapesium                                         |')
print('=======================================================')
print(' ')
bangun=input('Masukan kode bangun : ')
match bangun:
    case '1':
        # persegi
        panjang=float(input('Masukan panjang sisi : '))
        print(f'Kaliling persegi anda adalah {4*panjang} \nLuas persegi anda adalah {panjang**2}')
    case '2':
        # persegi panjang
        panjang=float(input('Masukan panjang sisi : '))
        lebar=float(input('Masukan lebar sisi : '))
        print(f'Kaliling persegi panjang anda adalah {(2*panjang)+(2*lebar)} \nLuas persegi panjang anda adalah {panjang*lebar}')
    case '3':
        # jajar genjang
        panjang=float(input('Masukan panjang sisi : '))
        miring=float(input('Masukan panjang sisi miring : '))
        tinggi=float(input('Maskan tinggi jajar genjang : '))
        print(f'Kaliling jajar genjang anda adalah {(2*panjang)+(2*miring)} \nLuas jajar genjang anda adalah {panjang*tinggi}')
    case '4':
        # layang layang
        diagonal1=float(input('Masukan panjang diagonal 1 : '))
        diagonal2=float(input('Masukan panjang diagonal 2 : '))
        sisi1=float(input('Masukan panjang sisi 1 : '))
        sisi2=float(input('Masukan panjang sisi 2 : '))
        print(f'Kaliling layang-layang anda adalah {(2*sisi1)+(2*sisi2)} \nLuas layang-layang anda adalah {diagonal1*diagonal2}')
    case '5':
        # lingkaran
        jari=float(input('Masukan jari-jari lingkaran'))
        print(f'Kaliling lingkaran anda adalah {2*3.14*jari} \nLuas lingkaran anda adalah {(jari**2)*3.14}')
    case '6':
        # trapesium
        panjang1=float(input('Masukan panjang sisi pendek : '))
        panjang2=float(input('Masukan panjang sisi panjang : '))
        miring=float(input('Masukan panjang sisi miring : '))
        tinggi=float(input('Maskan tinggi jajar genjang : '))
        print(f'Kaliling trapesium anda adalah {panjang1+panjang2+miring+tinggi} \nLuas trapesium anda adalah {(panjang1-panjang2)*tinggi*1/2+panjang1*tinggi}')
print('tekan enter untuk end')
print('=========================================================================================================================')
input()