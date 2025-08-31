# hiding
print('','-'*50)
print('|',' '*48,'|')
print('|   penghitung volume, luas, dan keliling balok    |')
print('|',' '*48,'|')
print('','-'*50)

# input
p=float (input ('masukan panjang balok : '))
l=float (input ('masukan lebar balok : '))
t=float (input ('masukan tinggi balok : '))

# oprasi dan print
print(f'volume balok anda adalah {p*l*t}')
print(f'luas balok anda adalah {2*(p*l+l*t+t*p)}')
print(f'keliling balok anda adalah {4*(p+l+t)}')