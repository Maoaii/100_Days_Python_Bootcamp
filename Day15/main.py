from Commands.constants import *

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0.0,
}


def handle_report():
    # For every resource, print the amount of resources of that type
    for resource in resources:
        if resource == Resources.WATER:
            print(OutputMessages.WATER_RESOURCE % (resources[resource]))
        elif resource == Resources.MILK:
            print(OutputMessages.MILK_RESOURCE % (resources[resource]))
        elif resource == Resources.COFFEE:
            print(OutputMessages.COFFEE_RESOURCE % (resources[resource]))
        elif resource == Resources.MONEY:
            print(OutputMessages.MONEY_RESOURCE % (resources[resource]))


def handle_drink(drink):
    # Check if there are enough resources for this drink
    if has_enough_resources(drink):

        # Prompt user to insert coins
        money = insert_coins()

        # Check if user has enough money for the drink
        if not has_enough_money(money, drink):
            print(OutputMessages.NOT_ENOUGH_MONEY)
        else:
            # Add money to the machine
            resources[Resources.MONEY] += money

            # If user needs change
            if needs_change(money, drink):
                # Give change back and remove from machine
                give_change(money, drink)

            # Make drink
            make_drink(drink)


def has_enough_resources(drink):
    # For every resource the drink needs, check if there are enough resources
    for resource in MENU[drink][MenuCommands.INGREDIENTS]:
        if resources[resource] < MENU[drink][MenuCommands.INGREDIENTS][resource]:
            print(OutputMessages.NOT_ENOUGH_RESOURCE % resource)
            return False
    return True


def insert_coins():
    money = 0

    print(InputMessages.COINS_MESSAGE)

    # Calculate money given
    money += float(input(InputMessages.QUARTERS_MESSAGE)) * MoneyValue.QUARTER
    money += float(input(InputMessages.DIMES_MESSAGE)) * MoneyValue.DIME
    money += float(input(InputMessages.NICKELS_MESSAGE)) * MoneyValue.NICKEL
    money += float(input(InputMessages.PENNIES_MESSAGE)) * MoneyValue.PENNIE

    return money


def has_enough_money(money, drink):
    return money >= MENU[drink][MenuCommands.COST]


def needs_change(money, drink):
    return money > MENU[drink][MenuCommands.COST]


def give_change(money, drink):
    # Calculate change
    change = money - MENU[drink][MenuCommands.COST]

    # Remove money from machine
    resources[Resources.MONEY] -= change

    # Output change message
    print(OutputMessages.CHANGE % change)


def make_drink(drink):
    # Remove resources
    for resource in MENU[drink][MenuCommands.INGREDIENTS]:
        resources[resource] -= MENU[drink][MenuCommands.INGREDIENTS][resource]

    # Print output message
    print(OutputMessages.DRINK_SERVED % drink)


while True:
    # Wait for user input
    command = input(InputMessages.INPUT_MESSAGE)

    # Do different things depending on the user command
    match command:
        case Commands.REPORT:
            handle_report()
        case Commands.ESPRESSO:
            handle_drink(Commands.ESPRESSO)
        case Commands.LATTE:
            handle_drink(Commands.LATTE)
        case Commands.CAPPUCCINO:
            handle_drink(Commands.CAPPUCCINO)
        case Commands.OFF:
            quit()
        case _:
            print(Commands.UNKNOWN)
