
# Task 1

# enter three favorite Nigerian dishes (one at a time)
fav_dish_1 = input("Enter your first Nigeria favorite dish: ")
fav_dish_2 = input("Enter your second Nigeria favorite dish: ")
fav_dish_3 = input("Enter your third Nigeria favorite dish: ")

# create empty list
fav_dish = []

# attached the entered dishes to the empty list
print(fav_dish.append(fav_dish_1))
print(fav_dish.append(fav_dish_2))
print(fav_dish.append(fav_dish_3))

# print the list
print(f"This list contains user favorite dish: {fav_dish}")

# formatting
print("\n")

# convert the list to tuple
favor_dish = (tuple(fav_dish))

# print the tuple
print(f"The tuple contains user favorite dish: {favor_dish}")

# formatting
print("\n")

# print each dish on a new line
print(f"This is the user favorite dish each on a new line:")
print("\n")
print("\n".join(favor_dish))