import time
from settings import setting
from pyglet.gl import *
frames = {}
renderOrderFrames = []
hold = 0 #When this is greater than 0 it means that either render or update are running
addedFrames = {} #Stores frames that are to be added after next update
removedFrames = [] #Frames to be removed after next update
animateOutFrames = []
animateInFrames = []
#Called FRAME_RATE times a frame, this will do several things
# - Update each frame
# - Run animations on each frame
def update():
    global hold,addedFrames,removedFrames
    hold += 1
    for i in frames:
        if frames[i].finished == 0:frames[i].update()
    for i in addedFrames:
        frames[i] = addedFrames[i]
        renderOrderFrames.append(frames[i])
    for frame in removedFrames:
        del frames[frame]
    removedFrames = []
    addedFrames = {}
    for i in animateInFrames:
        frames[i].position.x -= frames[i].position.x / 10.0
        if (frames[i].position.x <= 1):
            frames[i].position.x = 0
            animateInFrames.remove(i)
    for i in animateOutFrames:
        frames[i].position.x -= (frames[i].position.x + setting.SCREEN_WIDTH*2)/10.0
        if (frames[i].position.x <= 1+-setting.SCREEN_WIDTH*2):
            animateOutFrames.remove(i)
            del frames[i]
    hold -= 1
def render():
    global hold
    hold += 1
    for frame in renderOrderFrames:
        glPushMatrix()
        glTranslatef(frame.position.x,frame.position.y,0)
        frame.draw()
        glPopMatrix()
    hold -= 1
#Add a frame to the scene
def add(name,frame,animate=True):
    global addedFrames
    addedFrames[name] = frame
    if animate:
        global animateInFrames
        animateInFrames.append(name)
        frame.position.x = setting.SCREEN_WIDTH*2
#Remove a frame to the scene
def rem(name,animate=True):
    if (animate):
        global animateOutFrames
        animateOutFrames.append(name)
    else:
        global removedFrames
        removedFrames.append(name)