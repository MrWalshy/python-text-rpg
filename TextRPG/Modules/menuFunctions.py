import time

def createMenu(*args):
    ''' Takes a tuple or list of menu items, returns a menu as a list.
        Also creates a commands list, unsure what to do with yet.
    '''
    menu = ["---------------------------"]
    commands = []
    line = ""

    # Check if a tuple was passed, convert to a list if so
    if isinstance(args, tuple):
        args = args[0]

        for item in range(len(args)):
            line = "|" + args[item] + "\t\t\t[" + args[item][0] + "]"
            menu.append(line)
            commands.append(args[item][0])
            #"|", args[item], "        [", args[item][0], "]", end="/n"
    else:
        for item in range(len(args)):
            line = "|" + args[item] + "\t\t\t[" + args[item][0] + "]"
            menu.append(line)
            commands.append(args[item][0])
    menu.append("---------------------------")

    return menu

def printMenu(menu):
    ''' Prints the menu, row by row from a list '''
    for row in range(len(menu)):
        print(menu[row])

def getAndExecuteMenuInput(gameloop):
    ''' Currently has to be programmed manually for menu interaction.
        Returns True if the exit condition is specified. gameloop function is
        passed in, making this a higher order function, and is passed for
        execution.
    '''
    userInput = ""

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
        return True
    else:
        print("Please enter a valid input!")

    return False

def menuCreationSequence(menuItems):
    ''' Creates a menu from the supplied list of items. '''
    menu = createMenu(menuItems)
    return menu
