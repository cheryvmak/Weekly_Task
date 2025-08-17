
# Task 6

# user enter a word
end_user =  input("Enter a word: ")

# print the length of the word.
print(len(end_user))

# Check if it is all uppercase.
in_upper_case  =  end_user.isupper()

# print the output
print(f"The word entered is in upper_case: {in_upper_case}")

# Check if it is all lowercase.
in_lower_case  =  end_user.islower()

# print the output
print(f"The word entered is in lower_case: {in_lower_case}")

# Check if it is all title case.
in_title_case  =  end_user.istitle()

#print  the output
print(f"The word entered is in title_case: {in_title_case}")

# Reverse the word using slicing
print(f"This is the reverse word:", end_user[::-1])