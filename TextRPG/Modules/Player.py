class Player():
    ''' Player base class.'''
    def __init__(self, name="Degon", race="Elf", playerClass="Mage"):
        self.name = name
        self.race = race
        self.playerClass = playerClass
        self.health = 100
        self.mapPosition = [1, 1]
        self.currentMap = [0, "Forest of Algor"]
        self.inventory = {
            "gold": 10,
            "potion": 10
            }

    def __del__(self):
        print(self.name, "has died!\n")

    def description(self):
        print("\nName:", self.name)
        print("Race:", self.race)
        print("Player Class:", self.playerClass)
        print("Health:", self.health)
        print("Map Position:", self.mapPosition)
        print("Current Map:", self.currentMap)
        print("Inventory:", self.inventory)

    def reduceHealth(self, amount):
        self.health = self.health - amount

    def increaseHealth(self, amount):
        self.health = self.health + amount

    def setPosition(self, x, y):
        self.mapPosition = [x, y]

    def printCurrentMap(self, mapList):
        mapIndex, mapName = self.currentMap
        print("\n###############################")
        print("# " + mapName + "            #")
        print("###############################")
        for row in range(len(mapList[mapIndex].baseMap)):
            print(mapList[mapIndex].baseMap[row])

    def changeMap(self, mapToGoName):
        self.currentMap = mapToGoName

    def moveNorth(self, currentMap):
        ''' Move north unless a 1(wall) is encountered. '''
        x = self.mapPosition[0]
        y = self.mapPosition[1]
        
        if currentMap[x - 1][y] != 1:
            self.mapPosition[0] -= 1
            print("You take a step north...")
            return True
        else:
            print("Sorry, a wall is in the way!")
            return False

    def moveSouth(self, currentMap):
        ''' Move south unless a 1(wall) is encountered. '''
        x = self.mapPosition[0]
        y = self.mapPosition[1]

        if currentMap[x + 1][y] != 1:
            self.mapPosition[0] += 1
            print("You take a step south...")
            return True
        else:
            print("Sorry, a wall is in the way")
            return False

    def moveEast(self, currentMap):
        ''' Move east unless a 1(wall) is encountered. '''
        x = self.mapPosition[0]
        y = self.mapPosition[1]

        if currentMap[x][y + 1] != 1:
            self.mapPosition[1] += 1
            print("You take a step east...")
            return True
        else:
            print("Sorry, a wall is in the way")
            return False

    def moveWest(self, currentMap):
        ''' Move west unless a 1(wall) is encountered. '''
        x = self.mapPosition[0]
        y = self.mapPosition[1]

        if currentMap[x][y - 1] != 1:
            self.mapPosition[1] -= 1
            print("You take a step west...")
            return True
        else:
            print("Sorry, a wall is in the way")
            return False

    def addToInv(self, item, amount):
        if item in self.inventory:
            self.inventory[item] += amount
        else:
            self.inventory[item] = amount

    def removeFromInv(self, item, amount):
        try:
            if item in self.inventory:
                if (self.inventory[item] - amount) < 0:
                    raise
                else:
                    self.inventory[item] -= amount
            else:
                print("Item does not exist!")
        except:
            print("Not enough of item to do this!")

        if self.inventory[item] == 0:
            del self.inventory[item]
