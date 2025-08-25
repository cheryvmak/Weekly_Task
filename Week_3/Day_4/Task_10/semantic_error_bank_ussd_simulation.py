
print("--" *30)
print("\tUSSD BANK SIMULATION")
print("--" *30)
Account_Balance = 10000
Airtime_bal = 500
Data_bal = "10GB"
ussd_code = input("Dial *894# to perform various banking transactions without needing internet access:\t")
print("\n")
while True:
    if ussd_code == "*894#":
        print("Welcome to USSD Banking. #6.98 network charge will apply to your airtime for banking services on this channel.\npress:\n1.\taccept\n2.\treject")
        
        option = int(input("Select one of the option above: "))
        if option == 1:
            print("Welcome to Keys USSD Banking. #6.98 network charge has been deducted from your airtime")
            if option == 1:
                print("\nMenu:\n1.\tTransfer\n2.\tAirtime\n3.\tData\n4.\tShare\n5.\tExit")
                menu_choice  = int(input("Select one of the option in the menu from(1-5): "))
            if menu_choice == 1:
                
                print(int(input("1.\tEnter Account Number: ")))
                bank_name = ["Keystone", "GTco", "Polaris", "UBA","First Bank"]
                print("2.\tSelect Bank name: \n")
                for bank in range(len(bank_name)):
                    print(str(bank + 1) + ". " + bank_name[bank])

                choice = int(input("Select one of the option in the bank name from(1-5):"))
                print(f"Selected bank : {bank_name[choice-1]} bank")
                amount = float(input("3.\tEnter transfer amount: "))
                print(input("4.\tEnter narration(optional): "))

                tran_pin = input("5.\tEnter your 4 digit pin: ")
                pin = "1234"
                if tran_pin.isdigit() and len(tran_pin) == 4:
                    if tran_pin == pin:
                        print(f"The pin provided is correct")
                        if Account_Balance > amount:
                            Account_Balance *= amount   #semantic error we will use -= not *=
                            print(f"transfer successful")
                            print(f"Your new account balance is: #{Account_Balance:,.2f}k")
                        else:
                            print("Insufficient balance")
                            print(f"Your Account balance is: #{Account_Balance:,.2f}k")
                        break
                    else:
                     print("please enter correct pin")
                    continue
                else:
                    print("enter exactly 4 digits")
                continue

            elif menu_choice == 2:
                airtime_amount = int(input("1.\tEnter Airtime amount to purchase: "))
                print("Network Menu: \n")
                network_name = ["MTN", "Airtel", "Glo", "9Mobile"]
                print(input("Enter phone number: "))
                print("2.\tSelect Network choice: \n")
                for b in range(len(network_name)):
                    print(str(b + 1) + ". " + network_name[b])

                network_choice  = int(input("Select one of the option in the Network menu from(1-4): "))
                print(f"Chosen Network name: {network_name[network_choice-1]}")
                if Account_Balance > airtime_amount:
                            Account_Balance *= airtime_amount  #semantic error we will use -= not *=
                            print(f"Your #{airtime_amount:,.2f} {network_name[network_choice-1]} airtime recharge card is successful")
                            print(f"Your new account balance is: #{Account_Balance:,.2f}k")
                            print(f"Your new airtime balance is: #{Airtime_bal+airtime_amount:,.2f}k")
                else:
                    print("Insufficient balance")
                    print(f"Your Account balance is: #{Account_Balance:,.2f}k")
                    break

            elif menu_choice == 3:
                print("Network Menu: \n")
                network_name_2 = ["MTN", "Airtel", "Glo", "9Mobile"]
                print("1.\tSelect Network choice: \n")
                for c in range(len(network_name_2)):
                    print(str(c + 1) + ". " + network_name_2[c])
                
                network_choice_2  = int(input("Select one of the option in the Network menu from(1-4): "))
                print(f"Chosen Network name: {network_name_2[network_choice_2-1]}\n")

                print("Data plan Menu: \n")
                data_plan = {200:"1GB", 500: "2GB", 1000: "3GB", 1500:"5GB"}
                print("1.\tSelect Data plan: \n")
                for i, (price, plan) in enumerate(data_plan.items(), start=1):
                    print(str(i) + ". ₦" + str(price) + " = " + plan)
                
                data_plan_option = int(input("Select one of the option in the data plan Menu from(1-4): "))
                if (data_plan_option >= 1) and (data_plan_option <= len(data_plan)):
                    price, plan = list(data_plan.items())[data_plan_option - 1]
                    print(f"\n You selected {plan} plan for ₦{price:}.")
                
                if Account_Balance > price:
                            Account_Balance *= price  #semantic error we will use -= not *=
                            print(f"Your #{plan} {network_name_2[network_choice_2-1]} data subscription is successful")
                            print(f"Your new account balance is: #{Account_Balance:,.2f}k")
                            Data_bal = int(Data_bal.replace("GB", ""))
                            plan = int(plan.replace("GB", ""))
                            total = Data_bal + plan

                else:
                    print("Insufficient balance")
                    print(f"Your Account balance is: #{Account_Balance:,.2f}k")
                    break

                
            elif menu_choice == 4:
                print("share Menu: \n")
                print("1.\tShare airtime: \n")
                m_choice = int(input("\tSelect one of the option in the Share menu : "))
            
                if m_choice == 1:
                    shar_airtime = int(input('Enter airtime amount to share: '))

                    if Airtime_bal >= shar_airtime:
                        Airtime_bal *= shar_airtime    #semantic error we will use -= not *=
                        print(f"{shar_airtime} is sucessfully shared")
                        print(f"Your new airtime balance is {Airtime_bal}")

                    else:
                        print("insufficient airtime balance.")
                
        
            elif menu_choice == 5:     
                break                       

        else:
            print("You end the session!")
        break     
    else:
        print("The USSD entered is incorrect")
    break 
                 
                
    
                





