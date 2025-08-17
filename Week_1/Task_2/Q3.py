# Question 3

# School Registration Form

"""Ask for student’s name, class, and state of origin. Use string 
concatenation to print them in one sentence.

likely output
Student Ade is in SS2 and is from Ogun State."""

student_name = input("Enter your name: ")
student_class = input("Enter your class:  ")
student_state_origin = input("Enter your State of Origin: ")
#print(f"Student {student_name} is in {student_class} and is from {student_state_origin}.")
print("Student " + student_name + " is in " + student_class + " and is from "  + student_state_origin + " State." )
