# Tadk 1

# collecting student bio data
name = input("Enter name: ").title()
age = int(input("Enter age: "))
gender = input("Enter gender(M/F): ").title()
courses = input("Enter courses seperaed by spaces: ").title().split()

# Create empty dictionary name student_bio
student_bio = {}

# using dictionary operations to store data
student_bio["name"] = name
student_bio["age"] = age
student_bio["gender"] = gender
student_bio["courses"] = courses


print("--" * 10)
print("Student bio data")
print("--" * 10)

# formatting and printing the output
print(f"Name\t: \t {student_bio["name"]} \nAge\t: \t {student_bio["age"]} \nGender\t: \t {student_bio["gender"]} \nCourse\t: \t {student_bio["courses"]}")
print("--" * 10)