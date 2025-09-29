# Pengelanan
print("---tuple")

tuple_1 = (2, 3, 4, "Hello Python", False)
print("data:", tuple_1)
print("total elem:", len(tuple_1))

# Mengakses element tuple via index
print("---Akses tuple via index")

tuple_1 = (1, 2, 3, 4, 5)
print("element 0:", tuple_1[0])
print("element 1:", tuple_1[1])

# Perulangan tuple
print("---Perulangan tuple")

tuple_2 = ("ultra instinc shaggy", "nighwing", "noob saibot")

for t in tuple_2:
    print(t)

for i in range(0, len(tuple_2)):
    print("index:", i, "elem:", tuple_2[i])

# Fungsi enumerate
print("---Enumerate")

tuple_2 = ("ultra instinc shaggy", "nighwing", "noob saibot")
for i, v in enumerate(tuple_2):
    print("index:", i, "elem:", v)

# Mengecek apakah element ada
print("---Mengecek tuple")

tuple_1 = (10, 70, 20)
n = 70

if n in tuple_1:
    print(n, "is exists")
else:
    print(n, "is NOT exists")

# Nested tuple
print("---Nested tuple")

tuple_nested = ((0, 2), (0, 3), (2, 2), (2, 4))
tuple_nested = (
    (0, 2), 
    (0, 3), 
    (2, 2), 
    (2, 4)
)

for row in tuple_nested:
    for cell in row:
        print(cell, end=" ")
    print()

# List dan Tuple
print("---List dan Tuple")

data = [
    ("ultra instinc shaggy", 1, True, ['detective', 'saiyan']),
    ("nighwing", 3, True, ['teen titans', 'bat family'])
]

data.append(("noob saibot", 6, False, ['brotherhood of shadow']))
data.append(("tifa lockhart", 2, True, ['avalanche']))

print("name | rank | win | affiliation")
print("-------------------------------")
for row in data:
    for cell in row:
        print(cell, end=" | ")
    print()

# Fungsi tuple
print("---Fungsi tuple")

print("---1-string ke tuple")
alphabets = tuple('abcdef')
print(alphabets)

print("---2-list ke tuple")
numbers = tuple([2, 3, 4])
print(numbers)

print("---3-range ke tuple")
r = range(0, 4)
rtuple = tuple(r)
print(rtuple)

# Tuple Packing dan unpacking
print("---Tuple Packing")

first_name = "aerith gainshbor"
rank = 11
win = False

row_data = (first_name, rank, win)
print(row_data)

print("---Tuple unpacking")
row_data = ("aerith gainshbor", 11, False)
first_name, rank, win = row_data
print(first_name, rank, win)

# Tuple kosong
print("---Tuple kosong")

empty_tuple = ()
print(empty_tuple)