import pyglet
from pyglet.gl import *
from pyglet.window import key

from settings import setting
import assets
import frames.mainMenuFrame
from game.frame import *
from game.gameData import *
import frameController
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

#Each part of the game has a frame, each is self contained.
#There should only be one frame on screen EXCEPT when transitioning
#from say the main menu to the level selection
#Frames invoke other frames
frameList = {}

@window.event
def on_draw():
    window.clear()
    frameController.render()

#Initialize eventManager
eventManager.init()

@window.event
def on_key_press(symbol,mod):
    eventManager.keys[symbol] = 1
    eventManager.lastEvents.append(eventManager.Event("keydown",symbol))
@window.event
def on_key_release(symbol,mod):
    eventManager.keys[symbol] = 0
    eventManager.lastEvents.append(eventManager.Event("keyup",symbol))
         
@window.event
def on_mouse_motion(x,y,dx,dy):
    eventManager.mouse.position.set(x,y)
    eventManager.mouse.relative.set(dx,dy)
@window.event
def on_mouse_press(x,y,button,modifiers):
    if (button == pyglet.window.mouse.LEFT):
        eventManager.mouse.down = 1
        eventManager.lastEvents.append(eventManager.Event("mousedown",0))
    elif (button == pyglet.window.mouse.RIGHT):
        eventManager.mouse.rightDown = 1
        eventManager.lastEvents.append(eventManager.Event("mousedown",1))
    else:
        eventManager.mouse.middleDown = 1
        eventManager.lastEvents.append(eventManager.Event("mousedown",2))
@window.event
def on_mouse_release(x,y,button,modifiers):
    if (button == pyglet.window.mouse.LEFT):
        eventManager.mouse.down = 0
        eventManager.lastEvents.append(eventManager.Event("mouseup",0))
    elif (button == pyglet.window.mouse.RIGHT):
        eventManager.mouse.rightDown = 0
        eventManager.lastEvents.append(eventManager.Event("mouseup",1))
    else:
        eventManager.mouse.middleDown = 0
        eventManager.lastEvents.append(eventManager.Event("mouseup",2))
#this executes FRAME_RATE times a second, it updates all the frames
#TODO before calling update, call another function and pass a list full of 
#events (<key> down) then clear it after, this way it can act on one-time events
def update(dt):
    frameController.update()
    eventManager.lastEvents = []
pyglet.clock.schedule_interval(update, setting.FRAME_RATE)

#Change this to test different frames
frameController.add("main",frames.mainMenuFrame.MainMenuFrame())

pyglet.app.run()