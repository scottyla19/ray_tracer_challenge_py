from unittest import TestCase
from ray_tracing_challenge import Color, Canvas
import numpy as np

class TestColors(TestCase):
    def test_color(self):
        col = Color(-0.5, 0.4, 1.7)
        self.assertEqual(col.red, -0.5) 
        self.assertEqual(col.green, 0.4)
        self.assertEqual(col.blue, 1.7) 

    def test_color_add(self):
        c1 = Color(0.9, 0.6, 0.75)
        c2 = Color(0.7, 0.1, 0.25)
        self.assertTrue(c1 + c2 == Color(1.6, 0.7, 1.0))

    def test_color_subtract(self):
        c1 = Color(0.9, 0.6, 0.75)
        c2 = Color(0.7, 0.1, 0.25)
        self.assertTrue(c1 - c2 == Color(0.2, 0.5, 0.5))

    def test_color_multiply_scalar(self):
        c1 = Color(0.2, 0.3, 0.4)
        self.assertTrue(c1 * 2 == Color(0.4, 0.6, 0.8))

    def test_color_multiply_colors(self):
        c1 = Color(1, 0.2, 0.4)
        c2 = Color(0.9, 1, 0.1)
        self.assertTrue(c1 * c2 == Color(0.9, 0.2, 0.04))

    def test_canvas_construct(self):
        canv = Canvas(10, 20)
        self.assertEqual(canv.width, 10)
        self.assertEqual(canv.height, 20)
        expected = [[Color(0,0,0) for x in range(10)] for x in range(20)]
        self.assertTrue(np.array_equal(canv.pixels, expected))

    def test_canvas_write_pixel(self):
        canv = Canvas(10, 20)
        red = Color(1,0,0)
        canv.write_pixel(2,3, red)
        self.assertTrue(canv.pixel_at(2,3) == red)

    def test_canvas_to_ppm_header(self):
        canv = Canvas(5, 3)
        ppm = canv.canvas_to_ppm()
        ppm =  '\n'.join(ppm.splitlines()[:4]) 
        expected = """
P3
5 3
255"""
        self.assertEqual(ppm, expected)

    def test_canvas_to_ppm(self):
        canv = Canvas(5, 3)
        c1 = Color(1.5,0,0)
        c2 = Color(0, 0.5,0)
        c3 = Color(-0.5,0,1)
        canv.write_pixel(0,0, c1)
        canv.write_pixel(1,2, c2)
        canv.write_pixel(2,4, c3)

        ppm = canv.canvas_to_ppm()
        expected ="""
P3
5 3
255
255 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 128 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 255
"""
        self.assertEqual(ppm, expected)

    def test_ppm_line_length(self):
        c1 = Color(1.0,0.8,0.6)
        canv = Canvas(10, 2, c1)
        ppm = canv.canvas_to_ppm()
        expected =  """
P3
10 2
255
255 204 153 255 204 153 255 204 153 255 204 153 255 204 153 255 204
153 255 204 153 255 204 153 255 204 153 255 204 153
255 204 153 255 204 153 255 204 153 255 204 153 255 204 153 255 204
153 255 204 153 255 204 153 255 204 153 255 204 153
"""
        self.assertTrue(ppm[-1] == "\n")
        self.assertEqual(ppm, expected)
       


    
