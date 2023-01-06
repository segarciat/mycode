#!/usr/bin/env python3

MAX_GUESTS = 5
DRINKS = {"COFFEE": 2.00, "TEA": 1.50, "WATER": 1.00, "JUICE": 3.00, "SODA": 2.00}

def welcome():
    print("Welcome to Only-Drinks Cafe!")

def prompt_guest_count():
    """Ask how many guests will be eating at the diner"""
    while True:
        try:
            n = input("How many guests will be joining us today? ")
        except EOFError:
            print("\nPlease come again!")
            exit()
        if not n.isnumeric():
            print("Sir, we request you give us a number")
        elif int(n) <= 0:
            print("That's not a valid guest count")
        else:
            return int(n)

def prompt_for_drink():
    """Prompts guest for drink of choice"""
    while True:
        display_options()
        try:
            option = input("\nWhat would you like? ").upper()
            for drink in DRINKS:
                if option == drink or drink.startswith(option):
                    return drink
        except EOFError:
            print("\nPlease come back!")
            exit()

def display_options():
    print("These are our drink options: ")
    print("-" * 40)
    for drink, price in DRINKS.items():
        print(f"\t({drink[0]}){drink[1:]:10} - ${price:4.2f}")

def take_orders(number_of_guests):
    orders = []
    for i in range(number_of_guests):
        drink = prompt_for_drink()
        orders.append(drink)
        print(f"Guest {i + 1} wants a {drink}\n")
    return orders

def display_total(orders): 
    print("-" * 30)
    for n, drink in enumerate(orders):
        print(f"\t{drink:10} (${DRINKS[drink]:5.2f}) for guest {n + 1}")
    print("-" * 30)
    total = sum(DRINKS[order] for order in orders)
    print(f"Your total is: ${total:6.2f}")

if __name__ == '__main__':
    # welcome to diner
    welcome()
    # prompt for number of guests
    number_of_guests = prompt_guest_count()

    if number_of_guests > MAX_GUESTS:
        print(f"We apologize; we do not serve parties larger than {MAX_GUESTS}")
        exit()

    orders = take_orders(number_of_guests)
    display_total(orders)
    print("\nThanks for coming!")

        
        
