class Coffee_Machine():
    def __init__(self):
        self.water = 1000
        self.milk = 2000
        self.coffee = 1000
        self.money = 100
        self.give_resources()

    def give_resources(self):
        self.resources = [self.water, self.milk, self.coffee, self.money]
        return self.resources
    