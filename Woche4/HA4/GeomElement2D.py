from abc import abstractmethod
from GeomElement import GeomElement

class GeomElement2D(GeomElement):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def calc_area(self):
        """This one calcs Area of your 2D Geometry"""
        pass 

    @abstractmethod
    def calc_perimeter(self):
        """This one calcs Perimeter of your 2D Geometry"""
        pass 

    @abstractmethod
    def is_valid_geometry(self):
        """This one checks if ur 2D Geometry is valid"""
        pass 