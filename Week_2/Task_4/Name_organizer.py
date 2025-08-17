
# Task 4

# enter 5 names (separated by spaces) and convert all names to lowercase
names = input("Enter 5 names separated by spaces: ").lower()

all_names = names.split()
# Sort the list alphabetically
all_names.sort()
# print all the name
print(f"The sorted list of all names:", all_names)
# display one name per line using for, in, len
for name in range(len(all_names)):
    print(f"each name per line:", all_names[name])