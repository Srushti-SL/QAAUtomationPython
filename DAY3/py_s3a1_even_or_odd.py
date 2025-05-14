# write a program that:
# Takes a ticket number as input.
# Uses a function to check if the number is even or odd.
# Displays which gate the person should go to.
# Objectives:
# Take user input for the ticket number.
# Use a function to check if the number is even or odd.
# Display which gate the person should enter from.

def even_or_odd(tktno):
    if tktno%2 == 0:
        print("even numbered enter gate A")
    else:
        print("odd numbered enter gate B")

#input from user
tktno = int(input("Enter ticket number: "))
even_or_odd(tktno)