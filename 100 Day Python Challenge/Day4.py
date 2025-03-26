# Rock Paper Scissors Game

import random

# heads_or_tails = random.randint(1,2)
# if heads_or_tails == 1:

#     print("heads!")
# else:
#     print("tails!")



game = """

█▀█ █▀█ █▀▀ █▄▀  
█▀▄ █▄█ █▄▄ █░█  

█▀█ ▄▀█ █▀█ █▀▀ █▀█  
█▀▀ █▀█ █▀▀ ██▄ █▀▄  

█▀ █▀▀ █ █▀ █▀ █▀█ █▀█ █▀
▄█ █▄▄ █ ▄█ ▄█ █▄█ █▀▄ ▄█

"""


# Rock
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

# Paper
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# Scissors
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""


print(game)
print("Welcome to a game of Rock, Paper, Scissors!")
computer = random.randint(1,3)


move = int(input("What is your move: (Rock = 1, Paper = 2, and Scissors = 3) "))
if move == 1:
    print(rock)
elif move == 2:
    print(paper)
elif move == 3:
    print(scissors)


if computer == 1:
    print(rock)
elif computer == 2:
    print(paper)
elif computer == 3:
    print(scissors)

#Game Logic:

if move == computer:
    print("It's a tie!")
elif (move == 1 and computer == 3) or (move == 2 and computer == 1) or (move == 3 and computer == 2):
    print("You win!")
else:
    print("You lose!")



    




