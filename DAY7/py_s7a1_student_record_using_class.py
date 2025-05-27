# You are creating a system for a school to manage student records. Each student has:
# A name
# An age
# A grade
# A roll number
# Instead of writing separate variables for each student, you decide to create a class
# called Student to represent the blueprint for any student.
# By using a class, you can create multiple student records quickly and manage them
# efficiently.
# Objective
# Define a class called Student.
# Use attributes (name, age, grade, roll number).
# Create multiple student objects.
# Display each student’s information using a method.


class Student:
    def __init__(self, name, age, grade, roll_no):
        self.name = name
        self.age = age
        self.grade = grade
        self.roll_no = roll_no

    def display(self):
        print(f"Student name: {self.name}\n Student age: {self.age}\n Student grade: {self.grade}\n Student roll number: {self.roll_no}\n")


#list of student
students = []
print("-- Enter Student Details --")
student_no = input("How many students do you want to enter? ")
num_students = int(student_no)

for i in range(num_students):
    print(f"\nEntering details for student {i+1}:")
    name = input("Enter Name: ")
    age = input("Enter Age: ")
    grade = input("Enter Grade: ")
    roll_no = input("Enter Roll Number: ")

    # Create and store the student object
    student = Student(name, age, grade, roll_no)
    students.append(student)

# Display all students
print("\n-- Student Records --")
for student in students:
    student.display()