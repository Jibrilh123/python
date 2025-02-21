import random
while True:
    user_action = input("Enter a choice (rock, paper, scissors):")
    possible_actions = ["rock","paper","scissors"]
    computer_action = random.choice(possible_actions)
    print(f"\n you chose {user_action}, computer chose {computer_action}\n")

    if user_action == computer_action:
        print(f"Both players selected{user_action}. It is a tie")

    elif user_action == 'rock':
        if computer_action == "scissors":
            print("you win")
        else:
            print("You lose")

    elif user_action == "paper":
        if computer_action == "scissors":
            print("you lose")
        else:
            print("You win")

    elif user_action == "scissors":
        if computer_action == "rock":
            print("you lose")
        else:
            print("you win")

    play_again = input("Play again (Y/N):")
    if play_again !="Y":
        break
    

