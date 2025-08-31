# switch adalah cara mudah menggunakan if elif else

# logika switch.(match-cale)
# logika ini adalah pengandaian dari memasukan nilai yang cocok

# sama dengan if elif namun 86% lebih efesien

# syntax
# match (variabel):
#     case (isi pertama):
#         argument 1

# def input
hari=int(input('Masukan angka (1-7) : '))
# logika switch
match hari:
    case 1:
        print('Hari ini hari senin')
    case 2:
        print('Hari ini hari selasa')
    case 3:
        print('Hari ini hari rabu')
    case 4:
        print('Hari ini hari kamis')
    case 5:
        print('Hari ini hari jumat')
    case 6:
        print('Hari ini hari sabtu')
    case 7:
        print('Hari ini hari minggu')
    # else
    case _:
        print('hari tidak di ketahui')