# create empty list
nigeria_festival_info = []

# create a list that contains Festival name,Location,Month held
festival_info = ["Festival Name", "Location", "Month Held"]

# create a for loop to iterate through the festival_info
for info in festival_info:
    response = input(f"Enter {info}: ")
    nigeria_festival_info.append(response)


# # Display info with escape sequence for quotes
print("--" * 20)
print("         Festival Details")
print("--" * 20)
print(f"Festival: \"{nigeria_festival_info[3]}\"")
print(f"Location: {nigeria_festival_info[1]}")
print(f"Month Held: {nigeria_festival_info[-1]}")
print("\n")
print(f"The \"{nigeria_festival_info[0]}\"festival is held in {nigeria_festival_info[1]} in the month of {nigeria_festival_info[-1]}")

