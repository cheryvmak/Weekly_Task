
print("--"* 15)
print("Profile Information")
print("--"* 15)
# Ask user for details (with loop for control flow)
user_info = []
details = ["First Name", "Age", "Favorite Color", "Home Town"]

for info in details:   # control flow using loop
    value = input(f"Enter your {info}: ").title()
    user_info.append(value)

# Store in tuple
profile = tuple(user_info)

# Unpack tuple into variables
details[0],details[1],details[2],details[-1], = profile

# formatting and printing each user info 
print("\nYour Profile")
print(f"First Name:\t\t{details[0]}")
print(f"Age:\t\t\t{details[1]}")
print(f"Favorite Color:\t\t{details[2]}")
print(f"Home Town:\t\t{details[-1]}")



