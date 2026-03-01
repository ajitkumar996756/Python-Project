import random
def Number_Game():
    try:
        attempt = 0
        max_attempts = 5

        print("Let's play a Number Guess Game")
        while attempt < max_attempts:
            user = int(input("\nEnter your number (1-10): "))
            if 0 < user <= 10:
                guess = random.randint(1, 10)
                print(f"\nComputer Guess: {guess}")
                if guess == user:
                    print(f"Your number : {guess}")
                    print("It is a draw.\n")
                    break
                elif user > guess:
                    print(f"Your number : {user}")
                    print("You have won the Game.\n")
                    break
                else:
                    attempt += 1
                    print(f"Your Number : {user}")
                    print("Wrong guess....!")
                    print("You haave lost.")
                    print("Attempts left: ", max_attempts - attempt)
            else:
                print("Please choose a number from (1-10): \n")
        if attempt == max_attempts:
            print("You are blocked")
    except ValueError:
        print("Please enter a valid number!\n")

Number_Game()
