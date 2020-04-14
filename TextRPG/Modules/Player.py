# Classes
class Player():
    ''' Player base class. Move this to its own module.'''
    def __init__(self, name="Degon", race="Elf", playerClass="Mage"):
        self.name = name
        self.race = race
        self.playerClass = playerClass
        self.health = 100
        self.mapPosition = [0, 0]

    def description(self):
        print("\nName:", self.name)
        print("Race:", self.race)
        print("Player Class:", self.playerClass)
        print("Health:", self.health)
        print("Map Position:", self.mapPosition)

    def __del__(self):
        print(self.name, "has died!\n")

    def reduceHealth(self, amount):
        self.health = self.health - amount

    def increaseHealth(self, amount):
        self.health = self.health + amount
