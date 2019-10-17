class Item:
    def __init__(self, name: str, cost: str, nutrition: int):
        self.name = name
        self.cost = cost
        self.nutrition = nutrition


class Dog: 
    def __init__(self, breed: str, name: str, happiness: int):
        self.breed = breed
        self.name = name
        self.happiness = happiness

    def __str__(self):
        