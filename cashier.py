from typing import Optional
class PaymentCancelled(Exception):
    """Raised when the user cancels the payment."""
    pass

class Cashier:
    # Accept orders
    # Take payments
    # Give change
    # Give the order

    def __init__(self, balance: float = 0.0):
        self.balance = balance

    def accept_order(self):
        menu = {
            1: {"drink": "Hot Espresso", "price": 12.0},
            2: {"drink": "Cold Espresso", "price": 15.0},
            3: {"drink": "Hot Latte", "price": 19.0},
            4: {"drink": "Latte Affogato", "price": 25.0},
        }

        for number, item in menu.items():
            print(f"{number}. {item['drink']}: ${item['price']}")
        
        while True:
            try:
                order = int(input("Choose a drink number from the menu: "))
                if menu.get(order):
                    drink = menu.get(order).get("drink")
                    price = menu.get(order).get("price")
                    print(f"You choose {drink}, pay ${price}")
                    return drink, price
            except ValueError:
                print(f"Please enter a valid number.")

    def accept_payment(self, price: float) -> Optional[float]:
        
        """
        Prompt the user for cash until they pay >= price, then return the change.
        
        :param price: cost of the item
        :return: change due (>= 0)
        """

        while True:
            raw = input(f"Enter payment amount (e.g. 5, 10, 50) or 'c' to Cancel: ")
            if raw.lower() == "c":
                print("🔴 Transaction cancelled.")
                raise PaymentCancelled()

            try:
                amount = float(raw)
            except:
                print("❌ Please enter a valid number.")
                continue
            
            if amount < price:
                print(f"❌ Insufficient payment: need {price}, got {amount}")
                continue

            # Accept payment
            self.balance += price
            change = round(amount - price, 2)
            print(f"✅ Payment accepted. Change: {change}")
            return change
