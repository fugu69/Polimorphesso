class Cashier:
    # Accept orders
    # Take payments
    # Give change
    # Give the order

    def __init__(self, balance):
        self.balance = balance

    def accept_order(self):
        menu = {
            "1": "Hot Espresso",
            "2": "Cold Espresso",
            "3": "Hot Latte",
            "4": "Latte Affogato",
        }

        while True:
            order = input("Choose your drink:\n1. Hot Espresso\n2. Cold Espresso\n3. Hot Latte\n4. Latte Affogato\n")
            if order in menu:
                return menu[order]

            print("Choose an option from the menu.\n")

    def change(self, price, amount):
        if amount > price:
            self.balance += amount
            return round(amount - price, 2)
        elif amount == price:
            return
        else:
            return f"Payment is not enough"
