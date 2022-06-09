class Commands:
    OFF = "off"
    REPORT = "report"
    ESPRESSO = "espresso"
    LATTE = "latte"
    CAPPUCCINO = "cappuccino"
    UNKNOWN = "That's not a coffee, man."


class InputMessages:
    INPUT_MESSAGE = "What would you like? (espresso/latte/cappuccino): "
    COINS_MESSAGE = "Please insert coins."
    QUARTERS_MESSAGE = "How many quarters?: "
    DIMES_MESSAGE = "How many dimes?: "
    NICKELS_MESSAGE = "How many nickels?: "
    PENNIES_MESSAGE = "How many pennies?: "


class OutputMessages:
    WATER_RESOURCE = "Water: %dml"
    MILK_RESOURCE = "Milk: %dml"
    COFFEE_RESOURCE = "Coffee: %dg"
    MONEY_RESOURCE = "Money: $%0.2f"
    NOT_ENOUGH_RESOURCE = "Sorry there is not enough %s."
    NOT_ENOUGH_MONEY = "Sorry that's not enough money. Money refunded."
    CHANGE = "Here is $%0.2f dollars in change."
    DRINK_SERVED = "Here is your %s ☕️. Enjoy!"


class Resources:
    WATER = "water"
    MILK = "milk"
    COFFEE = "coffee"
    MONEY = "money"


class MenuCommands:
    INGREDIENTS = "ingredients"
    COST = "cost"


class MoneyValue:
    QUARTER = 0.25
    DIME = 0.10
    NICKEL = 0.05
    PENNIE = 0.01
