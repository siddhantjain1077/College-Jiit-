student_names = []

birth_months = []

for i in range(3):
    name = input("Enter the name of student {}: ".format(i + 1))
    month = int(input("Enter the birth month of student {} (in numeral form): ".format(i + 1)))

    student_names.append(name)

    birth_months.append(month)

print("\nNames of students excluding those born in July:")
for i in range(10):
    if birth_months[i] == 7:
        continue

    print(student_names[i])

