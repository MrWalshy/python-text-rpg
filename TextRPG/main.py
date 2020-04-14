# Text RPG
import time
from Modules.Player import Player

# Functions
def printMenu():
    ''' Prints the menu '''
    print("-----------------------")
    print("|Play              [P]|")
    print("|Load              [L]|")
    print("|Help              [H]|")
    print("|Exit              [E]|")
    print("-----------------------")

        

def executeMenuInput():
    exitVar = False
    userInput = ""

    while not(exitVar):
        userInput = input("Menu Command: ")
        userInput = userInput.lower()

        if userInput == 'p':
            gameloop()
            pass
        elif userInput == 'h':
            pass
        elif userInput == 'e':
            print("Exiting...")
            time.sleep(3)
            exitVar = True
        else:
            print("Please enter a valid input!")

def menuSequence():
    printMenu()
    executeMenuInput()

def playerCreation():
    '''Function handles creation of the player, returning player selected
       options. The methods of choosing race & class are very similar, I should
       make a function that can handle both.
    '''
    name = race = playerClass = ""
    races = ["Orc", "Elf", "Goblin", "Human"]
    classes = ["Warrior", "Archer", "Mage"]

    ## Welcome and choose name ##
    print("Welcome to Bretok!\n")
    name = input("What is your name traveller?\n")
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

def gameloop():
    ''' Does what it says on the tin, ensures the wheels keep turning, yada yada...
        Keeps the game running until an exit condition is met.
    '''
    exitGameLoop = False
    userInput = ""

    # Create the player - Players state is held as long as the gameloop() func runs
    playerCredentials = playerCreation()
    currentPlayer = Player(*playerCredentials)
    currentPlayer.description()

    # Create the map

    # Enter loop
    while not(exitGameLoop):
        # Get user position on map
        exitGameLoop = True

        # Tell user what they can see

        # Get user input on what to do next

### GAME START ###
# Deploy the menu
menuSequence()
