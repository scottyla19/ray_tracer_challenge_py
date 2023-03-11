from .rtc_tuple import float_equal
import numpy as np
from textwrap import wrap

class Color:
    def __init__(self, r, g, b):
        self.red = r
        self.green = g
        self.blue = b
    
    def __str__(self):
        return "r:{}, g:{}, b:{})".format(self.red, self.green, self.blue)

    def __eq__(color1, color2):
        return float_equal(color1.red, color2.red) and \
                float_equal(color1.green, color2.green) and \
                float_equal(color1.blue, color2.blue) 

    def __add__(self, b):
        if isinstance(b, self.__class__):
            return Color(self.red + b.red, self.green + b.green, self.blue + b.blue)
        elif isinstance(b, float):
            return Color(b+self.red, b+self.green, b+self.blue)
        elif isinstance(b, int):
            return Color(b+self.red, b+self.green, b+self.blue)
        else:
            raise TypeError("unsupported operand type(s) for +: '{}' and '{}'".format(self.__class__, type(b)))
        
    def __sub__(self, color2):
        return Color(self.red - color2.red, self.green - color2.green, self.blue - color2.blue)

    def __mul__(self, b):
        if isinstance(b, self.__class__):
            return Color(b.red*self.red, b.green*self.green, b.blue*self.blue)
        elif isinstance(b, float):
            return Color(b*self.red, b*self.green, b*self.blue)
        elif isinstance(b, int):
            return Color(b*self.red, b*self.green, b*self.blue)
        else:
            raise TypeError("unsupported operand type(s) for *: '{}' and '{}'".format(self.__class__, type(b)))

class Canvas:
    def __init__(self, w, h, color = Color(0,0,0)):
        self.width = w
        self.height = h
        self.pixels = [[color for x in range(w)] for x in range(h)]
    
    def __str__(self):
        return "rows: {}, columns: {} {}".format(self.height, 
        self.width, 
        self.canvas_to_ppm())

    def clamp_pixels(self, value, max_val = 255, min_val = 0):
        scaled_val = round(value*255)
        if scaled_val > max_val:
            scaled_val = max_val
        elif scaled_val < min_val:
            scaled_val = min_val
        return scaled_val

    def clean_ppm_output(self, ppm_str):
        lines = ppm_str.splitlines()
        metadata = lines[:4]
        lines = lines[4:]
        cleaned_output = "\n"
        for l in lines:
            # wrap defaults to 70 characters
            cleaned_output += '\n'.join(wrap(l)) + '\n'
    
        return '\n'.join(metadata) + cleaned_output

    def write_pixel(self, row, column, color):
        self.pixels[row][column] = color

    def pixel_at(self, row, column):
        return self.pixels[row][column]

    def canvas_to_ppm(self):
        ppm = """
P3
{} {}
255
""".format(self.width, self.height)
        
        pixel_str = ""
        for r in range(self.height):
            for c in range(self.width):
                px = self.pixel_at(r, c)
                pixel_str += "{} {} {} ".format(self.clamp_pixels(px.red), self.clamp_pixels(px.green), self.clamp_pixels(px.blue))
            # remove trailing space from row
            pixel_str = pixel_str.strip()
            # add new row
            pixel_str += "\n"
        ppm += pixel_str
        # turned off clean_ppm_output as it is too inefficient and causes crash
        ppm = self.clean_ppm_output(ppm)
        return ppm


    