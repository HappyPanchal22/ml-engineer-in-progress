def average_grade(student_dict):
    total = 0
    for grade in student_dict.values():
        total += grade
    average = total / len(student_dict)
    return average

def highest_grade(student_dict):
    first_name = list(student_dict.keys())[0]
    max_name = first_name
    max_grade = student_dict[first_name]
    for name, grade in student_dict.items():
        if grade > max_grade:
            max_name = name
            max_grade = grade
    return max_name, max_grade

def lowest_grade(student_dict):
    first_name = list(student_dict.keys())[0]
    min_name = first_name
    lowest = student_dict[first_name]
    for name, grade in student_dict.items():
       if grade < lowest:
          min_name = name
          lowest = grade

    return min_name, lowest


students = int(input("Enter the number of students: "))
student_dict = {}
for student in range(students):
    name = input("Enter the name of the student: ")
    grade = float(input("Enter the grade of the student: "))
    while grade < 0 or grade > 100:
        print("Invalid grade. Please enter a grade between 0 and 100.")
        grade = float(input("Enter the grade of the student: "))
    student_dict[name] = grade


for name, grade in student_dict.items():
    print(f"{name}: {grade}")

top_name, top_grade = highest_grade(student_dict)
low_name, low_grade = lowest_grade(student_dict)
print(f"Average grade: {average_grade(student_dict)}")
print(f"Highest grade: {top_grade} obtained by {top_name}")
print(f"Lowest grade: {low_grade} obtained by {low_name}")