# for and range
print('---for and range')
for i in range(5):
    print("index", i)

# list
print("---list")
r = range(5)
print("r:", list(r))

# penerapan fungsi range()
print("---penerapan fungsi range()")
# range(n)
for i in range(3):
    print("index:", i)

# range(start, stop)
print()
for i in range(1, 4):
    print("index:", i)

# range(start, stop, step)
print()
for i in range(1, 10, 2):
    print("index:", i)

# iterasi data list
print("---iterasi data list")
messages = ["morning", "afternoon", "evening"]
for m in messages:
    print(m)

# iterasi data tuple
print("---iterasi data tuple")
numbers = ("twenty four", 24)
for n in numbers:
    print(n)

# iterasi data string
for char in "hello python":
    print(char)

# iterasi data dict
bio = {
    "name": "toyota camry",
    "year": 2024
}
for key in bio:
    print("key:", key, "value:", bio[key])

# iterasi data set
numbers = { "twenty four", 24 }
for n in numbers:
    print(n)

# nested for
print("---nested for")
max = int(input("jumlah bintang:"))

for i in range(max):
    for j in range(0, max-i):
        print("*", end=" ")
    print()