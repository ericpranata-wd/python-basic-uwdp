user=['Kevin','Evelyn']
pas=['789','123']
urut=None
urut2=1
print('====================================================')
print('|    Sebelum koding, mohon login ke akun python    ')
nama=input ('|    Masukan username : ')
if nama in user:
    urut=user.index(nama)
    password=input ('|    Masukan password : ')
    if password in pas:
        urut2=pas.index(password)
        if urut==urut2:
            print('====================================================')
            print()
            print('====================================================')
            print('|               login berhasil                     |')
            print('====================================================')
            input('Tekan enter untuk mulai koding   ')
            input()
        else:
            print('====================================================')
            print()
            print('====================================================')
            print('|                 pasword salah                    |')
            print('====================================================')
            input('Tekan enter untuk exit')
    else :
        print('====================================================')
        print()
        print('====================================================')
        print('|                 pasword salah                    |')
        print('====================================================')
        input('Tekan enter untuk exit')
else:
    print('====================================================')
    print()
    print('====================================================')
    print('|               nama tidak terdaftar               |')
    print('====================================================')
    input('Tekan enter untuk exit')
