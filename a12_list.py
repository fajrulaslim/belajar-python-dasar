# list
print("---list")

list_1 = [10, 70, 12]

list_2 = [
    'ab',
    'cd',
    'ef'
]

list_3 = [3.14, "hello python", True, False]

list_4 = []

print(list_1)
print(list_2)
print(list_3)
print(list_4)

# perulangan list
print('---perulangan list')

for i in range(0, len(list_1)): # len() itu jumlah list sama dengan length
    print("index:", i, "elem:", list_1[i])

# enumerate
print("---enumerate")
# membuat data sequence menjadi data enumerasi
for i, v in enumerate(list_1):
    print("index:", i, "elem:", v)

# nested list
print("---nested list")

matrix = [
    [0, 1, 0, 1, 0],
    [1, 1, 1, 0, 0],
    [0, 0, 0, 1, 1],
    [0, 1, 1, 1, 0]
]

for row in matrix:
    for cel in row:
        print(cel, end=" ")
    print()

# konversi range ke list
print("---range to list")

range_1 = range(0, 10)
list_1 = list(range_1)
print(list_1)

range_2 = range(0, 22, 3)
list_2 = list(range_2)
print(list_2)

# konversi string ke list
print("---string to list")

alphabets = list('abcdefg')
print(alphabets)

# konversi tuple ke list
print("---tuple to list")
tuple_1 = (1, 2, 3)
numbers = list(tuple_1)
print(numbers)

# mengakses element via index
print("---cek element via index")
elem_1st = list_1[0]
elem_2nd = list_1[1]
print(elem_1st)
print(elem_2nd)

# cek apakah ada element
print("---cek apakah ada element")
list_1 = [10, 70, 20]
n = 70

if n in list_1:
    print(n, "is exists")
else:
    print(n, "is not exists")

# slicing list
print("---slicing list")

list_2 = ['ab', 'cd', 'ef', 'gh']
slice_1 = list_2[1:3] # dimulai dari index 1 hingga sebelum 3
print("slice:", slice_1)

# mengubah nilai element
print("---mengubah nilai element")

list_2 = ['ab', 'cd', 'hi', 'ca']
print('before:', list_2)

list_2[1] = 'zk'
list_2[2] = 'sa'
print('after:', list_2)

# append element
print("---append element")

list_1 = [10, 70, 20]
print('before: ', list_1)

list_1.append(88)
list_1.append(43)
print('after:', list_1)

# append via slicing
print("---append via slicing")
list_1 = [10, 70, 20]
print('before: ', list_1)

list_1[len(list_1):] = [88, 87]
print('after:', list_1)

# extend/concat/union element
print("---extend/concat/union via extend")

list_1 = [10, 70, 20]
list_2 = [88, 77]
list_1.extend(list_2)
print(list_1)

print("---extend/concat/union via slicing")
list_1 = [10, 70, 20]
list_2 = [88, 77]
list_1[len(list_1):] = list_2
print(list_1)

print("---extend/concat/union via operator +")
list_1 = [10, 70, 20]
list_2 = [88, 77]
list_3 = list_1 +  list_2
print(list_3)

# menyisipkan element pada index i - insert
print("---insert")

list_3 = [10, 70, 20, 30]

list_3.insert(0, 15)
print(list_3)

list_3.insert(2, 24)
print(list_3)

# menghapus element - remove
print("---remove")

list_3 = [10, 70, 20, 70]

list_3.remove(70)
print(list_3)

# menghapus element pada index i
print("---remove by index")

list_3 = [10, 70, 20, 70]

x = list_3.pop(2)
print('list 3:', list_3)
print('removed element:', x)

x = list_3.pop()
print('list 3:', list_3)
print('removed element:', x)

# error jika tidak ditemukan
# list_3 = [10, 70, 20, 70]
# x = list_3.pop(7)

# menghapus menggunakan del
print('---menghapus menggunakan del')

list_3 = [10, 80, 20, 70]
print('len:', len(list_3), "data:", list_3)

del list_3[1]
print('len:', len(list_3), "data:", list_3)

# menghapus element pada range index
print("---menghapus element pada range index")

list_3 = [10, 70, 20, 70]

del list_3[1:3]
print(list_3)

# menghitung jumlah element
print("---menghitung jumlah element")
list_3 = [10, 70, 20, 70]
total = len(list_3)
print(total)

# menghitung jumlah element dengan data 70
count = list_3.count(70) 
print(count)

# mencari index element list
print("---mencari index element list")

list_2 = ['ab', 'cd', 'hi', 'ca']

idx_1st =  list_2.index('cd')
print('idx_1st:', idx_1st)
# jika element yang dicari tidak ada maka error

# mengosongkan list
print('---mengosongkan list')

# method clear
list_1 = [10, 70, 20]
list_1.clear()
print(list_1)

# menimpanya dengan []
list_1 = [10, 70, 20]
list_1 = []
print(list_1)

# menggunakan del dan slicing
list_1 = [10, 70, 20]
del list_1[:]
print(list_1)

# membalikkan element list - reverse
print('---reverse')
list_1 = [10, 70, 20]
list_1.reverse()
print(list_1)

# copy list
print("---copy")
list_1 = [10, 70, 20]
list_2 = list_1.copy()
print(list_1)
print(list_2)

# combinaasi operasi assigment dan slicing
list_1 = [10, 70, 20]
list_2 = list_1[:]
print(list_2)

# mengurutkan element list - sorting
print('---sorting')
list_1 = [10, 70, 20]
list_1.sort()
print(list_1)

