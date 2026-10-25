
def add(a,b): 
    c = a + b
    return f"hasil penjumlahan {a} + {b} = {c}" # mengembalikan hasil penjumlahan dalam bentuk string
    

print(add(5,3)) # memanggil fungsi add dengan argumen 5 dan 3
print(add(10,12))
print(add(-5,3))


def subtract(a,b):
    return a - b            

# fungsi  =  menjalakan kode yang sudah dibuat


user_udin = 'udin', 10283
def get_user_info(user):
    username, user_id = user # unpacking tuple
    return f"Username: {username}, User ID: {user_id}" 

 

info = get_user_info(user_udin) # memanggil fungsi get_user_info dengan argumen user
print(info) # menampilkan hasil dari fungsi get_user_info


