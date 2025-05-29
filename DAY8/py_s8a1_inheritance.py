# Salary Management System using Object-Oriented Programming with inheritance,
# involving Employee and Manager classes.
# Scenario:
# You're creating a salary management program for a company. There are two types of people:
# Employees: Have basic details like name, ID, and base salary.
# Managers: Are also employees but get additional bonuses and perks.

class Employee:
    def __init__(self, ename, emp_id, esalary):
        self.ename = ename
        self.emp_id = emp_id
        self.esalary = esalary

    def display(self):
        print(f"Employee Name: {self.ename}")
        print(f"Employee ID: {self.emp_id}")
        print(f"Employee Salary: ${self.esalary:.2f}\n")


class Manager(Employee):
    def __init__(self, ename, emp_id, esalary, bonus, perks):
        super().__init__(ename, emp_id, esalary)
        self.bonus = bonus
        self.perks = perks

    def display(self):
        total_salary = self.esalary + self.bonus + self.perks
        print(f"Manager Name: {self.ename}")
        print(f"Manager ID: {self.emp_id}")
        print(f"Base Salary: ${self.esalary:.2f}")
        print(f"Bonus: ${self.bonus:.2f}")
        print(f"Perks: ${self.perks:.2f}")
        print(f"Total Salary: ${total_salary:.2f}\n")


employees = []

print("-- Salary Management System --")
n = int(input("How many people do you want to enter?: "))

for i in range(n):
    print(f"\nEntering details for person {i+1}")
    role = input("Is this person a Manager or Employee? (Manager/Employee): ").strip().upper()

    name = input("Enter Employee Name: ")
    emp_id = input("Enter Employee ID: ")
    base_salary = float(input("Enter Base Salary: "))

    if role == 'Manager':
        bonus = float(input("Enter Bonus: "))
        perks = float(input("Enter Perks: "))
        person = Manager(name, emp_id, base_salary, bonus, perks)
    else:
        person = Employee(name, emp_id, base_salary)

    employees.append(person)


print("\n-- Salary Details --")
for emp in employees:
    emp.display()