from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# TODO 1: Prompt user by asking “ What would you like? (espresso/latte/cappuccino/):

menu = Menu()
coffee_maker = CoffeeMaker()
calculator = MoneyMachine()

is_machine_on = True

while is_machine_on:
    chosen_drink = input(f' What would you like? {menu.get_items()}? ')
    order = menu.find_drink(chosen_drink.lower())

    # TODO 2: Turn off the Coffee Machine by entering “ off ” to the prompt

    if chosen_drink.lower() == 'off':
        is_machine_on = False

    # TODO 3: Print report

    elif chosen_drink.lower() == 'report':
        coffee_maker.report()
        calculator.report()

    elif chosen_drink.lower() == "latte" or chosen_drink.lower() == "espresso" or chosen_drink.lower() == "cappuccino":

        # TODO 4: Check resources sufficient

        if coffee_maker.is_resource_sufficient(order):

            # TODO 5/6: Process coins and transaction

            if calculator.make_payment(order.cost):

                # TODO 7: Make Coffee

                coffee_maker.make_coffee(order)
