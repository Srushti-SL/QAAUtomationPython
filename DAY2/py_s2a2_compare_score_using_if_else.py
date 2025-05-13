#Write a program that
#Takes the scores of two students as input.
#Compares the scores using an if-else statement.
#Displays who scored higher or if it’s a tie.

std1 = input("Enter the score of student1: ")
std1 = int(std1)
std2 = input("Enter the score of student2: ")
std2 = int(std2)
if std1>std2:
    print("student1 has scored higher")
elif std1<std2:
    print("student2 has scored higher")
elif std1==std2:
    print("It's a tie")
# else:
#     print("there is something missing")