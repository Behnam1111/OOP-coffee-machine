from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


class CoffeeMachine:
    def __init__(self):
        self.menu = Menu()
        self.coffee_maker = CoffeeMaker()
        self.money_machine = MoneyMachine()

    def coffee_machine(self):
        order = input(f"What would you like? {self.menu.get_items()}:")
        if "report" in order:
            self.coffee_maker.report()
        else:
            drink = self.menu.find_drink(order)
            if self.coffee_maker.is_resource_sufficient(drink):
                if self.money_machine.make_payment(drink.cost):
                    self.coffee_maker.make_coffee(drink)


coffee_machine = CoffeeMachine()
coffee_machine.coffee_machine()
