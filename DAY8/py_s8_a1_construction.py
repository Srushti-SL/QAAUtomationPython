# -You’re building a system for an online movie ticket booking app.
# Every time a user books a ticket, the system should store information like:
# Movie name
# Show time
# Seat number
# User name
# Whenever a ticket is created, these details should be initialized automatically
# using a constructor.
# Your job is to create a class called Ticket, and use a constructor
# (__init__ method in Python) to initialize ticket details when a new object is created.
# Objective:
# Create a class with a constructor.
# Use the constructor to initialize object attributes.
# Create multiple ticket objects and display their details

class Ticket:
    def __init__(self, mname, stime, sno, uname):
        self.mname = mname
        self.stime = stime
        self.sno = sno
        self.uname = uname

    def display(self):
        print(f"Movie name: {self.mname}\n Show time: {self.stime}\n Seat number: {self.sno}\n Username: {self.uname}\n")

# list of tickets
tickets = []
print("-- Enter Ticket Details --")
tkt_no = input("How many ticket details do you want to enter?: ")
num_tickets = int(tkt_no)

for i in range(num_tickets):
    print(f"\nEntering details for Ticket {i + 1}:")
    mname = input("Enter Movie Name: ")
    stime = input("Enter Show time: ")
    sno = input("Enter Seat Number: ")
    uname = input("Enter User name: ")

    # Create and store the ticket object
    ticket = Ticket(mname, stime, sno, uname)
    tickets.append(ticket)

# Display
print("\n-- Ticket details --")
for ticket in tickets:
    ticket.display()