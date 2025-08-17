# Question 5

# Daily Market Report Ask the user to input:
'''- Market name
 - Number of traders
 - Daily revenue in naira
- Display the result using f-string formatting with commas for 
thousands separator.'''

mkt_name = input("Enter Market name: ")
No_of_traders = int(input("Enter number of traders: "))
daily_rev = float(input("Enter daily revenue in naira: "))
print(f"The market name is {mkt_name} market, The number of traders are {No_of_traders:,} traders, and the daily revenue generated is #{daily_rev:,}")

