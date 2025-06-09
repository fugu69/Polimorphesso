from coffee_machine import CoffeeMachine

coffee_machine = CoffeeMachine()

def get_user_input():
    menu = {
        "1": "Hot Espresso",
        "2": "Cold Espresso",
        "3": "Hot Latte",
        "4": "Latte Affogato",
    }

    while True:
        choice = input("Choose your drink:\n1. Hot Espresso\n2. Cold Espresso\n3. Hot Latte\n4. Latte Affogato\n")
        if choice in menu:
            return menu[choice]

        print("Choose an option from the menu.\n")



coffee_machine.power_on()
# coffee_machine.power_off()
drink = get_user_input()
coffee_machine.brew(drink)
