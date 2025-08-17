# Question 7 

# Mixing Data Types
 # - Ask the user for:
'''    - Your age (integer)
    - Your height in meters (float)
    - Your name (string)
- Print a sentence using f-string showing all details in one line, making sure you type-cast where necessary.'''

user_age = int(input("Enter your age: "))
user_height = float(input("Enter your height: "))
user_name = input("Enter your name: ")
print(f"I am {user_age} year's old with height of {user_height} meters and my name is {user_name}.")
