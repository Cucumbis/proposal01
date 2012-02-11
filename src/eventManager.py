from pyglet.window import key
from prim.V2 import *
keys = {}
class Mouse():
    def __init__(self):
        self.down = 0
        self.rightDown = 0
        self.middleDown = 0
        self.position = V2()
        self.relative = V2()
class Event():
    def __init__(self,ty,value=1):
        self.type = ty
        self.value = value
mouse = Mouse()
lastEvents = []
def getKey(k):
    if (keys.has_key(k)):
        return keys[k]
    return 0
def init():
    pass