# Question 8

# Transport Fare Calculator
''' - Ask for:
    - Distance in km (float)
    - Fare per km (float)
- Calculate and display the total fare with two decimal places using `f"{value:.2f}"`.'''

distance = float(input("Enter the distance covered: "))
fare = float(input("Enter the fare rate: "))
total_fare = distance * fare
print(f"The total fare is {total_fare:.2f}")