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
other_scholarship = input("Are you on scholarship in the oil and gas industry whether national or international( Yes or No): ").capitalize()
academic_qualific = input("Enter five subject including English and Mathematics: ").split()

subject_1 = input(f"Enter your grade for {academic_qualific[0]}  : ").upper()
subject_2 = input(f"Enter your grade for {academic_qualific[1]}  : ").upper()
subject_3 = input(f"Enter your grade for {academic_qualific[2]}  : ").upper()
subject_4 = input(f"Enter your grade for {academic_qualific[-2]} : ").upper()
subject_5 = input(f"Enter your grade for {academic_qualific[-1]} : ").upper()

verify_subj = {academic_qualific[0] : subject_1, academic_qualific[1] : subject_2, academic_qualific[2] : subject_3, academic_qualific[-2] : subject_4, academic_qualific[-1] : subject_5 }

grade = (((subject_1 == 'A') or (subject_1 == 'B')) and ((subject_2 == 'A') or (subject_2 == 'B')) and ((subject_3 == 'A') or (subject_3 == 'B')) and ((subject_4 == 'A') or (subject_4 == 'B')) and ((subject_5 == 'A') or (subject_5 == 'B')))
print(grade)

eligibility = (age < 18) and (score > 70) and (citizenship == "Yes") and (Enrollment == "Yes") and (other_scholarship == "No") and (grade == True)      
print(f"Candidate: {name}\nAge: {age}\nScore: {score}\nCitizenship: {citizenship}\nEnrollment: {Enrollment}\nOther_scholarship: {other_scholarship}\nAcademic_qualific: {academic_qualific}\nEligible: {eligibility}")
