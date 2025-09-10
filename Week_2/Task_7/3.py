# Store days of the week in a tuple
days = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')

# Initialize lists to store selected days and their activities
selected_days = []
activities = []

# Collect activities for three specific days
print("Enter activities for three days of the week:")
for i in range(3):
    while True:
        day = input(f"Enter day #{i+1} (choose from {days}): ").capitalize().strip()
        if day in days:  # Validate day
            if day not in selected_days:  # Check for duplicates
                selected_days.append(day)
                activity = input(f"Enter activity for {day}: ").strip()
                if activity:  # Ensure non-empty activity
                    activities.append(activity)
                    break
                else:
                    print("Please enter a valid activity!")
            else:
                print("Day already selected! Choose a different day.")
        else:
            print(f"Invalid day! Please choose from {days}.")

# Create dictionary using dictionary comprehension with zip()
schedule = {day: activity for day, activity in zip(selected_days, activities)}

# Print the dictionary
print("\nWeekly Schedule:")
print("----------------")
for day, activity in schedule.items():
    print(f"\t{day}:\t{activity}")