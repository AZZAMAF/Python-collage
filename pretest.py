umur = 16
hari = "Minggu"
punya_kartu_pelajar = True

harga_tiket = 50000

if hari == "Sabtu" or  hari == "Minggu":
    harga_tiket += 10000
elif umur < 17 and punya_kartu_pelajar:
    harga_tiket += 15000

print(harga_tiket)


x = 12
y = 8
z = 20


if x + y > z :
    print("Kondisi Pertama")
elif x > y and z % x == 8 :
    print("Kondisi Kedua")
else:
    print("Kondisi Ketiga")

