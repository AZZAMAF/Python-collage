import functionn

antrean = ["Andi", "Budi"]
antrean.pop(1) # pop removes the first element
antrean.insert(2, "Citra") # insert at the beginning of the list
print(antrean)

titik_drone = (-6.9, 107.6, 120.0)
lat, lon, alt = titik_drone # unpacking a tuple
print(alt)

nama = ["Budi", "Rian", "Budi", "Siti", "Rian"]
nama_bersih = list(set(nama)) # remove duplicates using set and convert back to list
print(nama_bersih)

menu = {"kopi": 15000, "teh": 8000}
menu["roti"] = 10000 # add new item
menu["kopi"] = 18000 # update existing item
print(menu)

def cek_lulus(nilai): # function for checking if a student passes based on their score
    if nilai >= 60:
        return "Lulus"
    else:
        return "Remedial"


# Contoh pengujian fungsi:
print(cek_lulus(75))


transaksi = [
    {"id": "T01", "kategori": "elektronik", "harga": 500000},
    {"id": "T02", "kategori": "pakaian", "harga": 150000},
    {"id": "T03", "kategori": "elektronik", "harga": 1200000},
    {"id": "T04", "kategori": "makanan", "harga": 50000},
    {"id": "T05", "kategori": "pakaian", "harga": 200000},
]

def total_harga_kategori(data, min_price):
    output = {}
    for item in data:
        if item["harga"] >= min_price:
            # if item["kategori"] in output: # validation for existing category in output
            #     output[item["kategori"]] += [item["id"]]
            #     print(f"Kategori {item['kategori']} sudah ada di output, menambahkan ID {item['id']}.")
            # else: # if the category does not exist in output, create a new entry
            #     output[item["kategori"]] = [item["id"]]
            #     print(f"Kategori {item['kategori']} ditambahkan ke output.")    
        # Maksudnya: jika 'kategori' belum ada di output, buatkan list kosong [].
        # Lalu langsung tempelkan (.append) item id-nya.
            output.setdefault(item["kategori"], []).append(item["id"])  
    return output

total_harga = total_harga_kategori(transaksi, 500000)
print(total_harga)

fungsit_tambahan = functionn.add(10, 20)
print(fungsit_tambahan)