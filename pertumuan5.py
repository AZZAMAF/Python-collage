age = 12
day = 'sunday'
student_card =  True

harga_normal = 50000
def total_price(price):
    if day == 'sunday''saturday':
        price += 10000
        return price
    elif age < 17 and student_card:
        price-=15000
        return price
print(total_price(harga_normal))

# harga normal RP.50.000
# jika hari minggu atau sabtu:
    # true: tambah harga rp.10.000
# jika umur kurang dari 17 dan punya kartu siswa:
    #True : kurangin rp.15.000