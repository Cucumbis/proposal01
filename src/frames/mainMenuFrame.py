from settings import constants
from settings import setting
import eventManager
import assets
import frames
import frameController
from game.frame import *
from game.gameData import *

from pyglet.sprite import Sprite

#ATM this is not well documented, the reason being it will most
#likely be changed and made more relevant to the game
class MainMenuFrame(frames.basicFrame):
    def __init__(self):
        frames.basicFrame.__init__(self)        
        
        self.background = Sprite(assets.mainMenuBackground,0,0)
        self.background.scale = float(setting.SCREEN_HEIGHT) / self.background.height
        self.playButton = Sprite(assets.mainMenuPlay,0,0)
        self.optionsButton = Sprite(assets.mainMenuOptions,0,0)
        self.playButton.scale = self.optionsButton.scale = self.background.scale
        self.optionsButton.tx = self.optionsButton.x = self.playButton.x = self.playButton.tx = 1385 * self.playButton.scale
        self.playButton.ty = 520 * self.playButton.scale
        self.playButton.y = self.playButton.ty + 2000
        self.optionsButton.ty = 300 * self.optionsButton.scale
        self.optionsButton.y = self.optionsButton.y + 1000
    def update(self):
        self.playButton.x += (self.playButton.tx - self.playButton.x)/10
        if (abs(self.playButton.x - eventManager.mouse.position.x)<self.playButton.width/2):
            self.playButton.y += (self.playButton.ty + (self.playButton.ty - eventManager.mouse.position.y)**3/80000.0 - self.playButton.y)/10
            self.optionsButton.y += (self.optionsButton.ty + (self.optionsButton.ty - eventManager.mouse.position.y)**3/80000.0 - self.optionsButton.y)/10
        else:
            self.playButton.y += (self.playButton.ty - self.playButton.y)/10
            self.optionsButton.y += (self.optionsButton.ty - self.optionsButton.y)/10
        self.optionsButton.x += (self.optionsButton.tx - self.optionsButton.x)/10
        #check if play button pressed
        for event in eventManager.lastEvents:
            if (event.type == "mousedown" and event.value == 0):
                if (eventManager.mouse.position.withinRect(self.playButton,self.playButton.width,self.playButton.height)):
                    frameController.add("game",GameFrame(GameData()))
                    frameController.rem("main")
    def draw(self):
        self.background.draw()
        self.playButton.draw()
        self.optionsButton.draw()