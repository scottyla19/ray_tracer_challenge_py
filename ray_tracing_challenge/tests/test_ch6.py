from unittest import TestCase
from ray_tracing_challenge import *

class TestSpheres(TestCase):
    def test_sphere_ray_axis(self):
        s = Sphere(Point(0,0,0), 1)
        n = s.normal_at(Point(1,0,0))
        self.assertTrue(n == Vector(1,0,0))

        n = s.normal_at(Point(0,1,0))
        self.assertTrue(n == Vector(0,1,0))

        n = s.normal_at(Point(math.sqrt(3)/3, math.sqrt(3)/3, math.sqrt(3)/3))
        self.assertTrue(n == Vector(math.sqrt(3)/3, math.sqrt(3)/3,math.sqrt(3)/3))
        self.assertTrue(n == n.normalize())

    def test_sphere_translate(self):
        s = Sphere(Point(0,0,0), 1)
        s.set_transform(Transformation().translate(0,1,0))
        n = s.normal_at(Point(0, 1.70711, -0.70711))
        self.assertTrue(n == Vector(0, 0.70711, -0.70711))

    def test_sphere_transform(self):
        s = Sphere(Point(0,0,0), 1)
        m = Transformation().scale(1,0.5,1) * Transformation().rotate_z(math.pi/5)
        s.set_transform(m)
        n = s.normal_at(Point(0, math.sqrt(2)/2, -math.sqrt(2)/2))
        self.assertTrue(n == Vector(0, 0.97014, -0.24254))

    def test_reflect_vector(self):
        v = Vector(1,-1,0)
        n = Vector(0,1,0)
        r = v.reflect(n)
        self.assertTrue(r == Vector(1,1,0))

    def test_reflect_vector_slanted(self):
        v = Vector(0,-1,0)
        n = Vector(math.sqrt(2)/2, math.sqrt(2)/2,0)
        r = v.reflect(n)
        self.assertTrue(r == Vector(1,0,0))

    def test_point_light(self):
        intensity = Color(1,1,1)
        position = Point(0,0,0)
        light = PointLight(position, intensity)
        self.assertTrue(light.position == position)
        self.assertTrue(light.intensity == intensity)

    def test_default_material(self):
        m = Material()
        self.assertTrue(m.color == Color(1,1,1))
        self.assertEqual(m.ambient, 0.1)
        self.assertEqual(m.diffuse, 0.9)
        self.assertEqual(m.specular, 0.9)
        self.assertEqual(m.shininess, 200.0)

    def test_sphere_default_mat(self):
        s = Sphere(Point(0,0,0), 1)
        m = s.material
        self.assertTrue(m == Material())

    def test_sphere_update_mat(self):
        s = Sphere()
        m = Material(amb=1)
        s.material = m
        self.assertTrue(s.material == m)

    def test_lighting_eye_between(self):
        eyev = Vector(0,0,-1)
        normalv = Vector(0,0,-1)
        position = Point(0,0,0)
        light = PointLight(Point(0,0,-10), Color(1,1,1))
        m = Material()
        result = m.lighting(light, position, eyev, normalv)
        self.assertTrue(result == Color(1.9, 1.9, 1.9))

    def test_lighting_eye_between_45(self):
        eyev = Vector(0, math.sqrt(2)/2, -math.sqrt(2)/2)
        normalv = Vector(0,0,-1)
        position = Point(0,0,0)
        light = PointLight(Point(0,0,-10), Color(1,1,1))
        m = Material()
        result = m.lighting(light, position, eyev, normalv)
        self.assertTrue(result == Color(1, 1, 1))

    def test_lighting_eye_opposite_45(self):
        eyev = Vector(0,0,-1)
        normalv = Vector(0,0,-1)
        position = Point(0,0,0)
        light = PointLight(Point(0,10,-10), Color(1,1,1))
        m = Material()
        result = m.lighting(light, position, eyev, normalv)
        self.assertTrue(result == Color(0.7364, 0.7364, 0.7364))

    def test_lighting_eye_in_reflection(self):
        eyev = Vector(0, -math.sqrt(2)/2, -math.sqrt(2)/2)
        normalv = Vector(0,0,-1)
        position = Point(0,0,0)
        light = PointLight(Point(0,10,-10), Color(1,1,1))
        m = Material()
        result = m.lighting(light, position, eyev, normalv)
        self.assertTrue(result == Color(1.6364, 1.6364, 1.6364))

    def test_lighting_light_behind(self):
        eyev = Vector(0, 0,-1)
        normalv = Vector(0,0,-1)
        position = Point(0,0,0)
        light = PointLight(Point(0,0,10), Color(1,1,1))
        m = Material()
        result = m.lighting(light, position, eyev, normalv)
        self.assertTrue(result == Color(0.1,0.1,0.1))