
store = {"Book": 10, "Pen": 20, "Bag": 5}
item_to_buy = input("Enter the item to buy: ").title()
item_quant = int(input("Enter the quantity to purchase: "))

print(f"Before purchase:" , store)
store[item_to_buy] -= item_quant
print(f"After purchase:" , store)