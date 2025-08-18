# Task 4

# create empty dictionary called student
student = {}

# user input name and age
name = input("Enter your name: ")
age = int(input("Enter your age: "))

# store both name and age variable into the dictionary
student["name"] = name
student["age"] = age

# create score list
scores = [70, 85, 90]
# add score list to the empty dictionary using update method
student.update({"Scores": scores})
# print the student dictionary
print(student)

# create the total score of the student
total_score = 0  # assigning zero to start

total_score +=  scores[0] # using assignment operator to add the first score
total_score +=  scores[1] # using assignment operator to add the second score
total_score +=  scores[2] # using assignment operator to add the third score
# print the total score calculated
print(total_score)

# create the average score
average_score = total_score/len(scores)

# comparison operator to check conditional statement
passed = average_score >= 50
# logical operator to check conditional statement
teenager = (age >= 13) and (age <= 19)

# add passed and teenager variable to the student dictionary using update method
student.update({"passed" : passed})
student.update({"Teenager" : teenager})

# print the complete record
print("Student Record:\nName:", name)
print("Age:", age)
print("Scores:", scores)
print("Passed:", passed)
print("Teenager:", teenager)
