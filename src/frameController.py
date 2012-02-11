import time
frames = {}
hold = 0 #When this is greater than 0 it means that either render or update are running
addedFrames = {} #Stores frames that are to be added after next update
removedFrames = [] #Frames to be removed after next update
def update():
    global hold,addedFrames,removedFrames
    hold += 1
    for i in frames:
        frames[i].update()
    for i in addedFrames:
        frames[i] = addedFrames[i]
    for frame in removedFrames:
        del frames[frame]
    removedFrames = []
    addedFrames = {}
    hold -= 1
def render():
    global hold
    hold += 1
    for i in frames:
        frames[i].draw()
    hold -= 1
def add(name,frame):
    global addedFrames
    addedFrames[name] = frame
def rem(name):
    global removedFrames
    removedFrames.append(name)