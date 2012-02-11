from prim.V2 import *
from frames import *

from pyglet.sprite import *
from pyglet.graphics import *
from pyglet.gl import *

from settings.constants import *
from settings import setting

from eventManager import *
import assets

def isoDat(x,y):#Convert x,y coordinates to isometric coordinates
    x/=2;y/=2
    return V2(x*RAD2 - y*RAD2, y * RAD2 + x*RAD2)
class GameFrame(basicFrame):
    def __init__(self,gameData):
        
        basicFrame.__init__(self)          
        
        #The camera is basically a screen translation
        self.camera = V2()
        
        #Batches are used to draw many sprites at once, it's faster than calling
        #draw() on tiles individually
        self.tileBatch = Batch()
        self.tiles = []
        for xp in range(gameData.mapSizeX):
            self.tiles.append([])
            for yp in range(gameData.mapSizeY):
                iso = isoDat(xp*TILE_SIZE,yp*TILE_SIZE)
                tile = Sprite(gameData.getTileImageAt(xp,yp),iso.x,iso.y,batch=self.tileBatch)
                tile.rotation = 45
                self.tiles.append(tile)
        
    def update(self):
        self.camera.x += (getKey(key.A) - getKey(key.D))*setting.CAMERA_SPEED
        self.camera.y += (getKey(key.S) - getKey(key.W))*setting.CAMERA_SPEED
    def draw(self):
        glPushMatrix()
        glTranslatef(self.camera.x,self.camera.y,0)
        self.tileBatch.draw() #Draw all tiles at once
        glPopMatrix()