from GeomElement3D import GeomElement3D
import math


class Cylinder(GeomElement3D):
    def __init__(self, radius:float,height:float):
        print("Creating an instance of class Circle")
        self.radius:float = radius
        self.height:float = height


    def calc_volume(self):
        return math.pi * self.radius**2 * self.height

    def is_valid_geometry(self):
        return 