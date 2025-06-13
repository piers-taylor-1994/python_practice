from operator import indexOf
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    },
    "cortado": {
        "ingredients": {
            "water": 150,
            "milk": 50,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

default_resources = {
    "WATER": 300,
    "MILK": 200,
    "COFFEE": 100,
    "MONEY": 0.0
}

resources = {
    "water": default_resources["WATER"],
    "milk": default_resources["MILK"],
    "coffee": default_resources["COFFEE"],
    "money": default_resources["MONEY"]
}

drinks = []

for key in MENU:
   drinks.append(key)

def print_drinks():
    output = ""
    for d in drinks:
        output += d
        if indexOf(drinks, d) != len(drinks) - 1:
            output += "/"
    return output

def reset_resources():
    for k in resources:
        resources[k] = default_resources[k.upper()]

def print_resources():
    output = ""
    for r in resources:
        if r == "money":
            output += f"{r}: ${'{0:.2f}'.format(resources[r])}"
        else:
            output += f"{r}: {resources[r]}"
            if r == "water" or r == "milk":
                output += "ml"
            elif r == "coffee":
                output += "g"
        output += "\n"
    return output

def check_resources(drink):
    for r in MENU[drink]["ingredients"]:
        if resources[r] - MENU[drink]["ingredients"][r] < 0:
            return r
    return ""

def enough_money(choice_price, money):
    if money >= choice_price:
        return True
    else:
        return False

def process_coffee(choice, money):
    amount_to_deduct = MENU[choice]["cost"]
    for r in MENU[choice]["ingredients"]:
        resources[r] -= MENU[choice]["ingredients"][r]
    resources["money"] += amount_to_deduct
    return round((money - amount_to_deduct), 2)

def coffee_machine():
    choice = input(f"“What would you like? ({print_drinks()}): ")
    if choice in drinks:
        depleted_resource = check_resources(choice)
        if not depleted_resource == "":
            print(f"Sorry there isn't enough {depleted_resource}")
        else:
            do = float(input("How many dollar bills? "))
            q = float(input("How many quarters? ")) * 0.25
            d = float(input("How many dimes? ")) * 0.10
            n = float(input("How many nickles? ")) * 0.05
            p = float(input("How many pennies? ")) * 0.01
            total = round((do + q + d + n + p), 2)
            if not enough_money(MENU[choice]["cost"], total):
                print("Sorry that's not enough money. Money refunded.")
            else:
                change = process_coffee(choice, total)
                if not change == 0.0:
                    print(f"Here is ${'{0:.2f}'.format(change)} dollars in change.” ")
                print(f"Here is your {choice}. Enjoy!")
    elif choice == "report":
        print(print_resources())
    elif choice == "reset":
        print("\n" * 20)
        reset_resources()
    else:
        return
    coffee_machine()
coffee_machine()