import pyglet
from pyglet.gl import *
from pyglet.window import key

from settings import setting
import assets
from game.gameFrame import *
from game.gameData import *
import eventManager

#Create Window using user settings
window = pyglet.window.Window(width=setting.SCREEN_WIDTH,
                              height=setting.SCREEN_HEIGHT)

#Set some values to make the window render properly

#Allow alpha channel to be drawn (transparency)
glEnable(GL_BLEND)
glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)


#This will load the texture pack
assets.getImages(setting.TEXTURE_PACK)

#Each part of the game has a frame, it's self contained.
#There should only be one frame on screen EXCEPT when transitioning
#from say the main menu to the level selection
#Frames invoke other frames
frames = {}

@window.event
def on_draw():
    window.clear()
    #draw each frame
    for frame in frames:
        frames[frame].draw()

#Initialize eventManager
eventManager.init()

@window.event
def on_key_press(symbol,mod):
	eventManager.keys[symbol] = 1
@window.event
def on_key_release(symbol,mod):
	eventManager.keys[symbol] = 0

#this executes FRAME_RATE times a second, it updates all the frames
#TODO before calling update, call another function and pass a list full of 
#events (<key> down) then clear it after, this way it can act on one-time events
def update(dt):
    for frame in frames:
        frames[frame].update()
pyglet.clock.schedule_interval(update, setting.FRAME_RATE)


#For testing the game only, we'll set the "game" frame
frames["game"] = gameFrame(gameData())

pyglet.app.run()