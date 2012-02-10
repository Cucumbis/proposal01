from pyglet.window import key
keys = {}
def getKey(k):
    if (keys.has_key(k)):
        return keys[k]
    return 0
def init():
    pass