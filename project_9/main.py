from art import logo
from os import system

bids = []

print(logo)
print("Welcome to the secret auction program.")

should_continue = True
while should_continue:
    bidder_name = input("What is your name?: ")
    bid_price = int(input("What's your bid?: $"))

    bids.append({
        "name": bidder_name,
        "bid": bid_price,
    })

    other_bidder = input("Are there any other bidders? Type 'yes' or 'no'.\n")

    if other_bidder == "yes":
        system("clear")
    else:
        should_continue = False

bid_price = 0
highest_bid = {}
for bid in bids:
    if bid["bid"] > bid_price:
        highest_bid = bid
        bid_price = highest_bid["bid"]

print(f"The winner is {highest_bid["name"]} with a bid of ${highest_bid["bid"]}.")
