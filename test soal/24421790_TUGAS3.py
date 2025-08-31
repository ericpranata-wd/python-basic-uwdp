# soal 1

print('============================================')
print('|                                          |')
print('|           PENDETEKSI KELIPATAN           |')
print('|                                          |')
print('============================================')
print('|                  ATURAN                  |')
print('| 1. Kelipatan 3 : akan di lewati          |')
print('| 2. Kelipatan 5 : akan mencetak (angka+1) |')
print('| 3. Kelipatan 5 dan 3 : akan skip 2 angka |')
print('| 4. Angka tidak boleh lebih dari 100      |')
print('============================================')
print('|                                          |')
print('|          MADE BY : ERIC PRANATA          |')
print('|                                          |')
print('============================================')
print()
print()

angka=int(input('Masukan angka (1 sampai 100) : '))
print()
x=0
if angka <= 100:  # Untuk mendeteksi apakah angka melewati limit

    for i in range (1,angka):  # Looping
        if x==0:  # Untuk mendeteksi angka yang sama dan berdekatan
            if i%3==0:  # Mendeteksi angka kelipatan 3
                if i%5==0:  # Mendeteksi angka kelipatan 3 dan 5
                    x=1
                else: 
                    ()
            elif i%5==0:  # Mendeteksi angka kelipatan 5
                print(i+1)
            else:  # Output
                print (i)
        else:
            x=0
        if i==angka:
            print('============================================')
else:
    print('============================================')
    print (f'   Anda melewati limit')
    print('============================================') 


# soal 2
    
print()
print()
print('============================================')
print('|                                          |')
print('|               PENILAI KATA               |')
print('|                                          |')
print('============================================')
print('|                  ATURAN                  |')
print('| 1. Masukan sebuah kata                   |')
print('| 2. Tidak boleh ada kata selain alfabet   |')
print('| 3. Kata tidak boleh lebih dari 50        |')
print('============================================')
print('|                                          |')
print('|          MADE BY : ERIC PRANATA          |')
print('|                                          |')
print('============================================')
print()
print()

# Definisi variabel
out=1
a=None
kata=(input('Masukan sebuah kata (1 hingga 50 karakter) : ')).lower()
print()
skor=0
pengulangan=0

# Looping untuk mendeteksi huruf satu per satu
for i in (kata):
    pengulangan=pengulangan+1
    if pengulangan<=50:  # Untuk mendeteksi limit
        if a!=i:
            if i == 'a' or i== 'i' or i == 'u' or i == 'e' or i == 'o':  # Untuk huruf vokal
                skor = skor + 3
                a=i
            else: # Selain huruf fokal
                try:  # Untuk mencoba atau mengecek apakah i = angka
                    i=int(i)
                except ValueError:  # Jika i != angka
                    if i==' ':  # Untuk mendeteksi spasi (simbol lain belum dibuat :v )
                        ()
                    else:
                        skor=skor+1  # Untuk (huruf) selain vokal
                        a=i
    else:
        # Output jika melewati limit
        print('============================================')
        print (f'   Anda melewati limit')
        print('============================================')
        out=0
        break
if out==1:
    # Output
    print('============================================')
    print (f'   Skor anda adalah {skor}')
    print('============================================')


# soal 3
    
print()
print()
print('============================================')
print('|                                          |')
print('|         PENDETEKSI ANGKA POSITIF         |')
print('|                                          |')
print('============================================')
print('|                  ATURAN                  |')
print('| 1. Masukan angka positif                 |')
print('| 2. Untuk exit masukan angka negatif      |')
print('============================================')
print('|                                          |')
print('|          MADE BY : ERIC PRANATA          |')
print('|                                          |')
print('============================================')
print()
print()

# Definisi variabel
num2=0
x=0
genap=0
ganjil=0
caunt=0
while x==0:  # Loopint untuk memasukan angka berkali kali
    num=input('Masukan angka : ')
    try:  # Untuk mengecek apakah variabel num = angka
        num=int(num)
        if num<0:  # Untuk mendeteksi apakah angka negativ
            x=1
            if caunt==0:
                print()
                print('=================================================')
                print(' Anda tidak memasukan angka positif sama sekali')
                print('=================================================')
            else:
                print()
                print('|==============================================================')
                print(f'|  Jumlah angka positif anda adalah {num2}')
                print(f'|  Dengan {genap} angka genap dan {ganjil} angka ganjil.')
                print(f'|  Dengan {plus} angka maksumum dan {min} angka minimum.')
                print('|==============================================================')
        else:
            caunt=caunt+1
            if num%2==0:
                genap=genap+1
            else:
                ganjil=ganjil+1
            if caunt==1:
                min=num
                plus=num
            else:
                if num<min:
                    min=num
                if num>plus:
                    plus=num
            num=num2+num
            num2=num
    except ValueError:  # Jika variabel num bukan angka maka program akan melakukan looping lagi dan untuk melengkapi (try)
        ()