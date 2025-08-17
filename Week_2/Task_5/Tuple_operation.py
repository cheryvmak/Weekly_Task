
#  Task 3

# enter 5 nigerian state 
state_1 =  input("Enter state 1: ")
state_2 =  input("Enter state 2: ")
state_3 =  input("Enter state 3: ")
state_4 =  input("Enter state 4: ")
state_5 =  input("Enter state 5: ")

# create empty list
nigerian_state =  []

# attached the entered nigerian state to the empty list
print(nigerian_state.append(state_1))
print(nigerian_state.append(state_2))
print(nigerian_state.append(state_3))
print(nigerian_state.append(state_4))
print(nigerian_state.append(state_5))

# print the list
print(f"This is the list of nigerian state provided : {nigerian_state}")

# formatting
print("\n")

# convert the list to tuple
nigerian_state = tuple(nigerian_state)

# print the tuple
print(f"user provided nigerian state in tuple: {nigerian_state}")

# formatting
print("\n")

# print the first and last state
print(f"This is the first and last state:", (nigerian_state[0:5:4]))

# formatting
print("\n")

# check if "Lagos" is in the  tuple
print(f"This show if lagos is in tuple:", "Lagos" in nigerian_state)

# formatting
print("\n")

# print number of state entered
print(f"This the number of state entered:", (len(nigerian_state)))
