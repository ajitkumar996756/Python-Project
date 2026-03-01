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



# Password Strength Checker
# while True:
#     Password_Checker = input("Enter the Password : ")
#     Password_Checker1 = Password_Checker[0:9]

#     if Password_Checker <= Password_Checker1:
#         print("Please Enter greater than 8 digit value")
#         print()
#     else:
#         print(f"Your Password is {Password_Checker}")
#         print()
#         break



# while True:
#     Password_Checker = input("Enter the password : ")
#     print("----------------------------------------")
#     def password(pass1):
#         Password_Checker1 = Password_Checker[0:7]
#         if Password_Checker != Password_Checker1:
#             if Password_Checker.isalpha():
#                 print(f"Your Password : {Password_Checker}")
#                 print(f"Nor strong enough.")
#                 print(f"please Enter Sum digits and Symbols")
#                 print()
#             elif Password_Checker.isdigit():
#                 print(f"Your Password : {Password_Checker}")
#                 print(f"Nor strong enough.")
#                 print(f"please Enter Sum Charactors and Symbols")
#             else:
#                 print(f"Your Password : {Password_Checker}")
#                 print("Very strong Password.")
#                 print()
#         else:
#             print("Plesse Enter the password")
#             print("Greater than 8 digit.....")
#             print()
#     password(Password_Checker)