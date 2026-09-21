import math
from datetime import datetime, time

category = input('Motor atau Mobil? ').lower()
input_masuk= input('Masuk jam berapa? ')
input_keluar= input('Keluar jam Berapa? ')

total_biaya_parkir = 0
        
try:
    waktu_masuk = datetime.strptime(input_masuk, "%H:%M")
    waktu_keluar = datetime.strptime(input_keluar, "%H:%M")
    
        # 3. Hitung durasi (dalam jam)
    selisih = waktu_keluar - waktu_masuk
    durasi_jam = math.ceil(selisih.total_seconds() / 3600)

    
    if  category == "mobil":
        tarif_awal = 5000  # Tarif 2 jam pertama mobil
        tarif_lanjut = 3000 # Tarif per jam berikutnya mobil
    elif category == 'motor':  # Motor
        tarif_awal = 2000  # Tarif 2 jam pertama motor
        tarif_lanjut = 1000 # Tarif per jam berikutnya motor
    else:
        print('nothing')
    # 5. Hitung total bayar dengan logika if-else durasi
    
    if durasi_jam <= 2:
        total_bayar = tarif_awal
    else:
        total_bayar = tarif_awal + ((durasi_jam - 2) * tarif_lanjut)

    print(f"\nDurasi Parkir: {durasi_jam} jam")
    print(f"Total Bayar: Rp {total_bayar:,}")
        
    
except ValueError:
    print("Eror: Format jam salah! Gunakan format HH:MM (contoh: 08:30 atau 14:00)")