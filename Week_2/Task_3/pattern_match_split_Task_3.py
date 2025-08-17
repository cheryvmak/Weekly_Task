# Task 3

#Q11

# given a three fruits
fruits = ("apple,banana,orange")
#split the string into list
fruit_list = fruits.split(",")
# print output
print(fruit_list)

#Q12

# enter a sentence using input
user = input("Enter a sentence: ")
# split the sentence into each word
each_word = user.split()
#print each word on new line
print("\n".join(each_word))

#Q13

# enter string
a = "he ll o"
# replace space with underscore
print(a.replace(" ", "_"))


#Q14
# enter a variable fruit
fruit = "Banana"
# count number of times "a" appear in the variable
a = fruit.count("a")
# formatting and final output
print(f"The letter appears: {a} times.")

#Q15

# enter a string
address = "https://www.goal.com"
#checkif the string starts with "https://"
print(address.startswith("https://"))
