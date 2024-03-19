# Coffee Machine Project
from data import MENU, resources

def enough_resources(order: str) -> bool:
    """Return a boolean value telling if it's possible to take the order."""

    # Check water quantity
    if MENU[order]['ingredients']['water'] > resources['water']:
        print("Sorry, there's not enough water.")
        return False

    # Check coffee quantity
    if MENU[order]['ingredients']['coffee'] > resources['coffee']:
        print("Sorry, there's not enough coffee.")

    # Check milk quantity
    if order != "espresso":
        if MENU[order]['ingredients']['milk'] > resources['milk']:
            print("Sorry, there's not enough milk.")

    return True


def insert_coins(order: str) -> float:
    """Initialize the coin insertion and return the change value."""

    # Count all possible coins and sum the result
    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickles = int(input("How many nickes? "))
    pennies = int(input("How many pennies? "))

    total_amount = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
    change = total_amount - MENU[order]['cost']

    return change


def make_coffee(order: str) -> None:
    """Makes coffee and subtract the resources quantities."""
    resources['water'] -= MENU[order]['ingredients']['water']
    resources['coffee'] -= MENU[order]['ingredients']['coffee']

    if order != "espresso":
        resources['milk'] -= MENU[order]['ingredients']['milk']


money = 0
while True:
    order = input("What would you like to drink? (espresso/latte/cappuccino): ").lower()

    if order in MENU:
        is_enough = enough_resources(order)

        if is_enough:
            print("Please insert coins.")
            change = insert_coins(order)

            if change > 0:
                print(f"Here is ${change:.2f} in change.")
            elif change < 0:
                print("Sorry, there's not enough money. Money refunded.")
                continue

            make_coffee(order)
            money += MENU[order]['cost']
            print(f"Here is your {order}. Enjoy!")

    elif order == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${money}")

    elif order == "off":
        break

