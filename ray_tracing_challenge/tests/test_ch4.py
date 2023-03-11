from unittest import TestCase
from ray_tracing_challenge import *
import math

class TestTransformations(TestCase):
    def test_translation(self):
        transform = Transformation().translate(5,-3,2)
        p = Point(-3, 4, 5)
        self.assertTrue(transform * p == Point(2,1,7))

        inv = transform.inverse()
        self.assertTrue(inv * p == Point(-8,7,3))

        vec = Vector(-3, 4, 5)
        self.assertTrue(transform * vec == vec)
    
    def test_scaling(self):
        transform = Transformation().scale(2, 3, 4)
        p = Point(-4, 6, 8)
        self.assertTrue(transform * p == Point(-8, 18, 32))

        v = Vector(-4, 6, 8)
        self.assertTrue(transform * v == Vector(-8, 18, 32))

        inv = transform.inverse()
        self.assertTrue(inv * v == Vector(-2, 2, 2))

    def test_reflection(self):
        transform = Transformation().scale(-1,1,1)
        p = Point(2,3,4)
        self.assertTrue(transform * p == Point(-2,3,4))

    def test_rotate_x(self):
        p = Point(0,1,0)
        half_quarter = Transformation().rotate_x(math.pi/4)
        full_quarter = Transformation().rotate_x(math.pi/2)
        self.assertTrue(half_quarter * p == Point(0,math.sqrt(2)/2, math.sqrt(2)/2))
        self.assertTrue(full_quarter * p == Point(0,0,1))

    def test_inverse_rotate(self):
        p = Point(0,1,0)
        half_quarter = Transformation().rotate_x(math.pi/4)
        inv = half_quarter.inverse()
        self.assertTrue(inv * p == Point(0,math.sqrt(2)/2, -math.sqrt(2)/2))

    def test_rotate_y(self):
        p = Point(0,0,1)
        half_quarter = Transformation().rotate_y(math.pi/4)
        full_quarter = Transformation().rotate_y(math.pi/2)
        self.assertTrue(half_quarter * p == Point(math.sqrt(2)/2, 0, math.sqrt(2)/2))
        self.assertTrue(full_quarter * p == Point(1,0,0))

    def test_rotate_z(self):
        p = Point(0,1,0)
        half_quarter = Transformation().rotate_z(math.pi/4)
        full_quarter = Transformation().rotate_z(math.pi/2)
        self.assertTrue(half_quarter * p == Point(-math.sqrt(2)/2, math.sqrt(2)/2, 0))
        self.assertTrue(full_quarter * p == Point(-1,0,0))

    def test_shearing(self):
        transform = Transformation().shearing(1,0,0,0,0,0)
        p = Point(2,3,4)
        self.assertTrue(transform * p == Point(5,3,4))

        transform = Transformation().shearing(0,1,0,0,0,0)
        self.assertTrue(transform * p == Point(6,3,4))

        transform = Transformation().shearing(0,0,1,0,0,0)
        self.assertTrue(transform * p == Point(2,5,4))

        transform = Transformation().shearing(0,0,0,1,0,0)
        self.assertTrue(transform * p == Point(2,7,4))

        transform = Transformation().shearing(0,0,0,0,1,0)
        self.assertTrue(transform * p == Point(2,3,6))

        transform = Transformation().shearing(0,0,0,0,0,1)
        self.assertTrue(transform * p == Point(2,3,7))

    def test_chain_individual(self):
        p = Point(1,0,1)
        A = Transformation().rotate_x(math.pi/2)
        B = Transformation().scale(5,5,5)
        C = Transformation().translate(10,5,7)
        p2 = A*p
        self.assertTrue(p2 == Point(1,-1,0))

        p3 = B*p2
        self.assertTrue(p3 == Point(5,-5,0))

        p4 = C*p3
        self.assertTrue(p4 == Point(15,0,7))

    def test_chain_reverse(self):
        p = Point(1,0,1)
        A = Transformation().rotate_x(math.pi/2)
        B = Transformation().scale(5,5,5)
        C = Transformation().translate(10,5,7)
        T = C * B * A
        self.assertTrue(T*p == Point(15,0,7))

    