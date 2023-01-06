#!/usr/bin/env python3

MAX_GUESTS = 5
drinks = {"COFFEE": 2.00, "TEA": 1.50, "WATER": 1.00, "JUICE": 3.00, "SODA": 2.00}

def welcome():
    print("Welcome to Only-Drinks Cafe!")

def prompt_guest_count():
    """Ask how many guests will be eating at the diner"""
    while True:
        n = input("How many guests will be joining us today? ")
        if not n.isnumeric():
            print("Sir, we request you give us a number")
        elif int(n) <= 0:
            print("That's not a valid guest count")
        else:
            return int(n)

def prompt_for_drink(drinks):
    """Prompts guest for drink of choice"""
    while True:
        display_options(drinks)
        option = input("\nWhat would you like? ").upper()
        for drink in drinks:
            if option == drink or drink.startswith(option):
                return drink

def display_options(drinks):
    print("These are our drink options: ")
    print("-" * 40)
    for drink, price in drinks.items():
        print(f"\t({drink[0]}){drink[1:]:10} - ${price:4.2f}")

def take_orders(number_of_guests):
    orders = []
    for i in range(number_of_guests):
        drink = prompt_for_drink(drinks)
        orders.append(drink)
        print(f"Guest {i + 1} wants a {drink}\n")

    print("\nRepeating orders: ")
    print("-" * 30)
    for n, drink in enumerate(orders):
        print(f"\t{drink} for guest {n + 1}")
    return orders

def display_total(orders): 
    total = sum(drinks[order] for order in orders)
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

        
        
