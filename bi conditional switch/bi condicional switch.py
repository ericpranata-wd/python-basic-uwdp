# bi condicional switch

# contoh:
# hari senin dan selasa = seragam
# rabu dan kamis = batik
# jumat dan sabtu = pramuka

# definisi input
print('                        ====    =     =   ====  =    ==')
print('  <(.)__                =    =  =     =  =      =  ==  ')
print('   (    )               =    =  =     =  =      ===    ')
print('    |  |                =    =  =     =  =      =  ==  ')
print('   == ==                ====     =====    ====  =    ==')
print('')
print('|========================================================|')
print('| Hello, nama saya adalah duck,                          |')
print('| saya dapat membantu menemukan baju untuk anda sekolah. |')
print('|========================================================|')
print('')
hari = input ('Duck membutuhkan hari : ')
hari = hari.lower( )

# logika switch
match hari:
    case 'senin'|'selasa':
        print('hari ini pakai baju seragam.')
    case 'rabu'|'kamis':
        print('hari ini pakai baju batik.')
    case 'jumat'|'sabtu':
        print('hari ini pakai baju pramuka.')
    case 'minggu':
        print('hari ini libur.')
    case _:
        print('hari tidak diketahui.')
input(tekan enter untuk exit )