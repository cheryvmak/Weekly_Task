# Question 10
 
# School Fees Breakdown
'''- Ask for:
    - School name
    - Tuition fee (float)
    - Hostel fee (float)
    - Feeding fee (float)

- Calculate the total and print it in receipt format with each fee on a new line.'''

School_name = input("Enter your school name: ")
Tution_fee = float(input("Enter your tution fee: "))
Hostel_fee = float(input("Enter hostel fee: "))
Feeding_fee = float(input("Enter your feeding fee: "))
total_fee = Tution_fee + Hostel_fee + Feeding_fee
print(f"School name:\t\t{School_name}\nTution fee:\t\t#{Tution_fee:,.2f}k\nHostel fee:\t\t#{Hostel_fee:,.2f}k\nFeeding fee:\t\t#{Feeding_fee:,.2f}k\t\t\nTotal fee:\t\t#{total_fee:,.2f}k")
