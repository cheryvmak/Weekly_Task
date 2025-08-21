
# user enter a word
end_user = input("Enter a word: ").strip()

# Print the length of the word
print(f"\nLength of the word: {len(end_user)}")

# Check cases of the word
if end_user.isupper():
    print("The word is in uppercase.")
elif end_user.islower():
    print("The word is in lowercase.")
elif end_user.istitle():
    print("The word is in title case.")
else:
    print("The word contains combination of the three(i.e uppercase, lowercase, title case) characters.")

print("\n")

# Using slicing
reversed_word = end_user[::-1]

print(f"\n The Reversed word of the text entered '{end_user}' is\t :\t", reversed_word)


# create empty string
# reversed_word = ""

# for char in end_user:
#     print(char)
#     reversed_word = char + reversed_word #  adding each character to the front of the loop to the empty string which will reverse it

# print(f"\n The Reversed word of the text '{end_user}' entered is :", reversed_word)
