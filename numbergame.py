import random
playing = True
number = str(random.randint(6,12))

print("I will generate a number from 6 to 12, and you have to guess the number one digit at a time.")
print("The game ends when u get 1 hero!")

while playing:
    guess = input("Give me your best guess! \n")
    if number == guess:
        print("You win the game")
        print("The number was", number)
        break
    
    else:
        print("Your guess was incorrect, try again. \n" )