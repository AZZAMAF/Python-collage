# Data simulasi berat kendaraan (dalam kg) untuk diuji coba
data_kg = [800, 500, 400, 200]


# while True:
#     total_berat = 0
#     for d in range(len(data_kg)):
        
#         if d <= 1500:
#             tombol_darurat = int(input('Tombol Darurat : '))
#             total_berat += data_kg[d] 
#             print(f'Total berat kendaraan {total_berat}')
#             print(f"Jumlah truck yang lolos :{d}")    
    
#     break
 
bintang = '*'

for i in bintang:
    print(i*10)
    for x in i:
        print(f'{x*10}\n')