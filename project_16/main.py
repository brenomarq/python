# Coffee Machine with OPP
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_machine = CoffeeMaker()
money_machine = MoneyMachine()

drinks = {
    "espresso": menu.menu[0],
    "latte": menu.menu[1],
    "cappuccino": menu.menu[2],
}

while True:
    drink_option = input(f"What would you like to drink? {menu.get_items()}: ").lower()

    # Prints a report of the machine resources
    if drink_option == "report":
        coffee_machine.report()
        money_machine.report()

    # Turns off the machine
    elif drink_option == "off":
        break

    # Takes the order
    elif menu.find_drink(drink_option):
        ordered_drink = drinks[drink_option]

        sufficient_resources = coffee_machine.is_resource_sufficient(ordered_drink)

        if sufficient_resources:
            cost = ordered_drink.cost

            can_proceed = money_machine.make_payment(cost)
            if can_proceed:
                coffee_machine.make_coffee(ordered_drink)


