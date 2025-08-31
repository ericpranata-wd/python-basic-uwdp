# header
print('-==++==--==++==--==++==--==++==--==++==--==++==--==++==--==++==--==++==--==++==--==++==-')
print('|>>>>>                                                                            <<<<<|')
print('|>>                              ganjil genap detector                               <<|')
print('|>>>>>                                                                            <<<<<|')
print('-==++==--==++==--==++==--==++==--==++==--==++==--==++==--==++==--==++==--==++==--==++==-')
# definisi input
angka = int(input('                         masukan angka yang akan dideteksi: '))
# pendeteksi dengan menggunakan sisa pembagian angka dengan 2
modulo=angka%2
# penentu keluaran jika modulo = 0 (0 = genap)
if modulo==0:
    print('-==++==--==++==--==++==--==++==--==++==--==++==--==++==--==++==--==++==--==++==--==++==-')
    print('|>>>>>                                                                            <<<<<|')
    print('|>>                                 Angka anda genap                                 <<|')
    print('|>>>>>                                                                            <<<<<|')
    print('-==++==--==++==--==++==--==++==--==++==--==++==--==++==--==++==--==++==--==++==--==++==-')
    # meminta input agar program tidak hilang atau mati sebelum output akan dibaca
    input('                                 tekan enter untuk exit')
# else jika kondisi 1 false atau modulo = 1 (1 = ganjil)
else:
    print('-==++==--==++==--==++==--==++==--==++==--==++==--==++==--==++==--==++==--==++==--==++==-')
    print('|>>>>>                                                                            <<<<<|')
    print('|>>                                 Angka anda ganjil                                <<|')
    print('|>>>>>                                                                            <<<<<|')
    print('-==++==--==++==--==++==--==++==--==++==--==++==--==++==--==++==--==++==--==++==--==++==-')
    # meminta input agar program tidak hilang atau mati sebelum output akan dibaca
    input('                                 tekan enter untuk exit')