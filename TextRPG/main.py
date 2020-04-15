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
    currentPlayer = Player(*playerCredentials)
    currentPlayer.description()

    # Create the map
    algorForest = MapTile("Forest of Algor", currentPlayer.mapPosition, {"map2": [3, 6]})
    algorForest.addEvent("welcome", "One time event to welcome player", [1,1])
    algorForest.addEvent("gold20","Free gold for new player",[1,2])

    # Create list of maps
    mapList.append(algorForest)

    # Enter loop
    while not(exitGameLoop):
        # Get user position on map, then update the map
        playerPosition = currentPlayer.mapPosition
        currentPlayer.printCurrentMap(mapList)
        print("You are currently at location:", playerPosition)

        # Tell user what they can see, if event is found at current position.
        # Run the event, get event values from a file
        event = checkForEvent(algorForest, playerPosition)
        if event:
            print(event)

        # Get user input on what to do next
        userInput = input("--> ")

        if userInput == "north":
            if currentPlayer.moveNorth(algorForest.baseMap):
                algorForest.playerPosition = currentPlayer.mapPosition
        elif userInput == "south":
            if currentPlayer.moveSouth(algorForest.baseMap):
                algorForest.playerPosition = currentPlayer.mapPosition
        elif userInput == "east":
            if currentPlayer.moveEast(algorForest.baseMap):
                algorForest.playerPosition = currentPlayer.mapPosition
        elif userInput == "west":
            if currentPlayer.moveWest(algorForest.baseMap):
                algorForest.playerPosition = currentPlayer.mapPosition

        time.sleep(2)
            

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
