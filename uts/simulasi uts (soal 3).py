print('Penentu gaji')
nama=input('Masukan nama anda : ')
waktu=input('Masukan waktu anda kerja (tahun) : ')
gajipokok=(int(waktu))*500000
gajipokokbulan=gajipokok/12
anak=input('Masukan jumlah anak anda : ')
if int(anak)=='1':
    tunjangananak=200000
if int(anak)=='0':
    tunjangananak=0
if int(anak)>=2:
    tunjangananak=400000
kelamin=(input('Masukan jenis kelamin anda (1=laki-laki/0=perempuan) : '))
match kelamin:
    case '1':
        status=input('Apakah anda memiliki istri (1=ya/0=tidak) : ')
        match status:
            case '0':
                tunjangankelamin=1000000
            case '1':
                tunjangankelamin=2000000
    case '0':
        tunjangankelamin=500000
jabatan=input('Masukan jabatan anda (0=lainnya/1=staff/2=sekertaris daerah/3=kepala daerah) : ')
bonus=500000*(int(jabatan))
gaji=gajipokokbulan+tunjangananak+tunjangankelamin+bonus
print(gaji)
if gaji>=4500000:
    gaji=gaji-((gaji-4.5)*5/100)
else:
    ()
print(f'Gaji yang {nama} dapatkan ialah sebesar Rp.{gaji}')