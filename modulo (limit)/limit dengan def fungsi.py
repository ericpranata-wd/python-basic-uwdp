# limit
# hampiran nilai fungsi untuk peubah yang menuju nilai tertentu
# contoh lim x -> 3 2x+1
# anda akan menggantikan x dengan 3
# namun cara yang benar secara komputasional 

# pembuatan fungsi 
def f(x):
    y=(x**2-4*(x)+3)*(x-1)**-1
    return y
# nilai limit
n=3 

kiri=n-(10**-10)
kanan=n+(10**-10)
print(f'nilai limit x-> {n} dari kiri adalah {round(f(kiri),2)}')
print(f'nilai limit x-> {n} dari kanan adalah {round(f(kanan),2)}')
if round(f(kiri),2)==round(f(kanan),2):
    print('limit ada')
else:
    print('limit tak ada')


def f2(x):
    y=(1)*(x+3)**-1
    return y
# nilai limit
n=-3 

kiri=n-(10**-10)
kanan=n+(10**-10)
print(f'nilai limit x-> {n} dari kiri adalah {round(f2(kiri),2)}')
print(f'nilai limit x-> {n} dari kanan adalah {round(f2(kanan),2)}')
if round(f2(kiri),2)==round(f2(kanan),2):
    print('limit ada')
else:
    print('limit tak ada')