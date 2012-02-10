import pyglet
from settings.constants import *

tiles = None    # tiles is a multi-dimensional array once loaded with getImages
def getImages(source):
    global tiles
    tiles = []
    tileImage = getImage(source + "/tiles.png")#load tiles.png
    for xp in range(tileImage.width/TILE_SIZE):
        tiles.append([])
        for yp in range(tileImage.height/TILE_SIZE):
            #Seperate each tile from the tile spreadsheet,
            tiles[xp].append(tileImage.get_region(xp * TILE_SIZE,yp * TILE_SIZE, TILE_SIZE,TILE_SIZE))
def getImage(path):
    return pyglet.image.load(path)