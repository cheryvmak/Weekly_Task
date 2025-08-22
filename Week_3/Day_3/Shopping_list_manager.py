# Create an empty list
shopping_list = []

# enter 3 shopping items 
for item in range(3):
    shopping_item = input(f"Enter shopping item {item+1}: ").strip()
    if shopping_item: 
        shopping_list.append(shopping_item)
    else:
        print("Please enter a valid item!")

# print the list as string seperated by commas
print("\nShopping List:", ", ".join(shopping_list))