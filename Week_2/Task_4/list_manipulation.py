
# Task 7

# Create a list of five cities
cities = ["Abeokuta", "Ibadan", "Uyo", "Portharcourt", " Benin"]

# print the output
print(f"This is the list of cities entered:", cities)

# Replace the third city with a new one (entered by the user)
cities[2] = input("Enter a new city to replace the third city: ")

# print the output
print(f"This is the updated list after replacing the third city:", cities)

# Remove the last city.
remove_list_city = cities[0:4]

# print the output
print(f"This is the updated list after removing the last city:", remove_list_city)

# Add a new city to the beginning of the list
updated_city_list = remove_list_city
updated_city_list.insert(0, "Lagos")

# print the output
print(f"This is the updated city list after adding new city to the begining of the list:", updated_city_list)
