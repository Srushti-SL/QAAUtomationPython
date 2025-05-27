# Create an empty list (shopping cart).
# Ask the user to enter items they want to buy.
# Use a loop to append each item to the list.
# Show the final list at the end.

print("-- Grocery Shopping List --")

shopping_cart = []
print("Enter the item to add into the shopping cart, type 'done' to finish: \n")
while True:
    item = input("items: ")
    if item.lower() == 'done':
        break
    else:
        shopping_cart.append(item)

print("\nYour shopping cart contains:")
for i, item in enumerate(shopping_cart, start=1):
    print(f"{i}. {item}")
