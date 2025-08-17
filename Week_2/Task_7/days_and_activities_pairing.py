# Task 3

# Store days of the week in a tuple
days_of_the_week = ("Sunday", "Monday","Tuesday", "Wednesday","Thursday", "Friday", "Saturday")

# user entering both days and activities for three days
day_1 = input("Enter day one: ")
activity_1 = input("Enter activity for day one: ")

day_2 = input("Enter day two: ")
activity_2 = input("Enter activity for day two: ")

day_3 = input("Enter day three: ")
activity_3 = input("Enter activity for day three: ")

# both days and activities in one list respectively
days = [day_1, day_2, day_3]
act_for_days = [activity_1, activity_2, activity_3]

# use dictionary comprehension to pair days and activities
days_and_activ_dict = {day : activity for day, activity in zip(days, act_for_days) if day in days_of_the_week}

# print the output
print(days_and_activ_dict)