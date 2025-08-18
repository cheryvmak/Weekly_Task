# Task 1

# Question 1

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print(f"{num1} == {num2} : {num1 == num2}")

 # Output Explanation: 

'''
if the first number entered is either less than or greater
than the second number entered, and the comparison operator between them is 
equal to, each other then the output will always be False.

Also, if num 1 and num 2 entered are not the same and the comparison operator between them is
equal to, then the output will always be False.

'''
# Use cases examples:
 
# 5 bag of rice of is equal 6 bag of rice (False)
# 2 table is equal to 3 table (False)
# 3 laptop is equal to ten laptop (False)

# code: 
print("\n")
print("Enter Number of bag of rice in store 1 which must be less than those in store 2")

rice_1 = int(input("Enter the number of bag pf rice in store 1: "))
rice_2 = int(input("Enter the number of bag of rice in store 2: "))

print(f"{rice_1} == {rice_2} : {rice_1 == rice_2}")




# Question 2

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print(f"{num1} != {num2} : {num1 != num2}")

 # Output Explanation: 
'''
if the first number entered is either less than or greater
than the second number entered, and the comparison operator between them is 
not equal to, each other then the output will always be True.

Also, if num 1 and num 2 entered are not the same and the comparison operator between them is
not equal to, then the output will always be True.

'''
# Use cases examples:
 
# 5 bag of rice of is not equal 6 bag of rice (True)
# 2 table is not equal to 3 table (True)
# 3 laptop is not equal to ten laptop (True)

# code: 
print("\n")
print("Enter Number of table in room A which must be less than table in room B")

table_1 = int(input("Enter the number of table in room A: "))
table_2 = int(input("Enter the number of table in room B: "))

print(f"{table_1} != {table_2} : {table_1 != table_2}")




# Question 3

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print(f"{num1} > {num2} : {num1 > num2}")

 # Output Explanation: 

'''
if the first number entered is smaller to the second number entered, and the comparison operator between them is 
greater than, then the output will always be False.

'''
# Use cases examples:

# 5 bag of rice is greater than 6 bag of rice (False)
# 2 table is greater than 3 table (False)
# 3 laptop is greater than ten laptop (False)

# code: 
print("\n")
print("Enter number of laptop in Lab A which must be less than those in Lab B")

laptop_1 = int(input("Enter the number of laptop in lab A: "))
laptop_2 = int(input("Enter the number of laptop in lab B: "))

print(f"{laptop_1} > {laptop_2} : {laptop_1 > laptop_2}")





# Question 4
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print(f"{num1} < {num2} : {num1 < num2}")

 # Output Explanation: 

'''
if the first number entered is lower to the second number entered, and the comparison operator between them is 
less than, then the output will always be True.

'''
# Use cases examples:
 
# 5 bag of rice is less than 6 bag of rice (True)
# 2 table is less than 3 table (True)
# 3 house is less than ten laptop (True)

# code: 
print("\n")
print("Enter Number of house in Area A which must be less than house in Area B")

house_1 = int(input("Enter the number of house in area A: "))
house_2 = int(input("Enter the number of laptop in area B: "))

print(f"{house_1} < {house_2} : {house_1 < house_2}")