hari=(input('Masukan hari praktikum : '))
hari=hari.lower()
match hari:
    case 'senin'|'rabu':
        aslab1='Pak Kevin'
    case 'selasa'|'sabtu':
        aslab1='Bu Evelyn'
    case 'kamis'|'jumat':
        aslab1='Pak Noppri'
match hari:
    case 'senin'|'sabtu':
        aslab2='Pak Noppri'
    case 'selasa'|'jumat':
        aslab2='Pak Kevin'
    case 'kamis'|'rabu':
        aslab2='Bu Evelyn'
print(f'As lab pada hari itu adalah {aslab1} dan {aslab2}')