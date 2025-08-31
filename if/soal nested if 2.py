# header
print('----------------------------------------')
print('|                                      |')
print('|      penentu masuk kuliah/tidak      |')
print('|                                      |')
print('----------------------------------------')
print(' ')

# definisi variabel
cuaca=input('Masukan cuaca (hujan/tidak hujan): ')
# if tingkat 1 (kondisi 1)
if cuaca==('hujan'):
    # definisi variabel untuk kondisi 1 true (hujan)
    dosen=input('Masukan jenis dosen (killer/tidak killer): ')
    # if tingkat 2 (kondisi 1.1)
    if dosen==('killer'):
        print('Anda bolos kuliah')
    # else jika kondisi 1.1 tidak terpenuhi (dosen tidak killer)
    # kondisi 1.2
    else:
        print('Anda masuk kuliah')
# kembali ke tingkat 1 untuk kondisi 1 false (tidak hujan)
# kondisi 2
else:
    # definisi variabel untuk kondisi 1 false (tidak hujan)
    mood=input('masukan mood anda (mager/tidak mager): ')
    # if tingkat 2 untuk kondisi 2(kondisi 2.1)
    if mood==('mager'):
        print('Anda bolos kuliah')
    # else jika kondisi 2.1 false (tidak mager)
    # kondisi 2.2
    else:
        # definisi variabel untuk kondisi 2.2.1
        penampilan=input('Masukan penampilan dosen (cantik/sexy/biasa): ')
        # if tingkat 3 (kondisi 2.2.1)
        if (penampilan==('sexy') or penampilan==('cantik')):
            print('Anda masuk kuliah')
        # else jika kondisi 2.2.1 false (biasa)
        else:
            print('Anda ngantin')