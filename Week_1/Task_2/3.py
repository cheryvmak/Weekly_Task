
balance = 50000

while True:
    print("\nMenu:")
    print("1. Balance")
    print("2. Withdraw")
    print("3. Exit")
    
    choice = input("Choose an option: ")
    
    if choice == "1":
        print(f"Your balance is: {balance}")
    elif choice == "2":
        amount = int(input("Enter withdrawal amount: "))
        if amount <= balance:
            balance -= amount
            print(f"Withdrawal successful. New balance: {balance}")
        else:
            print("Insufficient funds.")
    elif choice == "3":
        print("Thank you for using our ATM. Goodbye!")
        break
    else:
        print("Invalid option. Try again.")
