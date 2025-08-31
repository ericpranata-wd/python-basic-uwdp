
# buat header
print('='*90)
print(' '*36,'kalkulator gaji',' '*36)
print('='*90)

# buat keterangan program
print('Petunjuk penggunaan program:')
print('1. Masukkan nama anda sesuai dengan kartu identitas anda')
print(' ')
print('2. Masukkan jenis kelamin anda: \n- Untuk laki-laki gunakan huruf l.\n- Untuk perempuan gunakan huruf p.')
print(' ')
print('3. Masukkan masa bekerja anda dalam satuan tahun')
print(' ')
print('4. Masukkan status pernikahan anda:\n- Jika sudah menikah dan belum bercerai gunakan huruf y.\n- Jika masih belum menikah atau telah bercerai gunakan huruf n')
print(' ')
print('5. Masukkan jumlah anak kandung yang terdata resmi (dibuktikan dengan akta kelahiran).')
print(' ')
print('6. Masukkan kode jabatan anda di kantor:\n- Jika staff biasa gunakan kode 1.\n- Jika sekretaris gunakan kode 2.\n- Jika kepala daerah gunakan kode 3.\n- Untuk lainnya gunakan kode 4.')
print(' ')

print('-'*90)
# definisikan input
nama = input('masukkan nama anda: ')
kelamin = input('masukkan kode jenis kelamin anda (l/p): ')
masa = int(input('sudah berapa tahun anda bekerja? : '))
nikah = input('apakah anda memiliki pasangan? (y/n): ')
anak = int(input('masukkan jumlah anak anda: '))
jabatan = input('apa jabatan anda di kantor (1/2/3/4): ')
print(' ')


# konversikan input menjadi huruf kecil
nikah=nikah.lower()

# alokasi space kosong untuk gaji
gaji =0

# gaji karena masak kerja
gaji = gaji+masa*500000

# gaji karena anak
if anak>0 and anak<=2:
    gaji =gaji +anak*200000
elif anak>2:
    gaji =gaji +400000
else:
    print('jumlah anak yang anda masukkan tidak sesuai')

#gaji karena jabatan 
match jabatan:
    case '1':
        gaji = gaji+500000
    case '2':
        gaji = gaji+1000000
    case '3':
        gaji = gaji+1500000
    case '4':
        pass #kondisi dilewatkan tanpa perlu memberikan nilai apapun
    case _:
        print('kode jabatan yang anda masukkan tidak sesuai')

#gaji karena jabatan
match kelamin:
    case 'l':
        gaji =gaji+1000000
    case 'p':
        gaji =gaji+500000
    case _:
        print('jenis kelamin yang anda masukkan tidak sesuaui dengan kriteria')

# gaji karena nikah
match nikah:
    case 'y':
        gaji =gaji+1000000
    case 'n':
        pass
    case _:
        print('status pernikahan yang anda masukkan tidak sesuai dengan kriteria')

# perhitungan pajak
if gaji>4500000:
    pajak = (gaji-4500000)*0.05
    sisa = gaji-pajak
    print(f"hello {nama}, gaji anda bulan ini adalah Rp. {gaji:,}.\nanda dikenakan potongan pajak sebesar Rp. {pajak:,}.\nsehingga gaji anda Rp. {sisa:,}")
else:
    print(f"hello {nama}, gaji anda bulan ini adalah Rp. {gaji:,}.")
print('='*90)
print(' '*36,'program selesai',' '*37)
print('='*90)

