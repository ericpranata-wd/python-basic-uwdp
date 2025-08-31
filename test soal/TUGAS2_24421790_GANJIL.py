print('|===========================================================================|')
print('|>>>                                                                     <<<|')
print('|>>                         PENGHITUNG BATU KAKEK                         <<|')
print('|>>>                                                                     <<<|')
print('|===========================================================================|')
print('|>>>                                                                     <<<|')
print('|>>                            BY:ERIC PRANATA                            <<|')
print('|>>>                                                                     <<<|')
print('|===========================================================================|')
print(' ')
hari=input('Masukan nama hari ini (senin sampai minggu)              : ')
waktu=input('Masukan waktu hari ini (pagi/siang)                      : ')
jarak=float(input('Masukan jarak perjalanan kakek ke pasar (satuan=m/meter) : '))
spas=19
if waktu=='siang':
    jrk=jarak//10
    batu=(5)*jrk
elif waktu=='pagi':
    if hari=='senin' or hari=='sennin':
        jrk=jarak//10
        batu=(10)*jrk
    elif hari=='selasa' or hari=='rabu':
        jrk=jarak//5
        batu=(5)*jrk
    elif hari=='kamis' or hari=='jumat' or hari=='jummat' or hari=='sabtu':
        jrk=jarak//10
        batu=(8)*jrk
    elif hari=='minggu':
        batu=0
    else:
        print('input hari salah')
else:
    print('input waktu salah')
s=batu%10
spasi=batu//10
sk=spasi%2
spasikanan=spasi//2
print
print(s,spasi,sk,spasikanan)
print(f'|========================{'='*spasi}=========|')
print(f'|>>>                     {' '*spasi}      <<<|')
print(f'|>> Kakek mengambil {batu} buah batu {' '*spasikanan}<<|')
print(f'|>>>                     {' '*spasi}      <<<|')
print(f'|========================{'='*spasi}=========|')
print(f'')

# tampilan=input('Apakah tampilan makanan rapi? (y/t)          : ')
# ukuran=input('Apakah porsi makanan (kecil/sedang/besar)    : ')
# harga=float(input('Masukan harga (satuan=Rupiah)                : '))
# bintang=float(input('Masukan rating/bintang restoran (1 sampai 5) : '))
# if bintang>=4:
#     if ukuran=='kecil':
#         if harga>500000:
#             print('Rasa makanan adalah biasa.')
#     elif ukuran=='sedang' or ukuran=='besar':
#         if harga<500000:
#             print('Rasa makanan adalah enak.')
# if bintang<4:
#     if ukuran=='sedang' or ukuran=='besar':
#         if tampilan=='y':
#             print('Rasa makanan adalah enak.')
#         if tampilan=='t':
#             print('Rasa makanan adalah biasa.')
#     elif ukuran=='kecil':
#         if harga<500000:
#             print('Rasa makanan adalah enak.')
#         if harga>=500000:
#             print('Rasa makanan adalah tidak enak.')