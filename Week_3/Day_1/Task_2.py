# Task 2

name = input("Enter your name: ")
age = int(input("Enter your age: "))
score = int(input("Enter your test score: "))

eligibility = (age < 18) and (score > 70)
print(f"Candidate: {name}\nAge: {age}\nScore: {score}\nEligible: {eligibility}")


'''
In the first line of code the user enter the name, age, score,where
age and score should be an integer data type.

In the next paragraph, the line code shows that the age of the 
candidate should be less than 10 years old and the candidate
score should be more than 70 marks, both condition should be satisfy
before considered for eligibility. 

The information is stored in a variable name eligibility

'''

name = input("Enter your name: ")
age = int(input("Enter your age: "))
score = int(input("Enter your test score: "))
citizenship = input("Are you a citizen of Nigeria(Yes or No):").capitalize()
Enrollment = input("Are you a registered, full-time undergraduate student(Yes or No: ").capitalize()
other_scholarship = input("on scholarship in the oil and gas industry whether national or international( Yes or No): ").capitalize()
academic_qualific = input("Do you have five distinctions (As and Bs) in relevant subjects in your WAEC/WASSCE (May/June) exams, including English and Mathematics(Yes or No): ").title()

eligibility = (age < 18) and (score > 70) and (citizenship == "Yes") and (Enrollment == "Yes") and (other_scholarship == "Yes") and (academic_qualific == "Yes")      
print(f"Candidate: {name}\nAge: {age}\nScore: {score}\nCitizenship: {citizenship}\nEnrollment: {Enrollment}\nOther_scholarship: {other_scholarship}\nAcademic_qualific: {academic_qualific}\nEligible: {eligibility}")
