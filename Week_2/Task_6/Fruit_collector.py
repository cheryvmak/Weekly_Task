# Task 1

# User enter five favorite fruits
fav_fruit_1 = input("Enter favorite fruit 1: ")
fav_fruit_2 = input("Enter favorite fruit 2: ")
fav_fruit_3 = input("Enter favorite fruit 3: ")
fav_fruit_4 = input("Enter favorite fruit 4: ")
fav_fruit_5 = input("Enter favorite fruit 5: ")

# all the fruits entered in one tuple
user_entry = (fav_fruit_1, fav_fruit_2, fav_fruit_3, fav_fruit_4, fav_fruit_5)

# create empty set 
fav_fruit = set()

# use add method in set to attach all the fruit in the empty tuple created earlier
fav_fruit.add(user_entry)

# print the output
print(fav_fruit)
