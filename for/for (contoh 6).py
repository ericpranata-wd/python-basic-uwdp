print('|=================================|')
print('|                                 |')
print('|         PENGGANTI HURUF         |')
print('|                                 |')
print('|=================================|')
n=(input('Masukan sebuah kata atau kalimat : '))
u=input('Masukan huruf yang ingin digantikan : ')
m=input('Masukan huruf penganti : ')
print()
for i in n:
    if i.lower()==u.lower():
        print(m)
        continue
    print(i)
input('Tekan enter untuk exit   ')