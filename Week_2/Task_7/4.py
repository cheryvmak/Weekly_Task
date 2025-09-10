# Get input from user
names_input = input("Enter three names separated by commas (e.g., John, Jane, Bob): ")

# Split input by commas and convert to set to remove duplicates
names_set = set(name.strip() for name in names_input.split(","))

# Create dictionary using dictionary comprehension
name_lengths = {name: len(name) for name in names_set}

# Display the dictionary
print("\nName Lengths:")
print("-------------")
for name, length in name_lengths.items():
    print(f"\t{name}:\t{length}")