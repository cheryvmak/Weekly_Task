
print("--"* 15)
print("Nigerian States")
print("--"* 15)

# enter 5 nigerian state using for loop
states = ()
for state in range(5):
user = input(f"Enter state {state+1}: ") # indentation error, user should be tab spaced
    states += (user,)  # indentation error, states += (user,) should be tab spaced

# Print first and last state
print("\nFirst state entered:", states[0])
print("Last state entered:", states[-1])

# Check if Lagos is in the tuple
if "Lagos" in states:    # control flow with if
print("Yes, Lagos is in the list.")
else:
    print("No, Lagos is not in the list.")

# Print number of states entered
print("The total number of states entered:", len(states))