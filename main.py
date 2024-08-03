from menu import MENU, resources
from art import coffee

Profit = 0


# TODO 4- Check if the resources are sufficient enough for an order
def resource_sufficient(check_ingredients):
    for item in check_ingredients:
        if check_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True


# TODO 5- if there are enough resources for the drink, calculate the coins inserted
def process_coin():
    total = int(input("💲 How many quarters?: ")) * 0.25
    total += int(input("💲 How many dimes?: ")) * 0.1
    total += int(input("💲 How many nickles?: ")) * 0.05
    total += int(input("💲 How many pennies?: ")) * 0.01
    return total


# TODO 6-  Check that the user inserted the right amount for the drink
def right_amount(inserted_coins, cost_of_drink):
    if cost_of_drink > inserted_coins:
        print(f"Sorry, that's not enough money :[. Money refunded.")
        return False
    elif cost_of_drink == inserted_coins:
        print("You put in the right amount :]")
        return True
    else:
        change = round((inserted_coins - cost_of_drink), 2)
        print(f"Your change is ${change}")
        global Profit
        Profit += cost_of_drink
        return True


# TODO 7-  if everything checks out, make the coffee
def make_coffee(name_of_drink, ingredients_used):
    for items in ingredients_used:
        resources[items] -= ingredients_used[items]
    drink = name_of_drink.capitalize()
    print(f"Here is your {drink} ☕️. Enjoy!")
    print()


# TODO 1- Prompt user on what they would like to drink
order = True
while order:
    print(coffee)
    choice = input("- What would you like to drink? (Espresso/Latte/Cappuccino): ").lower()

# TODO 2- turn off the machine when the user inputs "off"
    if choice == 'off':
        order = False
# # TODO 3- Quantity of ingredients in the machine when the user inputs "report"
    elif choice == 'report':
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${Profit}")
    else:
        drink_of_choice = MENU[choice]
        selected = choice.capitalize()
        print(f"{selected} cost ${drink_of_choice['cost']}")

        if resource_sufficient(drink_of_choice["ingredients"]):
            print("-- Insert your coin --")
            payment = process_coin()
            if right_amount(payment, drink_of_choice["cost"]):
                make_coffee(choice, drink_of_choice["ingredients"])


