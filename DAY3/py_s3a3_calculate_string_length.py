# you need a program that:
# Accepts a username from the user.
# Calculates the length of the username.
# Displays the length.
# Optionally tells the user whether the username is too short, too long, or acceptable.

MIN_LEN = 5
MAX_LEN = 15

#Input from user
username = input("Enter username: ")
len_un = len(username)
print(f"Your username is {len_un} characters long.")

if len_un < MIN_LEN:
    print("Your Username is too short, minimum length is 5 characters")
elif len_un > MAX_LEN:
    print("Your Username is too long, maximum length is 15 characters")
else:
    print("Username is valid")


