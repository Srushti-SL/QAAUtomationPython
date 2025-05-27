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
    def display(self):
        print(f"Student name: {self.name}")
        print(f"Student age: {self.age}")
        print(f"Student grade: {self.grade}")
        print(f"Student roll number: {self.roll_no}\n")

# List of students
students = []

print("-- Enter Student Details --")
num_students = int(input("How many students do you want to enter? :"))

for i in range(num_students):
    print(f"\nEntering details for student {i+1}:")
    name = input("Enter Name: ")
    age = input("Enter Age: ")
    grade = input("Enter Grade: ")
    roll_no = input("Enter Roll Number: ")

    student = Student()
    student.name = name
    student.age = age
    student.grade = grade
    student.roll_no = roll_no

    students.append(student)

# Display
print("\n-- Student Records --")
for student in students:
    student.display()
