
# create empty set
fav_fruits = set()

# User enter five favorite fruits
print("Enter your 5 favorite fruits:")

while len(fav_fruits) < 5:
    print("\n")
    fruit = input(f"Enter favorite fruit {len(fav_fruits) + 1}: ")
    if fruit.strip(): 
        fav_fruits.add(fruit.strip())
        print(f"attached {fruit.strip()} to your favorites!")
    else:
        print("No input")

# Display the set of fruits
print("\nYour favorite fruits are:", fav_fruits)