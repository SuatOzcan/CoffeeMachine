from coffee_types import Cappuccino, Espresso, Latte
from coffee_machine import Coffee_Machine

coffee_machine = Coffee_Machine()
espresso = Espresso()
cappuccino = Cappuccino()
latte = Latte()

def user_input():
    prompt = input("What would you like? espresso, latte, capuccino.\n")
    return prompt

def deduct_resources(coffee_machine,coffee_type, inserted_money):

    resource_checker = True

    for i in range((coffee_machine.resources.__len__())):
         if coffee_machine.resources[i] < coffee_type.costs[i]:
              resource_checker = False

    if inserted_money > coffee_type.price:
         refund = inserted_money - coffee_type.price
         print(f'Here is your refund of ${refund}.')

    enough_money = inserted_money >= coffee_type.price

    if resource_checker and enough_money:
        for i in range(coffee_machine.resources.__len__()):
            if i < (coffee_machine.resources.__len__() - 1):
                coffee_machine.resources[i] = coffee_machine.resources[i] - coffee_type.costs[i]
                continue
            coffee_machine.resources[i] = coffee_machine.resources[i] + coffee_type.costs[i]
            print(f'Enjoy your {coffee_type.name}!')
    else:
         print('Please insert more money.')

def menu():
    prompt = user_input()
    while prompt != 'off':
        if prompt == 'report':
                print(f'Water: {coffee_machine.resources[0]}ml\nMilk: {coffee_machine.resources[1]}ml\nCoffee: {coffee_machine.resources[2]}g\nMoney: ${coffee_machine.resources[3]}')          
    
        elif prompt in [espresso.name, latte.name, cappuccino.name]:
            for coffee in [espresso.name, latte.name, cappuccino.name]:
                if prompt == coffee:
                    coffee_kinds = {'espresso': espresso,'latte': latte,'cappuccino':cappuccino}
                    coffee_type = coffee_kinds[prompt]
                    break

            number_checker = True
            while number_checker:
                try:
                    inserted_money = float(input(f'Please insert ${coffee_type.price}.\n'))
                    break
                except:
                    print('Please insert in numbers.')

            deduct_resources(coffee_machine,coffee_type, inserted_money)

        prompt = user_input()
