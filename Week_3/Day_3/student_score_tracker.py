
student_name =  []
student_score = []

# Enter 3 student names and scores
for i in range(3):
    name = input(f"Enter the name of student_{i+1}: ").strip()
    while True:
        score = input(f"Enter the score for {name}: ").strip()
        if score.replace('.', '', 1).isdigit() and int(score) >= 0:  # replace the first decimal with empty string to make it a digit and the score should not be negative
            student_name.append(name)
            student_score.append(int(score))
            break
        else:
            print("Please enter a valid non-ne")

# Print formatted output
print("\nStudent Scores:")
print("--"*20)
print("Name\t|\tScore")
print("--"*20)
for name, score in zip(student_name, student_score):
    print(f"{name:<5}\t|\t{score}")
