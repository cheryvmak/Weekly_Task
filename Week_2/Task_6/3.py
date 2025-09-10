# Initialize empty set for names
attendees = set()

while True:
    # Get name input
    name = input("Enter attendee name (or 'done' to finish): ")
    
    # Exit condition
    if name.lower() == 'done':
        break
    
    # Add name to set (duplicates automatically ignored)
    if name.strip():  # Check for non-empty input
        attendees.add(name.strip())
    else:
        print("Please enter a valid name!")

# Display names in alphabetical order
if attendees:
    print("\nSeminar Attendees (in alphabetical order):")
    for name in sorted(attendees):
        print(name)
else:
    print("\nNo attendees registered.")