from coffee_machine import Coffee_Machine
from main_functions import user_input
from coffee_types import Cappuccino, Espresso, Latte

coffee_machine = Coffee_Machine()
espresso = Espresso()
cappuccino = Cappuccino()
latte = Latte()
    
def deduct_resources(coffee_type):
    coffee_type_costs = coffee_type.give_costs()
    for i in range(coffee_machine.resources.__len__()):
        if i < (coffee_machine.resources.__len__() - 1):
            coffee_machine.resources[i] = coffee_machine.resources[i] - coffee_type_costs[i]
            continue
        coffee_machine.resources[i] = coffee_machine.resources[i] + coffee_type_costs[i]

prompt = user_input()
while prompt != 'off':
    if prompt == 'report':
        for item in coffee_machine.resources:
            print(item)
    elif prompt == 'espresso':
        deduct_resources(espresso)
    elif prompt =='latte':
        deduct_resources(latte)
    elif prompt == 'cappuccino':
        deduct_resources(cappuccino)
    
    prompt = user_input()
