from unittest import TestCase
from ray_tracing_challenge import *
import math

class TestRays(TestCase):
    def test_ray_constructor(self):
        origin = Point(1,2,3)
        direction = Vector(4,5,6)
        r = Ray(origin, direction)
        self.assertTrue(r.origin == origin)
        self.assertTrue(r.direction == direction)

    def test_ray_distance(self): 
        r = Ray(Point(2,3,4), Vector(1,0,0))
        self.assertTrue(r.position(0) == Point(2,3,4))
        self.assertTrue(r.position(1) == Point(3,3,4))
        self.assertTrue(r.position(-1) == Point(1,3,4))
        self.assertTrue(r.position(2.5) == Point(4.5,3,4))

    def test_ray_hits_twice(self):
        r = Ray(Point(0,0,-5), Vector(0,0,1))
        s = Sphere(Point(0,0,0), 1)
        xs = r.intersects(s)
        self.assertEqual(xs.count, 2)
        self.assertEqual(xs[0], 4.0)
        self.assertEqual(xs[1], 6.0)

    def test_ray_tangent(self):
        r = Ray(Point(0,1,-5), Vector(0,0,1))
        s = Sphere(Point(0,0,0), 1)
        xs = r.intersects(s)
        self.assertEqual(xs.count, 2)
        self.assertEqual(xs[0], 5.0)
        self.assertEqual(xs[1], 5.0)

    def test_ray_miss(self):
        r = Ray(Point(0,2,-5), Vector(0,0,1))
        s = Sphere(Point(0,0,0), 1)
        xs = r.intersects(s)
        self.assertEqual(xs.count, 0)

    def test_ray_inside(self):
        r = Ray(Point(0,0,0), Vector(0,0,1))
        s = Sphere(Point(0,0,0), 1)
        xs = r.intersects(s)
        self.assertEqual(xs.count, 2)
        self.assertEqual(xs[0], -1.0)
        self.assertEqual(xs[1], 1.0)

    def test_object_behind_ray(self):
        r = Ray(Point(0,0,5), Vector(0,0,1))
        s = Sphere(Point(0,0,0), 1)
        xs = r.intersects(s)
        self.assertEqual(xs.count, 2)
        self.assertEqual(xs[0], -6.0)
        self.assertEqual(xs[1], -4.0)

    def test_intersection_constructor(self):
        s = Sphere(Point(0,0,0), 1)
        i = Intersection(3.5, s)
        self.assertEqual(i.t , 3.5)
        self.assertTrue(i.object == s)
        
    def test_intersectionlist(self):
        s = Sphere(Point(0,0,0), 1)
        i1 = Intersection(1, s)
        i2 = Intersection(2,s)
        xs = IntersectionList(i1, i2)
        self.assertEqual(xs.count, 2)
        self.assertEqual(xs[0].t , 1)
        self.assertEqual(xs[1].t , 2)

    def test_intersection_sets_object(self):
        r = Ray(Point(0,0,-5), Vector(0,0,1))
        s = Sphere(Point(0,0,0), 1)
        xs = r.intersects(s)
        self.assertEqual(xs.count, 2)
        self.assertTrue(xs[0].object == s)
        self.assertTrue(xs[1].object == s)

    def test_hit_positive(self):
        s = Sphere(Point(0,0,0), 1)
        i1 = Intersection(1, s)
        i2 = Intersection(2,s)
        xs = IntersectionList(i1, i2)
        i = xs.hit()
        self.assertTrue(i == i1)

    def test_hit_some_positive(self):
        s = Sphere(Point(0,0,0), 1)
        i1 = Intersection(-1, s)
        i2 = Intersection(2,s)
        xs = IntersectionList(i1, i2)
        i = xs.hit()
        self.assertTrue(i == i2)

    def test_hit_negative(self):
        s = Sphere(Point(0,0,0), 1)
        i1 = Intersection(-2, s)
        i2 = Intersection(-1,s)
        xs = IntersectionList(i1, i2)
        i = xs.hit()
        self.assertTrue(i is None)

    def test_hit_lowest(self):
        s = Sphere(Point(0,0,0), 1)
        i1 = Intersection(5, s)
        i2 = Intersection(7,s)
        i3 = Intersection(-3, s)
        i4 = Intersection(2,s)
        xs = IntersectionList(i1, i2, i3, i4)
        i = xs.hit()
        self.assertTrue(i == i4)

    def test_ray_translation(self): 
        r = Ray(Point(1,2,3), Vector(0,1,0))
        m = Transformation().translate(3,4,5)
        r2 = r.transform(m)
        self.assertTrue(r2.origin == Point(4,6,8))
        self.assertTrue(r2.direction == Vector(0,1,0))
        
    def test_ray_scaling(self): 
        r = Ray(Point(1,2,3), Vector(0,1,0))
        m = Transformation().scale(2,3,4)
        r2 = r.transform(m)
        self.assertTrue(r2.origin == Point(2,6,12))
        self.assertTrue(r2.direction == Vector(0,3,0))

    def test_sphere_default_transform(self):
        s = Sphere(Point(0,0,0), 1)
        self.assertTrue(s.transform == IdentityMatrix(4))

    def test_sphere_change_transform(self):
        s = Sphere(Point(0,0,0), 1)
        t = Transformation().translate(2,3,4)
        s.set_transform(t)
        self.assertTrue(s.transform == t)

    def test_intersection_sphere_translated(self):
        r = Ray(Point(1,2,3), Vector(0,1,0))
        s = Sphere(Point(0,0,0), 1)
        s.set_transform(Transformation().translate(5,0,0))
        xs = r.intersects(s)
        self.assertEqual(xs.count, 0)

    def test_intersection_sphere_scaled(self):
        r = Ray(Point(0,0,-5), Vector(0,0,1))
        s = Sphere(Point(0,0,0), 1)
        s.set_transform(Transformation().scale(2,2,2))
        xs = r.intersects(s)
        self.assertEqual(xs.count, 2)
        self.assertEqual(xs[0].t, 3)
        self.assertEqual(xs[1].t, 7)








