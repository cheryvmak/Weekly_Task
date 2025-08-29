

import csv
from pathlib import Path
from participant_pkg.file_op import save_participant,load_participant

workspace = Path("participant_pkg")
csv_file = workspace / "contacts.csv"


# Create participant data

while True:
    participant_dict = {}

    name = input("Enter your name:").title().strip()
    if name == "":
        print("Name must not be empty, please enter your name: ")
    else:
        break

while True:
    try:
        age =  int(input("Enter your age: "))
    except ValueError:
        print("\nYour Age should be an integer\n")
        continue
    phone_number = input("Enter your phone number: ")
    if len(phone_number) != 11:
        print("The phone number must be 11 digit")
        
    elif not phone_number.isdigit():
        print("The phone number entered must be digit")
        
    else:
        break
        print("Enter correct and valid phone number")
       
        
while True:
    track = input("Enter your track: ")
    if track == "":
        print("Track must not be empty, please enter your track: ")
    else:
        break
print(f"Name: \t{name}\nAge:\t{age}\nPhone Number: \t{phone_number}\nTrack: \t{track}")

participant_dict["Name"] = name
participant_dict["Age"] = age
participant_dict["Phone_number"] = phone_number
participant_dict["Track"] = track
print(participant_dict)



print("Participant data written to CSV file!")



print("Student data written to CSV file!")

save_participant(csv_file, participant_dict)

print("\nReading CSV file:")

load_participant(csv_file)
print(f"The total participant is:{len(participant_dict)}")


# file_ops.save_participants(csv_file, participant_dict)

# print("\nReading CSV file:")

# file_ops.load_participant(csv_file)



   