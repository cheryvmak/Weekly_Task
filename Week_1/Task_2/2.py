print("Fare Calculator")

# Get distance (km) with validation
while True:
        distance_km = float(input("Enter distance in km: "))
        if distance_km < 0:
            print("Distance cannot be negative. Try again.")
            continue
        break
        print("Please enter a valid number (e.g., 12.5).")

# Get fare per km with validation
while True:
        fare_per_km = float(input("Enter fare per km: "))
        if fare_per_km < 0:
            print("Fare per km cannot be negative. Try again.")
            continue
        break
print("Please enter a valid number (e.g., 150.0).")

# to calculate total fare
total_fare = distance_km * fare_per_km

# formatting with two decimal places using f-strings
print("\nFare Summary")
print(f"Distance:\t{distance_km:.2f} km")
print(f"Fare/km:\t{fare_per_km:.2f}")
print(f"Total Fare:\t{total_fare:.2f}")
