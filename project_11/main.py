# Number Guessing Game
from art import logo
from os import system
from random import randint

def game() -> None:
    """Initalizes the number guessing game."""
    chosen_number = randint(1, 100)
    lives = 10

    print("I'm thinking in a number between 1 and 100, can you guess it?")
    difficulty = input("Select a difficulty. Type 'easy' or 'hard': ")

    if difficulty == "hard":
        lives = 5

    should_continue = True
    while should_continue:
        if lives <= 0:
            print("\nUnfortunately, you ran out of lives. :(")
            print(f"The correct number was {chosen_number}")
            should_continue = False
        else:
            print(f"\nNumber of lives: {lives}")
            guessed_number = int(input("Guess a number: "))

            if guessed_number > chosen_number:
                print("The number is lower.")
                lives -= 1
            elif guessed_number < chosen_number:
                print("The number is higher.")
                lives -= 1
            else:
                print(f"Congratulations! The correct number is {chosen_number}. :D")
                should_continue = False

    keep_playing = input("Do you want to play again? Type 'y' or 'n': ")

    if keep_playing == "y":
        system("clear")
        game()

    return


print(logo)
game()
print("Thank you for playing the game!")
