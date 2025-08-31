print('Pilih salah satu dari angka berikut ')
print('0. Exit')
print('1. Octahedron')
print('2. Hexagon')
print('3. Honeycomb') 
bangun= (input('Masukan angka atau kode : '))
match bangun:
    case '0':
        ()
    case 1:
        print('Octahedron')
        s=float(input ('Masukan panjang sisi Octahedron : '))
        hasil=12*s
        bangun=('Octahedron')
    case '2':
        print('Hexagon')
        s=float(input('Masukan panjang sisi Hexagon : '))
        hasil=6*s
        bangun='Hexagon'
    case '3':
        print('Honeycomb')
        s=float(input('Masukan panjang sisi Honeycomb : '))
        n=float(input('Masukan banyak sisi Honeycomb : '))
        hasil=(n*(6*s))-(n*s)
        bangun='Honeycomb'
    case _:
        print('Nomor tak dikenal')
        input('tekan enter untuk exit')
        # untuk tidak kembali mengeprint?
print(f'Keliling bangun {bangun} anda adalah {hasil}')