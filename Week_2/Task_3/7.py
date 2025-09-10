# 4. Count the number of characters in a string without using len()
string_input = input("Enter a string to count characters: ")
count = 0
for char in string_input:   # control flow using for loop
    count += 1
print("Number of characters:", count)