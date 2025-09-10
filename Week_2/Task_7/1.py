# Initialize empty dictionary for student bio-data
student = {}

# Collect bio-data
student['name'] = input("Enter student name: ").strip()
student['age'] = input("Enter student age: ").strip()
student['gender'] = input("Enter student gender: ").strip()

# Collect courses as a list
courses = []
print("Enter courses (type 'done' to finish):")
while True:
    course = input(f"Enter course #{len(courses) + 1} (or 'done'): ").strip()
    if course.lower() == 'done':
        break
    if course:  # Check for non-empty input
        courses.append(course)
student['courses'] = courses

# Display bio-data with escape sequences
print("\nStudent Bio-Data:")
print("-----------------")
print(f"\tName:\t{student['name']}")
print(f"\tAge:\t{student['age']}")
print(f"\tGender:\t{student['gender']}")
print("\tCourses:")
for course in student['courses']:
    print(f"\t\t- {course}")
if not student['courses']:
    print("\t\tNo courses registered.")