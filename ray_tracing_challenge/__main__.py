from .rtc_tuple import *
from .rtc_color import *
from .rtc_matrix import *
from .rtc_ray import *
from .rtc_material import *
from .rtc_shape import *
from .virtual_cannon import *

# ch1 putting it together
# p = Projectile(Point(0,1,0), Vector(1,1,0).normalize())
# e = Environment(Vector(0,-0.1, 0), Vector(0,-0.01,0))
# tick_count = 0
# while p.position.y > 0:
#     p = tick(e, p)
#     tick_count += 1
#     print('position: ({}, {}) tick_count: {}'.format(p.position.x, p.position.y, tick_count))

# ch2 putting it together
# p = Projectile(Point(0,1,0), Vector(1,1.8,0).normalize()*11.25)
# e = Environment(Vector(0,-0.1, 0), Vector(-0.01,0, 0))
# c = Canvas(900, 560)
# tick_count = 0
# while p.position.y > 0:
#     p = tick(e, p)
#     posx = int(p.position.x)
#     posy = c.height - int(p.position.y)
#     if posx <= c.width and posy <= c.height:
#         c.write_pixel(posy, posx, Color(0,1,0))

# text_file = open("ch2_image.ppm", "w")
# n = text_file.write(c.canvas_to_ppm())
# text_file.close()

# ch3 putting it all together
# 1 inverse of the identity
# I = IdentityMatrix(4)
# print(I.inverse())

# # 2 matrix times inverse
# a = Matrix([[-5 , 2,  6 , -8 ],[ 1 , -5 ,  1 ,  8],[  7 ,  7 , -6 , -7],[  1 , -3 ,  7 ,  4]])   
# aI = a.inverse()
# print(a*aI)

# # inverse of a transpose vs transpose of an inverse
# aIT = a.inverse().transpose()
# aTI = a.transpose().inverse()
# print(aIT)
# print(aTI)

# # 4 changing a value changes the output tuple
# # changing a value in the first row affects the first element, second row -> second element, etc.
# tup = Tuple(1,2,3,1)
# print(I*tup)
# I[0,2] = 1
# I[0,1] = 2
# print(I*tup)

# ch4 putting it all together
# c = Canvas(800, 800)
# radius = c.width * 3 / 8

# center_origin = Transformation().translate(c.width/2,0,c.height/2)
# points = [ Transformation().rotate_y(x*math.pi/6)*Point(0,0,1) for x in range(12)]
# for p in points:
#     p.x *= radius
#     p.z *= radius
#     p = center_origin * p
#     p.z = c.height - int(p.z)
#     c.write_pixel(int(p.z), int(p.x), Color(0,1,0))

# text_file = open("ch4_image.ppm", "w")
# n = text_file.write(c.canvas_to_ppm())
# text_file.close()


# ch5 putting it all together
# ray_origin = Point(0,0,-5)
# wall_z = 10
# wall_size = 7
# canvas_pixels = 100
# pixel_size = wall_size/canvas_pixels
# half = wall_size/2

# c = Canvas(100,100)
# color = Color(0,0,1)
# shape = Sphere(Point(0,0,0), 1)
# t = Transformation().scale(0.5,1,1)*Transformation().shearing(1,0,0,0,0,0)
# shape.set_transform(t)

# for y in range(canvas_pixels):
#     world_y = half - pixel_size*y
#     for x in range(canvas_pixels):
#         world_x = -half + pixel_size*x
#         position = Point(world_x, world_y, wall_z)
#         direction = position - ray_origin
#         r = Ray(ray_origin, direction.normalize() )
#         xs = r.intersects(shape)
#         if xs.hit() is not None:
#             c.write_pixel(x, y, color)
# text_file = open("ch5_image.ppm", "w")
# n = text_file.write(c.canvas_to_ppm())
# text_file.close()

# ch6 putting it all together
ray_origin = Point(0,0,-5)
wall_z = 10
wall_size = 7
canvas_pixels = 100
pixel_size = wall_size/canvas_pixels
half = wall_size/2

c = Canvas(canvas_pixels,canvas_pixels)
color = Color(0,0,1)
shape = Sphere(Point(0,0,0), 1)
# t = Transformation().scale(0.5,1,1)*Transformation().shearing(1,0,0,0,0,0)
# shape.set_transform(t)
shape.material = Material(Color(0,1,0))

light = PointLight(Point(-10, 10,-10), Color(1,1,1))

for y in range(canvas_pixels):
    world_y = half - pixel_size*y
    for x in range(canvas_pixels):
        world_x = -half + pixel_size*x
        position = Point(world_x, world_y, wall_z)
        direction = position - ray_origin
        r = Ray(ray_origin, direction.normalize() )
        xs = r.intersects(shape)
        if xs.hit() is not None:
            hit = xs.hit()
            p = r.position(hit.t)
            n = hit.object.normal_at(p)
            eye = -r.direction
            color = hit.object.material.lighting(light,p, eye, n)
            c.write_pixel(x, y, color)
text_file = open("ch6_image.ppm", "w")
n = text_file.write(c.canvas_to_ppm())
text_file.close()
