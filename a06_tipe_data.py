# integer
number_1 = 1234
print("integer:", number_1)

# float
number_2 = 3.14
print("float:", number_2)

# complex
number_3 = 120+3j
print("complex:", number_3)

# string sebaris
string_1 = "hello python"
print(string_1)

string_2 = """\
Selamat
Belajar
Python"""
print(string_2)

# boolean
bool_1 = True
bool_2 = False

# none
data = None
print(data)

# list - Mutable (bisa diubah isinya)
list_1 = [2, 4, 6, 8]
list_2 = ["grayson", "jason", "tim", "damian"]
list_3 = [24, False, "Hello Python"]

print(list_1)
print(list_2)
print(list_3)
print(list_3[1])

# tuple - Immutable (tidak bisa diubah)
tuple_1 = (1, 2, 3)
tuple_2 = ("numenor", "valinor")
tuple_3 = (24, True, "Hello Python")

# Dictionary
profile_1 = {
    "name": "Fajrul",
    "is_male": True,
    "age": 35,
    "hobbies": ["gaming", "learning"]
}
print("name:", profile_1["name"])

# Set, sama dengan dictionari tapi: tidak bisa menyimpan urutan, tidak bisa diakses dengan index, tidak bisa diubah tapi bisa dihapus
set_1 = {"pineapple", "spaghetti"}
print(set_1)