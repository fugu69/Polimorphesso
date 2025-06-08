from coffee_machine import CoffeeMachine

coffee_machine = CoffeeMachine()

def user_input():
    return input("Choose your drink:\n1. Hot Espresso\n2. Cold Espresso\n3. Hot Latte\n4. Latte Affogato\n")

while True:
    drink = user_input()
    
    if drink =="1":
        drink = "Hot Espresso"
        break
    elif drink == "2":
        drink = "Cold Espresso"
        break
    elif drink == "3":
        drink = "Hot Latte"
        break
    elif drink == "4":
        drink =  "Latte Affogato"
        break
    else:
        print("choose from the menu\n")

coffee_machine.power_on()
# coffee_machine.power_off()
coffee_machine.brew(drink)
