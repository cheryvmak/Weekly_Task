# Question 12 

# Simulated USSD Menu Interaction
'''- You are to design a mock USSD interface for a mobile service.
 - Requirements:
   1. When the user runs the program, display a welcome screen with a Nigerian context greeting.
   2. Ask the user to "dial" a USSD code (e.g., *123#) and store it in a variable.
   3. Print a menu with at least 3 options (e.g., "Check Balance", "Buy Airtime", "Buy Data") using newline escape sequences `(\n)` for formatting.
   4. Ask the user to choose an option (1, 2, or 3) and store their choice in a variable.'''



print(f"You are welcome to chery Mobile Service\n")
ussd = input("Please dial your USSD code(e.g *123#): ")
print("\n you have dialed:", ussd)
print("\n1. Check balance\n2. Buy Airtime\n3. Buy Data")
choice = input("Enter an option (1, 2, or 3):")
print(f"\nThank you! You selected option: {choice}")

amount = 0
if choice in ["2", "3"]:  # Airtime or Data
    amount = float(input("Enter the amount: "))

if choice == "1":
    print("\nTransaction Summary: Your account balance is ₦10,000.00.")
elif choice == "2":
    print(f"\nTransaction Summary: You have successfully purchased ₦{amount:,.2f} worth of airtime.")
elif choice == "3":
    print(f"\nTransaction Summary: You have successfully purchased ₦{amount:,.2f} worth of data.")
else:
    print("\nInvalid selection. Please try again.")
