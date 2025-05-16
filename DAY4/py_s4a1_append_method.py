# Create an empty list (shopping cart).
# Ask the user to enter items they want to buy.
# Use a loop to append each item to the list.
# Show the final list at the end.

def my_grocery_cart(items):
    seen = set()
    item_list = []
    for item in items:
        if item in seen:
            item_list.append(item)
        else:
            seen.add(item)
    return item_list

shopping_cart = []

print("Enter items to add to the shopping cart. Type 'done' when finished:")

while True:
    item = input("Enter item: ")
    if item.lower() == 'done':
        break
    shopping_cart.append(item)

print("\nFinal Shopping Cart:")
print(shopping_cart)
