n=int(input('Masukan angka (1 sampai 100) : '))
if n<=100:
    for i in range (2,n):
        cek=(n%i)
        if cek==0:
            pernyataan=0
            print('bukan prima')
            break
        else:
            if i==n-1:
                print('prima')
else:
    print('Angka anda melewati limit 100')
input ('Masukan ')