import random

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif ( 
        (user == "rock" and computer == "scissors") or
        (user == "paper" and computer == "rock") or
        (user == "scissors" and computer == "paper")

    ):
       return "You win!"

    else:
        return "Computer wins!"

def rock_paper_scissors():
    print("Welcome to Rock, Paper, Scissors!")
    choices = ["rock", "paper", "scissors"]
    user_choice = input("Enter your choice (rock/paper/scissors): ").lower()
    if user_choice not in choices:
        print("Invalid choice. Please try again.")
        return
    
    computer_choice = get_computer_choice()
    print (f"Computer chose: {computer_choice}")
    
    result = determine_winner(user_choice, computer_choice)
    print(result)

#Run the game
rock_paper_scissors()