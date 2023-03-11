from .rtc_matrix import *
from .rtc_material import *

class Shape:
    count = 0
    def __init__(self, center = Point(0,0,0), t= IdentityMatrix(4), mat = Material()):
        Shape.count += 1
        self.id = Sphere.count
        self.origin = center
        self.transform = t
        self.material = mat


class Sphere(Shape):
    def __init__(self, center = Point(0,0,0), radius= 1 ):
        super().__init__(center)
        self.radius = radius
    
    def set_transform(self, t):
        self.transform = t

    def normal_at(self, world_point):
        t = self.transform.inverse()
        object_point = t * world_point
        object_normal = object_point - self.origin
        world_normal = t.transpose() * object_normal
        world_normal.w = 0
        return world_normal.normalize()