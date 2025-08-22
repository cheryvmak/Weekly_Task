
print("--" * 15)
print("Best friend's name")
print("--" * 15)

# create empty tuple
best_friends = ()
# enter 5 best friends’ names using control flow
for friend in range(5):   
    friends = input(f"Enter friend {friend+1}'s name: ")
    best_friends += (friends,)

# Print tuple in reverse order
print("\nYour friends in reverse order:")
print("--" * 20)
reversed_name = best_friends[::-1]
print(reversed_name)
print("--" * 20)