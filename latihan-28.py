nilai_ujian = [65, 80, 75, 50, 90, 72]

for nilai in nilai_ujian:
    
    
    # syarat lulus nilai sama dengan or lebih besar dari 75
    message_succes = "lulus"
    if nilai >= 75:
        
        print("lulus = " + str(nilai))
    else:
        print("Gagal = " + str(nilai))
        
        

      
def cek_number_status(number):
    
    for no in number:
        if no % 2 == 0:
            print('Nomor genap = ' + str(no) )
        else:
            print('Nomor ganji = ' + str(no))
            
cek_number_status(nilai_ujian)

data_mahasiswa = [
    {"nama": "Budi", "nilai": 80},
    {"nama": "Siti", "nilai": 65},
    {"nama": "Andi", "nilai": 90},
    {"nama": "Dina", "nilai": 72}
]

def data_parse(data):
    for n in data:
        if n["nilai"] >= 75:
            print(n["nama"] + " Selamat anda lulus")
            
data_parse(data_mahasiswa)

respons_api = {
    "status": "berhasil",
    "pesan": "Data nilai ujian akhir",
    "data_peserta": [
        {"nama": "Alex", "skor": [80, 90, 85]},
        {"nama": "Budi", "skor": [70, 60, 65]},
        {"nama": "Citra", "skor": [95, 90, 95]},
        {"nama": "Dina", "skor": [75, 80, 85]}
    ]
}

def filter_peserta_berpretasi(data):
    while data["status"] == "berhasil":
        for d in data:
            if data["data_peserta"]:
                print(data)
            
filter_peserta_berpretasi(respons_api)