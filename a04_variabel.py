# Membuat variabel seperti m,emberi label pada kotak
nama = "Budi"       # Kotak bernama 'nama' berisi text 'Budi'
umur = 25
tinggi = 170.5
nol = 0

populasi_dunia = 780000000
angka_besar = 123456789005236532632632

print(nama)
print(type(umur))
print(type(populasi_dunia))

nama = 'Budi'
kota = 'Jakarta'

alamat = "Jl. Merdeka No. 123"
pesan = "Selamat data di python"

puisi = """
Ini adalah puisi
yang terdiri dari
beberapa baris
"""

empty_string = ''
another_empty = ""

hobi = "Nonton"
laki = True

print("nama: %s" % nama)
print("hobi: %s, umur: %d, laki: %r" % (hobi, umur, laki))

nilai1, nilai2, nilai3, nilai4 = 24, 25, 26, 27
nilai_rata_rata = (nilai1 + nilai2 + nilai3 + nilai4) / 4
print("rata-rata: %d" % nilai_rata_rata)