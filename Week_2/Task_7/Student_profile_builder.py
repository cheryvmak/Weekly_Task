
# Compulsory Task

# Collect Basic Info
name = input('Enter student\'s full name: ')
age = int(input('Enter student\'s age: '))
gender = input('Enter student\'s gender(M or F): ')

#Collect scores for subjects
subjects = ('Eng', 'Yor', 'Math', 'Agric', 'chem')
scores = tuple(float(input(f'Enter score for {subject}: ')) for subject in subjects)

# collect guardian info
guardian_name = input('Enter guardian name: ')
guardian_phone_no = input('Enter guardian phone number: ')

# collect hobbies details
hobbies = input('Enter hobbies seperated by comma: ').split(",")
hobbies_set = set(hobby.strip() for hobby in hobbies)

# create a dictionary for the student profile
student_profile = {

    'Basic Info': {'Name': name.title(), 'Age': age,  'Gender': gender}, 
    'Performance': {subject: score for subject, score in zip(subjects, scores)}, 
    'Guardian info': {'guardian name': guardian_name.title(), 'guardian phone number': guardian_phone_no}, 
    'Hobbies': list(hobbies)}

# create a formatting for the title of each category
title = 'Student Profile'
title2 = 'Student\'s Performance'
title3 = 'Guardian Information'
title4 = 'Hobbies'

# formatting 
print('\n')
print(f'{title:^50}')

# using foramtting to derived data for basic info 
print(f"Name: {student_profile['Basic Info']['Name']:>44}")
print(f"Age: {student_profile['Basic Info']['Age']:>45}")
print(f"Gender: {student_profile['Basic Info']['Gender']:>42}")

# formatting
print('\n')
print(f'{title2:^50}')

# using foramtting to derived data for student performance
print(student_profile["Performance"])

# formatting
print('\n')
print(f'{title3:^50}')

# using foramtting to derived data for guardian info 
print(student_profile["Guardian info"])

# formatting
print('\n')
print(f'{title4:^50}')

# using foramtting to derived data for hobbies details
print(student_profile["Hobbies"])

# u# using foramtting to derived data for average performance 
student_profile["Performance"]["Average"] = sum(scores) / len(scores)

# using foramtting to derived data for basic info initials 
student_profile["Basic Info"]["Initials"] = "".join([n[0] for n in name.split()])

# using foramtting derived data for hobbies count
student_profile["Hobbies Count"] = len(hobbies_set)

# using foramtting to print final output
print(f"\nTotal Hobbies:\t{student_profile['Hobbies Count']}")
print(f"Average Score:\t{student_profile['Performance']['Average']:.2f}")