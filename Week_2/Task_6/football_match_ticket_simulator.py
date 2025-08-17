# Task  3

# formatting
print("--" * 25)
print("All seat number from 1 to 50")
print("--" * 25)

# create seat numbers from 1 to 50 in a set
seat_no = set(range(1,51))

# print the seat numbers
print(seat_no)

# formatting
print("\n")

# user booked a seat number
user_1 = int(input("Book a seat by entering a number: "))

# removed booked seat from the remaining set
seat_no.remove(user_1)

# formatting and print the remaining seat number
print("\n")
print("The remaining seat_no:", seat_no)

# formatting
print("\n")

# another user booked a seat number
user_2 = int(input(f"Book a seat by entering a number: "))

# removed the booked seat from the remaining set
seat_no.remove(user_2)

# formatting and print the remaining seat number
print("\n")
print(f"The remaining seat_no are:", seat_no)

# formatting
print("\n")

# another user booked a seat number
user_3 = int(input("Book a seat by entering a number: "))

# removed the booked seat from the remaining set
seat_no.remove(user_3)

# formatting and print the remaining seat number
print("\n")
print("The remaining seat_no are:", seat_no)

# formatting
print("\n")

# another user booked a seat number
user_4 = int(input("Book a seat by entering a number: "))

# removed the booked seat from the remaining set
seat_no.remove(user_4)

# formatting and print the remaining seat number
print("\n")
print("The remaining seat_no are:", seat_no)

print("\n")

# another user booked a seat number
user_5 = int(input("Book a seat by entering a number: "))

# removed the booked seat from the remaining set
seat_no.remove(user_5)

# formatting and print the remaining seat number
print("\n")
print("The remaining seat_no are:", seat_no)
