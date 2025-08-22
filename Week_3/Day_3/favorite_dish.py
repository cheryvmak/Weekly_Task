
print("--" * 15)
print("Favorite Nigerian Dishes")
print("--" * 15)

# enter three favorite Nigerian dishes (one at a time) using for loop
fav_dishes = ()
for dish in range(3):   # control flow with loop
    dishes = input(f"Enter favorite dish {dish+1}: ")
    fav_dishes += (dishes,)

# Print tuple in one line separated by commas
print("\nYour favorite dishes (one line):")
print(", ".join(fav_dishes))

# Print each dish on a new line using \n
print("\nYour favorite dishes (each on new line):")
print("\n".join(fav_dishes))



