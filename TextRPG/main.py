# Text RPG
import time
import csv
from Modules.Player import Player
from Modules.Map import MapTile
from Modules.menuFunctions import *

# Functions
def playerCreation():
    '''Function handles creation of the player, returning player selected
       options. The methods of choosing race & class are very similar, I should
       make a function that can handle both.
    '''
    name = race = playerClass = ""
    races = ["Orc", "Elf", "Goblin", "Human"]
    classes = ["Warrior", "Archer", "Mage"]

    ## Welcome and choose name ##
    print("\n###############################")
    print("# Welcome to Bretok!          #")
    print("###############################")
    name = input("What is your name traveller? ")
    print("A soldiers name, yes! You,", name, "will save us from the darkness!\n")

    ## Choose race ##
    exitRace = False
    print("What race would you like to be?")
    # Prints list of races to choose from
    for race in range(len(races)):
        print("|", race, "|", races[race], end="\n")
    # Conditional check to ensure race entered is int in range of races
    while exitRace == False:
        try:
            race = input()
            race = int(race)
            
            exitRace = True
        except:
            print("Please select a valid race using the number!")

    ## Choose class ##
    exitClass = False
    print("What class would you like to be?")
    # Print list of classes
    for playerClass in range(len(classes)):
        classString = "| {} | {}".format(playerClass, classes[playerClass])
        print(classString, end="\n")
        
    # Conditional loop, check if input is int & in range of classes
    while exitClass == False:
        try:
            playerClass = input()
            playerClass = int(playerClass)

            exitClass = True
        except:
            print("Please select a valid race using the number!")

    return (name, races[race], classes[playerClass])

def checkForEvent(currentMap, playerPosition):
    for event, values in currentMap.events.items():
            if values[1] == playerPosition:
                with open('events.txt', 'r') as csv_file:
                    csvReader = csv.reader(csv_file, delimiter=',')
                    lineCount = 0

                    for row in csvReader:
                        try:
                            if lineCount == 0:
                                lineCount += 1
                                continue
                            elif row[0] == event:
                                return row
                        except:
                            pass
    return False

def gameloop():
    ''' Does what it says on the tin, ensures the wheels keep turning, yada yada...
        Keeps the game running until an exit condition is met.
    '''
    exitGameLoop = False
    userInput = ""
    mapList = []

    # Create the player - Players state is held as long as the gameloop() func runs
    playerCredentials = playerCreation()
    player = Player(*playerCredentials)
    player.description()

    # Create the map
    algorForest = MapTile("Forest of Algor", player.mapPosition, {"Dalor Bay": [3, 7]})
    algorForest.addEvent("welcome", "One time event to welcome player", [1, 1])
    algorForest.addEvent("gold20","Free gold for new player",[1, 2])

    dalorBay = MapTile("Dalor Bay", player.mapPosition, {"Forest of Algor": [3, 0]})

    # Create list of maps
    mapList.append(algorForest)
    mapList.append(dalorBay)

    # Enter loop
    while not(exitGameLoop):
        # Get user position on map, then update the map
        playerPosition = player.mapPosition
        player.printCurrentMap(mapList)
        print("You are currently at location:", playerPosition)
        currentMap = mapList[player.currentMap[0]]

        # Tell user what they can see, if event is found at current position.
        # Run the event, get event values from a file
        event = checkForEvent(currentMap, playerPosition)
        if event:
##            print(event)
            pass

        # Get user input on what to do next
        userInput = input("--> ")
        # Execute input
        if userInput == "north":
            if player.moveNorth(currentMap.baseMap):
                currentMap.playerPosition = player.mapPosition
        elif userInput == "south":
            if player.moveSouth(currentMap.baseMap):
                currentMap.playerPosition = player.mapPosition
        elif userInput == "east":
            if player.moveEast(currentMap.baseMap):
                currentMap.playerPosition = player.mapPosition
        elif userInput == "west":
            if player.moveWest(currentMap.baseMap):
                currentMap.playerPosition = player.mapPosition
        playerPosition = player.mapPosition

        # Change map if on connecting tile
        for connectingMapName, coords in currentMap.mapConnections.items():
            if playerPosition == coords:
                if connectingMapName == "Dalor Bay":
                    print(connectingMapName, coords)
                    player.changeMap(1, connectingMapName)
                    player.mapPosition = [3, 0]
                elif connectingMapName == "Forest of Algor":
                    player.changeMap(0, connectingMapName)
                    player.mapPosition = [3, 7]
                

        time.sleep(0)
            

### GAME START ###
# Create the menu - pass in menu items
menuItems = ["Play", "Load", "Help", "Exit"]
menu = menuCreationSequence(menuItems)

# Start main loop - iterates over the menu
exitCondition = False

while exitCondition == False:
    printMenu(menu)
    if getAndExecuteMenuInput(gameloop):
        # If True is returned, the exit condition has been met
        exitCondition = True
