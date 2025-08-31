hitung=1
hari=10
batang=0
a=2
lim=8
power=1
while hari>0:
    for i in range(a,hari+1):
        print(hitung)
        count=2**(power)
        if i>lim-1:
            hari-=lim
            if hari<=7:
                lim=hari
            batang+=hitung
            hitung=1
            a=1
            power=1
            break
        if i==3 or i==4:
            count=0
            power-=1
        power+=1
        hitung+=count