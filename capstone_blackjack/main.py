############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game:
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here:
#   http://blackjack-final.appbrewery.repl.run
from art import logo
from os import system
from random import choice

def check_scores(user_score: int, computer_score: int):
    ...

def game() -> None:
    user_cards = [choice(cards) for _ in range(2)]
    computer_cards = [choice(cards) for _ in range(2)]

    should_continue = True
    while should_continue:
        user_score = sum(user_cards)
        computer_score = sum(computer_cards)

        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")



cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

wanna_play = input("Do you want to play a game of blackjack? Type 'y' or 'n': ")
if wanna_play == "y":
    system("clear")
    print(logo)
    game()
