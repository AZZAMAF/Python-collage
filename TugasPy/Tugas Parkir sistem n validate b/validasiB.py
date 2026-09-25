a = int(input('A = '))
b = int(input('B = '))
c = int(input('C = '))

if a == b == c:
    print('Semua Indentik')
elif a == b or a == c:
    print('Ada Angka Kembar') 
elif b == c:
        print('Ada angka kembar')
elif b > a and b > c:
    print('B terbesar')
elif a > b and c < b :
    print('B Berada Di Antara A dan C')  
elif b < a and b < c:
    print('B  Terkecil')
    