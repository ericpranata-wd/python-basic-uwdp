print('|================================|')
print('|                                |')
print('|        PENDETEKSI HURUF        |')
print('|                                |')
print('|================================|')
n=(input('Masukan sebuah kata : '))
u=input('Masukan huruf yang ingin dideteksi : ')
print()
j=0
vokal=0
spasi=0
konsonan=0
x=0
p1=0
p2=0
p3=0
for i in n:
    x=x+1
    if i.lower()==u:
        j=1
        p=x
    if i.lower()=='a' or i.lower()=='i' or i.lower()=='u' or i.lower()=='e' or i.lower()=='o':
        vokal=vokal+1
    else:
        konsonan=konsonan+1
    if i.lower()==' ':
        spasi=spasi+1
        konsonan=konsonan-1
if j==0:
    print(f'huruf {u} tidak terdeteksi ')
if j==1:
    print(f'huruf {u} terdeteksi di pengulangan ke {p}')
print(f'dengan {vokal} huruf vokal.')
print(f'dengan {konsonan} huruf konsonan')
print(f'dengan {spasi} spasi.')
print()
input('tekan enter untuk exit   ')