import pyglet
from settings.constants import *

mainMenuBackground = None
mainMenuPlay = None
mainMenuOptions = None
tiles = None    # tiles is a multi-dimensional array once loaded with getImages
def getImages(source):
    global tiles,mainMenuBackground,mainMenuPlay,mainMenuOptions
    tiles = []
    tileImage = getImage(source + "/tiles.png")#load tiles.png
    for xp in range(tileImage.width/TILE_SIZE):
        tiles.append([])
        for yp in range(tileImage.height/TILE_SIZE):
            #Seperate each tile from the tile spreadsheet,
            tiles[xp].append(tileImage.get_region(xp * TILE_SIZE,yp * TILE_SIZE, TILE_SIZE,TILE_SIZE))
    mainMenuBackground = getImage(source + "/mainMenuBackground.png")
    mainMenuPlay = getImage(source + "/mainMenuPlay.png",True)
    mainMenuOptions = getImage(source + "/mainMenuOptions.png",True)
def getImage(path,center=False):
    if (center):
        img = pyglet.image.load(path)
        img.anchor_x = img.width/2
        img.anchor_y = img.height/2
        return img
    else:
        return pyglet.image.load(path)