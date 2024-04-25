def calculate_percentage(marks):
    total_marks = sum(marks)
    return (total_marks / (len(marks) * 100)) * 100

num_students = int(input("Enter the number of students: "))
students = []

for i in range(num_students):
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    section = input("Enter section: ")
    marks = []
   
    for j in range(1,4):
        mark =input(f"Enter marks for subject {j}:")
        marks.append(mark)
       
    total_marks = sum(marks)
    percentage = calculate_percentage(marks)
    student_info = {'name': (first_name, last_name), 'section': section, 'marks': marks, 'percentage': percentage}
    students.append(student_info)

print("\nResult Sheet:")
for student in students:
    first_name, last_name = student['name']
    section = student['section']
    percentage = student['percentage']
    print(f"Name: {first_name} {last_name}, Section: {section}, Percentage: {percentage}%")
