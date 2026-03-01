# Logged In system based on RBAC
while True:
    users = {
        "admin":"admin123",
        "user":"user123",
        "editor":"editor123"
        }
    user = input("Enter the Permission (User/Admin/Editor) : ").lower()
    password = input(f"Enter the {user} password : ")
    if (users.get(user)) == password and user == "admin":
        print(f"You are the {user}.")
        print("You have all Access")
        print()
        break
    elif (users.get(user)) == password and user == "user":
        print(f"You are a Normal {user}.")
        print()
        break
    elif (users.get(user)) == password and user == "editor":
        print(f"You are the {user}.")
        print("You have limited Access.")
        print()
        break
    else:
        print()
        print("Please Enter Valid Role and Password form Below : ")
        print("User's permission like these......")
        print("Permission (User/Admin/Editor) ")
        print()



        
