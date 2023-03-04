from .rtc_tuple import *
from .rtc_color import *
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
p = Projectile(Point(0,1,0), Vector(1,1.8,0).normalize()*11.25)
e = Environment(Vector(0,-0.1, 0), Vector(-0.01,0, 0))
c = Canvas(900, 560)
tick_count = 0
while p.position.y > 0:
    p = tick(e, p)
    posx = int(p.position.x)
    posy = c.height - int(p.position.y)
    if posx <= c.width and posy <= c.height:
        c.write_pixel(posy, posx, Color(0,1,0))

text_file = open("ch2_image.ppm", "w")
n = text_file.write(c.canvas_to_ppm())
text_file.close()