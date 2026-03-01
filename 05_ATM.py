print("-------------Welcome to the ATM ----------------")
pin1 = {
    "2580" : 1234
    }
transaction_history = []
saving_balance = 1000
current_balance = 2000
attempt = 0
max_attempt = 3
# asking for login
while attempt < max_attempt:
    account_number = input("Enter the user account No. : ")
    pin = int(input("Enter the 4-digit pin : "))
    if pin1.get(account_number) == pin:
        print("You are Logged In.......\n")
        break
    else:
        attempt += 1
        print(f"Remaing attempt : {max_attempt - attempt}")
    if attempt == max_attempt:
        print("You are blocked")
        exit()
# asking the language
print("1.English")
print("2.Hindi")
language = input("Enter the language (1 / 2) : ")
if language == "1":
    print("You have selected English langusge.\n")
    print("1.Saving")
    print("2.Current")
    account = input("Enter the Account type (1 / 2) : ")
    if account == "1":
        account_type = "saving"
        print("You have selected Savings Account.\n")
    else:
        account_type = "current"
        print("You have seleceted Current Account.\n")
else:
    print("Aapne Hindi language select kiya hai.\n")
    print("1.Bachat Khata")
    print("2.Chaloo Khata")
    account = input("Enter the Account type (1 / 2) : ")
    if account == "1":
        account_type = "saving"
        print("Apne Bachat Khata select kiya hai.\n")
    else:
        account_type = "current"
        print("Apne Chaloo Khata select kiya hai.\n")
while True:
    # asking the category (check_balance/withdraw/transaction_history)
    if account_type == "saving":
        balance = saving_balance
    else:
        balance = current_balance
    print("\n1.Check Balance.")
    print("2.Withdraw")
    print("3.transaction History")
    print("4.Exit")
    category = input("Enter the Account type (1 / 2 / 3 / 4) : ")
    # checking rhe balance
    if category == "1":
        print(f"Available Balance : {balance}\n")
    # withdrawal amount system
    elif category == "2":
        withdraw = int(input("Enter the withdrawal ammount : "))
        if withdraw < 0:
            print("Invalid amount.....!\n")
        elif withdraw > balance:
            print("Insuficient Balance....!\n")
        else:
            balance -= withdraw
            transaction_history.append(f"Transaction : {withdraw}")
            print("You can cash out the money.\n")
            if account_type == "saving":
                saving_balance = balance
            else:
                current_balance = balance
    # Transaction history
    elif category == "3":
        if len(transaction_history) == 0:
            print("No transaction...!")
        else:
            print("Transaction History.")
            for i in transaction_history:
                print("-->", i)
    # exit
    elif category == "4":
        print("Come back next time.....!")
        break
    else:

        print("Invalid category")
