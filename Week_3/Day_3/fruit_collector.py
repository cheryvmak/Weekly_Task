




#Simulated USSD Menu Interaction
print('Welcome, I hope your day is going fine ')
print('Dial *555# ')

#Continue running code until condition is met
while True:
    print('1. Check Balance\n2. Buy Airtime \n3. Buy Data \n4. Share Data/ Airtime \n5. Exit')
    balance_airtime = 1000
    balance_data = '5 GB'
    balance_data_val = float(balance_data.split(' ')[0])
    choice = int(input('Choose one of the options above(1-5): '))
    if choice == 1:
        print('1. Airtime balance ')
        print('2. Data balance ')
        choice_bal = int(input('Choose one of the options above(1-2): '))
        if choice_bal == 1:
            print(f'Your airtime balance is ₦{balance_airtime}')
        elif choice_bal == 2:
            print(f'Your data balance is {balance_data}')
        else:
            print('Your choice isn\'t among the available options')
    elif choice == 2:
        choice_buy_airtime  = float(input('How much airtime do you want to buy: '))
        if balance_airtime >= choice_buy_airtime:
            balance_airtime += choice_buy_airtime
            print(f'You have successfully purchased {choice_buy_airtime}')
            print(f'Your new airtime balance is {balance_airtime}')
        else:
            print(f'Your balance is not enough for this purchase. Please recharge.')
    elif choice == 3:
        print('Choose from the options below: ')
        print('1. ₦200 - 1GB')
        print('2. #500 - 2GB')
        print('3. #1000 - 5GB')
        choice_buy_data  = float(input('How much airtime do you want to buy: '))
        if balance_airtime >= choice_buy_data:
            balance_airtime -= choice_buy_data
            if choice_buy_data == 200:
                balance_data_val += 1
                balance_data = f'{balance_data_val} GB'
                print('You have successfully purchased 1 GB')
                print(f'Your data balance is {balance_data_val} GB')
            elif choice_buy_data == 500:
                balance_data_val += 2
                balance_data = f'{balance_data_val} GB'
                print('You have successfully purchased 2 GB')
                print(f'Your data balance is {balance_data_val} GB')
            elif choice_buy_data == 1000:
                balance_data_val += 5
                balance_data = f'{balance_data_val} GB'
                print('You have successfully purchased 5 GB')
                print(f'Your data balance is {balance_data_val} GB')
            else:
                print('Your choice isn\'t here, try our other code meant for rich people.')
        else:
            print(f'Your balance is not enough for this purchase. Please recharge.')

    elif choice == 4:
        print('Choose from the options below: ')
        print('1. Share Airtime')
        print('2. Share Data')
        choice2  = float(input('Choose suitable options from options above: '))

        if choice2 == 1:
            airtime_share = float(input('Enter airtime amount you want to share: '))
            if airtime_share <= balance_airtime:
                balance_airtime -= airtime_share
                print(f'You have sucessfully shared {airtime_share}')
                print(f'Your new airtime balance is {balance_airtime}')
            else:
                print('You do not have sufficient airtime to share.')
        elif choice2 == 2:
            data_share = int(input('Enter data in GB you want to share: '))
            if data_share <= balance_data_val:
                balance_data_val -= data_share
                print(f'You have sucessfully shared {data_share} GB')
                print(f'Your new data balance is {balance_data_val} GB')
            else:
                print('You do not have sufficient data to share.')
    elif choice == 5:
        break


           
            