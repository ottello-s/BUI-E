from GeomElement2D import GeomElement2D
from GeomElement import GeomElement
from Rectangle import Rectangle
from RectangularTriangle import RectangularTriangle
from Square import Square
from Cuboid import Cuboid
from Cube import Cube
from Cylinder import Cylinder



# geomElem = GeomElement2D()

rect1 = Rectangle(20, 30)

print(rect1.calc_area())

tri1 = RectangularTriangle(10, 5)

print(tri1.calc_area())
print(tri1.is_valid_geometry())


sq1 = Square(100)

print(sq1.calc_area())

cuboid1 = Cuboid(5,8,0.5)
wuerf1 = Cube(4)
cylind1 = Cylinder(1,10)

liste3D = [cuboid1, wuerf1, cylind1]


print(cuboid1.calc_volume())
print(wuerf1.calc_volume())
print(cylind1.calc_volume())