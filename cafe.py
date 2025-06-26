from coffee_machine import CoffeeMachine
from cashier import Cashier, PaymentCancelled

coffee_machine = CoffeeMachine()

def pay(amount):
    pass

cashier = Cashier(1000)

coffee_machine.power_on()
# coffee_machine.power_off()
drink, price = cashier.accept_order()
try:
    payment = cashier.accept_payment(price)
    if isinstance(payment, float):
        coffee_machine.brew(drink)
except PaymentCancelled:
    print("User cancelled the order.")
