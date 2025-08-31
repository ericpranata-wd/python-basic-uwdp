p=float(input('Masukan panjang prisma segiempat : '))
l=float(input('Masukan lebar prisma segiempat   : '))
t=float(input('Masukan tinggi prisma segiempat  : '))

print(f' Volume prisma segiempat adalah {p*l*t}')
print(f' Luas silinder prisma segiempat adalah {2*((p*l)+(p*t)+(l*t))}')
print(f' Keliling prisma segiempat adalah {4*(p+l+t)}')
print(f' Diagonal ruang prisma segiempat adalah {(p**2+l**2+t**2)**1/2}')