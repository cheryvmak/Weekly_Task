# enter 5 names (separated by spaces) and convert all names to lowercase
names = input("Enter 5 names separated by spaces: ").strip().lower()

# Split name into a list 
names = [name for name in names.split()]
# print the output
print(names)

# using control structure to check if the name entered is 5 names
if len(names) != 5:
    print("enter five names!")
else:
    # Sort the list alphabetically
    names.sort()
    
    # formatting and printing each name per line
    print("\nSorted Names:")
    print("-------------")
    for name in range(len(names)):
        print(names[name])