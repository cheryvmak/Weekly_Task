

from pathlib import Path
import csv



# def save_participant(csv_file, participant_dict):
#     file = Path(csv_file)

#     with open(csv_file, "a", newline="", encoding="utf-8") as f:
#         writer = csv.writer(f)
#         if file.exists:
#             writer.writerow(participant_dict)
#         else:
#             writer.writerow(["Name", "Age", "Phone", "Track"])
#             writer.writerow(participant_dict) # Write all rows at once
        

# def load_participant(csv_file):
    
#     try:
#         with open(csv_file, "r", encoding="utf-8") as f:
#             reader = csv.reader(f)
#         for row_number, row in enumerate(reader):
#             if row_number == 0:  # Header row
#                 print(f"Headers: {' | '.join(row)}")
#             else:
#                 print(f"Row {row_number}: {' | '.join(row)}")

    
#     except ValueError as e:
#         print(f"ValueError: {e}")
    # Read the CSV file back
    # #try:
    #     with open(csv_file, "r", encoding ="utf-8") as f:
    #         reader = csv.reader(f)

    #     for row_number, row in enumerate(reader):
    #         if row_number == 0:  # Header row             print(f"Headers: {' | '.join(row)}"
    #             print(f"Headers: {' | '.join(row)}")
    #     rows  = []
    #     for row in reader:
    #         rows.append(row)
    #         return rows
    # except FileNotFoundError:
    #     return []    
        
    
#     for row_number, row in enumerate(reader):
#         if row_number == 0:  # Header row
#             print(f"Headers: {' | '.join(row)}")
#             print("-" * 40)
#         else:  # Data rows
#             name, age, phone_number, track = row
#             print(f"{name} ({age} years) - {phone_number}: {track}")











import csv
from pathlib import Path

header = ["Name", "Age", "Phone_number", "Track"]

def save_participant(file_path, participant_dict):
    file = Path(file_path)
    with open(file, "a", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=header)
        
        if not file.exists() or file.stat().st_size == 0:
            writer.writeheader()
        writer.writerow(participant_dict)


def load_participant(file_path):
    file = Path(file_path)
    if not file.exists():
        print("file does not exist")
    else:
        print(f"Loading participants from {file.name}")
        with open(file, mode="r", newline="", encoding="utf-8") as f:
            print(f.read())



# def save_participant(csv_file, participant_dict):
#     file = Path(csv_file)

#     with open(csv_file, "a", newline="", encoding="utf-8") as f:
#         writer = csv.writer(f)
#         if file.exists:
#             writer.writerow(participant_dict)
#         else:
#             writer.writerow(["Name", "Age", "Phone", "Track"])
#             writer.writerow(participant_dict) # Write all rows at once




# def load_participant(csv_file):
#     try:
#         with open(csv_file, "r", encoding="utf-8") as f:
#             reader = csv.reader(f)
#         for row_number, row in enumerate(reader):
#             if row_number == 0:  # Header row
#                 header = row
#                 #print(f"Headers: {' | '.join(row)}")
#             else:
#                 print(dict(zip(header,row)))
#                 # print(f"Row {row_number}: {' | '.join(row)}")
#     except ValueError as error:
#          print(f"ValueError: {error}")