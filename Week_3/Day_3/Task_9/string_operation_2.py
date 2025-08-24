# Get sentence from user
clients = input("Enter a sentence: ")

# enter each vowel as variable and count
#vowels = ("aeiou")
# Count vowels
vowels = "aeiou"
count = 0
for char in clients.lower():
    if char in vowels:
        count += 1

# Print the result
print(f"The number of vowel in it:", counts)
