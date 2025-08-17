# Task 2

# Create list to store items
items = ["pencil", "dettol","batteries","shoe","detergent"]

# Collect price entered by the users
user_price_1 = float(input("price of the first item: "))
user_price_2 = float(input("price of the second item: "))
user_price_3 = float(input("price of the third item: "))
user_price_4 = float(input("price of the fourth item: "))
user_price_5 = float(input("price of the fifth item: "))

# All price collected in one list
user_prices = [user_price_1, user_price_2, user_price_3, user_price_4, user_price_5]

# Create empty dictionary to store items and their prices
super_market_p_list = {}

# Use dictionary operation to store items and their prices
super_market_p_list["items"] = items
super_market_p_list["user_prices"] = user_prices

# print the dictionary to see the store item and their prices
print(super_market_p_list) 

# Allow user to Update the price of an item
new_user_price_1 = float(input("updated price of the first item: "))
new_user_price_2 = float(input("updated price of the second item: "))
new_user_price_3 = float(input("updated price of the third item: "))
new_user_price_4 = float(input("updated price of the fourth item: "))
new_user_price_5 = float(input("updated price of the fifth item: "))

# All the new prices updated in one list
updated_prices = [new_user_price_1, new_user_price_2, new_user_price_3, new_user_price_4, new_user_price_5]

# Allow user to update the price of an item
super_market_p_list.update({"user_price": updated_prices})

# display all items and prices
print(super_market_p_list)
