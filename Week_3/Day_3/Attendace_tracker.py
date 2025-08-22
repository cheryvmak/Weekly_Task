
# Stores day of week in a tuple
days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")

# Stores month of the year in a tuple
months = ("January", "February", "March", "April", "May", "June",
          "July", "August", "September", "October", "November", "December")

# Enter user info
student_name = input("Enter Student's Name: ")
gender = input("Enter Gender: ")
course_track = input("Enter Course Track: ")

# Current month number (1-12)
month_num = int(input("Enter Current Month Number (1-12): "))
if (month_num >= 1) and (month_num <= 12) : 
    current_month = months[month_num - 1] 
else:
    current_month = "Invalid month number"

# Current day number (1-7)
day_num = int(input("Enter Current Day Number (1-7): "))
if (day_num >= 1 and day_num <= 7):
    current_day = days[day_num - 1] 
else:
    current_day = "Invalid day number"

# Display collected information
print("\nStudent Information")
print("Name:", student_name)
print("Gender:", gender)
print("Course Track:", course_track)
print("Current Month:", current_month)
print("Current Day:", current_day)
