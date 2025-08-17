
# Task 5

# Create a tuple for names and phone numbers
name_1 = input("Enter first name: ")
phone_no_1 = int(input("Enter the first phone number: "))

name_2 = input("Enter second name: ")
phone_no_2 = int(input("Enter the second phone number: "))

name_3 = input("Enter third name: ")
phone_no_3 = int(input("Enter the third phone number: "))

# All name and phone number should be in one tuple respectively
name = (name_1, name_2, name_3)
phone_no = (phone_no_1, phone_no_2, phone_no_3)

# create a dictionary from name and phone number
contact = dict(zip(name,phone_no))

# print the dictionary
print(contact)

# ask user to search a name in the dictionary 
search_name = input("search for a name: ")

# if name is present display ,if not display not found
contact_look_up = contact.get(search_name, "Name not found")

# print the output
print(f"{search_name} phone number\t:\t {contact_look_up}")
