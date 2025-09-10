
# Task 5


# Enter 3 student names
student_name_1 = input("Enter the name of the first student: ")
student_name_2 = input("Enter the name of the second student: ")
student_name_3 = input("Enter the name of the third student: ")

# Enter 3 student scores
student_score_1 = input(f"Enter {student_name_1} score: ")
student_score_2 = input(f"Enter {student_name_2} score: ")
student_score_3 = input(f"Enter {student_name_3} score: ")

# create empty list for both student name and student  score


# attached the entered student name to the empty list student name
student_name.append(student_name_1)
student_name.append(student_name_2)
student_name.append(student_name_3)

# attached the entered student score to the empty list student score
student_score.append(student_score_1)
student_score.append(student_score_2)
student_score.append(student_score_3)

# print a formatted output showing Name — Score, aligned neatly
print("\n")
print("--" *20)
print("This is the student name and their scores")
print("--" *20)
print(f"{student_name[0]} \t—\t{student_score[0]}")
print(f"{student_name[1]} \t—\t{student_score[1]}")
print(f"{student_name[2]} \t—\t{student_score[2]}")