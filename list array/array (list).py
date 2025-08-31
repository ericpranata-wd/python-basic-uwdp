# array (larik)
# variabel yang dapat menyimpan lebih dari satu data dengan variabel serupa
# dengan 1 jenis data

# dalam python array disetarakan dengan kelas list
# contoh
# 1. tabel 
# 2. kordinat
# 3. matriks

# contoh 
# <variabel>=[<data 1>,<data 2>]
y=['susu','keju','roti','keju']
print (y)

# 1 syntax dasar oprasi array (nambah data)
# <variabel>.append(<data>)
y.append('selai') #tambah elemen ke list y (di belakang)
print (y)

# 2 syntax dasar oprasi array (nambah data di titik tertentu)
# <variabel>.insert(<nomor(kordinat)>,<data>)
y.insert(0,'ceres') 

# 3 syntax menghapus data di list sesuai nomor data
# <variabel>.pop(<nomor>) 
print(y.pop(2) ) # menghapus data dengan nomor 2

# 4 syntax remove data dengan (data)
# <variabel>.remove(<data>)
print(y.remove('keju')) # menghapus keju dari data y

# 5 syntax mengurut y sesuai nomor unicode
# <variabel>.sort()
y.sort()
print(y)

# 6 syntax mengambil data penjang list
# len(<variabel>)
print(len(y))  #length (list y)







# 7 syntax meng hapus semua data 
# <variabel>.clear()
print(y.clear())  #hapus data dalam list

y=[1,2,3,4,5]

# output
# syntax print data di list y dengan nomor data tertentu
# print(<variabel[<nomor dat>]>)
print(y[0])

# oprasi
# looping pada array
for i in y:
    print(i) # data ke 0,1,2,3 sesuai repetisi
for i in range (len(y)):
    print(i) #