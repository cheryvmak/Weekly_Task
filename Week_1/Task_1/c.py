# # tran_pin = print(int(input("5.\tEnter your 4 digit pin: ")))

# # #if tran_pin == int(2511) and len(tran_pin) == 4:
# # if tran_pin.isdigit() and len(pin) == 4:
# #     print(f"The pin provided is correct")
# # else:
# #     print("please check your transaction pin correctly and enter exactly 4 digits.")




# # Fixed PIN
# fixed_pin = "1234"

# # Allow 3 attempts
# for attempt in range(3):
#     user_pin = input("5.\tEnter your 4 digit pin: ")

#     if user_pin.isdigit() and len(user_pin) == 4:
#         if user_pin == fixed_pin:
#             print("✅ PIN accepted. Access granted.")
#             break
#         else:


#             print("❌ Incorrect PIN.")
#     else:
#         print("⚠️ PIN must be exactly 4 digits.")

#     if attempt == 2:
#         print("🚫 Too many attempts. Access blocked.")



#   data_amount = int(input("1.\tEnter data amount to purchase: "))


# Data plans dictionary
data_plan = {200: "1GB", 500: "2GB", 1000: "3GB", 1500: "5GB"} 

# Display menu
print("Available Data Plans:")
for i, (price, plan) in enumerate(data_plan.items(), start=1):
    print(str(i) + ". ₦" + str(price) + " = " + plan)

# Ask user to choose a plan
choice = int(input("\nEnter the number of your choice: "))

# Convert choice into dictionary item
if 1 <= choice <= len(data_plan):
    # Convert dictionary to list of tuples to access by index
    price, plan = list(data_plan.items())[choice - 1]
    print(f"\n✅ You selected {plan} plan for ₦{price:,}.")
else:
    print("\n❌ Invalid choice. Please try again.")
