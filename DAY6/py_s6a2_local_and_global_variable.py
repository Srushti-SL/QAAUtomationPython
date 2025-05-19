# You’re building a basic banking system. There’s a global variable balance that stores
# the user’s total account balance. Inside a function, you perform a temporary
# calculation (like a test deposit) using a local variable, which does not affect the
# actual balance unless updated globally.
# Create a global variable to store the account balance.
# Write a function that uses a local variable to simulate a change.
# Show how local changes don't affect the global value unless explicitly updated.
g_balance = 1000
def temp_deposit(l_balance):        #updating the deposit using the local variable
    temp_amt = g_balance + l_balance
    print(f"temp_amt: {temp_amt}")

def actual_deposit(l_balance):
    global g_balance
    g_balance += l_balance
    print(f"Updated global amount: {g_balance}")

temp_deposit(1000)
print(f"Initial global amount: {g_balance}")
actual_deposit(500)
