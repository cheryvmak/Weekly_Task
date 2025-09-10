# Predefined list of items
items = ['apple', 'banana', 'orange', 'milk', 'bread']

# Initialize empty dictionary for items and prices
store = {}

# Collect prices for each item
print("Enter prices for the following items:")
for item in items:
    while True:
        price = input(f"Enter price for {item}: ")
        if price.replace('.', '', 1).isdigit() and float(price) >= 0:  # Basic validation for non-negative number
            store.update({item: float(price)})  # Use .update() to add item-price pair
            break
        else:
            print("Please enter a valid non-negative number!")

# Display all items and prices
print("\nStore Inventory:")
print("---------------")
for item in store.keys():  # Use .keys() to iterate over items
    print(f"\t{item}:\t${store[item]:.2f}")

# Allow user to update a price
while True:
    print("\nAvailable items:", list(store.keys()))  # Show available items
    item_to_update = input("Enter item to update price (or 'done' to exit): ").lower().strip()
    
    if item_to_update == 'done':
        break
    
    if item_to_update in store:  # Check if item exists
        while True:
            new_price = input(f"Enter new price for {item_to_update}: ")
            if new_price.replace('.', '', 1).isdigit() and float(new_price) >= 0:
                store[item_to_update] = float(new_price)  # Update price with assignment
                print(f"Price for {item_to_update} updated to ${new_price:.2f}")
                break
            else:
                print("Please enter a valid non-negative number!")
    else:
        print("Item not found! Please choose from the available items.")

# Display final inventory
print("\nUpdated Store Inventory:")
print("-----------------------")
for item in store.keys():
    print(f"\t{item}:\t${store[item]:.2f}")