
tinggi = 5

for i in range(1, tinggi +1):
    
    spasi = " " *(tinggi - i)
    bintang ="*" * (2 * i -1)
    
    print(spasi + bintang)
    
# Menentukan tinggi segitiga bintang
tinggi = 5

for i in range(1, tinggi + 1):
    print("*" * i)

# for i in range(1, 5):
#     print(i)
#     for t in range(1,5):
#         space =" " * i
#         print("*" + space)

for outer in range(1, 4):         # Outer loop runs 3 times (1, 2, 3)
    print(f"--- Outer is {outer} ---")
    
    for inner in range(1, 3):     # Inner loop runs 2 times (1, 2)
        print(f"Inner is {inner}")
        
for i in range(1,10, +1):
    print(" " * +(10-i) +"*" * (2*i -1))
n = 10
for i in range(n, 0, -1):
    print(" " * (n - i) + "*" * (2 * i - 1)     ) 
    

#-------------------------*
#------------------------***
#----------------------******
# -------------------*********
# -----------------************
# ---------------***************
# --------------

    