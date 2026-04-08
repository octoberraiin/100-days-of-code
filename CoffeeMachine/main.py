MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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
    "money": 0
}


def check_correct_coffee_input(u_input):
    if u_input != "espresso" and u_input != "latte" and u_input != "cappuccino" and u_input != "report" and u_input != "off":
        print("Invalid input. Please enter a coffee.")



def formatted_resources(resource_dict):
    water = resource_dict["water"]
    milk = resource_dict["milk"]
    coffee = resource_dict["coffee"]
    money = resource_dict["money"]

    print(f"Water: {water}ml")
    print(f"Milk: {milk}ml")
    print(f"Coffee: {coffee}g")
    print(f"money: ${money}")



def check_resources_sufficient(resource_dict, drink):
    drink_water_amount = MENU[drink]["ingredients"]["water"]
    drink_milk_amount = MENU[drink]["ingredients"]["milk"]
    drink_coffee_amount = MENU[drink]["ingredients"]["coffee"]

    global resources_available
    if drink_water_amount > resource_dict["water"]:
        print("Sorry, we don't have enough water.")
        resources_available = False
    elif drink_milk_amount > resource_dict["milk"]:
        print("Sorry, we don't have enough milk.")
        resources_available = False
    elif drink_coffee_amount > resource_dict["coffee"]:
        print("Sorry, we don't have enough coffee.")
        resources_available = False
    else:
        resources_available = True


def process_coins():
    print("Please insert coins.")

    quarter = 0.25
    dime = 0.10
    nickel = 0.05
    penny = 0.01

    try:
        quarters_q = int(input("how many quarters?: "))
        dimes_q = int(input("how many dimes?: "))
        nickles_q = int(input("how many nickles?: "))
        pennies_q = int(input("how many pennies?: "))

        global total_money_given
        total_money_given = (quarter * quarters_q) + (dime * dimes_q) + (nickel * nickles_q) + (penny * pennies_q)
    except ValueError:
        print("Sorry, please enter a number.")
        global invalid_syntax
        invalid_syntax = True


def transaction_successful(drink, resource_dict):
    global total_money_given

    if total_money_given < MENU[drink]["cost"]:
        print("Sorry that's not enough money. Money refunded.")

    elif total_money_given >= MENU[drink]["cost"]:
        if total_money_given > MENU[drink]["cost"]:
            change = round(total_money_given - MENU[drink]["cost"], 2)
            print(f"Here is ${change} in change.")
        print(f"Here is your {drink} ☕️. Enjoy!")
        global transactions_successful
        transactions_successful = True


def make_coffee(drink, resource_dict):
    resource_dict["money"] += (MENU[drink]["cost"])
    resource_dict["water"] -= MENU[drink]["ingredients"]["water"]
    resource_dict["milk"] -= MENU[drink]["ingredients"]["milk"]
    resource_dict["coffee"] -= MENU[drink]["ingredients"]["coffee"]






machine_working = True
while machine_working:
    transactions_successful = False
    total_money_given = 0
    resources_available = False
    invalid_syntax = False

    coffee_type = input("What would you like? (espresso/latte/cappuccino): ")
    check_correct_coffee_input(coffee_type)

    if coffee_type == "espresso" or coffee_type == "latte" or coffee_type == "cappuccino":
        check_resources_sufficient(resources, coffee_type)

        if resources_available:
            process_coins()
            if invalid_syntax:
                continue
            transaction_successful(coffee_type, resources)

        if transactions_successful and resources_available:
            make_coffee(coffee_type, resources)


    if coffee_type == "off":
        machine_working = False

    if coffee_type == "report":
        formatted_resources(resources)








