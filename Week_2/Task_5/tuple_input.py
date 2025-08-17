
# Task 2

# enter 5 best friends’ names
best_friend_1 =  input("Enter best friend's name 1: ")
best_friend_2 =  input("Enter best friend's name 2: ")
best_friend_3 =  input("Enter best friend's name 3: ")
best_friend_4 =  input("Enter best friend's name 4: ")
best_friend_5 =  input("Enter best friend's name 5: ")

# create empty list
best_friend_name =  []

# attached the entered dishes to the empty list
print(best_friend_name.append(best_friend_1))
print(best_friend_name.append(best_friend_2))
print(best_friend_name.append(best_friend_3))
print(best_friend_name.append(best_friend_4))
print(best_friend_name.append(best_friend_5))

# print the list
print(f"This is the best friend list: {best_friend_name}")

# formatting
print("\n")

# convert the list to tuple
best_friend_name = tuple(best_friend_name)

# print the tuple
print(f"This is the best friend tuple: {best_friend_name}")

# formatting
print("\n")

# print the tuple in reverse order
Reversed_name = best_friend_name[::-1]
print(f" This is the best friend tuple in reversed order: {Reversed_name}")