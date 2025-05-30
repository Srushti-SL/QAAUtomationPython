# You’re developing an ATM withdrawal system. The user can:
# Enter an amount to withdraw
# Get an error if they enter invalid input (non-numeric or negative)
# Get an error if they try to withdraw more than the balance
# Always see a thank-you message, no matter what happens

def atm_withdrawal_system():
    balance = 5000  # Initial balance
    try:
        amount = input("Enter amount to withdraw: ")

        # Check if input is numeric
        if not amount.isdigit():
            raise ValueError("Invalid input. Please enter a numeric value.")

        amount = int(amount)

        # Check for non-positive withdrawal
        if amount <= 0:
            raise ValueError("Withdrawal amount must be greater than zero.")

        # Check if balance is sufficient
        if amount > balance:
            raise ValueError("Insufficient balance.")

        # Proceed with withdrawal
        balance -= amount
        print(f"Withdrawal successful. Remaining balance: ₹{balance}")

    except ValueError as ve:
        print("Error:", ve)

    finally:
        print("Thank you for using the ATM!")


atm_withdrawal_system()
