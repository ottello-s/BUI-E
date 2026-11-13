from GeomElement2D import GeomElement2D
import math


class Circle(GeomElement2D):
    """ instantiable class representing a circular 2D shape """

    # constructor
    def __init__(self, r):
        print('create an instance of class Circle')
        self.radius = r

    # implementation of calc_area() requested by parent class GeomElement2D
    def calc_area(self):
        a = math.pi * self.radius ** 2
        return a

    # implementation of calc_perimeter() requested by parent class GeomElement2D
    def calc_perimeter(self):
        return 2 * math.pi * self.radius
