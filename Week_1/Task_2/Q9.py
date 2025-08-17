# Question 9

# Nigerian Festival Info
'''- Ask for:
     - Festival name (string)
     - Location (string)
     - Month held (string)
- Display the info with quotation marks around the festival name using escape sequences `(\")`.'''


fest_name = input("Enter festival name: ")
location =  input("Enter the location: ")
month_held = input("Enter the month it is held: ")
print(f"The \"{fest_name}\"festival is held in {location} in the month of {month_held}")