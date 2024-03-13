# Rock, Paper and Scissors Game
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_images = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

# Prevents any bugs
if user_choice >= 0 and user_choice < 3:
    print("User chooses:")
    print(game_images[user_choice])

    computer_choice = random.randint(0, 2)

    print("Computer chooses:")
    print(game_images[computer_choice])

    if user_choice == 0 and computer_choice == 1:
        print("You lose!")
    elif user_choice == 1 and computer_choice == 2:
        print("You lose!")
    elif user_choice == 2 and computer_choice == 0:
        print("You lose!")
    elif user_choice == computer_choice:
        print("It's a draw!")
    else:
        print("You win!")
else:
    print("That's an invalid number, you lose!")
