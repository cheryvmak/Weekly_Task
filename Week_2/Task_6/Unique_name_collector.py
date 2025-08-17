
# Task 2
#Enter names of people attending seperated by space
sem_attendee = input("Enter names of seminar attendee seperated by space: ").title().split()

# convert to set
attendance_list = set(sem_attendee)

# formatting 
print("--" * 20)
print("\tSeminar Attendance list")
print("--" * 20)

# print set output
print(attendance_list)

# formating
print("\n")
print("--" * 30)
print("\tSorted Seminar Attendance list")
print("--" * 30)

# print the final output after the sorted attendance list
print("\n".join(sorted(attendance_list)))
