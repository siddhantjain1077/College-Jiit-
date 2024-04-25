student_names = []
student_marks = []

for i in range(10):
    name = input("Enter the name of student {}: ".format(i + 1))
    marks = int(input("Enter the marks of student {}: ".format(i + 1)))

    student_names.append(name)

    student_marks.append(marks)


grades = []
for marks in student_marks:
    if marks >= 90:
        grades.append('A')
    elif 75 <= marks <= 89:
        grades.append('B')
    elif 60 <= marks <= 74:
        grades.append('C')
    elif 45 <= marks <= 59:
        grades.append('D')
    else:
        grades.append('E')

print("\nStudent Report:")
for i in range(10):
    print("Name: {}, Marks: {}, Grade: {}".format(student_names[i], student_marks[i], grades[i]))
