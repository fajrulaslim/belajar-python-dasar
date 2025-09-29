# break
print("---break")

while True:
    n = int(input("enter a number divisible by 3: "))

    if n % 3 != 0:
        break

    print("%d is divisible by 3" % (n))

# continue
print("---continue")

for i in range(10):
    if i < 3 or i > 7:
        continue
    print(i)

# label perulangan
print("---label perulangan")

max = int(input("jumlah bintang: "))

outer_loop = True
for i in range(max):
    if not outer_loop:
        break

    for j in range(i + 1):
        print("*", end=" ")
        if j >= 7:
            outer_loop = False
            break
    
    print()