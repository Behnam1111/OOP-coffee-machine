from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

is_on = True
while is_on:
    menu = Menu()
    coffee_maker = CoffeeMaker()
    money_machine = MoneyMachine()
    order = input(f"What would you like? {menu.get_items()}:")
    if order == "report":
        coffee_maker.report()
    elif order == "off":
        is_on = False
    else:
        drink = menu.find_drink(order)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
