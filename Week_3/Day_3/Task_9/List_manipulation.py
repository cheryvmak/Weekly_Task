# Create a list of five cities
cities = ["Abeokuta", "Ibadan", "Uyo", "Portharcourt", " Benin"]

# print the output
print(f"This is the list of cities entered:", cities)
print("\n")
# Replace third city with the new one
new_city = input("Enter a new city to replace uyo: ").strip().title()

 # using control structure to replace third city with a new one
if new_city: 
    cities[2] = new_city
else:
    print("please provide input")
print(f"This is city list after replacing the third city:", cities)
print("\n")

# Remove the last city
remove_list_city = cities[0:4]
print(f" This is the city list after removing the last city:", remove_list_city)
print("\n")

# # Add a new city to the beginning
updated_city_list = input("Enter a new city for addition at the beginning of the list: ").strip().title()

# Using control structure to add new city to the list
if updated_city_list:
    remove_list_city.insert(0, updated_city_list)
else:
    print("No input provided, there is no city added at the beginning.")

# Print the updated list
print("\n")
print("--"*20)
print("\t Final city list")
print("--"*20)
print("\n")
print(f"Final city:", remove_list_city)
