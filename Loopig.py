take_a_plate = int(input('Ambil berapa piring?'))



for x in range(take_a_plate):
    print (x + 1)
    
rasa_haus = True
minum = 0


# while rasa_haus == True:
#     minum += 1
#     if rasa_haus == True:
#         minum =+ 1
#     else:
#         print('udh kembung')
#     print('asikkk udh gak haus')

while rasa_haus == True:
    minum += 1  # Operator yang benar untuk menambah 1 di setiap putaran
    print(f'Glek! Minum tegukan ke-{minum}')
    
    # Syarat berhenti yang lu usulkan
    if minum == 1: 
        rasa_haus = False
        print('asikkk udh gak haus')
        
angka = 1
while angka <= 4:
    print("Langkah ke-", angka)
    angka = angka + 1
print("Selesai!")

# Target sudah ditetapkan dari awal sebanyak 20 kali
for hitungan in range(1, 21):
    print(f"Melakukan sit-up ke-{hitungan}")

print("Hitungan ke-20 selesai. Aksi otomatis berhenti tanpa peduli fisik masih kuat atau tidak.")

ban_lembek = True
jumlah_pompa = 0

# Aksi diulang selama kondisi ban masih lembek (True)
while ban_lembek == True:
    jumlah_pompa += 1
    print(f"Menarik tuas pompa ke-{jumlah_pompa}...")
    
    # Simulasi syarat berhenti: anggaplah ban terasa keras di pompaan ke-5
    if jumlah_pompa == 5: 
        ban_lembek = False # Syarat terpenuhi, saklar dimatikan
        print("Ban sudah terasa keras! Aksi memompa dihentikan.")