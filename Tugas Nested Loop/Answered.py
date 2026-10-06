print('# Soal 1: Kotak Bintang Penuh  ')
print('='*30)
n=5
stars='*'
for h in range(n):
    for w in range(n):
        print(stars, end=" ")
    print()
    
print('\n')


for h in range(n):
    for w in range(1):
        print(stars * (w+n))
    
print('\n')


print('Soal 2: Segitiga Bintang ')
print('='*30) 
for h in range(n):
    print(stars*(h+1))

print('\n')
    
for h in range(n):
    for w in range(h+1):
        print(stars, end="")
    print()
    
print('\n')

for h in range(1,n+1):
    for w in range(h):
        print(stars ,end="")
    print()


print('\n')

for h in range(0,n+1):
    for w in range(h):
        print(' ' + stars, end='')
    print()
    

print('\n')

    

print('Soal 3: Segitiga Angka Terbalik ')
print('='*30) 
  
for h in range(n, 0, -1):  # h berjalan mundur: 5, 4, 3, 2, 1
    print(stars * h) 
    
for h in range(n, 0, -1):
    for w in range(h):
        print(stars ,end=" ")
    print()
    
print('\n')

print('Soal 4: Segitiga Rata Kanan ')
print('='*30) 


# for h in range(n,0, -1):
#     for w in range((n-h)+1):
#         print(' '*(h-w) + stars, end='') // Expeeriment hampir berhasil
#     print()

for h in range(1, n + 1):
    print(' ' * (n - h), end='')
    for w in range(h):
        print(stars, end='')
    print()
    
print('\n')
    
for h in range(0,n+1):
    print(' '*(n-h) + stars*h)
    
print('\n')

print('Soal 5: Kotak Bintang Bolong ')
print('='*30) 

for h in range(n):  
    for w in range(n):  
    
        if h == 0 or h == n - 1 or w == 0 or w == n - 1:
            print(stars, end=" ")
        else:
            print(" ", end=" ")  
    print()  


print('Soal 6: Piramida Angka ')
print('='*30)
for i in range(1,10, +1):
    print(" " * +(10-i) +"*" * (2*i -1))
 
print('Soal 7: Diamond Huruf')
print('='*30) 

for i in range(1,10, +1):
    print(" " * +(10-i) +"*" * (2*i -1))
n = 10
for i in range(n, 0, -1):
    print(" " * (n - i) + "*" * (2 * i - 1)     ) 