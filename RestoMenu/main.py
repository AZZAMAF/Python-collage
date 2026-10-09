menu_makanan = [
    {"nomor": 1, "nama": "Nasi Goreng", "harga": 15000},
    {"nomor": 2, "nama": "Mie Goreng", "harga": 12000},
    {"nomor": 3, "nama": "Ayam Geprek", "harga": 18000},
    {"nomor": 4, "nama": "Bakso", "harga": 15000},
    {"nomor": 5, "nama": "Mie Ayam", "harga": 13000},
    {"nomor": 6, "nama": "Soto Ayam", "harga": 17000},
    {"nomor": 7, "nama": "Nasi Padang", "harga": 20000},
    {"nomor": 8, "nama": "Sate Ayam", "harga": 22000},
    {"nomor": 9, "nama": "Burger", "harga": 25000},
    {"nomor": 10, "nama": "Pizza", "harga": 35000}
]

print("=== Menu warunng makjo ===")
print("Menu Perintah:")
print("- ketik '0' untuk cek menu ")
print("- ketik '1' untuk memilih menu ")
print("- ketik '2' untuk hitung total belanja dan keluar")
print("- ketik '3' Kurangi menu")

# total menu// total price // selected meny\



MenuCostumer=[]

def addMenu(menu):
    for no_menu in menu:
        for input_user in list_angka:
            if  input_user == no_menu['nomor']:
                MenuCostumer.append(no_menu)
                print(f"{no_menu['nomor']}. {no_menu['nama']} - Rp{no_menu['harga']:,} berhasil dimasukkan ke menu.")
        
    if input_user > 10:
        print("-> Maaf, Mennu tersebut tidak tersedia.")
            
         # print(no_menu['nomor'])
   
        

while True:
    
    perintah = input("\nMasukkan perintah Anda: ")

    match perintah:
        
        case '0': 
            for menu in menu_makanan:
                print(f"{menu['nomor']}. {menu['nama']} - Rp{menu['harga']:,}")
    
        case '1':
            input_user = input("Masukkan Nomor menu (1/2/4/5 dll): ")
            
            # 2. Memotong teks berdasarkan koma dan mengubahnya langsung menjadi list angka (integer)
            list_angka = [int(x.strip()) for x in input_user.split(",")]
            # print(list_angka)

            addMenu(menu_makanan)

            # if no_menu_customer in menu_makanan[0]["nomor"]:
            #     MenuCostumer.append(no_menu_customer)
            #     print(f"{no_menu_customer['nomor']}. {no_menu_customer['nama']} - Rp{no_menu_customer['harga']:,} berhasil dimasukkan ke menu.")
     
        case'2':
            total_price = 0
            for menu in MenuCostumer:
                price = menu['harga']
                total_price += price
            print(f'total harga :: Rp{total_price:,}')  
            
        case'3':
            total_price = 0
            input_delete = int(input('Masukan No Menu yanng akan di hapus?'))
            for menu in MenuCostumer:
                no_menu = menu['nomor']
                if input_delete == no_menu :
                    MenuCostumer.remove(menu)
                    print(f"{menu['nomor']}. {menu['nama']} - Rp{menu['harga']:,} berhasil dihapus dari menu.")
            if input_delete > 10:
                    print("-> Maaf, Mennu tersebut tidak tersedia.")
                         
        case _:
            print('not found action')