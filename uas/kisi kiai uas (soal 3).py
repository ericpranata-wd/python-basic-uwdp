list_nama=['Valentino Pratama ', 'Alessandro d\'Innocenzo ' ,'Francesco Smarra ']
# aray=[[[]],[[]],[[]]]
aray=[[[1,2,3,4],[5,6,7,8]],[[2,3],[9,5]],[[12,2]]]
count=[]
limit=[4,2,3]
hari = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu","Minggu"]
for i in range(3):
    count.append(0)
while True:
    print('''
        menu

0. Keluar
1. Input nama
2. Lihat antrian
3. Proses mahasiswa
    ''')
    pilih = input('Pilih menu : ')
    if pilih=='1':
        print('''
        bidang
    
1. Machine Learning 
2. Control Theory 
3. Neural Network 
    ''')
        
        bidang=input('Pilih bidang konsentrasi : ')
        try:
            bidang=int(bidang)
        except ValueError:
            continue
        if bidang!=1 and bidang!=2 and bidang!=3:
            continue
        for i in range(3):
            if len(aray[i][count[i]])>=limit[i]:
                count[i]+=1
                aray[i].append(0)
                aray[i][count[i]]=[]
        nama=input('Masukan nama anda : ')
        aray[bidang-1][count[bidang-1]].append(nama)
    elif pilih=='2':
        nam=-1
        for i in aray:
            nam+=1
            if i[0]==[]:
                continue
            print(list_nama[nam])
            day=0
            for j in i:
                if j==[]:
                    continue
                print()
                print(hari[day])
                day+=1
                num=1
                for k in j:
                    print(f'{num}. {k}')
                    num+=1
            print()
            print()
    elif pilih=='0':
        break
    elif pilih=='3':
        ()