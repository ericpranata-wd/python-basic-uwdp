warna=input('warna : ')
bentuk=input('bentuk : ')
berat=int(input('berat : '))
rasa=input('rasa : ')
if bentuk=='bulat' or bentuk=='lonjong':
    if warna=='merah' or warna=='kuning':
        print('tidak beracun')
    elif warna=='hijau' or warna=='ungu':
        if rasa=='manis':
            print('tidak beracun')
else:
    if bentuk=='kubus':
        if warna=='hijau' or warna=='kuning':
            if berat%4 == 0:
                print('tidak beracun')
            else:
                print('beracun')
        elif warna=='merah' or warna=='ungu':
            print('beracun')
    else:
        print('tidak beracun')
