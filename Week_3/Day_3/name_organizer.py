# enter 5 names (separated by spaces) and convert all names to lowercase
names = input("Enter 5 names separated by spaces: ").strip().lower()

# Split name into a list 
names = [name for name in names.split()]
print(names)

# using len to check if the name entered is 5 names
if len(names) != 5:
    print("Please enter five names!")
else:
    # Sort the list alphabetically
    names.sort()
    
    # formatting and printing each name per line
    print("\nSorted Names:")
    print("-------------")
    for i in range(len(names)):
        print(names[i])