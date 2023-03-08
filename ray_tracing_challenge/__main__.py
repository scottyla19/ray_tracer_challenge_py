from .rtc_tuple import *
from .rtc_color import *
from .rtc_matrix import *
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
I = IdentityMatrix(4)
print(I.inverse())

# 2 matrix times inverse
a = Matrix([[-5 , 2,  6 , -8 ],[ 1 , -5 ,  1 ,  8],[  7 ,  7 , -6 , -7],[  1 , -3 ,  7 ,  4]])   
aI = a.inverse()
print(a*aI)

# inverse of a transpose vs transpose of an inverse
aIT = a.inverse().transpose()
aTI = a.transpose().inverse()
print(aIT)
print(aTI)

# 4 changing a value changes the output tuple
# changing a value in the first row affects the first element, second row -> second element, etc.
tup = Tuple(1,2,3,1)
print(I*tup)
I[0,2] = 1
I[0,1] = 2
print(I*tup)