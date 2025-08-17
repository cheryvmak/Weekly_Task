
# Task  4

# create a Voter names
voter_names = input("Enter voter's name seperated by spaces: ").split()

# store the names in a set 
updated_voter_names = set(voter_names)

# print the set output
print(updated_voter_names)

# formatting
print("\n")

# check a voter name
voter = input("Enter your name: ")

# formatting
print("\n") 

#  if voter register twice display a warning!!!
if voter in updated_voter_names:
    print("voter name already registered!!!")

#  formatting    
print("\n")  

# if the voter has not register before use add method in tuple to add the voter
updated_voter_names.add(voter)

# print the set output
print(updated_voter_names)

# check total number of unique voter
unique_voter = len(updated_voter_names)

# formatting and printing final output
print("\n")
print(f"The total number of unique voters is:\t{unique_voter}")

