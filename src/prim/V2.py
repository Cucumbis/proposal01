#Basically a point
#TODO functions such as add, dot, addSelf, sub, distance etc.
import math
class V2():
    def __init__(self,x=0,y=0):
        self.set(x,y)
    def set(self,x,y):
        self.x = x
        self.y = y
        return self
    def copy(self,v2):
        return self.set(v2.x,v2.y)
    def clone(self):
        return V2(self.x,self.y)
    def add(self,v20,v21):
        self.x = v20.x + v21.x
        self.y = v20.y + v21.y
    def addSelf(self,v2):
        self.x += v2.x
        self.y += v2.y
        return self
    def sub(self,v20,v21):
        self.x = v20.x - v21.x
        self.y = v20.y - v21.y
        return self
    def subSelf(self,v2):
        self.x -= v2.x
        self.y -= v2.y
        return self
    def multiplyScalar(self,s):
        self.x *= s
        self.y *= s
        return self
    def divideScalar(self,s):
        if (s):
            self.x /= s
            self.y /= s
        else:
            self.set(0,0)
        return self
    def negate(self):
        return self.multiplyScalar(-1)
    def normalize(self):
        return self.divideScalar(self.length())
    def dot(self,v2):
        return self.x * v2.x + self.y * v2.y
    def lengthSq(self):
        return self.x * self.x + self.y * self.y
    def length(self):
        return math.sqrt(self.lengthSq())
    def distanceTo(self,v2):
        return math.sqrt(self.distanceToSquared(v2))
    def distanceToSquared(self,v2):
        dx = self.x - v2.x
        dy = self.y - v2.y
        return dx * dx + dy * dy
    def setLength(self,l):
        return self.normalize().multiplyScalar(l)
    def equals(self,v2):
        return (self.x == v2.x and self.y == v2.y)
    def withinRect(self,v2,rectx,recty):
        return (abs(self.x - v2.x) < rectx/2 and abs(self.y - v2.y)<recty/2)
    