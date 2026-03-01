def Pass_Strenth_Check():
    while True:
        password = input("Enter the Password : ")
        if 0 < len(password) <= 12:
            if any(char.isspace() for char in password):
                print("Please Don't Enter")
                print("The 'space' in the password\n")
            elif password.isdigit():
                print("Too weak")
                print("Your Password Only contains the Digits\n")
            elif password.isalpha():
                print("Too weak")
                print("Your Password Only Contains the Alphabets\n")
            elif (
                any(char.isalpha() for char in password) 
                and any(char.isdigit() for char in password) 
                and any(char in "!@#$%^&*" for char in password)
            ):
                print("Very Strong Password")
                print("Contains letters + numbers + symbols.\n")
                exit()
            elif (
                any(char.isdigit() for char in password) 
                and any(char in "!@#$%^&*" for char in password)
            ):
                print("Stronge but weak password")
                print("Your Password Only Contains numbers + symbols.\n")
            elif (
                any(char.isalpha() for char in password) 
                and any(char in "!@#$%^&*" for char in password)
            ):
                print("Stronge but weak password")
                print("Your Password Only Contains letters + symbols.\n")
            elif (
                any(char.isdigit() for char in password) 
                and any(char.isalpha() for char in password)
            ):
                print("Stronge but weak password")
                print("Your Password is mixing of")
                print("Alhabates and the numbers.\n")
            elif any(char in "~!@#$%^&*()_+=-/><.," for char in password):
                print("Your Password only")
                print("contains Symbolic characters.\n")
        else:
                print("Please Enter the Password.")
                print("Form (1-12 digit).\n")
Pass_Strenth_Check()
