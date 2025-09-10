# Initialize set with seat numbers 1 to 50
available_seats = set(range(1, 51))

while len(available_seats) > 0:
    # Show available seats
    print("\nAvailable seats:", sorted(available_seats))
    
    # Get user input
    seat = input("Enter seat number to book (1-50, or 0 to exit): ")
    
    # Check if input is a number
    if seat.isdigit():
        seat = int(seat)
        
        # Exit condition
        if seat == 0:
            print("Exiting booking system.")
            break
            
        # Check if seat is valid and available
        if seat >= 1 and seat <= 50:
            if seat in available_seats:
                available_seats.remove(seat)
                print("Seat", seat, "booked successfully!")
            else:
                print("Seat already booked or invalid!")
        else:
            print("Invalid seat number! Please choose between 1 and 50.")
    else:
        print("Please enter a valid number!")