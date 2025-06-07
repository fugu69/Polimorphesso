class CoffeeMachine:

    menu = ["Hot Espresso", "Cold Espresso", "Hot Latte", "Latte Affogato"]
    
    # def __init__(self, menu):
    #     self.menu = ["Hot Espresso", "Cold espresso", "Hot Latte", "Latte Affogato"]

    def brew(self, drink):
        if drink in self.menu:
            print(f"Enjoy your {drink}")
        else:
            print(f"We can't brew {drink} right now. But you can choose a drink from our menu.")

