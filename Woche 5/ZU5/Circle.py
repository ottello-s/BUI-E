from GeomElement2D import GeomElement2D
import math


class Circle(GeomElement2D):
    def __init__(self, radius:float):
        print("Creating an instance of class Circle")
        self.radius:float = radius

    def calc_area(self):
        return math.pi * self.radius**2 * 0.5

    def calc_perimeter(self):
        return 2*math.pi*self.radius


    def is_valid_geometry(self):
        if self.radius >= 0:
            print("Great Success")
            return True
        else:
            ValueError


    