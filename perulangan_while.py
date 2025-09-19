# keyword while
print("---while")
should_continue = True

while should_continue:
    n = int(input("enter an even number greater than 0: "))

    if n <= 0 or n % 2 == 1:
        print(n, "is not even number greater than 0")
        should_continue = False

    else:
        print("number:", n)

print()
n = int(input("enter max data: "))
i = 0

while i < n:
    print("number", i)
    i += 1

# nested while
print("---nested while")

n = int(input("enter max data:"))
i = 0

while i < n:
    j = 0

    while j < n - i:
        print("*", end=" ")
        j += 1

    print()
    i += 1

    