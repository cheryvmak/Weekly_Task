
# if statement

# for single condition
# age = 20
# if age >= 18:
#     print("You are eligible to vote")


# if else

# for two condition 
# wallet = 400
# price = 500

# if wallet >= price:
#     print("Purchase successful")
# else:
#     print("Insufficient balance")

# if elif else     

# for multiple condition
# score = 85
# if score >= 70:
#     print("Grade A")
# elif score >= 50:
#     print("Grade B")
# else:
#     print("Grade C")

# Nested if 

# if inside if
# age = 19
# citizen = True

# if age >= 18:
#     if citizen:
#         print("You can vote")
#     else:
#         print("You must be a citizen to vote")
# else:
#     print("Too young to vote")


# for LOOP in a list
# Iterates through each element in a LIST.

# fruits = ["apple", "banana", "orange"]
# for fruit in fruits:
#     print(f"I like {fruit}")


# for LOOP for tuple

# Iterates through each element in a TUPLE.This Works like lists, but remember that tuples are immutable.

# coordinates = (0.34654, -0.48585, 0.57477)
# for point in coordinates:
#     print(f"Point: {point}")



# for LOOP for dictionary

# Iterates through each element in a DICTIONARY. Remember that dictionaries have key-value pairs.

# student = {"name": "Tunde", "age": 16, "grade": "A"}
# for key, value in student.items():
#     print(f"{key}: {value}")


# for LOOP for string
# Iterates through each element in a STRING. Remember that strings are sequences of characters.

# word = "PYTHON"
# for char in word:
#     print(char)


# WHILE LOOP

# it is used to execute block of code when the condition is true or false unlike for loop that use sequence

## My code
# count = 1
# while count <= 5:
#     print("Number:", count)
#     count += 1


# Incrementing with `while`

# num = 1
# while num <= 10:
#     print(num, end=" ")   # The loop result will be in one single horizontal
#     num += 1


# Decrementing with `while`

# timer = 10
# while timer > 0:
#     print("Countdown:", timer)
#     timer -= 1


# While with User Input

## Keep asking until the user enters a correct password.

# password = ""
# while password != "python123":
#     password = input("Enter the password: ")

# print("Access Granted!")


# WHILE TRUE

# Keep asking the user for a name until they type "exit".
# while True:
#     name = input("Enter your name (type 'exit' to quit): ")
#     if name.lower() == "exit":
#         print("Goodbye!")
#         break
#     print(f"Hello, {name}")

# ---> I used `break` here. If you dont know what it is or what it is doing, its OK. I will explain it next...

## Useful in chat-like applications, forms, or data entry programs where users may input multiple times until they decide to stop.


#  LOOP CONTROL STATEMENT(BREAK, CONTINUE, PASS)

# They are used to control the behaviour of the loop


# BREAK 

# for num in range(1, 10):
#     if num == 5:
#         break
#     print(num)

#The loop stops completely when num == 5.

# Stop searching when an item is found.

# Exit when user input matches a condition.

# Prevent unnecessary iterations.


# CONTINUE

# this skip unwanted character
# for num in range(1, 6):
#     if num == 3:
#         continue
#     print(num)

# 3 is skipped, but the loop continues.

## Some usecases

#Skip invalid data.

#Ignore unwanted characters (like spaces in a string).


# PASS

# for num in range(1, 6):
#     if num == 3:
#         pass   # do nothing for now
#     else:
#         print(num)

# At num == 3, Python executes pass (nothing happens).

## Some usecases

# Writing code structure (to fill in later).

# Placeholders in class/method definitions.

# Temporarily disable parts of code.


# Try and think through this...

# while True:
    # print("\nMenu:")
    # print("1. Say Hello")
    # print("2. Say Goodbye")
    # print("3. Exit")
    
    # choice = input("Choose an option: ")
    
    # if choice == "1":
    #     print("Hello")
    # elif choice == "2":
    #     print("Goodbye")
    # elif choice == "3":
    #     print("Exiting program...")
    #     break
    # else:
    #     print("Invalid choice. Try again.")


# Try and use while True for validation

# while True:
#     age = input("Enter your age: ")
#     if age.isdigit():
#         print(f"Your age is {age}")
#         break
#     else:
#         print("Invalid input. Please enter a number.")



# LEets make a guess

# secret = "python"

# while True:
#     guess = input("Guess the secret word: ")
#     if guess.lower() == secret:
#         print("Correct! You guessed the word.")
#         break
#     else:
#         print("Wrong! Try again.")


# Do you remember this?

balance = 1000  

while True:
    print("\nATM Menu:")
    print("1. Check Balance")
    print("2. Withdraw")
    print("3. Exit")

    choice = input("Enter choice: ")

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
