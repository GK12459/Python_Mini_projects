def mini_statement():
    if(len(account_statement) == 0):
        print("No previous transactions recorded!")
    else:
        for i in range(len(account_statement), len(account_statement) - 5, -1):
            print(* account_statement[i-1])

def money_withdraw():
    global balance, account_statement
    print("\nNOTE: Withdrawal ammount must in multiples of 100, 200, and 500.")
    withdrawal_money = int(input("Enter money that to be withdrawn: "))
    if(balance >= 100):
        if(withdrawal_money % 100 == 0):
            balance -= withdrawal_money
            print(f"Withdrawal of {withdrawal_money}/- is successful.")
            account_statement.append(["Money withdrawal"," ", withdrawal_money])
        else:
            print("Invalid amount entered!\nKindly read the note.")
    else:
        print("Insufficient balance to initiate withdrawal!\nAccount balance must be above 100/-")

def money_deposit():
    global balance, account_statement
    print("\nNOTE: Deposit money in denominations of 100, 200, and 500.")
    deposit_money = int(input("Enter amount that to be deposited: "))
    if(deposit_money >= 100):
        if(deposit_money % 100 == 0):
            balance += deposit_money
            print(f"Deposit of {deposit_money}/- is successful.")
            account_statement.append(["Money deposit","  ", deposit_money])
        else:
            print("Invalid amount entered!\nKindly read the note.")
    else:
        print("Insufficient amount to initiate deposit!\nAmount must be greater than 100.")

def balance_enquiry():
    print(f"Account balance: {balance}/-")

def service_menu():
    while(True):
        
        print("\n------- SERVICE MENU -------")
        print("1. Balance Enquiry\n2. Deposit Money\n3. Withdraw Money\n4. Mini Statement\n5. Exit Transaction")
        serial_num = int(input("\nEnter serial number of service needed: "))
        
        match(serial_num):
            case 1:
                print("\nService - 'Balance Enquiry'")
                balance_enquiry()
            
            case 2:
                print("\nService - 'Deposit Money'")
                money_deposit()
            
            case 3:
                print("\nService - 'Withdraw Money'")
                money_withdraw()
                
            case 4:
                print("\nService - 'Mini Statement'")
                mini_statement()
                
            case 5:
                print("\nTransaction Completed.\nThank you! Visit again.")
                break
            case _:
                print("\nInvalid service request!")

def verify_pin():
    for i in range(3):
        atm_pin = input("\nEnter ATM pin(pin must be only 4 or 6-digits): ")

        if((len(atm_pin) == 4 or len(atm_pin) == 6) and atm_pin.isdigit()):
            service_menu()
            break
        else:
            if(i < 2):
                print("\nInvalid pin!\nPlease enter valid pin number.")
            else:
                print("\nInvalid pin!")
                print("\nYou have exceeded no. of tries!\nYour card has been blocked for 24hrs.\n")

balance = 0
account_statement = []
verify_pin()
