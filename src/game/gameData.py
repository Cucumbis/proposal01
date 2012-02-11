import assets
class GameData():
    def __init__(self):
        #This will normally be loaded from a file, for now
        #Default values will do
        self.mapSizeX = 32
        self.mapSizeY = 32
    def getTileImageAt(self,x,y):
        #This should normally be based on the actually data
        return assets.tiles[(x*7 + y)%2][(y*2 + x*13)%2]