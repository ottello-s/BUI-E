from abc import ABC, abstractmethod
from GeomElement2D import  GeomElement2D

class Rectangle(GeomElement2D):
    def __init__(self,length:float, height:float):
        print("Creating an instance of class Rectangle")
        self.length: float = length
        self.height: float = height

    def calc_area(self):
        return self.length * self.height

    def calc_perimeter(self):
            return 2*(self.length + self.height)

    def is_valid_geometry(self):
        if self.length >= 0 and self.height >= 0:
            print("Great Success")
            return True
        else:
             ValueError