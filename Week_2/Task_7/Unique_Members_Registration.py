# Task 4

# user enter for 3 names seperated by commas
names = input("Enter three names seperated by commas: ").split(",")

# Convert to set to ensure uniqueness
set_of_names = set(names)

# print set of names
print(set_of_names)

# create dictionary using dictionary comprehension
names_dict  = {name: len(name) for name in set_of_names }

# print the output
print(names_dict)
