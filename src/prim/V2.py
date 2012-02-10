#Basically a point
#TODO functions such as add, dot, addSelf, sub, distance etc.
class V2():
    def __init__(self,x=0,y=0):
        self.set(x,y)
    def set(self,x,y):
        self.x = x
        self.y = y