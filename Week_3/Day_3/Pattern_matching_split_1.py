# Enter a web address
web_address = input("Enter a web address: ")

#using control structure to verify if the web address start with a string or not
if web_address.startswith("https://"):
    print("\nYes, It starts with  'https://'")
else:
    print("\nNo, It did not")