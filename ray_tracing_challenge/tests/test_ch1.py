from unittest import TestCase
import math
from ray_tracing_challenge import Tuple, Vector, Point, float_equal

class TestTuples(TestCase):
    def test_tuple_returns_point(self):
        tup = Tuple(4.3, -4.2, 3.1, 1.0)
        self.assertTrue(isinstance(tup, Tuple))
        self.assertAlmostEqual(tup.x, 4.3)
        self.assertAlmostEqual(tup.y, -4.2)
        self.assertAlmostEqual(tup.z, 3.1)
        self.assertAlmostEqual(tup.w, 1.0)
        
    def test_tuple_returns_vector(self):
        tup = Tuple(4.3, -4.2, 3.1, 0.0)
        self.assertTrue(isinstance(tup, Tuple))
        self.assertAlmostEqual(tup.x, 4.3)
        self.assertAlmostEqual(tup.y, -4.2)
        self.assertAlmostEqual(tup.z, 3.1)
        self.assertAlmostEqual(tup.w, 0.0)
    
    def test_point_returns_point(self):
        tup = Point(4.3, -4.2, 3.1)
        self.assertTrue(isinstance(tup, Point))
        self.assertAlmostEqual(tup.x, 4.3)
        self.assertAlmostEqual(tup.y, -4.2)
        self.assertAlmostEqual(tup.z, 3.1)
        self.assertAlmostEqual(tup.w, 1.0)

    def test_vector_returns_vector(self):
        tup = Vector(4.3, -4.2, 3.1)
        self.assertTrue(isinstance(tup, Vector))
        self.assertAlmostEqual(tup.x, 4.3)
        self.assertAlmostEqual(tup.y, -4.2)
        self.assertAlmostEqual(tup.z, 3.1)
        self.assertAlmostEqual(tup.w, 0.0)

    def test_tuples_equal(self):
        tup1 = Tuple(4.3, -4.2, 3.1, 0.0)
        tup2 = Tuple(4.3, -4.2, 3.1, 0.0)
        tup3 = Tuple(4.3, -4.5, 0.0, 1.0)
        self.assertTrue(tup1 == tup2)
        self.assertFalse(tup1 == tup3)

    def test_points_vectors_equal(self):
        pt1 = Point(4.3, -4.2, 3.1)
        pt2 = Point(4.3, -4.2, 3.1)
        pt3 = Point(4.3, -4.1, 3.7)
        vec1 = Vector(4.3, -4.5, 0.0)
        vec2 = Vector(4.3, -4.5, 0.0)
        vec3 = Vector(4.3, -4.4, 3.0)
        self.assertTrue(pt1 == pt2)
        self.assertFalse(pt1 == pt3)

        self.assertTrue(vec1 == vec2)
        self.assertFalse(vec1 == vec3)

    def test_adding_tuples(self):
        pt = Point(3, -2, 5)
        vec = Vector(-2, 3, 1)
        result1 = pt + vec
        result2 = vec + vec
        
        self.assertTrue(result1 == Tuple(1,1,6,1))
        self.assertTrue(result2 == Tuple(-4,6,2,0))

        # no change as adding points doesn't make sense
        result3 = pt + pt
        print(result3)
        self.assertTrue(result3 == Tuple(3,-2,5,1))

    def test_subtracting_tuples(self):
        pt1 = Point(3, 2, 1)
        pt2 = Point(5, 6, 7)
        vec1 = Vector(3, 2, 1)
        vec2 = Vector(5, 6, 7)

        pt_pt_result = pt1 - pt2
        pt_vec_result = pt1 - vec2
        vec_vec_result = vec1 - vec2
        vec_pt_result = vec1 - pt2

        self.assertTrue(pt_pt_result == Vector(-2, -4, -6))
        self.assertTrue(pt_vec_result == Point(-2, -4, -6))
        self.assertTrue(vec_vec_result == Vector(-2, -4, -6))
        self.assertTrue(vec_pt_result ==  vec1)

    def test_negate_tuple(self):
        tup1 = Tuple(1,-2,3,-4)
        expected = Tuple(-1,2,-3,4)
        self.assertTrue(-tup1 == expected)

    def test_multiply_tuple(self):
        tup1 = Tuple(1,-2,3,-4)
        expected = Tuple(2,-4,6,-8)
        self.assertTrue(tup1*2 == expected)
        self.assertTrue(tup1 == expected*0.5)

    def test_divide_tuple(self):
        tup1 = Tuple(1,-2,3,-4)
        expected = Tuple(0.5,-1,1.5,-2)
        self.assertTrue(tup1/2 == expected)
        self.assertTrue(tup1 == expected/0.5)

    def test_magnitude_vector(self):
        self.assertTrue(float_equal(Vector(1,0,0).magnitude(),1))
        self.assertTrue(float_equal(Vector(0,1,0).magnitude(),1))
        self.assertTrue(float_equal(Vector(0,0,1).magnitude(),1))
        self.assertTrue(float_equal(Vector(1,2,3).magnitude(),math.sqrt(14)))
        self.assertTrue(float_equal(Vector(-1,-2,-3).magnitude(),math.sqrt(14)))

    def test_normalizing_tuple(self):
        self.assertTrue(Vector(4,0,0).normalize() == Vector(1,0,0))
        self.assertTrue(Vector(1,2,3).normalize() == Vector(1/math.sqrt(14),2/math.sqrt(14),3/math.sqrt(14)))
        norm = Vector(1,2,3).normalize()
        magnitude = norm.magnitude()
        self.assertTrue(float_equal(magnitude, 1))

    def test_dot_product(self):
        vec1 = Vector(1,2,3)
        vec2 = Vector(2,3,4)
        self.assertEqual(vec1.dot(vec2), 20)

    def test_cross_product(self):
        vec1 = Vector(1,2,3)
        vec2 = Vector(2,3,4)
        self.assertTrue(vec1.cross(vec2) == Vector(-1,2,-1))
        self.assertTrue(vec2.cross(vec1) == Vector(1,-2,1))

        


        
