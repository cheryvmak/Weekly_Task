# enter a string
string = input("Enter a string: ")

# reverse a string without using ([::-1])
# create empty string
reversed_string = ""

# Using control structure to reverse the text
for char in string:
   reversed_string = char + reversed_string #  adding each character of the loop to the the empty string which will reverse it

# formatting and printing the result
print(f"\n The Reversed string of the text '{string}' entered is :", reversed_string)