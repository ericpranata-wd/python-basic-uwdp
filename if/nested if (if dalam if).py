# nested if (if dalam if)
# untuk kondisi yang harus dipenuhi satu per satu
# syntax:
# if(kondisi 1):
#     statement 1,2,3,....
#     if (kondisi 2):
#         statement 1,2,3,....

# contoh
# titanic
gender=input('masukan jenis kelamin anda (p/l): ')
gender=gender.lower()
usia=int(input('masukan usia anda: '))
if (gender=='perempuan'or gender=='p'):
    print('Anda selamat')
else: 
    if usia<15:
        print('Anda selamat')
    else:
        print('Anda tidak selamat')