# enter a variable fruit
fruit = "Banana"

# using control structure to count number of times "a" appear in the variable
word_count = 0
for a in fruit:
    if a == 'a':
        word_count += 1

# formatting and final output
print(f"The letter 'a' appear: {word_count} times.")