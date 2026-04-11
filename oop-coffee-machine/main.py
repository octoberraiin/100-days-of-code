from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


is_coffee_making = True
menu = Menu()
coffee_checker = CoffeeMaker()
money_management = MoneyMachine()

while is_coffee_making:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_coffee_making = False

    if choice == "report":
        coffee_checker.report()
        money_management.report()

    if choice in menu.get_items():
        u_drink = menu.find_drink(choice)

        resources_sufficient = coffee_checker.is_resource_sufficient(u_drink)
        if resources_sufficient:
            payment_successful = money_management.make_payment(u_drink.cost)
            if payment_successful:
                coffee_checker.make_coffee(u_drink)
