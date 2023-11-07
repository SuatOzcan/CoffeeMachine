from coffee_machine import Coffee_Machine
from main_functions import user_input, deduct_resources
from coffee_types import Cappuccino, Espresso, Latte

coffee_machine = Coffee_Machine()
espresso = Espresso()
cappuccino = Cappuccino()
latte = Latte()
    
prompt = user_input()
while prompt != 'off':
    if prompt == 'report':
            print(f'Water: {coffee_machine.resources[0]}ml\nMilk: {coffee_machine.resources[1]}ml\nCoffee: {coffee_machine.resources[2]}g\nMoney: ${coffee_machine.resources[3]}')          
    elif prompt == 'espresso':
        inserted_money = float(input('Please insert $4.\n'))
        deduct_resources(coffee_machine, espresso, inserted_money)
    elif prompt =='latte':
        inserted_money = float(input('Please insert $5.\n'))
        deduct_resources(coffee_machine,latte, inserted_money)
    elif prompt == 'cappuccino':
        inserted_money = float(input('Please insert $2.\n'))
        deduct_resources(coffee_machine, cappuccino, inserted_money)
    
    prompt = user_input()
