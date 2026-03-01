users = {
    "admin": "pass1234"
}
attempt = 0
max_attempts = 3
while attempt < max_attempts:
    username = input("Enter the username: ").lower()
    password = input("Enter the password: ")
    if users.get(username) == password:
        print("Logged in.....\n")
        break
    else:
        attempt += 1
        print("Incorrect Credentials")
        print(f"Attempts left : {max_attempts - attempt}\n")
    if attempt == max_attempts:
        print("You are blocked\n")