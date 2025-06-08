# import asyncio

# TO-DO: add @require_power functionality

class CoffeeMachine:

    menu = ["Hot Espresso", "Cold Espresso", "Hot Latte", "Latte Affogato"]
    
    def __init__(self):

        self.power = False
        

    def on_power(f):
        def wrapper(self, *args, **kwargs):
            if self.power:
                return f(self, *args, **kwargs)
            else:
                print("Beep! Beep!")
        return wrapper

    def power_on(self):
        self.power = True

    def power_off(self):
        self.power = False

    @on_power
    def brew(self, drink):
        if drink in self.menu:
            print(f"Enjoy your {drink}")
        else:
            print(f"We can't brew {drink} right now. But you can choose a drink from our menu.")

