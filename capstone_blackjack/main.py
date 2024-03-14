# Blackjack game project
from art import logo
from os import system
from random import choice

def check_scores(user_score: int, computer_score: int) -> str:
    """Return a string telling if the user won or lost against the computer."""
    message = ""

    if computer_score == user_score:
        message = "It's a draw. 😐"
    elif user_score == 21:
        message = "Blackjack! You win. 😮"
    elif user_score > 21 and computer_score > 21:
        if user_score < computer_score:
            message = "You win! 🤩"
        else:
            message = "You lose! 😟"
    elif user_score > 21:
        message = "You lose! 😟"
    elif computer_score > 21 or user_score > computer_score:
        message = "You win! 🤩"
    else:
        message = "You lose! 😟"

    return message

def game() -> None:
    user_cards = [choice(cards) for _ in range(2)]
    computer_cards = [choice(cards) for _ in range(2)]

    should_continue = True
    while should_continue:
        user_score = sum(user_cards)
        computer_score = sum(computer_cards)

        if user_score > 21 and 11 in user_cards:
            ace_index = user_cards.index(11)
            user_cards[ace_index] = 1
            user_score = sum(user_cards)  # Solves user score bugs

        print(f"\nYour cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if computer_score <= 16:
            computer_cards.append(choice(cards))
            computer_score = sum(computer_cards)  # Solves computer score bugs

        if user_score < 21:
            get_card = input("Type 'y' to get another cards, or 'n' to pass: ")

            if get_card == "y":
                user_cards.append(choice(cards))
                continue

        print(f"\nYour cards: {user_cards}, computer's cards: {computer_cards}")
        print(f"Your score: {user_score}, computer's score: {computer_score}")
        print(check_scores(user_score, computer_score))

        keep_playing = input("\nDo you want to keep playing? Type 'y' or 'n': ")

        if keep_playing == "y":
            system("clear")
            game()

        should_continue = False

    return


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

wanna_play = input("Do you want to play a game of blackjack? Type 'y' or 'n': ")
if wanna_play == "y":
    system("clear")
    print(logo)
    game()
    print("Thank you for playing our game!")
