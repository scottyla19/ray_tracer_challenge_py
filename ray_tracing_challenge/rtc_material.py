from .rtc_matrix import *
from .rtc_color import *

class Light:
    def __init__(self, pos, intensity):
        self.position = pos
        self.intensity = intensity

class PointLight(Light):
    def __init__(self, pos, intensity):
        super().__init__(pos, intensity)

class Material:
    def __init__(self, c = Color(1,1,1), amb = 0.1, diff = 0.9, spec = 0.9, shine = 200.0):
        self.color = c
        self.ambient = amb
        self.diffuse = diff
        self.specular = spec
        self.shininess = shine

    def __eq__(self, mat2):
        return (self.color == mat2.color and 
                self.ambient == mat2.ambient and
                self.diffuse == mat2.diffuse and
                self.specular == mat2.specular and
                self.shininess == mat2.shininess )
    
    def lighting(self, light, point, eyev, normalv):
        effective_color = self.color * light.intensity
        lightv = (light.position - point).normalize()
        ambient = effective_color * self.ambient
        light_dot_normal = lightv.dot(normalv)
        if light_dot_normal < 0:
            diffuse = Color(0,0,0)
            specular = Color(0,0,0)
        else:
            diffuse = effective_color * self.diffuse * light_dot_normal
            reflectv = -lightv.reflect(normalv)
            reflect_dot_eye = reflectv.dot(eyev)
            if reflect_dot_eye < 0:
                specular = Color(0,0,0)
            else:
                factor = pow(reflect_dot_eye, self.shininess)
                specular = light.intensity * self.specular * factor
        return ambient + diffuse + specular
        

