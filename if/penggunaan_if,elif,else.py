# LOGIKA -> KONDISI JIKA
# SYNTAX:
# if (KONDISI):
#     (perintah)


# nilai = 60

# if nilai >= 75:
#     print("Selamat, Anda lulus!")
# else:
#     print("Maaf, Anda belum lulus.")

# math                         python
# >                            >
# <                            <
# kurang dari sama dengan      <=
# lebih dari sama dengan       >=
# =                            ==
# tidak sama dengan            !=



# definisi input
print(' ')
print('                     ---------')
print('                 --/          \\--')
print('           -----/                 \\-----')
print('          /                             \\')
print('         /                               \\')
print('        /                                 \\')
print('       /                                   \\')
print('      /                                     \\')
print('     /                                       \\')
print('    |                                         |')
print('    |              penentu nilai              |')
print('    |                                         |')
print('     \\                                       /')
print('      \\                                     /')
print('       \\                                   /')
print('        \\                                 /')
print('         \\                               /')
print('          \\                             /')
print('           \\                           /')
print('            \\                         /')
print('             \\                       /')
print('              \\                     /')
print('               |----------|--------|')
print('               |     ( )  |        |')
print('               |      |   |        |')
print('               |===================|')
print('               |===================|')
print('               |===================|')
print(' ')
nama = input('masukan nama anda                       : ')
nilai = float(input('masukan nilai anda                      : '))
kehadiran = int(input('masukan berapa kali kehadiran anda      : '))
print(' ')
maks=28
if nilai >= 80 and (kehadiran*(maks**(-1))>= 0,75):
    print(nama+', nilai anda adalah A')
elif 70 <= nilai < 80:
    print(nama+', nilai anda adalah B')
elif 60 <= nilai < 70:
    print(nama+', nilai anda adalah C')
elif 50 <= nilai < 60:
    print(nama+', nilai anda adalah D')    
elif nilai < 50:
    print(nama+' nilai anda adalah E') 
else :
    print('nilai anda adalah X')
print('=========================================================')