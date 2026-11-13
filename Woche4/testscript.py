from GeomElement2D import GeomElement2D
from GeomElement import GeomElement
from Rectangle import Rectangle
from RectangularTriangle import RectangularTriangle
from Square import Square
# geomElem = GeomElement2D()

rect1 = Rectangle(20, 30)

print(rect1.calc_area())

tri1 = RectangularTriangle(10, 5)

print(tri1.calc_area())

sq1 = Square(100)

print(sq1.calc_area())