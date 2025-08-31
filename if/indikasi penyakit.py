print('================================================')
print('|                                               |')
print('|                                               |')
print('|       /\\                     /\\               |')
print('|      /  \\  /\\               /  \\  /\\          |')
print('|  ---/    \\/   \\    --------/    \\/   \\    ----|')
print('| /              \\  /                   \\  /    |')
print('|/                \\/                     \\/     |')
print('|                                               |')
print('================================================')

print('')
print('-----------------------------------------------------------------------')
print('|                                                                     |')
print('|                  anda sedang berada di rumah sakit                  |')
print('|---------------------------------------------------------------------|')
print('|                                                                     |')
print('|                        isi data anda di bawah                       |')
print('|                                                                     |')
print('-----------------------------------------------------------------------')

tekanan_darah = float(input('masukan tekanan darah anda           : '))
suhu_tubuh = float(input('masukan suhu tubuh anda              : '))
jenis_kelamin = input('masukan jenis kelamin anda anda (p/l): ')
gula_darah = float(input('masukan gula darah anda              : '))

if tekanan_darah >140 and suhu_tubuh > 38:
    print('anda darah tinggi')
if gula_darah >130:
    print('anda diabetes')
if suhu_tubuh > 40 or 110< tekanan_darah <130:
    print('anda demam')
if suhu_tubuh > 39 and tekanan_darah>140 and jenis_kelamin==('perempuan'or'p'):
    print('anda hamil')
elif suhu_tubuh<20:
    print('anda mati')
    print('mungkin anda sehat')