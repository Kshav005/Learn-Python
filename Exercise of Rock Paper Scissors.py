# In this exercise, you have to create a 'Rock, Paper, Scissor' game
# Hint : Use nested 'if'
# Good luck, below is the solution if you are unable to solve this








import random

a1 = ["rock", "paper", "scissors"]
b = random.choice(a1)
user = int(input("Enter your choice - 1 for Rock, 2 for Paper and 3 for Scissors\n"))
if b == "rock" : 
    if user == 2 : 
        print(f"You chose PAPER and Computer chose {b.upper()}. You won!")
    elif user == 3 : 
        print(f"You chose SCISSORS and Computer chose {b.upper()}. You lost D:")
    else : 
        print(f"You both chose ROCK. It's a TIE")    

elif b == "paper" : 
    if user == 1 : 
        print(f"You chose ROCK and Computer chose {b.upper()}. You lost D:")
    elif user == 3 : 
        print(f"You chose SCISSOR and Computer chose {b.upper()}. You won!")
    else : 
        print(f"You both chose PAPER. It's a TIE")

elif b == "scissors" : 
    if user == 1 : 
        print(f"You chose ROCK and Computer chose {b.upper()}. You won!")
    elif user == 2 : 
        print(f"You chose PAPER and Computer chose {b.upper()}. You lost D:")
    else : 
        print(f"You both chose SCISSORS. It's a TIE")

# END OF EXERCISE!