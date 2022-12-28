# Rock, Paper, Scissors game!
import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

#List of images
images = [rock, paper, scissors]

#Input Validation
user_choice = int(input('What do you chose? 0 for "Rock", 1 for "Paper" or 2 for "Scissors". '))
if user_choice > 2 or user_choice < 0:
    print("You choose an invalid number, you lose!")
else:
    print(images[user_choice])

    computer_choice = random.randint(0, 2)
    print("Computer chose: ")
    print(images[computer_choice])

    #Conditions
    if user_choice == 0 and computer_choice == 2:
        print('You win!')
    elif computer_choice == 0 and user_choice == 2:
        print('You lose!')
    elif computer_choice > user_choice:
        print('You lose!')
    elif user_choice > computer_choice:
        print('You win!')
    elif user_choice == computer_choice:
        print("It's a draw!")
