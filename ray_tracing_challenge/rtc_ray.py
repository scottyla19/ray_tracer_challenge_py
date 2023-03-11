from .rtc_tuple import *
from .rtc_matrix import *
from .rtc_shape import *

class Ray:
    def __init__(self, point, vector):
        self.origin = point
        self.direction = vector
        self.intersections = IntersectionList()

    def __str__(self):
        return "origin: {} direction: {}".format(self.origin, self.direction)

    def position(self, t):
        return self.origin + self.direction * t
    
    def intersects(self, object):
        # transform ray around object
        inv = object.transform.inverse()
        ray2 = self.transform(inv)

        object_to_ray = ray2.origin - object.origin
        a = ray2.direction.dot(ray2.direction)
        b = 2*ray2.direction.dot(object_to_ray)
        c = object_to_ray.dot(object_to_ray) -1

        discriminant = b**2 - 4*a*c
        if discriminant < 0:
            return ray2.intersections
        else:
            ray2.intersections.append(Intersection((-b - math.sqrt(discriminant)) / (2*a), object))
            ray2.intersections.append(Intersection((-b + math.sqrt(discriminant)) / (2*a), object))
            ray2.intersections.sort()
            return ray2.intersections
        
    def transform(self, t):
        new_origin = t * self.origin
        new_direction = t * self.direction
        return Ray(new_origin, new_direction)

class Intersection:
    def __init__(self, t, obj):
        self.t = t
        self.object = obj

    def __eq__(self, object):
        if isinstance(object, self.__class__):
            return self.t == object.t
        else:
            return self.t == object
        
    
    def __gt__(self, object):
        if isinstance(object, self.__class__):
            return self.t > object.t
        else:
            return self.t > object
    
    def __lt__(self, object):
        if isinstance(object, self.__class__):
            return self.t < object.t
        else:
            return self.t < object
    
    def __ge__(self, object):
        if isinstance(object, self.__class__):
            return self.t >= object.t
        else:
            return self.t >= object
    
    def __le__(self, object):
        if isinstance(object, self.__class__):
            return self.t <= object.t
        else:
            return self.t <= object
        

class IntersectionList:
    def __init__(self, *args):
        self.intersections = list(args)
        self.count = len(self.intersections)

    def append(self, intersection):
        self.intersections.append(intersection)
        self.count = len(self.intersections)

    def __getitem__(self, index):
        return self.intersections[index]
    
    def sort(self):
        self.intersections.sort()
        return self.intersections.sort()
    
    def hit(self):
        hit = [h for h in self.intersections if h.t > 0]
        hit.sort()
        if len(hit) > 0:
            return hit[0]
        else:
            return None