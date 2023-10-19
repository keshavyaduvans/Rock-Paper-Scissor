import random

# Initialize scores
user_score = 0
computer_score = 0

# Dictionary to map choices to their corresponding numbers
choices = {"1": "rock", "2": "paper", "3": "scissors"}

def get_user_choice():
    print("Choose your weapon:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    choice = input("Enter the number of your choice (1/2/3): ")
    return choices.get(choice)

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (
        (user_choice == "rock" and computer_choice == "scissors")
        or (user_choice == "scissors" and computer_choice == "paper")
        or (user_choice == "paper" and computer_choice == "rock")
    ):
        return "You win!"
    else:
        return "Computer wins!"

while True:
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()

    print(f"You chose {user_choice}")
    print(f"Computer chose {computer_choice}")

    result = determine_winner(user_choice, computer_choice)
    print(result)

    if "You win" in result:
        user_score += 1
    elif "Computer wins" in result:
        computer_score += 1

    print(f"Your Score: {user_score}")
    print(f"Computer Score: {computer_score}")

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        break
