# Question 6 

# Electricity Bill Formatter

''' - Ask for:
   - Customer’s full name
   - Units consumed (kWh) – integer
   - Cost per unit – float
- Calculate the total bill and print it in a neatly formatted receipt using escape sequences for line breaks.'''

cus_last_name = input("Enter your last name: ")
cus_first_name = input("Enter your first name: ")
unit_cons = int(input("Enter units consumed: "))
Cost_per_unit = float(input("Enter cost per unit: "))
total_bill = unit_cons * Cost_per_unit
print(f"Fullname:\t\t{cus_last_name} {cus_first_name}\nUnits consumed:\t\t{unit_cons}kWh\nCost per unit:\t\t{Cost_per_unit}\nTotal bill:\t\t{total_bill:,}")
