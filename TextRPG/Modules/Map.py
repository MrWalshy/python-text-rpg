class MapTile():
    ''' Base map tile class. Creates a tile of tiles.
        Arg 'name' takes a string
        Arg 'currentPlayerPosition' takes a list of a single coord set
        Arg 'mapConnections' takes a dict of 'map_name': [coords_on_map]
    '''
    def __init__(self, name, currentPlayerPosition, mapConnections):
        self.name = name
        self.baseMap = [[1, 1, 1, 1, 1, 1, 1, 1],
                        [1, 0, 0, 0, 0, 0, 9, 1],
                        [1, 0, 0, 0, 0, 0, 0, 1],
                        [0, 0, 0, 0, 0, 0, 0, 0],
                        [1, 0, 0, 1, 1, 1, 0, 1],
                        [1, 0, 0, 1, 0, 1, 0, 1],
                        [1, 0, 0, 0, 0, 1, 0, 1],
                        [1, 1, 1, 1, 1, 1, 1, 1]]
        self.mapConnections = mapConnections
        self.playerPosition = currentPlayerPosition # None if not not on this map
        self.events = {}

    def printMap(self):
        ''' Iterates over rows in the map, printing each row. '''
        for row in range(len(self.baseMap)):
            print(self.baseMap[row])

    def printConnectedMaps(self):
        ''' Prints maps connected to the current map. '''
        for key, value in self.mapConnections.items():
            print(key, "=", value)

    def modifyMap(self, row, column, value):
        ''' Takes a row and column to select the element to be modified.
            Takes a value to change the selected element to.
        '''
        self.baseMap[row][column] = value

    def printEvents(self):
        try:
            for key, value in self.events.items():
                print(key + " is at " + str(value[1][0]) + "," + str(value[1][1]), end="\n")
                print("- " + value[0])
        except:
            print("No events found!")

    def addEvent(self, eventName, eventDescription, eventCoords):
        self.events[eventName] = [eventDescription, eventCoords]

    def removeEvent(self, eventName):
        self.events.pop(eventName)
        
        
