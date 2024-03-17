# Higher Lower Game

from art import logo, vs
from game_data import data
from os import system
from random import randint

def choose_account() -> dict[str, any]:
    """Return a random account from the accounts list."""

    # Chooses a random account from accounts list
    random_index = randint(0, len(accounts) - 1)
    chosen_account = accounts[random_index]

    # Deletes the selected account from accounts list
    account_index = accounts.index(chosen_account)
    accounts.pop(account_index)

    return chosen_account


def define_answer() -> str:
    """Return a string informing which account has more followers."""
    answer = ""

    if account_a['follower_count'] > account_b['follower_count']:
        answer = 'a'
    else:
        answer = 'b'

    return answer

accounts = data
account_a = choose_account()
score = 0
while True:
    system("clear")
    print(logo)
    print(f"Compare A: {account_a['name']}, a {account_a['description']} from {account_a['country']}")
    print(vs)

    # Chooses the second account to compare
    account_b = choose_account()
    print(f"Compare B: {account_b['name']}, a {account_b['description']} from {account_b['country']}")

    # Define who has more followers
    has_more_followers = define_answer()

    # The uses chooses an option
    user_choice = input("\nWho has more followers? Type 'a' or 'b': ").lower()

    # User answers right
    if user_choice == has_more_followers:
        print("\nCongratulations, that's correct!")
        input("Press enter to continue: ")
        score += 1
        account_a = account_b
    # User answers wrong
    else:
        print("\nSorry, that's wrong! :(")
        print(f"Total score: {score}")

        keep_playing = input("\nDo you want to continue the game? Type 'y' or 'n': ").lower()
        if keep_playing == "y":
            score = 0
            account_a = choose_account()
            accounts = data
        else:
            break

system("clear")
print("Thank you for playing our game!")


