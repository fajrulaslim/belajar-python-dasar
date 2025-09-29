# Assigment
num_1 = 12
num_2 = 24
num_3 = num_1 + num_2
print(num_3)

# perbandingan
res_1 = 4 == 5
res_2 = 4 != 5
res_3 = 4 > 5
res_4 = 4 < 5
res_5 = 5 >= 5
res_6 = 4 <=5
print(res_1)
print(res_2)
print(res_3)
print(res_4)
print(res_5)
print(res_6)

# operator logika
res_1 = (4 == 5) and (2 != 3)
res_2 = (4 == 5) or (2 != 3)
res_3 = not(2 == 3)
print("---")
print(res_1)
print(res_2)
print(res_3)

# operator membership (in)
sample_list = [2, 3, 4]
is_3_exist = 3 in sample_list
print("---")
print(is_3_exist)

sample_tuple = ("hello", "python")
is_hello_exist = "hello" in sample_tuple
print(is_hello_exist)

sample_dict = { "nama": "Fajrul", "age": 16 }
is_key_nama_exists = "nama" in sample_dict
print(is_key_nama_exists)

sample_set = {"sesuk", "preiii"}
is_prei = "preiii" in sample_set
print(is_prei)

text = "hello world"
is_substring = "orl" in text
print(is_substring)