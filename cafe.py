from coffee_machine import CoffeeMachine
from cashier import Cashier

coffee_machine = CoffeeMachine()

def pay(amount):
    pass

cashier = Cashier(1000)

coffee_machine.power_on()
# coffee_machine.power_off()
drink = cashier.accept_order()
coffee_machine.brew(drink)
