# keyword if
grade = 90

if grade == 100:
    print("perfect")

if grade == 90:
    print("ok")
    print("keep working hard!")

print("---")
# keyword elif
str_input = input("Enter your grade: ")
grade = int(str_input)

if grade == 100:
    print("perfect")

elif grade >= 85:
    print("awesome")

elif grade >= 65:
    print("passed the exam")

print("---")
# keyword else
str_input = input("Enter your grade: ")
grade = int(str_input)

if grade == 100:
    print("perfect")

elif grade >= 85:
    print("awesome")

elif grade >= 65:
    print("passed the exam")

else:
    print("below the passing grade")

print("---")
# nested
str_input = input("Enter your grade: ")
grade = int(str_input)

if grade == 100:
    print("perfect")

elif grade >= 85:
    print("awesome")

elif grade >= 65:
    print("passed the exam")

    if grade <= 70:
        print("but you need to improve it")
    else:
        print("with ok grade")

else:
    print("below the passing grade")

print("---")
# dengan operator logika
grade = int(input("Enter your current grade: "))
prev_grade = int(input("Enter your previous grade: "))

if grade >= 90 and prev_grade >= 65:
    print("awesome")

elif grade >= 90 and prev_grade < 65:
    print("awesome.  you definitely working hard, right?")

elif grade > 65:
    print("passed the exam")

else: 
    print("below the passing grade")

if (grade >= 65 and not prev_grade >= 65) or (not grade >=65 and prev_grade >= 65):
    print("at least you passed one exam. good job!")

print("---")
# Ternary
print("passed") if grade >= 65 else print("below the passing grade")

# ternary dengan nilai balik
message = print("passed") if grade >= 65 else print("below the passing grade")
print(message)