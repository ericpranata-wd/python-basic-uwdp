n=0
while n==0:
    print('Pilih salah satu angka di bawah')
    print('0. Exit')
    print('1. Posisi')
    print('2. Kecepatan')
    print('3. Percepatan')
    pilihan=(input('Masukan angka : '))
    match pilihan: 
        case '0':
            n=1
        case '1':
            n=1
            p0=float(input ('Masukan posisi awal partikel (satuan=meter) : '))
            t=float(input('Masukan waktu yang ditempuh partikel (satuan=detik) : '))
            hasil=p0+t**3-(2*t)+6
            info='Posisi'
            satuan='meter'
        case '2':
            n=1
            t=float(input('Masukan waktu yang ditempuh partikel (satuan=detik) : '))
            hasil=(3*(t**2))-2
            info='Kecepatan'
            satuan ='m/s'
        case '3':
            n=1
            t=float(input('Masukan waktu yang ditempuh partikel (satuan=Detik) : '))
            hasil=6*t
            info='Percepatan'
            satuan='m/s\u00b2'
        case _:
            print('=========================')
            print('Masukan angka yang sesuai')
            print('=========================')
print(f'{info} partikel anda adalah {hasil} {satuan}')