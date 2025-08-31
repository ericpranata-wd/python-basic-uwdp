print('|===================================|')
print('|>>          daftar menu          <<|')
print('|===================================|')
print('|1. Indomie rebus + telur           |')
print('|2. Bubur ayam                      |')
print('|3. Nasi kuning                     |')
print('|4. Soto                            |')
print('|5. Sate ayam                       |')
print('|6. Nasi goreng                     |')
print('|===================================|')
pilihan=int(input('Masukan nomor makanan    : '))
jumlah=int(input ('Masukan jumlah pemesanan : '))
match pilihan:
    case 1|2:
        harga = 10000
    case 3|4|5:
        harga = 15000
    case 6:
        harga = 12000
spasi=int((harga*jumlah)//10)
# spasi1=10-spasi
print('|',spasi,'|')
# print('|',spasi1,'|')
# whtSpc = " " * 10
# print(f"a{whtSpc}b")
# exit

# print("")
# print('|============================================================|')
# print('|>>',' '*spasi1,'Total pemesanan anda adalah Rp.',harga*jumlah,' '*spasi1,'<<|')
# print('|============================================================|')
# # print('|>>{' '*spasi}Total pemesanan anda adalah Rp.{harga*jumlah}{' '*spasi}')
# input('tekan enter unutuk exit   ')
# if spasi==4:
#     print('spasi')
#     print('|============================================================|')
#     print(f'|>>          Total pemesanan anda adalah Rp.{harga*jumlah}          <<|')
#     print('|============================================================|')
#     # print('|>>{' '*spasi}Total pemesanan anda adalah Rp.{harga*jumlah}{' '*spasi}')
#     input('tekan enter unutuk exit   ')
# else:
print('============================================================')
print(f'          Total pemesanan anda adalah Rp.{harga*jumlah}')
print('============================================================')
input('tekan enter untuk exit   ')