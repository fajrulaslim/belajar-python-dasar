# Set
print('---Pengenalan set')

data_1 = {1, "abc", False, ('banana', 'spaghetti')}
print('data: ', data_1)
print("len:", len(data_1))

data_2 = set()
print('data:', data_2)
print('len:', len(data_2))

# Mengakses element set
print('---Mengakses element set')
fellowship = {'aragorn', 'gimli', 'legolas'}

for p in fellowship:
    print(p)

# Otomatis elemininasi duplikat
print('---Eleminiasi duplikat')
data = {1, 2, 2, 3, 4, 2, 4, 2, 1}
print(data)

# Cek element ada
print('---Cek element')
fellowship = {'aragorn', 'gimli', 'legolas'}
to_find = "gimli"

if to_find in fellowship:
    print(to_find, "is exist")

# Menambah element
print('---Menambah element')

fellowship = set()

fellowship.add('aragorn')
print("len:", len(fellowship), "data:", fellowship)

fellowship.add('gimli')
print("len:", len(fellowship), "data:", fellowship)

# Menghapus secara acak
print('---Menghapus element secara acak')

fellowship = {'narya', 'nenya', 'nilya'}
fellowship.pop()
print("len:", len(fellowship), "data:", fellowship)

# Menghapus spesifik element
print('---Menghapus spesifik element')

fellowship = {'aragorn', 'gimli', 'legolas', 'gandalf', 'boromir', 'frodo', 'sam', 'merry', 'pippin'}
print("fellowship:", fellowship)

# jika tidak ada, tidak eror
fellowship.discard("boromir")
print("fellowship:", fellowship)

# jika tidak ada, akan error
fellowship.remove('gandalf')
print("fellowship:", fellowship)

# Mengosongkan set
print('---Mengosongkan set')

fellowship = {'aragorn', 'gimli', 'legolas'}
fellowship.clear()
print("len:", len(fellowship), "data:", fellowship)

# Copy set
print('---Copy set')

data1 = {'aragorn', 'gimli', 'legolas'}
print("len:", len(data1), "data1:", data1)

data2 = data1.copy()
print("len:", len(data2), "data2:", data2)

# Difference antar set (yang tidak ada)
print("---Difference antar set")

fellowship = {'aragorn', 'gimli', 'legolas', 'gandalf', 'boromir', 'frodo', 'sam', 'merry', 'pippin'}
hobbits = {'frodo', 'sam', 'merry', 'pippin', 'bilbo'}

diff1 = fellowship.difference(hobbits)
print('diff1:', diff1)

diff2 = hobbits.difference(fellowship)
print('diff2:', diff2)

fellowship.difference_update(hobbits)
print('fellowship:', fellowship)

# Intersection antar set (yang ada)
print("---Intersection antar set")
fellowship = {'aragorn', 'gimli', 'legolas', 'gandalf', 'boromir', 'frodo', 'sam', 'merry', 'pippin'}
hobbits = {'frodo', 'sam', 'merry', 'pippin', 'bilbo'}

duplicates = fellowship.intersection(hobbits)
print("duplicates:", duplicates)

# Pengecekan keanggotaan subset
print('---Pengecekan keanggotaan subset')
fellowship = {'aragorn', 'gimli', 'legolas', 'gandalf', 'boromir', 'frodo', 'sam', 'merry', 'pippin'}

hobbits_1 = {'frodo', 'sam', 'merry', 'pippin', 'bilbo'}
res_1 = hobbits_1.issubset(fellowship)
print('res_1', res_1)

hobbits_2 = {'frodo', 'sam', 'merry', 'pippin'}
res_2 = hobbits_2.issubset(fellowship)
print("res_2:", res_2)

# Pengecekan keanggotaan superset
print('---Pengecekan keanggotaan superset')
fellowship = {'aragorn', 'gimli', 'legolas', 'gandalf', 'boromir', 'frodo', 'sam', 'merry', 'pippin'}

hobbits_1 = {'frodo', 'sam', 'merry', 'pippin', 'bilbo'}
res_1 = fellowship.issuperset(hobbits_1)
print("res_1:", res_1)

hobbits_2 = {'frodo', 'sam', 'merry', 'pippin'}
res_2 = fellowship.issuperset(hobbits_2)
print("res_2:", res_2)

# Pengecekan keanggotaan disjoint
print('---Pengecekan keanggotaan disjoint')
fellowship = {'aragorn', 'gimli', 'legolas', 'gandalf', 'boromir', 'frodo', 'sam', 'merry', 'pippin'}

res_1 = fellowship.isdisjoint({'aragorn', 'gimli'})
print('res_1', res_1)

res_2 = fellowship.isdisjoint({'pippin', 'bilbo'})
print("res_2:", res_2)

res_3 = fellowship.isdisjoint({'bilbo'})
print("res_3:", res_3)

# Union
print('---Union')
hobbits = {'frodo', 'sam', 'merry', 'pippin'}
dunedain = {'aragorn'}
elf = {'legolas'}
dwarf = {'gimly'}
human = {'boromir'}
maiar = {'gandalf'}

fellowship_1 = hobbits.union(dunedain).union(elf).union(dwarf).union(human).union(maiar)
print("fellowship_1", fellowship_1)

# Update
print('---Update')
hobbits = {'frodo', 'sam', 'merry', 'pippin'}
dunedain = {'aragorn'}
elf = {'legolas'}
dwarf = {'gimly'}
human = {'boromir'}
maiar = {'gandalf'}

fellowship_2 = set()
fellowship_2.update(hobbits)
fellowship_2.update(dunedain)
fellowship_2.update(elf)
fellowship_2.update(dwarf)
fellowship_2.update(human)
fellowship_2.update(maiar)
print("fellowship_2", fellowship_2)

# Operator bitwise or
print('---Operator bitwise or')

a = set('abracadabra')
b = set('alacazam')

res = a | b
print(res)

# Operator bitwise and
print('---Operator bitwise and')

a = set('abracadabra')
b = set('alacazam')

res = a & b
print(res)

# Operator bitwise exclusive or

a = set('abracadabra')
b = set('alacazam')

res = a ^ b
print(res)

# Operator -
print('---Operator -')
a = set('abracadabra')
b = set('alacazam')  

res = a - b
print(res)

# Konversi string ke set
print('---KOnversi string ke set')

data = set('abcda')
print('data', data)

# Konversi list ke set
print('---Konversi list ke set')

data = set(['a', 'b', 'c'])
print('data', data)

# Konversi tuple ke set
print('---Konversi tuple ke set')

data = set(('a', 'b', 'c'))
print('data', data)

# Set comprehension
print('---Set comprehension')

res = { x for x in set('abracadabra') if x not in set('abc')}
print(res)

# frozenset
print('---Frozenset')

a = frozenset('abracadabra')
print(a)

b = frozenset('alacazam')
print(b)