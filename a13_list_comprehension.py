# contoh 1
print("---contoh 1")

seq = []
for i in range(5):
    seq.append(i * 2)
print(seq)

# bisa ditulis menggunakan list comprehension seperti ini:
seq = [i * 2 for i in range(5)]
print(seq)

# contoh 2
print("---contoh 2")

seq = []
for i in range(10):
    if i % 2 == 1:
        seq.append(i)
print(seq)

# bisa ditulis seperti ini:
seq = [i for i in range(10) if i % 2 == 1]
print(seq)

# contoh 3
print("---contoh 3")

seq = []
for i in range(1, 10):
    if i % 2 == 0:
        seq.append(i * 2)
    else:
        seq.append(i * 3)
print(seq)

# bisa ditulis seperti ini:
seq = []
for i in range(1, 10):
    seq.append(i * (2 if i % 2 == 0 else 3))
print(seq)

# atau
seq = [(i * (2 if i % 2 == 0 else 3)) for i in range(1, 10)]
print(seq)

# contoh 4
print("---contoh 4")

list_x = ['a', 'b', 'c']
list_y = ['1', '2', '3']

seq = []
for x in list_x:
    for y in list_y:
        seq.append(x + y)
print(seq)

# bisa ditulis seperti ini:
seq = [x + y for x in list_x for y in list_y]
print(seq)

# contoh 5
print("---contoh 5")

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

tranposed = []
for i in range(4):
    tr = []
    for row in matrix:
        tr.append(row[i])
    tranposed.append(tr)
print(tranposed)

# bisa ditulis
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

tranposed = []
for i in range(4):
    tranposed.append([row [i] for row in matrix])
print(tranposed)

# atau
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]
tranposed = [[row[i] for row in matrix] for i in range(4)]
print(tranposed)
