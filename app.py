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
    
    if prompt in [espresso.name, latte.name, cappuccino.name]:
        for coffee in [espresso.name, latte.name, cappuccino.name]:
            if prompt == coffee:
                coffee_kinds = {'espresso': espresso,'latte': latte,'cappuccino':cappuccino}
                coffee_type = coffee_kinds[prompt]
                break
        inserted_money = float(input(f'Please insert ${coffee_type.price}.\n'))
        deduct_resources(coffee_machine,coffee_type, inserted_money)

    prompt = user_input()
