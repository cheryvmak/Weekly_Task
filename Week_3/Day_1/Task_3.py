# Task 3

# create list of item and another list of prices
items = ["Book", "Pen", "Bag"]
prices = [500, 100, 2000]

#  start with empty cart_total
cart_total = 0

# using assignment operator to add the first, second, and third score
cart_total +=  prices[0] 
cart_total +=  prices[1] 
cart_total +=  prices[2] 

# print the items
print(f"Items: ",  items)
# print the total price of the item
print(f"Total price: ", cart_total)