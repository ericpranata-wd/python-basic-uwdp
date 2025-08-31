# looping (pengulangan)
# peroses mengulang sebagian atau seluruh skrip
# looping dilakukan dengan dua perintah dasar

# syntax

# for <variabgel>(jalan berapa kali) :
#     argument 1
#     argument 2

# i(satuan penglulangan nasional)(interasi)

for i in range (10):
    print('selamat datang')
    print(i)
print()
print()
for i in range (7,10):
    print('selamat datang')
    print(i)
    print('*'*i)
print()
print()
for i in range (1,11,2):
    print('selamat datang')
    print(i)
print()
print()
# downfall
for i in range (5,0,-1):
    print('selamat datang')
    print(i)


for i in range (-9):
    print('selamat datang')
    print(i)
# tidak akan dikerjakan karena i=0 dan sudah lebih besar dari -9