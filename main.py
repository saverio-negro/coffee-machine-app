# The Coffee Machine App

from data import MENU
from data import resources
from data import profit


def display_report(machine_resources):
    print(f"Water: {machine_resources['water']}ml")
    print(f"Milk: {machine_resources['milk']}ml")
    print(f"Coffee: {machine_resources['coffee']}g")
    print(f"Money: ${profit}")


def is_resource_sufficient(drink_ingredients):
    """Returns True if ingredients are sufficient; otherwise, it returns False."""
    for ingredient in drink_ingredients:
        if drink_ingredients[ingredient] > resources[ingredient]:
            print(f"Sorry, there is not enough {ingredient}.")
            return False
    return True


def process_coins():
    """Returns total calculated from coins inserted."""
    print("Please, insert coins.")
    num_quarters = int(input("How many quarters?: "))
    num_dimes = int(input("How many dimes?: "))
    num_nickels = int(input("How many nickels?: "))
    num_pennies = int(input("How many pennies?: "))

    return (num_quarters * 0.25) + (num_dimes * 0.10) + (num_nickels * 0.05) + (num_pennies * 0.01)


def is_transaction_successful(money_received, drink_cost):
    """Returns True if the payment is accepted, or False if payment is rejected for insufficient money."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry, that's not enough money. Money refunded.")
        return False


def make_drink(drink_name, drink_ingredients, machine_resources):
    """Deduct the required ingredients from the resources."""
    for ingredient in drink_ingredients:
        machine_resources[ingredient] -= drink_ingredients[ingredient]
    print(f"Here is your {drink_name} ☕️. Enjoy!")


is_on = True

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if choice == "off":
        is_on = False
    elif choice == "report":
        display_report(resources)
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            total = process_coins()
            if is_transaction_successful(total, drink["cost"]):
                make_drink(choice, drink["ingredients"], resources)


