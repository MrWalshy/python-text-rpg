class MapTile():
    ''' Base map tile class.
        Arg 'name' takes a string
        Arg 'currentPlayerPosition' takes a list of a single coord set
        Arg 'mapConnections' takes a dict of 'map_name': [coords_on_map]
    '''
    def __init__(self, name, currentPlayerPosition, mapConnections):
        self.name = name
        self.baseMap = [[1, 1, 1, 1, 1, 1, 1, 1],
                        [1, 0, 0, 0, 0, 0, 9, 1],
                        [1, 0, 0, 0, 0, 0, 0, 1],
                        [1, 0, 0, 0, 0, 0, 0, 1],
                        [1, 0, 0, 0, 0, 0, 0, 1],
                        [1, 0, 9, 0, 0, 0, 0, 1],
                        [1, 0, 0, 0, 0, 9, 0, 1],
                        [1, 1, 1, 1, 1, 1, 1, 1]]
        self.mapConnections = mapConnections
        self.playerPosition = currentPlayerPosition # None if not not on this map

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
        
        
