# Task 5

# enter 3 shopping_item 
shopping_item_1 = (input("Enter shopping item 1: "))
shopping_item_2 = (input("Enter shopping item 2: "))
shopping_item_3 = (input("Enter shopping item 3: "))

# create empty list
shopping_list = []

# attached the entered shopping list to the empty list
print(shopping_list.append(shopping_item_1))
print(shopping_list.append(shopping_item_2))
print(shopping_list.append(shopping_item_3))

# print the list
print(f"The list of shopping item:", shopping_list)

# convert the list to tuple
my_shopping_list = tuple(shopping_list)

# print the tuple
print("The shopping item in a tuple:", my_shopping_list)

# create a new shopping list from the tuple created earlier
new_shopping_list = (list(my_shopping_list))
# print the new shopping list
print(f"Convert back to list:", new_shopping_list)

# enter additional items
new_item_1 = input("Enter additional item 1: ")
new_item_2 = input("Enter additional item 2: ")

# attached the additional item to the new shopping list
new_shopping_list.append(new_item_1)
new_shopping_list.append(new_item_2)

# print the new list
print(f"This now the shopping list:", new_shopping_list)

# convert the updated list to tuple
updated_shopping_list = tuple(new_shopping_list)
# print the updated shopping  list
print(f"This is the updated shopping list in tuple:", updated_shopping_list)
# print the updated list to display items seperated by|
print(f"This is the updated shpping list seperated by |:", "|".join(updated_shopping_list))
