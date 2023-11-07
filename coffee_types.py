from coffee import Coffee

class Espresso(Coffee):
    def __init__(self):
        super().__init__()
        self.milk = 2
        self.coffee = 100
        self. price = 4
        self.name = 'espresso'
        self.give_costs()
        
    def give_costs(self):
        self.costs = [self.water, self.milk, self.coffee, self.price]
        return self.costs
    
class Latte(Coffee):
    def __init__(self):
        super().__init__()
        self.milk = 200
        self.coffee = 100
        self.price = 5
        self.name = 'latte'
        self.give_costs()

    def give_costs(self):
        self.costs = [self.water, self.milk, self.coffee,self.price]
        return self.costs

class Cappuccino(Coffee):
    def __init__(self):
        super().__init__()
        self.milk = 50
        self.coffee = 12
        self.price = 2
        self.name ='cappuccino'
        self.give_costs()

    def give_costs(self):
        self.costs = [self.water, self.milk, self.coffee, self.price]
        return self.costs
