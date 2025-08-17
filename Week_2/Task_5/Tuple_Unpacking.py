# Task 4


# enter user info
first_name = input("Enter your first_name: ")
age = int(input("Enter your age: "))
fav_color = input("Enter your favorite color: ")
home_town = input("Enter your home town: ")

# create empty list
profile = []

# attached the entered user info to the empty list
print(profile.append(first_name))
print(profile.append(age))
print(profile.append(fav_color))
print(profile.append(home_town))

# print the list
print(f"This is the user profile entered:",profile)

# formatting
print("\n")

# convert the list to tuple
updated_profile = tuple(profile)

# print the tuple
print(f"This is user profile list:",updated_profile)

# formatting
print("\n")

# formatting and printing each user info 
print(f"first_name:\t{updated_profile[0]}")
print(f"age:      \t{updated_profile[1]}")
print(f"fav_color:\t{updated_profile[2]}")
print(f"home_town:\t{updated_profile[3]}")

