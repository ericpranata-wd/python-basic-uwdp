umur=int(input('masukan umur anda: '))
if umur<5:
    print('anda adalah bayi')
elif 5<=umur<13:
    print('anda adalah anak-anak')
elif 13<=umur<20:
    print('anda adalah remaja')
elif 20<=umur: 
    print('anda adalah orang dewasa')
# sama dengan
if umur>=5:
    if umur <13:
        print('Anda adalah anak-anak')
    else:
        if umur<20:
            print('Anda adalah remaja')
        else:
            print('Anda adalah orang dewasa')
else:
    print ('Anda adalah bayi')