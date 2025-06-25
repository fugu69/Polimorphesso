class Cashier:
    # Accept orders
    # Take payments
    # Give change
    # Give the order

    def __init__(self, balance):
        self.balance = balance

    def accept_order(self):
        menu = {
            1: {"drink": "Hot Espresso", "price": 12},
            2: {"drink": "Cold Espresso", "price": 15},
            3: {"drink": "Hot Latte", "price": 19},
            4: {"drink": "Latte Affogato", "price": 25},
        }

        for number, item in menu.items():
            print(f"{number}. {item['drink']}: ${item['price']}")
        
        while True:
            try:
                order = int(input("Choose a drink number from the menu: "))
                if menu.get(order):
                    drink = menu.get(order).get("drink")
                    price = menu.get(order).get("price")
                    return drink, price
            except ValueError as e:
                print(f"Please enter a valid number.")

    def change(self, price, amount):
        if amount > price:
            self.balance += amount
            change = round(amount - price, 2)
            self.balance -= change
            return change
        elif amount == price:
            return
        else:
            return f"Payment is not enough"
