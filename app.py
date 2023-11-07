from coffee_machine import Coffee_Machine
from main_functions import user_input
from coffee_types import Cappuccino, Espresso, Latte

coffee_machine = Coffee_Machine()
espresso = Espresso()
cappuccino = Cappuccino()
latte = Latte()
    
def deduct_resources(coffee_type, inserted_money):

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

prompt = user_input()
while prompt != 'off':
    if prompt == 'report':
            print(f'Water: {coffee_machine.resources[0]}ml\nMilk: {coffee_machine.resources[1]}ml\nCoffee: {coffee_machine.resources[2]}g\nMoney: ${coffee_machine.resources[3]}')          
    elif prompt == 'espresso':
        inserted_money = float(input('Please insert $4.\n'))
        deduct_resources(espresso, inserted_money)
    elif prompt =='latte':
        inserted_money = float(input('Please insert $5.\n'))
        deduct_resources(latte, inserted_money)
    elif prompt == 'cappuccino':
        inserted_money = float(input('Please insert $2.\n'))
        deduct_resources(cappuccino, inserted_money)
    
    prompt = user_input()
