import math

def float_equal(f1, f2):
        epsilon = 0.000001   
        return abs(f1-f2) < epsilon

class Tuple:
    def __init__(self, x,y,z,w):
        self.x = x
        self.y = y
        self.z = z
        self.w = w

    def __str__(self):
        return "({}, {}, {}, {})".format(self.x, self.y, self.z, self.w)
    
    def __eq__(tup1, tup2):
        return float_equal(tup1.x, tup2.x) and \
                float_equal(tup1.y, tup2.y) and \
                float_equal(tup1.z, tup2.z) and \
                float_equal(tup1.w, tup2.w)
    
    def __add__(self, tup2):
        new_tup = Tuple(self.x, self.y, self.z, self.w)
        if not(new_tup.w == 1 and tup2.w == 1):
            new_tup.x += tup2.x
            new_tup.y += tup2.y
            new_tup.z += tup2.z
            new_tup.w += tup2.w
        
        return new_tup
    
    def __sub__(self, tup2):
        new_tup = Tuple(self.x, self.y, self.z, self.w)
        if not(new_tup.w == 0.0 and tup2.w == 1):
            new_tup.x = new_tup.x - tup2.x
            new_tup.y = new_tup.y - tup2.y
            new_tup.z = new_tup.z - tup2.z
            new_tup.w = new_tup.w - tup2.w

        return new_tup
    
    def __neg__(self):
        return Tuple(-self.x, -self.y, -self.z, -self.w)
    
    def __mul__(self, scalar):
        return Tuple(scalar*self.x, scalar*self.y, scalar*self.z, scalar*self.w)
    
    def __truediv__(self, scalar):
        return Tuple(self.x/scalar, self.y/scalar, self.z/scalar, self.w/scalar)
    
    
        
    
class Point(Tuple):
    def __init__(self,x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.w = 1.0

class Vector(Tuple):
    def __init__(self,x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.w = 0.0

    def magnitude(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2 + self.w**2)
    
    def normalize(self):
        mag = self.magnitude()
        return Vector(self.x/mag, self.y/mag, self.z/mag)
    
    def dot(self, b):
        return (self.x*b.x + self.y*b.y + self.z*b.z + self.w*b.w)
    
    def cross(self, b):
        x = self.y*b.z - self.z*b.y
        y = self.z*b.x - self.x*b.z
        z = self.x*b.y - self.y*b.x
        return Vector(x,y,z)
