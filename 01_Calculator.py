def calculator():
    history = []
    try:
        while True:
            print("\n==== CALCULATOR ====")
            print("1. Add (+)")
            print("2. Subtract (-)")
            print("3. Multiply (*)")
            print("4. Divide (/)")
            print("5. Power (**)")
            print("6. View History")
            print("7. Exit")
            operation = input("Enter Operation (1-7) : ")
            if operation.isdigit():
                if operation == '6':
                    print("\nCalculation History: ")
                    for item in history:
                        print(item)
                    continue
                elif operation == "7":
                    print("Exiting calculator...\n")
                    break
                else:
                    x = int(input("Enter First Number : "))
                    y = int(input("Enter Second Number : "))
                    if operation == "+" or operation == "1":
                        print(f"{x} + {y} = {x + y}")
                        history.append(f"{x} + {y} = {x + y}")
                    elif operation == "-" or operation == "2":
                        print(f"{x} - {y} = {x - y}")
                        history.append(f"{x} - {y} = {x + y}")
                    elif operation == "*" or operation == "3":
                        print(f"{x} * {y} = {x * y}")
                        history.append(f"{x} * {y} = {x + y}")
                    elif operation == "/" or operation == "4":
                        print(f"{x} / {y} = {x / y}")
                        history.append(f"{x} / {y} = {x + y}")
                    elif operation == "**" or operation == "5":
                        print(f"{x} ** {y} = {x ** y}")
                        history.append(f"{x} ** {y} = {x + y}")
                    else:
                        print("Invalid operation")
            else:
                print("Please Enter the Numeric values")
    except:
        print("Please Enter the Numbers....!\n")
calculator()
