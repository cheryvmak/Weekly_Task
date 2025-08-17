# Question 11

# Nigerian Currency Converter (Very Advanced)
'''Ask for:
    - Amount in Naira (float)
    - Exchange rate to US Dollars (float)
    - Exchange rate to British Pounds (float)

- Convert and print results with thousands separators and currency symbols, neatly aligned in a table-like format using escape sequences.'''


amount = float(input("Enter the Amount in Naira: "))
exch_rate_usd = float(input("Enter the Exchange rate to US Dollars: "))
exch_rate_pounds = float(input("Enter the Exchange rate to British Pounds: "))
Convert_usd = amount/exch_rate_usd
Convert_pounds = amount/exch_rate_pounds
print("\nNigerian Currency Converter")
print("........................................")
print(f"Currency:\t\t\tAmount\nNaira(#):\t\t\t{amount:,.2f}\nDollar($):\t\t\t{Convert_usd:,.2f}\nPounds(£):\t\t\t{Convert_pounds:,.2f}")
